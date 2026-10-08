import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME IN ('NUVERSAO', 'IDMODULO', 'CODMOD', 'CODAPL', 'CODCON', 'CODTELA')
""")
print("Cols:", res.get('responseBody', {}).get('rows', []))
