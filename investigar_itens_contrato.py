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
        print(f"Colunas ({len(fields)}): {fields}")
        print(f"Total registros: {len(rows)}")
        for i, r in enumerate(rows):
            row_dict = dict(zip(fields, r))
            print(f"[{i+1}] {json.dumps(row_dict, default=str, ensure_ascii=False)}")
        return fields, rows
    except Exception as e:
        print(f"ERRO: {e}")
        return None, None

# 1. LGH_LICCAB
query("SELECT * FROM LGH_LICCAB WHERE NULIC IN (27, 1304)", "LGH_LICCAB NULIC 27 e 1304")

# 2. LGH_LICITECON (Itens dos contratos 8 e 332)
query("SELECT * FROM LGH_LICITECON WHERE NUMCONTRATO IN (8, 332)", "LGH_LICITECON Contratos 8 e 332")

# 3. TCSCON
query("SELECT * FROM TCSCON WHERE NUMCONTRATO IN (8, 332)", "TCSCON Contratos 8 e 332")
