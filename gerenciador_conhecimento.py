"""
Gerenciador e Crawler de Alta Performance da Base de Conhecimento Sankhya Help Center.
Suporta rastreamento recursivo de seções pai/filhas, download paralelo e estruturação em Markdown.
"""

import os
import re
import sys
import json
import time
import html
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from typing import List, Dict, Any, Tuple, Optional, Set

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)


class HTMLToMarkdownParser(HTMLParser):
    """Converte HTML do Zendesk para Markdown limpo e estruturado."""

    def __init__(self):
        super().__init__()
        self.output: List[str] = []
        self.links: List[Tuple[str, str]] = []
        self.tags_stack: List[str] = []
        self.current_link_url: Optional[str] = None
        self.current_link_text: List[str] = []
        self.in_table = False
        self.in_table_row = False
        self.table_row_cells: List[str] = []
        self.table_rows: List[List[str]] = []
        self.in_code = False
        self.list_depth = 0

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]):
        tag = tag.lower()
        self.tags_stack.append(tag)
        attr_dict = {k.lower(): (v or "") for k, v in attrs}

        if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            level = int(tag[1])
            self.output.append(f"\n\n{'#' * level} ")
        elif tag == "p":
            self.output.append("\n\n")
        elif tag == "br":
            self.output.append("\n")
        elif tag in ["strong", "b"]:
            self.output.append("**")
        elif tag in ["em", "i"]:
            self.output.append("*")
        elif tag == "code":
            if "pre" not in self.tags_stack:
                self.output.append("`")
        elif tag == "pre":
            self.output.append("\n\n```text\n")
            self.in_code = True
        elif tag in ["ul", "ol"]:
            self.list_depth += 1
            self.output.append("\n")
        elif tag == "li":
            indent = "  " * max(0, self.list_depth - 1)
            bullet = "-" if (len(self.tags_stack) >= 2 and self.tags_stack[-2] == "ul") else "1."
            self.output.append(f"\n{indent}{bullet} ")
        elif tag == "a":
            href = attr_dict.get("href", "").strip()
            self.current_link_url = href
            self.current_link_text = []
        elif tag == "table":
            self.in_table = True
            self.table_rows = []
        elif tag == "tr":
            self.in_table_row = True
            self.table_row_cells = []
        elif tag in ["th", "td"]:
            self.table_row_cells.append("")
        elif tag == "img":
            alt = attr_dict.get("alt", "Imagem")
            src = attr_dict.get("src", "")
            if src:
                self.output.append(f"\n\n![{alt}]({src})\n\n")

    def handle_endtag(self, tag: str):
        tag = tag.lower()
        if self.tags_stack and self.tags_stack[-1] == tag:
            self.tags_stack.pop()

        if tag in ["strong", "b"]:
            self.output.append("**")
        elif tag in ["em", "i"]:
            self.output.append("*")
        elif tag == "code":
            if not self.in_code:
                self.output.append("`")
        elif tag == "pre":
            self.output.append("\n```\n\n")
            self.in_code = False
        elif tag in ["ul", "ol"]:
            self.list_depth = max(0, self.list_depth - 1)
            self.output.append("\n")
        elif tag == "a":
            link_text = "".join(self.current_link_text).strip()
            url = self.current_link_url or ""
            if url:
                if not link_text:
                    link_text = url
                self.output.append(f"[{link_text}]({url})")
                self.links.append((link_text, url))
            else:
                self.output.append(link_text)
            self.current_link_url = None
            self.current_link_text = []
        elif tag == "tr":
            if self.in_table:
                self.table_rows.append(self.table_row_cells)
            self.in_table_row = False
        elif tag == "table":
            self.in_table = False
            self.output.append(self._format_markdown_table(self.table_rows))
            self.table_rows = []

    def handle_data(self, data: str):
        if self.current_link_url is not None:
            self.current_link_text.append(data)
        elif self.in_table and self.in_table_row and self.table_row_cells:
            self.table_row_cells[-1] += data
        else:
            self.output.append(data)

    def _format_markdown_table(self, rows: List[List[str]]) -> str:
        if not rows:
            return ""
        max_cols = max(len(r) for r in rows) if rows else 0
        if max_cols == 0:
            return ""

        table_md = ["\n"]
        clean_rows = []
        for r in rows:
            padded = [c.replace("\n", " ").strip() for c in r] + [""] * (max_cols - len(r))
            clean_rows.append(padded)

        headers = clean_rows[0]
        table_md.append("| " + " | ".join(headers) + " |")
        table_md.append("| " + " | ".join(["---"] * max_cols) + " |")

        for r in clean_rows[1:]:
            table_md.append("| " + " | ".join(r) + " |")
        table_md.append("\n\n")
        return "\n".join(table_md)

    def get_markdown(self) -> str:
        raw_text = "".join(self.output)
        cleaned = re.sub(r"\n{3,}", "\n\n", raw_text)
        return html.unescape(cleaned.strip())


