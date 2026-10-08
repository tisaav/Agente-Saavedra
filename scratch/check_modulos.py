import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT DISTINCT MODULO FROM TSIREM
""")
print("MODULOS in TSIREM:", res.get('responseBody', {}).get('rows', []))

res2 = c.execute_query("""
SELECT MODULO, CODIGO, TITULO FROM TSIREM WHERE TITULO LIKE '%SAFRA%'
""")
print("SAFRA in TSIREM:", res2.get('responseBody', {}).get('rows', []))
