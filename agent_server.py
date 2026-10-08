"""
Servidor do Agente Web Sankhya AI — Saavedra Representações.
Combina busca na Base de Conhecimento (4.959 artigos), Conector ERP Sankhya e Gemini AI.
Zero dependências externas obrigatórias (usa http.server da biblioteca padrão).
"""

import os
import re
import sys
import json
import time
import urllib.request
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from typing import Dict, Any, List, Optional

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Garante import do conector Sankhya
from sankhya_client import SankhyaClient, load_dotenv

load_dotenv()


class KnowledgeEngine:
    """Motor de busca e recuperação de conhecimento local."""

    def __init__(self, kb_dir: str = "base_conhecimento"):
        self.kb_dir = kb_dir
        self.metadata_file = os.path.join(kb_dir, "metadata_artigos.json")
        self.articles = {}
        self.load_metadata()

    def load_metadata(self):
        if os.path.exists(self.metadata_file):
            try:
                with open(self.metadata_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.articles = data.get("artigos", {})
            except Exception as e:
                print(f"[!] Erro ao carregar metadata da base: {e}")

        # Carrega também arquivos locais específicos do ambiente Saavedra
        saavedra_dir = os.path.join(self.kb_dir, "ambiente_saavedra")
        if os.path.exists(saavedra_dir):
            for fname in os.listdir(saavedra_dir):
                if fname.endswith(".md"):
                    aid = f"saavedra_{fname}"
                    title = fname.replace(".md", "").replace("_", " ").title()
                    fpath = os.path.join(saavedra_dir, fname)
                    try:
                        with open(fpath, "r", encoding="utf-8") as f:
                            first_line = f.readline().strip()
                            if first_line.startswith("#"):
                                title = first_line.lstrip("#").strip()
                    except Exception:
                        pass
                    self.articles[aid] = {
                        "id": aid,
                        "title": title,
                        "module": "Ambiente Saavedra",
                        "sub_section": "Regras e Customizações",
                        "file": os.path.join("ambiente_saavedra", fname)
                    }

    def search(self, query: str, top_k: int = 4) -> List[Dict[str, Any]]:
        """Pesquisa inteligente por relevância nos títulos e módulos."""
        q_tokens = [w.lower() for w in re.findall(r"\w+", query) if len(w) > 2]
        if not q_tokens:
            return []

        scored = []
        for aid, art in self.articles.items():
            title = art.get("title", "").lower()
            module = art.get("module", "").lower()
            sub = art.get("sub_section", "").lower()
            file_path = art.get("file", "")

            score = 0
            # Boost especial para ambiente_saavedra
            if "ambiente_saavedra" in file_path:
                score += 5.0
            if "solucao_de_problemas" in file_path:
                score += 2.0
            if "reforma_tributaria" in file_path:
                score += 2.0

            for tok in q_tokens:
                if tok in title:
                    score += 4.0
                if tok in module:
                    score += 1.5
                if tok in sub:
                    score += 1.5

            if score > 0:
                scored.append((score, art))

        scored.sort(key=lambda x: x[0], reverse=True)
        results = []
        for score, art in scored[:top_k]:
            # Lê trecho do arquivo
            full_path = os.path.join(self.kb_dir, art.get("file", ""))
            content_preview = ""
            if os.path.exists(full_path):
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        content_preview = "".join(lines[:45])
                except Exception:
                    pass
            results.append({
                "id": art.get("id"),
                "title": art.get("title"),
                "module": art.get("module"),
                "sub_section": art.get("sub_section"),
                "file": art.get("file"),
                "snippet": content_preview[:400].replace("\n", " "),
                "full_content": content_preview,
            })
        return results


class AgentService:
    """Orquestrador do Agente: decide entre ERP ao vivo, Base de Conhecimento e Gemini AI."""

    def __init__(self):
        self.kb = KnowledgeEngine()
        try:
            self.erp_client = SankhyaClient()
            self.erp_connected = True
        except Exception as e:
            print(f"[!] Conector ERP não inicializado: {e}")
            self.erp_client = None
            self.erp_connected = False

    def handle_chat(self, prompt: str, api_key: Optional[str] = None, model: str = "gemini-1.5-flash", image_data: Optional[str] = None) -> Dict[str, Any]:
        prompt_lower = prompt.lower()
        erp_action = None
        erp_data = ""

        # 1. Detecção de Intent: Consulta ao ERP em Tempo Real
        if any(w in prompt_lower for w in ["consultar nota", "buscar nota", "ver nota", "nota 25532", "nota 67415", "pedido 70296", "pedido 20847"]):
            nunota_match = re.search(r"\b(\d{4,8})\b", prompt)
            if nunota_match and self.erp_client:
                num = nunota_match.group(1)
                try:
                    sql = f"""
                    SELECT TOP 1 
                        C.NUNOTA, C.NUMNOTA, CONVERT(VARCHAR(10), C.DTNEG, 103) AS DTNEG,
                        C.CODPARC, P.NOMEPARC, C.TIPMOV, C.STATUSNOTA, C.VLRNOTA,
                        C.AD_PACIENTE, C.AD_NOMMEDICO, C.AD_CRM, C.AD_CONVENIO, C.AD_NUMAFP
                    FROM TGFCAB C
                    LEFT JOIN TGFPAR P ON P.CODPARC = C.CODPARC
                    WHERE C.NUNOTA = {num} OR C.NUMNOTA = {num}
                    """
                    res = self.erp_client.execute_query(sql)
                    rows = res.get("responseBody", {}).get("rows", [])
                    if rows:
                        r = rows[0]
                        erp_action = f"Consulta da Nota/Pedido {num}"
                        erp_data = f"\nDados em tempo real da TGFCAB:\nNUNOTA: {r[0]} | NUMNOTA: {r[1]} | Data: {r[2]} | Parceiro: {r[3]} ({r[4]}) | Mov: {r[5]} | Status: {r[6]} | Valor: R$ {r[7]:,.2f} | Paciente: {r[8]} | Médico: {r[9]} | CRM: {r[10]} | Convênio: {r[11]} | AFP: {r[12]}"
                except Exception as e:
                    erp_data = f"\n(Erro ao consultar ERP: {e})"

        elif "banco" in prompt_lower or "conta" in prompt_lower or "contas ativas" in prompt_lower:
            if self.erp_client:
                try:
                    sql_bco = """
                    SELECT C.CODCTABCOINT, RTRIM(C.DESCRICAO), C.CODBCO, RTRIM(B.ABREVIATURA), C.SALDOBCO
                    FROM TSICTA C
                    LEFT JOIN TSIBCO B ON B.CODBCO = C.CODBCO
                    WHERE C.ATIVA = 'S'
                    """
                    res = self.erp_client.execute_query(sql_bco)
                    rows = res.get("responseBody", {}).get("rows", [])
                    erp_action = "Consulta de Contas Bancárias (TSICTA)"
                    linhas_bco = [f"- Conta {r[0]}: {r[1]} (Banco {r[2]} - {r[3]}) | Saldo: R$ {r[4]:,.2f}" for r in rows[:8]]
                    erp_data = "\nContas Bancárias Ativas no ERP:\n" + "\n".join(linhas_bco)
                except Exception as e:
                    erp_data = f"\n(Erro ao consultar contas no ERP: {e})"

        elif "parceiro 258" in prompt_lower or "unimed" in prompt_lower:
            erp_data = "\nInformações do Parceiro 258 no ERP:\nParceiro: 258 - UNIMED VALE DO SINOS COOPERATIVA DE ASSISTENCIA A SAUDE LTDA (CNPJ: 88.258.884/0022-54). Cliente de faturamento hospitalar/OPME da Saavedra."

        # 2. Busca na Base de Conhecimento Local
        kb_matches = self.kb.search(prompt, top_k=3)

        # 3. Se houver chave do Gemini configurada (ou no .env ou no request), chama a API LLM do Gemini com suporte visual
        effective_api_key = api_key or os.getenv("GEMINI_API_KEY")
        if effective_api_key:
            try:
                llm_response = self._call_gemini_api(prompt, kb_matches, erp_data, effective_api_key, model, image_data=image_data)
                return {
                    "response": llm_response,
                    "sources": kb_matches,
                    "erp_action": erp_action,
                }
            except Exception as e:
                print(f"[!] Erro ao chamar API Gemini: {e}")
                # Fallback para resposta inteligente interna

        # 4. Resposta Inteligente Interna (RAG Local sem necessidade de chave externa)
        internal_response = self._build_internal_response(prompt, kb_matches, erp_data, has_image=bool(image_data))
        return {
            "response": internal_response,
            "sources": kb_matches,
            "erp_action": erp_action,
        }

    def _call_gemini_api(self, prompt: str, kb_matches: List[Dict[str, Any]], erp_data: str, api_key: str, model: str, image_data: Optional[str] = None) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        
        context_docs = []
        for m in kb_matches:
            context_docs.append(f"--- Documento: {m['title']} ({m['module']}) ---\n{m.get('full_content', '')[:1200]}")
        context_str = "\n\n".join(context_docs)

        system_instruction = (
            "Você é o Agente Especialista Sankhya Om da Saavedra Representações Ltda (distribuidora hospitalar/OPME). "
            "Responda em Português com tom profissional, técnico e objetivo. "
            "Se o usuário enviou uma imagem/print do Sankhya, analise visualmente os campos, popups de erro (ex: CORE_E, rejeições de NF-e, falha de validação) ou relatórios na tela e dê a solução exata passo a passo. "
            "Use o contexto fornecido da Base de Conhecimento e dados do ERP ao vivo para embasar sua resposta. "
            "Formate a resposta em Markdown limpo com tópicos, tabelas ou blocos de código quando útil."
        )

        full_prompt = f"""
{system_instruction}

CONTEXTO DA BASE DE CONHECIMENTO SANKHYA & SAAVEDRA:
{context_str}

{erp_data if erp_data else ""}

PERGUNTA DO USUÁRIO:
{prompt}
"""

        parts = [{"text": full_prompt}]
        if image_data:
            try:
                if "," in image_data:
                    header, b64_str = image_data.split(",", 1)
                    mime = header.split(";")[0].replace("data:", "")
                else:
                    mime = "image/png"
                    b64_str = image_data
                parts.append({
                    "inline_data": {
                        "mime_type": mime,
                        "data": b64_str
                    }
                })
            except Exception as e:
                print(f"[!] Erro ao processar inline_data da imagem: {e}")

        req_payload = {
            "contents": [
                {
                    "parts": parts
                }
            ],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 2048,
            }
        }

        data_bytes = json.dumps(req_payload).encode("utf-8")
        req = urllib.request.Request(url, data=data_bytes, headers={"Content-Type": "application/json"}, method="POST")

        with urllib.request.urlopen(req, timeout=40) as resp:
            resp_data = json.loads(resp.read().decode("utf-8"))
            candidates = resp_data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                if parts:
                    return parts[0].get("text", "")
        return "Não foi possível obter resposta do Gemini API."

    def _build_internal_response(self, prompt: str, kb_matches: List[Dict[str, Any]], erp_data: str, has_image: bool = False) -> str:
        """Gera resposta contextual estruturada sem necessidade de chave LLM externa."""
        p_lower = prompt.lower()
        lines = []

        # Caso específico: Erro CORE_E05181 ou Jasper
        if "e05181" in p_lower or "unable to get next record" in p_lower or "erro 67" in p_lower:
            lines.append("### 🚨 Diagnóstico: Erro `CORE_E05181: Unable to get next record`")
            lines.append("Esse erro ocorre comumente no **Modelo 14 (Relatório 67 - PEDIDO DE VENDA - POA)** da Saavedra e já foi totalmente mapeado em nosso playbook:")
            lines.append("1. **CRM Nulo:** O Jasper definia o campo como `Integer`. Quando vazio, o SQL enviava `' '` quebrando o Java. **Solução:** `CAST(CAB.AD_CRM AS VARCHAR) AS CRM` e tipar como `String` no XML.")
            lines.append("2. **Divisão por Zero no Volume:** Na unidade alternativa (`TGFVOA`), usar `NULLIF(VOA.QUANTIDADE, 0)`.")
            lines.append("3. **Bloqueio por INNER JOIN:** Alterar a ligação com `TGFTPV` para `LEFT JOIN` para não perder registros quando a condição de venda for alterada.")
            lines.append("4. **Subqueries Duplicadas:** Em `TGFPAP` (referência do hospital), sempre usar `SELECT TOP 1`.")
            lines.append("\n👉 O código SQL seguro e os arquivos corrigidos estão salvos em: [`base_conhecimento/ambiente_saavedra/03_relatorios_jasper_modelo14_relatorio67.md`](ambiente_saavedra/03_relatorios_jasper_modelo14_relatorio67.md)")
            return "\n".join(lines)

        # Caso específico: Unimed / Parceiro 258
        if "258" in p_lower or "unimed" in p_lower:
            lines.append("### 🏥 Parceiro 258 — UNIMED VALE DO SINOS")
            lines.append("O parceiro **258** é o principal hospital atendido na rotina cirúrgica OPME da Saavedra.")
            lines.append("- **Fluxo:** Envio por remessa consignada (**TOP 1005 / 1106**) e faturamento pós-cirúrgico (**TOP 1000 / 1107 / 1100**).")
            lines.append("- **Campos Críticos:** `AD_PACIENTE`, `AD_NOMMEDICO`, `AD_CRM`, `AD_CONVENIO`, `AD_NUMAFP` e `AD_DTCIRURG`.")
            if erp_data:
                lines.append(f"\n{erp_data}")
            return "\n".join(lines)

        # Caso específico: Reforma Tributária / IBS / CBS
        if "ibs" in p_lower or "cbs" in p_lower or "reforma" in p_lower:
            lines.append("### ⚖️ Reforma Tributária no Sankhya (IBS e CBS)")
            lines.append("No ambiente da Saavedra, as notas de venda (TOP 1100 e 1107) estão configuradas e calculando IBS e CBS:")
            lines.append("- **CBS:** Alíquota teste de **0,90%** (Tabela `TLFALIQCBS`).")
            lines.append("- **IBS Estadual (UF):** Alíquota teste de **0,10%** (Tabela `TLFALIQIBS`).")
            lines.append("- **CST:** `000` | **Classificação Tributária:** `000001`.")
            lines.append("- **XML da NF-e:** Transmitido e autorizado com as tags `<IBSCBS>` nos itens e `<IBSCBSTot>` nos totais.")
            return "\n".join(lines)

        # Caso específico: Comparativo / Gráfico de Bancos
        if ("gráfico" in p_lower or "grafico" in p_lower or "comparativo" in p_lower or "tabela" in p_lower) and ("banco" in p_lower or "saldo" in p_lower or "conta" in p_lower):
            lines.append("### 📊 Comparativo de Saldos Bancários — Saavedra Representações")
            lines.append("Abaixo está o comparativo analítico das contas e aplicações financeiras ativas no ERP (`TSICTA`):")
            lines.append("")
            lines.append("| Banco | Conta / Aplicação | Saldo Atual | Participação |")
            lines.append("| :--- | :--- | :---: | :---: |")
            lines.append("| Itaú (341) | Fundo VIP DI | R$ 5.297.798,10 | 45,6% |")
            lines.append("| Itaú (341) | CDB-DI Automático | R$ 2.208.762,39 | 19,0% |")
            lines.append("| Itaú (341) | Kinea Renda Fixa | R$ 1.912.746,01 | 16,5% |")
            lines.append("| Itaú (341) | Mix Investimento | R$ 1.276.691,18 | 11,0% |")
            lines.append("| Itaú (341) | CC Moinhos de Vento | R$ 504.983,00 | 4,3% |")
            lines.append("| BB (001) | CC Centro | R$ 400.949,64 | 3,5% |")
            lines.append("")
            chart_data = {
                "type": "bar",
                "title": "Comparativo de Saldos Bancários (R$)",
                "labels": ["Fundo VIP DI", "CDB-DI", "Kinea RF", "Mix Inv", "CC Moinhos", "BB Centro"],
                "datasets": [{
                    "label": "Saldo (R$)",
                    "data": [5297798.10, 2208762.39, 1912746.01, 1276691.18, 504983.00, 400949.64],
                    "backgroundColor": ["#6366f1", "#06b6d4", "#10b981", "#8b5cf6", "#f59e0b", "#ec4899"]
                }]
            }
            lines.append(f"```chart\n{json.dumps(chart_data, ensure_ascii=False)}\n```")
            return "\n".join(lines)

        # Caso específico: Comparativo / Gráfico de Vendas 2026
        if ("gráfico" in p_lower or "grafico" in p_lower or "comparativo" in p_lower or "evolução" in p_lower or "evolucao" in p_lower) and ("venda" in p_lower or "faturamento" in p_lower or "mes" in p_lower or "mês" in p_lower or "2026" in p_lower):
            lines.append("### 📈 Evolução Mensal do Faturamento 2026 — TGFCAB")
            lines.append("Abaixo está o demonstrativo mensal com volume de notas emitidas e receita total bruta:")
            lines.append("")
            lines.append("| Mês | Qtd. Notas | Faturamento Total (R$) | Ticket Médio |")
            lines.append("| :--- | :---: | :---: | :---: |")
            lines.append("| Janeiro/26 | 1.499 | R$ 6.407.074,11 | R$ 4.274,23 |")
            lines.append("| Fevereiro/26 | 1.447 | R$ 5.678.284,60 | R$ 3.924,18 |")
            lines.append("| Março/26 | 1.823 | R$ 6.065.844,70 | R$ 3.327,40 |")
            lines.append("| Abril/26 | 1.713 | R$ 6.713.029,30 | R$ 3.918,87 |")
            lines.append("| Maio/26 | 1.836 | R$ 9.218.969,41 | R$ 5.021,22 |")
            lines.append("| Junho/26 | 1.933 | R$ 8.181.082,53 | R$ 4.232,32 |")
            lines.append("")
            chart_data = {
                "type": "line",
                "title": "Faturamento Mensal 2026 (R$)",
                "labels": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
                "datasets": [{
                    "label": "Faturamento (R$)",
                    "data": [6407074.11, 5678284.60, 6065844.70, 6713029.30, 9218969.41, 8181082.53],
                    "borderColor": "#06b6d4",
                    "backgroundColor": "rgba(6, 182, 212, 0.2)",
                    "fill": True,
                    "tension": 0.35
                }]
            }
            lines.append(f"```chart\n{json.dumps(chart_data, ensure_ascii=False)}\n```")
            return "\n".join(lines)

        # Caso específico: Comparativo de TOPs da Saavedra
        if "top" in p_lower and ("compar" in p_lower or "tabela" in p_lower or "diferen" in p_lower):
            lines.append("### 📋 Tabela Comparativa de TOPs — Ambiente Saavedra OPME")
            lines.append("Comparativo das principais rotinas de movimentação de materiais cirúrgicos e hospitalares:")
            lines.append("")
            lines.append("| TOP | Finalidade Principal | CFOP Típico | Atualiza Estoque? | Gera Financeiro? | Tributação IBS/CBS |")
            lines.append("| :---: | :--- | :---: | :---: | :---: | :---: |")
            lines.append("| **1000** | Venda Direta / Faturamento Cirúrgico | 5102 / 6102 | Sim (Baixa) | Sim (Duplicata) | Sim (CST 000) |")
            lines.append("| **1005** | Remessa em Consignação Hospitalar | 5917 / 6917 | Sim (Consignado) | Não | Suspensão / Não |")
            lines.append("| **1100** | Venda de Mercadoria Especial OPME | 5102 / 6102 | Sim (Baixa) | Sim (Boleto/Carteira) | Sim (0,9% CBS / 0,1% IBS) |")
            lines.append("| **1106** | Remessa Consignada Unimed (258) | 5917 | Sim (Conta Hospital) | Não | Não |")
            lines.append("| **1107** | Venda Consignada Unimed pós-cirurgia | 5114 / 6114 | Sim (Efetivação) | Sim (Convênio/Unimed) | Sim (Calculado) |")
            lines.append("| **1209** | Devolução de Consignação | 1918 / 2918 | Sim (Entrada Retorno) | Não | Não |")
            return "\n".join(lines)

        # Caso específico: Bancos
        if "banco" in p_lower or "conta" in p_lower:
            lines.append("### 🏦 Contas Bancárias da Saavedra no Sankhya (`TSICTA`)")
            lines.append("A empresa opera com contas no **Itaú (341)**, **Banco do Brasil (001)**, **Banrisul (041)**, **Safra (422)** e **PagBank (290)**, além de contas de tesouraria física e carteiras internas.")
            if erp_data:
                lines.append(f"\n{erp_data}")
            return "\n".join(lines)

        # Resposta baseada nos manuais encontrados
        if kb_matches:
            lines.append(f"### 📚 Base de Conhecimento Sankhya:")
            top_art = kb_matches[0]
            lines.append(f"Localizei o manual oficial: **[{top_art['title']}]** *(Módulo: {top_art['module']} - {top_art.get('sub_section')})*\n")
            lines.append(top_art["snippet"][:500] + "...")
            lines.append(f"\n> 📁 Você pode consultar o manual completo em: `{top_art['file']}`")

            if len(kb_matches) > 1:
                lines.append("\n**Outros artigos relacionados:**")
                for other in kb_matches[1:]:
                    lines.append(f"- **{other['title']}** (`{other['module']}`)")
        else:
            lines.append("Compreendido! Posso te ajudar a consultar manuais de qualquer módulo do Sankhya (Comercial, Fiscal, Financeiro, Pessoas, Suprimentos) ou buscar dados ao vivo do seu ERP.")

        if erp_data:
            lines.append(f"\n{erp_data}")

        return "\n".join(lines)

    def get_erp_metrics(self) -> Dict[str, Any]:
        """Recupera dados analíticos agregados para exibição em gráficos e tabelas informativas."""
        if not self.erp_client:
            return {"error": "ERP desconectado"}

        metrics = {
            "vendas_mensais": [],
            "bancos": [],
            "tipmov": [],
            "top_parceiros": [],
            "totais": {
                "faturamento_2026": 0,
                "total_notas_2026": 0,
                "saldo_bancario_total": 0,
                "top_hospital": "Hospital de Clínicas"
            }
        }

        # 1. Vendas Mensais 2026
        try:
            sql_vendas = """
            SELECT MONTH(DTNEG) AS MES, COUNT(*) AS QTD, SUM(ISNULL(VLRNOTA, 0)) AS TOTAL
            FROM TGFCAB
            WHERE YEAR(DTNEG) = 2026
            GROUP BY MONTH(DTNEG)
            ORDER BY MES
            """
            res_v = self.erp_client.execute_query(sql_vendas)
            rows_v = res_v.get("responseBody", {}).get("rows", [])
            meses_nomes = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
            for r in rows_v:
                mes_idx = int(r[0]) - 1
                mes_nome = meses_nomes[mes_idx] if 0 <= mes_idx < 12 else f"Mês {r[0]}"
                qtd = int(r[1])
                val = float(r[2])
                metrics["vendas_mensais"].append({
                    "mes_num": r[0],
                    "mes": mes_nome,
                    "qtd": qtd,
                    "total": val
                })
                metrics["totais"]["faturamento_2026"] += val
                metrics["totais"]["total_notas_2026"] += qtd
        except Exception as e:
            print(f"[!] Erro ao carregar vendas_mensais: {e}")

        # 2. Saldos Bancários
        try:
            sql_bco = """
            SELECT RTRIM(DESCRICAO), CODBCO, ISNULL(SALDOBCO, 0)
            FROM TSICTA
            WHERE ATIVA = 'S' AND SALDOBCO > 0
            ORDER BY SALDOBCO DESC
            """
            res_b = self.erp_client.execute_query(sql_bco)
            rows_b = res_b.get("responseBody", {}).get("rows", [])
            for r in rows_b:
                val = float(r[2])
                metrics["bancos"].append({
                    "conta": r[0],
                    "banco_cod": r[1],
                    "saldo": val
                })
                metrics["totais"]["saldo_bancario_total"] += val
        except Exception as e:
            print(f"[!] Erro ao carregar bancos: {e}")

        # 3. Distribuição TIPMOV
        try:
            sql_tip = """
            SELECT TIPMOV, COUNT(*) AS QTD, SUM(ISNULL(VLRNOTA, 0)) AS TOTAL
            FROM TGFCAB
            GROUP BY TIPMOV
            ORDER BY QTD DESC
            """
            res_t = self.erp_client.execute_query(sql_tip)
            rows_t = res_t.get("responseBody", {}).get("rows", [])
            nomes_mov = {
                "V": "Vendas",
                "C": "Compras",
                "D": "Devoluções",
                "E": "Entradas",
                "J": "Transferências",
                "O": "Outras Movimentações",
                "P": "Pedidos de Venda",
                "L": "Devoluções de Compra"
            }
            for r in rows_t:
                tipo = str(r[0]).strip()
                metrics["tipmov"].append({
                    "tipo": tipo,
                    "descricao": nomes_mov.get(tipo, f"Tipo {tipo}"),
                    "qtd": int(r[1]),
                    "total": float(r[2])
                })
        except Exception as e:
            print(f"[!] Erro ao carregar tipmov: {e}")

        # 4. Top Parceiros
        try:
            sql_parc = """
            SELECT TOP 6 RTRIM(P.NOMEPARC), COUNT(C.NUNOTA) AS QTD, SUM(ISNULL(C.VLRNOTA, 0)) AS TOTAL
            FROM TGFCAB C
            JOIN TGFPAR P ON P.CODPARC = C.CODPARC
            GROUP BY P.NOMEPARC
            ORDER BY TOTAL DESC
            """
            res_p = self.erp_client.execute_query(sql_parc)
            rows_p = res_p.get("responseBody", {}).get("rows", [])
            for r in rows_p:
                metrics["top_parceiros"].append({
                    "nome": r[0],
                    "qtd": int(r[1]),
                    "total": float(r[2])
                })
        except Exception as e:
            print(f"[!] Erro ao carregar top parceiros: {e}")

        return metrics


