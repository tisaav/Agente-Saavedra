import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT DISTINCT CODIGO
FROM TSIIRE
WHERE CODIGO >= 26000000
ORDER BY CODIGO
""")
print(">= 26000000:")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
