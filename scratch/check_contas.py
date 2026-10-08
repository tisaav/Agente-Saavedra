import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT COUNT(*), COUNT(CASE WHEN DHBAIXA IS NULL THEN 1 END)
FROM TGFFIN
WHERE CODCTABCOINT = 17
""")
print("Conta 17 total e em aberto:", res.get('responseBody', {}).get('rows'))

# Let's see what CODCTABCOINT exist for open receivables
res2 = c.execute_query("""
SELECT CODCTABCOINT, COUNT(*)
FROM TGFFIN
WHERE RECDESP = 1 AND DHBAIXA IS NULL
GROUP BY CODCTABCOINT
""")
print("Contas com titulos abertos:", res2.get('responseBody', {}).get('rows'))