class SankhyaCrawler:
    """Crawler e Indexador de alta capacidade para o Help Center Sankhya."""

    BASE_URL = "https://ajuda.sankhya.com.br"
    API_URL = "https://ajuda.sankhya.com.br/api/v2/help_center/pt-br"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

    def __init__(self, output_dir: str = "base_conhecimento"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.metadata_file = os.path.join(self.output_dir, "metadata_artigos.json")
        self.metadata = self._load_metadata()

        # Árvore de seções em cache
        self.sections_by_id: Dict[int, Dict[str, Any]] = {}
        self.sections_by_parent: Dict[Optional[int], List[Dict[str, Any]]] = {}
        self._load_section_tree()

    def _load_metadata(self) -> Dict[str, Any]:
        data = {"artigos": {}, "links_internos": {}, "modulos": {}, "secoes": {}}
        if os.path.exists(self.metadata_file):
            try:
                with open(self.metadata_file, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    data.update(loaded)
            except Exception:
                pass
        data.setdefault("modulos", {})
        data.setdefault("artigos", {})
        data.setdefault("links_internos", {})
        data.setdefault("secoes", {})
        return data

    def _save_metadata(self):
        with open(self.metadata_file, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)

    def _request_json(self, url: str) -> Dict[str, Any]:
        full_url = url if url.startswith("http") else f"{self.API_URL}/{url}"
        req = urllib.request.Request(full_url, headers={"User-Agent": self.USER_AGENT, "Accept": "application/json"})
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    retry_after = int(e.headers.get("Retry-After", 5))
                    print(f"    [!] Rate limit (429). Aguardando {retry_after}s...", flush=True)
                    time.sleep(retry_after + 1)
                    continue
                if attempt == 4:
                    print(f"    [!] Erro HTTP {e.code} em {full_url}", flush=True)
                    return {}
                time.sleep(1 + attempt * 2)
            except Exception as e:
                if attempt == 4:
                    print(f"    [!] Falha de conexão: {e}", flush=True)
                    return {}
                time.sleep(1 + attempt * 2)
        return {}

    def _load_section_tree(self):
        """Carrega e mapeia a árvore completa de seções da Sankhya."""
        cache_path = os.path.join(self.output_dir, ".sections_cache.json")
        if os.path.exists(cache_path):
            try:
                with open(cache_path, "r", encoding="utf-8") as f:
                    cached = json.load(f)
                    self.sections_by_id = {int(k): v for k, v in cached.items()}
                    for s in self.sections_by_id.values():
                        pid = s.get("parent_section_id")
                        self.sections_by_parent.setdefault(pid, []).append(s)
                    return
            except Exception:
                pass

        print("[+] Carregando mapa completo de seções do Help Center Sankhya...")
        next_url = f"{self.API_URL}/sections.json?per_page=100"
        while next_url:
            data = self._request_json(next_url)
            for s in data.get("sections", []):
                sid = s["id"]
                pid = s.get("parent_section_id")
                self.sections_by_id[sid] = s
                self.sections_by_parent.setdefault(pid, []).append(s)
            next_url = data.get("next_page")

        # Salva cache
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(self.sections_by_id, f, ensure_ascii=False)
        print(f"[OK] Total de {len(self.sections_by_id)} seções mapeadas na árvore do Help Center.")

    def sanitize(self, text: str) -> str:
        import unicodedata
        nfkd = unicodedata.normalize("NFKD", text)
        ascii_text = nfkd.encode("ascii", "ignore").decode("ascii")
        s = re.sub(r"[^\w\s-]", "", ascii_text).strip()
        s = re.sub(r"[-\s]+", "_", s)
        return s[:60].lower()

    def get_descendants(self, section_id: int) -> List[int]:
        """Obtém todas as seções filhas, netas e a própria seção."""
        desc = [section_id]
        for child in self.sections_by_parent.get(section_id, []):
            desc.extend(self.get_descendants(child["id"]))
        return desc

    def get_articles_for_section(self, section_id: int) -> List[Dict[str, Any]]:
        """Busca artigos de uma seção individual (incluindo paginação)."""
        articles = []
        next_url = f"{self.API_URL}/sections/{section_id}/articles.json?per_page=100"
        while next_url:
            try:
                data = self._request_json(next_url)
                arts = data.get("articles", [])
                articles.extend(arts)
                next_url = data.get("next_page")
            except Exception:
                break
        return articles

    def process_module(self, module_name: str, module_id: int, max_articles: Optional[int] = None) -> int:
        """Processa um macro-módulo completo e todas as suas subseções."""
        print(f"\n=======================================================")
        print(f"[+] INICIANDO MÓDULO: {module_name} (ID: {module_id})")
        print(f"=======================================================")

        descendants = self.get_descendants(module_id)
        print(f"  • Hierarquia: {len(descendants)} seções/subseções pertencem a este módulo.")

        mod_slug = self.sanitize(module_name)
        mod_dir = os.path.join(self.output_dir, mod_slug)
        os.makedirs(mod_dir, exist_ok=True)

        # 1. Coleta lista de todos os artigos
        all_articles: List[Dict[str, Any]] = []
        for sid in descendants:
            sec_meta = self.sections_by_id.get(sid, {})
            sec_name = sec_meta.get("name", f"Sec_{sid}")
            arts = self.get_articles_for_section(sid)
            for a in arts:
                a["_parent_module"] = module_name
                a["_sub_section_name"] = sec_name
            all_articles.extend(arts)

        # Remove duplicados por ID se houver
        unique_articles = {str(a["id"]): a for a in all_articles}
        article_list = list(unique_articles.values())

        if max_articles:
            article_list = article_list[:max_articles]

        print(f"  • Total de artigos a processar: {len(article_list)}")

        # 2. Processa e salva artigos em paralelo (Worker Pool)
        saved_count = 0
        with ThreadPoolExecutor(max_workers=6) as executor:
            future_to_art = {
                executor.submit(self._save_article_task, art, mod_dir): art
                for art in article_list
            }
            for idx, future in enumerate(as_completed(future_to_art), 1):
                try:
                    res = future.result()
                    if res:
                        saved_count += 1
                        if saved_count % 10 == 0 or saved_count == len(article_list):
                            print(f"    -> [{saved_count}/{len(article_list)}] artigos convertidos e salvos...")
                except Exception as e:
                    print(f"    [!] Erro ao salvar artigo: {e}")

        self.metadata["modulos"][str(module_id)] = {
            "id": module_id,
            "nome": module_name,
            "secoes_total": len(descendants),
            "artigos_processados": saved_count,
            "pasta": mod_slug,
        }
        self._save_metadata()
        self.generate_global_index()
        print(f"[OK] Módulo '{module_name}' concluído com sucesso ({saved_count} artigos)!", flush=True)
        return saved_count

    def process_category(self, category_name: str, category_id: int, max_articles: Optional[int] = None) -> int:
        """Processa uma categoria completa do Help Center (todas as suas seções e subseções)."""
        print(f"\n=======================================================", flush=True)
        print(f"[+] INICIANDO CATEGORIA: {category_name} (ID: {category_id})", flush=True)
        print(f"=======================================================", flush=True)

        url = f"{self.API_URL}/categories/{category_id}/sections.json?per_page=100"
        top_sections = []
        while url:
            data = self._request_json(url)
            top_sections.extend(data.get("sections", []))
            url = data.get("next_page")

        all_descendants = set()
        for s in top_sections:
            desc = self.get_descendants(s["id"])
            all_descendants.update(desc)

        descendants = list(all_descendants)
        print(f"  • Hierarquia: {len(descendants)} seções/subseções pertencem a esta categoria.", flush=True)

        cat_slug = self.sanitize(category_name)
        cat_dir = os.path.join(self.output_dir, cat_slug)
        os.makedirs(cat_dir, exist_ok=True)

        all_articles: List[Dict[str, Any]] = []
        for sid in descendants:
            sec_meta = self.sections_by_id.get(sid, {})
            sec_name = sec_meta.get("name", f"Sec_{sid}")
            arts = self.get_articles_for_section(sid)
            for a in arts:
                a["_parent_module"] = category_name
                a["_sub_section_name"] = sec_name
            all_articles.extend(arts)

        unique_articles = {str(a["id"]): a for a in all_articles}
        article_list = list(unique_articles.values())

        if max_articles:
            article_list = article_list[:max_articles]

        print(f"  • Total de artigos a processar: {len(article_list)}", flush=True)

        saved_count = 0
        with ThreadPoolExecutor(max_workers=8) as executor:
            future_to_art = {
                executor.submit(self._save_article_task, art, cat_dir): art
                for art in article_list
            }
            for idx, future in enumerate(as_completed(future_to_art), 1):
                try:
                    res = future.result()
                    if res:
                        saved_count += 1
                        if saved_count % 50 == 0 or saved_count == len(article_list):
                            print(f"    -> [{saved_count}/{len(article_list)}] artigos convertidos e salvos...", flush=True)
                except Exception as e:
                    print(f"    [!] Erro ao salvar artigo: {e}", flush=True)

        self.metadata["modulos"][str(category_id)] = {
            "id": category_id,
            "nome": category_name,
            "secoes_total": len(descendants),
            "artigos_processados": saved_count,
            "pasta": cat_slug,
        }
        self._save_metadata()
        self.generate_global_index()
        print(f"[OK] Categoria '{category_name}' concluída com sucesso ({saved_count} artigos)!", flush=True)
        return saved_count

    def _save_article_task(self, art: Dict[str, Any], target_dir: str) -> Optional[Dict[str, Any]]:
        art_id = str(art.get("id"))
        title = art.get("title", f"Artigo_{art_id}")
        html_url = art.get("html_url", "")
        updated_at = art.get("updated_at", "")
        body_html = art.get("body", "")
        sub_sec = art.get("_sub_section_name", "")
        module_name = art.get("_parent_module", "")

        parser = HTMLToMarkdownParser()
        parser.feed(body_html)
        md_content = parser.get_markdown()
        internal_links = parser.links

        sankhya_links = []
        for l_text, l_url in internal_links:
            if "sankhya.com.br" in l_url:
                sankhya_links.append({"texto": l_text, "url": l_url})

        filename = f"{art_id}_{self.sanitize(title)}.md"
        filepath = os.path.join(target_dir, filename)

        if not os.path.exists(filepath) or os.path.getsize(filepath) < 100:
            doc = []
            doc.append(f"# {title}\n")
            doc.append(f"> **Módulo:** {module_name} | **Subseção:** {sub_sec}  ")
            doc.append(f"> **Fonte Oficial:** [{html_url}]({html_url})  ")
            doc.append(f"> **ID:** `{art_id}` | **Última Atualização:** {updated_at}\n")
            doc.append("---\n")
            doc.append(md_content)

            if sankhya_links:
                doc.append("\n\n---\n\n### 🔗 Links e Referências Internas:\n")
                seen = set()
                for lk in sankhya_links:
                    u = lk["url"]
                    if u not in seen:
                        seen.add(u)
                        doc.append(f"- [{lk['texto']}]({u})")

            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(doc))

        rel_path = os.path.relpath(filepath, self.output_dir).replace("\\", "/")
        art_data = {
            "id": art_id,
            "title": title,
            "module": module_name,
            "sub_section": sub_sec,
            "url": html_url,
            "updated_at": updated_at,
            "file": rel_path,
            "internal_links_count": len(sankhya_links),
        }
        self.metadata["artigos"][art_id] = art_data

        for lk in sankhya_links:
            u = lk["url"]
            if u not in self.metadata["links_internos"]:
                self.metadata["links_internos"][u] = {
                    "url": u,
                    "texto": lk["texto"],
                    "citado_em": [title],
                    "processado": (u in [a.get("url") for a in self.metadata["artigos"].values()]),
                }
            else:
                if title not in self.metadata["links_internos"][u]["citado_em"]:
                    self.metadata["links_internos"][u]["citado_em"].append(title)

        return art_data

    def generate_global_index(self):
        """Gera README.md mestre com índice e estatísticas de todos os módulos."""
        index_path = os.path.join(self.output_dir, "README.md")
        lines = []
        lines.append("# 📚 Base de Conhecimento Sankhya ERP / Om\n")
        lines.append("Esta base de conhecimento consolida a documentação técnica oficial extraída do **Sankhya Help Center** (`ajuda.sankhya.com.br`). Ela está estruturada localmente por módulos e subseções para suporte a consultas, automações e integração com o conector ERP.\n")
        lines.append("---\n")

        total_arts = len(self.metadata["artigos"])
        total_links = len(self.metadata["links_internos"])
        total_mods = len(self.metadata.get("modulos", {}))

        lines.append("### 📊 Visão Geral da Base Local:")
        lines.append(f"- **Total de Artigos Baixados e Convertidos:** `{total_arts}`")
        lines.append(f"- **Módulos do ERP Cobertos:** `{total_mods}`")
        lines.append(f"- **Referências Internas Mapeadas:** `{total_links}`\n")
        lines.append("---\n")

        lines.append("## 📦 Módulos Cadastrados na Base\n")
        lines.append("| Módulo ERP | Seções/Subseções | Artigos Salvos | Pasta Local |")
        lines.append("| :--- | :---: | :---: | :--- |")

        for mid, mdata in self.metadata.get("modulos", {}).items():
            nome = mdata.get("nome")
            sec_tot = mdata.get("secoes_total")
            art_tot = mdata.get("artigos_processados")
            pasta = mdata.get("pasta")
            lines.append(f"| **{nome}** | {sec_tot} | {art_tot} | [`{pasta}/`]({pasta}/) |")

        lines.append("\n---\n")
        lines.append("## 📂 Artigos Principais por Módulo\n")

        by_module: Dict[str, List[Dict[str, Any]]] = {}
        for art in self.metadata["artigos"].values():
            m = art.get("module", "Geral")
            by_module.setdefault(m, []).append(art)

        for m_name, arts in by_module.items():
            lines.append(f"### 📁 {m_name} ({len(arts)} artigos)")
            for a in sorted(arts, key=lambda x: x["title"])[:25]:  # Amostra dos primeiros 25
                lines.append(f"- [{a['title']}]({a['file']}) — *Subseção: {a.get('sub_section')}*")
            if len(arts) > 25:
                lines.append(f"- *(... e mais {len(arts) - 25} artigos completos salvos na pasta)*")
            lines.append("")

        with open(index_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"\n[OK] Índice geral atualizado em: {index_path}")


def main():
    crawler = SankhyaCrawler()

    # Módulos informados pelo usuário
    TARGET_MODULES = [
        ("Comercial e Vendas", 43501923946391),
        ("Produção", 43502003428759),
        ("Financeiro e Patrimônio", 43502544066199),
        ("Inteligência e Análise", 43502137153815),
        ("Imobiliária", 43502675616535),
        ("Configurações e Cadastros", 43501591371927),
        ("Fiscal e Contábil", 43502077596951),
        ("Contratos e Serviços", 43502073610263),
        ("Pessoas+", 41982477972759),
        ("Suprimentos e Estoque", 43502312343319),
        ("Plataforma e Integrações", 43502692007063),
    ]

    print("Iniciando processamento dos 11 módulos enviados...")
    for name, mid in TARGET_MODULES:
        crawler.process_module(name, mid)

    crawler.generate_global_index()


if __name__ == "__main__":
    main()
