from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME LIKE 'TSI%' OR TABLE_NAME LIKE 'TDD%' OR TABLE_NAME LIKE 'AD_%'
ORDER BY TABLE_NAME
"""
try:
    res = client.execute_query(sql)
    rows = res.get("responseBody", {}).get("rows", [])
    print(f"Total tabelas encontradas: {len(rows)}")
    for r in rows:
        name = r[0]
        if any(k in name for k in ['DASH', 'GAD', 'PAN', 'LAN', 'CON', 'MOD', 'REP', 'BI', 'REL', 'VIS']):
            print(" ", name)
except Exception as e:
    print("Erro:", e)
