import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME LIKE '%FORMATADOR%' OR COLUMN_NAME LIKE '%LAYOUT%' OR TABLE_NAME LIKE '%REM%' OR TABLE_NAME LIKE '%EDI%' OR TABLE_NAME LIKE '%REC%'
""")
print("=== TABLES MATCHING ===")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
