from sankhya_client import SankhyaClient

client = SankhyaClient()

def inspect_table(tab_name):
    print(f"\n--- Inspecionando {tab_name} ---")
    sql = f"SELECT TOP 3 * FROM {tab_name}"
    try:
        res = client.execute_query(sql)
        f_meta = [f.get("name") for f in res.get("responseBody", {}).get("fieldsMetadata", [])]
        rows = res.get("responseBody", {}).get("rows", [])
        print("Colunas:", f_meta)
        print("Linhas:", rows)
        cnt = client.execute_query(f"SELECT COUNT(*) FROM {tab_name}").get("responseBody", {}).get("rows", [[0]])[0][0]
        print("Total de linhas na tabela:", cnt)
    except Exception as e:
        print("Erro:", e)

inspect_table("LGH_LICITECON")
inspect_table("LGH_LICCAB")
inspect_table("LGH_LICCONT")
