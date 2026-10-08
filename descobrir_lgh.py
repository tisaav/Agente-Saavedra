from sankhya_client import SankhyaClient
import json

client = SankhyaClient()

def query(sql, label=""):
    print(f"=== {label} ===")
    res = client.execute_query(sql)
    rows = res.get("responseBody", {}).get("rows", [])
    for r in rows:
        print(" ", r)
    return rows

# 1. Todas as tabelas LGH
query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'LGH_%' ORDER BY TABLE_NAME", "Tabelas LGH")

# 2. Definição da view TCSCON_VIEW
query("SELECT definition FROM sys.sql_modules WHERE object_id = OBJECT_ID('TCSCON_VIEW')", "TCSCON_VIEW")
