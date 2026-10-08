from sankhya_client import SankhyaClient
import json

client = SankhyaClient()

def query(sql, label=""):
    print("=" * 80)
    print(f"--- {label} ---")
    try:
        res = client.execute_query(sql)
        f_meta = res.get("responseBody", {}).get("fieldsMetadata", [])
        fields = [f.get("name") for f in f_meta]
        rows = res.get("responseBody", {}).get("rows", [])
        print(f"Colunas: {fields}")
        print(f"Total registros: {len(rows)}")
        for r in rows:
            print(" ", dict(zip(fields, r)))
        return fields, rows
    except Exception as e:
        print(f"ERRO: {e}")
        return None, None

# 1. Procurar em TSIGBI
query("SELECT NUINST, TITULO, DESCRICAO FROM TSIGBI WHERE TITULO LIKE '%2302%' OR TITULO LIKE '%CONTRATO%' OR TITULO LIKE '%LICITA%' OR DESCRICAO LIKE '%2302%'", "TSIGBI")

# 2. Procurar em TSIBIGDG
query("SELECT NUGDG, NUBI, TITULO FROM TSIBIGDG WHERE TITULO LIKE '%2302%' OR TITULO LIKE '%CONTRATO%' OR TITULO LIKE '%LICITA%'", "TSIBIGDG")
