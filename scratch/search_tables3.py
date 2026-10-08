import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sankhya_client import SankhyaClient

c = SankhyaClient()
for t in ['TSIREC', 'TSILAY', 'TSIIRF', 'TSIBLC']:
    res = c.execute_query(f"SELECT COUNT(*) FROM {t}")
    print(f"{t} count:", res.get('responseBody', {}).get('rows', []))

# Let's search for HEADER SAFRA across TSIREC and TSILAY
res = c.execute_query("SELECT * FROM TSIREC WHERE DESCRICAO LIKE '%SAFRA%' OR CODIGO LIKE '%27%'")
print("TSIREC:", res.get('responseBody', {}).get('rows', []))

res2 = c.execute_query("SELECT TOP 10 * FROM TSILAY")
print("TSILAY fields:", [f['name'] for f in res2.get('responseBody', {}).get('fieldsMetadata', [])])
print("TSILAY rows:", res2.get('responseBody', {}).get('rows', []))
