import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT NOMECAMPO, DESCRCAMPO, TIPCAMPO, OPCOES
FROM TDDFLD
WHERE NOMETAB = 'TSIIRE' AND NOMECAMPO = 'TIPO'
""")
print("=== TDDFLD TSIIRE.TIPO ===")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)

res2 = c.execute_query("""
SELECT DISTINCT TIPO FROM TSIIRE
""")
print("=== DISTINCT TIPO IN TSIIRE ===")
for r in res2.get('responseBody', {}).get('rows', []):
    print(r)
