import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT NOMETAB, NOMECAMPO, OPCAO, DESCRICAO
FROM TDDOPC
WHERE DESCRICAO LIKE '%Alfanum%' OR OPCAO IN ('C', 'E', 'A', 'D')
""")
print("TDDOPC results:")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
