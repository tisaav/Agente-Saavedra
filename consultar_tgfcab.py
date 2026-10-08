"""
Consulta e análise de registros da tabela TGFCAB (Cabeçalho de Notas / Movimentações).
Suporta consulta direta via SQL (DbExplorerSP) ou via Entidade CRUD (CabecalhoNota).
"""

from sankhya_client import SankhyaClient


def format_currency(val):
    try:
        return f"R$ {float(val):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return str(val)


def main():
    client = SankhyaClient()
    print("=" * 80)
    print("               CONSULTA DA TABELA TGFCAB (ERP SANKHYA)")
    print("=" * 80)

    # 1. Total de registros na TGFCAB
    print("\n[+] Verificando total de registros e tipos de movimento...")
    try:
        sql_summary = """
        SELECT 
            COUNT(*) AS TOTAL_NOTAS,
            MIN(DTNEG) AS PRIMEIRA_DATA,
            MAX(DTNEG) AS ULTIMA_DATA
        FROM TGFCAB
        """
        summary_res = client.execute_query(sql_summary)
        rows = summary_res.get("responseBody", {}).get("rows", [])
        if rows:
            total, dt_ini, dt_fim = rows[0]
            print(f"  • Total de Notas/Movimentações: {total}")
            print(f"  • Período: de {dt_ini} até {dt_fim}")
    except Exception as e:
        print(f"  [!] Aviso ao obter resumo: {e}")

    # 2. Distribuição por Tipo de Movimento (TIPMOV)
    try:
        sql_tipmov = """
        SELECT TIPMOV, COUNT(*) AS QTD
        FROM TGFCAB
        GROUP BY TIPMOV
        ORDER BY QTD DESC
        """
        tipmov_res = client.execute_query(sql_tipmov)
        rows_tipmov = tipmov_res.get("responseBody", {}).get("rows", [])
        mov_labels = {
            "V": "Venda",
            "C": "Compra",
            "P": "Pedido de Venda",
            "O": "Pedido de Compra",
            "E": "Devolução de Venda",
            "D": "Devolução de Compra",
            "T": "Transferência",
            "L": "Lançamento",
            "J": "Pedido de Requisição"
        }
        print("\n[+] Distribuição por Tipo de Movimento (TIPMOV):")
        for tip, qtd in rows_tipmov:
            label = mov_labels.get(tip, "Outro")
            print(f"  • [{tip}] {label:<22}: {qtd:>6} registros")
    except Exception as e:
        print(f"  [!] Aviso na distribuição de tipos: {e}")

    # 3. Listando as 10 notas mais recentes com detalhes
    print("\n[+] Últimas 10 Notas/Movimentações cadastradas:")
    print("-" * 80)
    print(f"{'NUNOTA':<8} | {'NUMNOTA':<8} | {'DTNEG':<12} | {'PARCEIRO':<10} | {'MOV':<4} | {'STATUS':<6} | {'VALOR':>14}")
    print("-" * 80)

    sql_recent = """
    SELECT TOP 10 
        C.NUNOTA, 
        C.NUMNOTA, 
        CONVERT(VARCHAR(10), C.DTNEG, 103) AS DTNEG_FMT, 
        C.CODPARC,
        ISNULL(P.NOMEPARC, 'N/D') AS NOMEPARC,
        C.TIPMOV, 
        C.STATUSNOTA, 
        C.VLRNOTA
    FROM TGFCAB C
    LEFT JOIN TGFPAR P ON P.CODPARC = C.CODPARC
    ORDER BY C.NUNOTA DESC
    """
    try:
        recent_res = client.execute_query(sql_recent)
        rows_recent = recent_res.get("responseBody", {}).get("rows", [])
        for r in rows_recent:
            nunota, numnota, dtneg, codparc, nomeparc, tipmov, statusnota, vlrnota = r
            nome_abrev = (nomeparc[:18] + "..") if len(nomeparc) > 20 else nomeparc
            print(
                f"{nunota:<8} | {numnota:<8} | {dtneg:<12} | {codparc:<4} ({nome_abrev:<8}) | {tipmov:<4} | {statusnota:<6} | {format_currency(vlrnota):>14}"
            )
    except Exception as e:
        print(f"[!] Erro ao listar notas recentes: {e}")

    print("-" * 80)
    print("\n>> Tabela TGFCAB acessada e verificada com sucesso!")


if __name__ == "__main__":
    main()
