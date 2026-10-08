import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT CODCON, TITULO, URL, NOMETAB, NOMETABELABROWSE
FROM TSICON
WHERE CODCON = 522
""")
print("TSICON 522:", res.get('responseBody', {}).get('rows', []))

res2 = c.execute_query("""
SELECT *
FROM TSIAPL
WHERE CODAPL = 522 OR CODMOD = 522
""")
print("TSIAPL 522:", res2.get('responseBody', {}).get('rows', []))
