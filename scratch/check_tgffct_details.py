import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("SELECT * FROM TGFFCT")
cols = [f['name'] for f in res.get('responseBody', {}).get('fieldsMetadata', [])]
print("TGFFCT columns:", cols)
for r in res.get('responseBody', {}).get('rows', []):
    print(dict(zip(cols, r)))
