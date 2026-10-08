import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sankhya_client import SankhyaClient

c = SankhyaClient()
# Let's see what layout records exist for Safra:
res = c.execute_query("""
SELECT CODIGO, DESCRICAO
FROM TSIREC
WHERE DESCRICAO LIKE '%SAFRA%' OR CODIGO IN (27010000, 27020000)
""")
print("=== LAYOUTS SAFRA (TSIREC) ===")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)

# Let's inspect fields of 27010000 and 27020000
res_campos = c.execute_query("""
SELECT CODIGO, SEQUENCIA, NOMECAMPO, CAMPO, TAMANHO, TIPO, POSINI, POSFIM
FROM TSIIRE
WHERE CODIGO IN (27010000, 27020000)
ORDER BY CODIGO, SEQUENCIA
""")
print("=== CAMPOS SAFRA (TSIIRE) ===")
for r in res_campos.get('responseBody', {}).get('rows', []):
    print(r)
