import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT DISTINCT NOMETAB
FROM TDDOPC
WHERE NOMETAB LIKE '%REM%' OR NOMETAB LIKE '%EDI%' OR NOMETAB LIKE '%LAY%'
""")
print(res)
