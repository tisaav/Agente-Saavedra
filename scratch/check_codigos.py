import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT DISTINCT CODIGO
FROM TSIIRE
ORDER BY CODIGO
""")
print("=== DISTINCT CODIGO IN TSIIRE ===")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
