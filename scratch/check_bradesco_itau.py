import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT TOP 20 SEQUENCIA, CAMPO, TAMANHO, TIPO
FROM TSIIRE
WHERE CODIGO = 15010100
ORDER BY SEQUENCIA
""")
print("=== BRADESCO 15010100 ===")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)

res2 = c.execute_query("""
SELECT TOP 20 SEQUENCIA, CAMPO, TAMANHO, TIPO
FROM TSIIRE
WHERE CODIGO = 8010100
ORDER BY SEQUENCIA
""")
print("=== ITAU 8010100 ===")
for r in res2.get('responseBody', {}).get('rows', []):
    print(r)
