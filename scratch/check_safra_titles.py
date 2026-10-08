import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT TOP 20 
    F.NUFIN, F.NUMNOTA, F.NOSSONUM, F.DTVENC, F.VLRDESDOB, F.CODPARC, P.RAZAOSOCIAL, F.CODCTABCOINT
FROM TGFFIN F
LEFT JOIN TGFPAR P ON F.CODPARC = P.CODPARC
WHERE F.RECDESP = 1 
  AND F.CODCTABCOINT = 17
  AND F.DHBAIXA IS NULL
ORDER BY F.DTVENC DESC
""")
print("=== TITULOS ABERTOS CONTA 17 ===")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)

# And let's check what titles were in the previous remessa to Safra!
res_prev = c.execute_query("""
SELECT TOP 10 R.IDREMESSA, R.NUFIN, R.NUMREMESSA, R.DHGERACAO, F.NUMNOTA, F.DTVENC, F.VLRDESDOB
FROM TGFRCI R
JOIN TGFFIN F ON R.NUFIN = F.NUFIN
WHERE F.CODCTABCOINT = 17 OR R.IDREMESSA IN (SELECT MAX(IDREMESSA) FROM TGFRC)
ORDER BY R.IDREMESSA DESC
""")
print("=== ULTIMA REMESSA ===")
for r in res_prev.get('responseBody', {}).get('rows', []):
    print(r)
