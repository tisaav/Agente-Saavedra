from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME LIKE '%DSB%' 
   OR TABLE_NAME LIKE '%DSH%' 
   OR TABLE_NAME LIKE '%GAD%' 
   OR TABLE_NAME LIKE '%BI%' 
   OR TABLE_NAME LIKE '%HTML%' 
   OR TABLE_NAME LIKE '%PAINEL%'
   OR TABLE_NAME LIKE '%COMP%'
ORDER BY TABLE_NAME
"""
res = client.execute_query(sql)
rows = res.get("responseBody", {}).get("rows", [])
print(f"Total tabelas encontradas: {len(rows)}")
for r in rows:
    t = r[0]
    # Testa se tem registros
    try:
        cnt = client.execute_query(f"SELECT COUNT(*) FROM [{t}]").get("responseBody", {}).get("rows", [[0]])[0][0]
        if cnt > 0:
            print(f"  [+] {t}: {cnt} registros")
    except Exception:
        pass