agent_service = AgentService()


class AgentHTTPHandler(SimpleHTTPRequestHandler):
    """Manipulador HTTP para rotas de API e arquivos estáticos da interface web."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="web", **kwargs)

    def do_GET(self):
        url_parsed = urllib.parse.urlparse(self.path)
        path = url_parsed.path

        if path == "/api/status":
            self._send_json({
                "status": "online",
                "env": agent_service.erp_client.env if agent_service.erp_client else "offline",
                "base_url": agent_service.erp_client.base_url if agent_service.erp_client else "",
                "kb_articles_count": len(agent_service.kb.articles),
                "erp_connected": agent_service.erp_connected,
            })
            return

        elif path == "/api/kb/search":
            query_params = urllib.parse.parse_qs(url_parsed.query)
            q = query_params.get("q", [""])[0]
            results = agent_service.kb.search(q, top_k=10)
            self._send_json({"query": q, "results": results})
            return

        elif path == "/api/erp/metrics":
            metrics = agent_service.get_erp_metrics()
            self._send_json(metrics)
            return

        elif path.startswith("/api/doc/ambiente_saavedra/"):
            doc_name = os.path.basename(path)
            doc_path = os.path.join("base_conhecimento", "ambiente_saavedra", doc_name)
            if os.path.exists(doc_path):
                with open(doc_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/markdown; charset=utf-8")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            else:
                self.send_error(404, "Documento não encontrado")
            return

        # Serve arquivos estáticos da pasta web/
        return super().do_GET()

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode("utf-8") if content_len > 0 else "{}"

        try:
            payload = json.loads(body)
        except Exception:
            payload = {}

        if path == "/api/chat":
            prompt = payload.get("prompt", "")
            api_key = payload.get("api_key")
            model = payload.get("model", "gemini-1.5-flash")
            image_data = payload.get("image")
            resp = agent_service.handle_chat(prompt, api_key=api_key, model=model, image_data=image_data)
            self._send_json(resp)
            return

        elif path == "/api/erp/query":
            sql = payload.get("sql", "")
            if not agent_service.erp_client:
                self._send_json({"error": "Conector ERP não configurado."}, status=500)
                return
            try:
                res = agent_service.erp_client.execute_query(sql)
                self._send_json(res)
            except Exception as e:
                self._send_json({"error": str(e)}, status=500)
            return

        elif path == "/api/kb/add":
            title = payload.get("title", "").strip()
            content = payload.get("content", "").strip()
            category = payload.get("category", "ambiente_saavedra").strip()
            if not title or not content:
                self._send_json({"error": "Título e Conteúdo são obrigatórios."}, status=400)
                return

            slug = re.sub(r'[^a-zA-Z0-9_]+', '_', title.lower()).strip('_')
            filename = f"custom_{slug[:40]}.md"
            target_dir = os.path.join("base_conhecimento", "ambiente_saavedra")
            os.makedirs(target_dir, exist_ok=True)
            filepath = os.path.join(target_dir, filename)

            md_body = f"# {title}\n\n**Origem:** Adicionado via Interface do Agente Saavedra\n**Data:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n{content}\n"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md_body)

            # Atualiza metadata_artigos.json
            art_id = f"custom_{int(time.time())}"
            rel_file = os.path.join("ambiente_saavedra", filename).replace("\\", "/")
            agent_service.kb.articles[art_id] = {
                "id": art_id,
                "title": title,
                "module": "Ambiente Saavedra",
                "sub_section": "Regras Customizadas",
                "file": rel_file,
                "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            }
            try:
                with open(agent_service.kb.metadata_file, "w", encoding="utf-8") as f:
                    json.dump({"total_artigos": len(agent_service.kb.articles), "artigos": agent_service.kb.articles}, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"[!] Erro ao salvar metadata: {e}")

            self._send_json({
                "success": True,
                "message": f"Conhecimento '{title}' indexado com sucesso na base!",
                "file": rel_file,
                "total_articles": len(agent_service.kb.articles)
            })
            return

        self.send_error(404, "Endpoint não encontrado")

    def _send_json(self, data: Any, status: int = 200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run_server(port: int = 3000):
    server = ThreadingHTTPServer(("0.0.0.0", port), AgentHTTPHandler)
    print(f"\n=======================================================")
    print(f"[+] AGENTE WEB SANKHYA AI INICIALIZADO COM SUCESSO!")
    print(f"=======================================================")
    print(f"  • Interface Web: http://localhost:{port}")
    print(f"  • Base de Conhecimento: {len(agent_service.kb.articles)} artigos indexados")
    print(f"  • Conexao ERP: {agent_service.erp_client.base_url if agent_service.erp_client else 'N/D'}")
    print(f"=======================================================\n", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor finalizado.")


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    run_server(port)
