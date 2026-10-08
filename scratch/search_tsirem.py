import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT TOP 10 *
FROM TSIREM
""")
print("TSIREM fields:", [f['name'] for f in res.get('responseBody', {}).get('fieldsMetadata', [])])
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
