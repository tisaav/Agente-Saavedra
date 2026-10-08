from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT t.name AS table_name, c.name AS column_name
FROM sys.tables t
JOIN sys.columns c ON t.object_id = c.object_id
WHERE c.name LIKE '%RFE%' OR c.name LIKE '%REL%' OR c.name LIKE '%BOLE%' OR c.name LIKE '%MOD%'
"""
res = client.execute_query(sql)
for r in res.get("responseBody", {}).get("rows", []):
    tbl, col = r[0], r[1]
    try:
        q = f"SELECT COUNT(*) FROM {tbl} WHERE {col} IN (8, 9, 10, 11, 12, 13, 14)"
        r2 = client.execute_query(q)
        cnt = r2.get("responseBody", {}).get("rows", [[0]])[0][0]
        if cnt >= 6:
            print(f"Candidate: {tbl}.{col} -> count {cnt}")
    except:
        pass
