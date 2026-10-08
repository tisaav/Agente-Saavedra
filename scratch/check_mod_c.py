import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT CODIGO, TITULO, TAMREGISTRO, GRAU, CODPAI
FROM TSIREM
WHERE MODULO = 'C' AND (CODPAI = -999999999 OR CODIGO LIKE '27%')
ORDER BY CODIGO
""")
print("MODULO C root or 27%:")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
