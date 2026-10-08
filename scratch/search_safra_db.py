import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT DISTINCT MODULO, CODIGO, TITULO
FROM TSIREM
WHERE TITULO LIKE '%SAFRA%' OR TITULO LIKE '%HEADER%' OR CODIGO LIKE '27%'
""")
print("TSIREM search:")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)

res2 = c.execute_query("""
SELECT DISTINCT MODULO, CODIGO
FROM TSIIRE
WHERE CODIGO LIKE '27%'
""")
print("TSIIRE 27%:")
for r in res2.get('responseBody', {}).get('rows', []):
    print(r)
