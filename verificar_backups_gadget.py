from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME LIKE 'TSIGDG%' OR TABLE_NAME LIKE 'TSI%HIST%' OR TABLE_NAME LIKE 'TSI%LOG%'
"""
res = client.execute_query(sql)
for r in res.get("responseBody", {}).get("rows", []):
    print(r)
