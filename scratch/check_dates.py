import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT MAX(DTVENC), MAX(DTNEG), GETDATE()
FROM TGFFIN
""")
print("Dates in TGFFIN:", res.get('responseBody', {}).get('rows'))

# Let's see how DTVENC is formatted in DB
res2 = c.execute_query("""
SELECT TOP 5 NUFIN, DTVENC, DTNEG, RECDESP, CODCTABCOINT, DHBAIXA
FROM TGFFIN
WHERE RECDESP = 1
ORDER BY NUFIN DESC
""")
print("Latest TGFFIN:", res2.get('responseBody', {}).get('rows'))
