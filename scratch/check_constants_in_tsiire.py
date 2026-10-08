import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
# Let's see some fixed values in TSIIRE across different banks
res = c.execute_query("""
SELECT TOP 30 CODIGO, SEQUENCIA, CAMPO, TAMANHO, TIPO
FROM TSIIRE
WHERE CAMPO LIKE '%01%' OR CAMPO LIKE '%REMESSA%' OR CAMPO LIKE '%COBRANCA%' OR CAMPO LIKE '0%'
ORDER BY CODIGO, SEQUENCIA
""")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
