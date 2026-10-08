import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sankhya_client import SankhyaClient

c = SankhyaClient()
# Let's search tables with columns containing TITULO or DESCRICAO
tables = ['TSILAY', 'TSIFOR', 'TGFPAR', 'TSIREM', 'TSIIRF', 'TSIREC', 'TSIIRE', 'TSICTA', 'TDDFLD', 'TSIRGL', 'TSICPO']
for t in ['TSILAY', 'TSIREC', 'TSIIRE', 'TSIFOR', 'TSIIRF', 'TSIBLC', 'TSICPO']:
    try:
        res = c.execute_query(f"SELECT TOP 5 * FROM {t}")
        print(f"Table {t} exists! Columns: {[f['name'] for f in res.get('responseBody', {}).get('fieldsMetadata', [])]}")
    except Exception as e:
        pass
