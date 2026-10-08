import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT NOMETAB, NOMECAMPO, OPCAO, DESCRICAO
FROM TDDOPC
WHERE NOMETAB IN ('TSIIRE', 'TSIREM', 'TSIREC')
ORDER BY NOMETAB, NOMECAMPO, ORDEM
""")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
