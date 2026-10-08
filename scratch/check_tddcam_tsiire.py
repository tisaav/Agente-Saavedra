import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT c.NOMETAB, c.NOMECAMPO, o.VALOR, o.OPCAO
FROM TDDCAM c
JOIN TDDOPC o ON c.NUCAMPO = o.NUCAMPO
WHERE c.NOMETAB = 'TSIIRE'
ORDER BY c.NOMECAMPO, o.ORDEM
""")
print("TSIIRE options:")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
