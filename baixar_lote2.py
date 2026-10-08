"""
Script para baixar o Lote 2 de Conhecimento Sankhya:
- Seções: Reforma Tributária e Notas Técnicas
- Categorias: Melhores Práticas, Assistente de Melhores Práticas e Solução de Problemas
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)

from gerenciador_conhecimento import SankhyaCrawler

def main():
    crawler = SankhyaCrawler()

    # 1. Seções específicas
    sections_to_process = [
        ("Reforma Tributaria", 41867438393623),
        ("Notas Tecnicas", 42731935259415),
    ]

    for name, sid in sections_to_process:
        print(f"\n[+] Processando seção: {name} (ID: {sid})...", flush=True)
        crawler.process_module(name, sid)

    # 2. Categorias
    categories_to_process = [
        ("Melhores Praticas", 360003117673),
        ("Assistente de Melhores Praticas", 32174002694551),
        ("Solucao de Problemas", 360003116793),
    ]

    for name, cid in categories_to_process:
        print(f"\n[+] Processando categoria: {name} (ID: {cid})...", flush=True)
        crawler.process_category(name, cid)

    crawler.generate_global_index()
    print("\n[OK] Lote 2 de Conhecimento baixado e indexado com sucesso!", flush=True)

if __name__ == "__main__":
    main()
