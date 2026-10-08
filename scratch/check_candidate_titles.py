import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT TOP 10 
    NUFIN, NUMNOTA, NOSSONUM, DTVENC, VLRDESDOB, CODPARC, CODCTABCOINT, RECDESP, DHMOV
FROM TGFFIN
WHERE RECDESP = 1 
  AND CODCTABCOINT = 17
  AND DTVENC >= '2026-10-16'
  AND DHBAIXA IS NULL
ORDER BY DTVENC ASC
""")
print("=== TITULOS CONTA 17 DTVENC >= 16/10/2026 ===")
rows = res.get('responseBody', {}).get('rows', [])
for r in rows:
    print(r)

if not rows:
    print("Nenhum com CODCTABCOINT=17. Verificando títulos a receber futuros em geral:")
    res2 = c.execute_query("""
    SELECT TOP 10 
        NUFIN, NUMNOTA, NOSSONUM, DTVENC, VLRDESDOB, CODPARC, CODCTABCOINT, RECDESP
    FROM TGFFIN
    WHERE RECDESP = 1 
      AND DTVENC >= '2026-10-16'
      AND DHBAIXA IS NULL
    ORDER BY DTVENC ASC
    """)
    for r in res2.get('responseBody', {}).get('rows', []):
        print(r)
