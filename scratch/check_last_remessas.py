import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT TOP 10 IDREMESSA, CODREM, NUMREMESSA, NOMEARQ, DHGERACAO, CODLAYOUT, CODCTABCOINT, VLRREMESSA
FROM TGFHGR
ORDER BY IDREMESSA DESC
""")
cols = [f['name'] for f in res.get('responseBody', {}).get('fieldsMetadata', [])]
for r in res.get('responseBody', {}).get('rows', []):
    print(dict(zip(cols, r)))
