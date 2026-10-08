import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("SELECT TOP 5 * FROM TDDOPC")
print("TDDOPC columns:", [f['name'] for f in res.get('responseBody', {}).get('fieldsMetadata', [])])
print("TDDOPC sample:", res.get('responseBody', {}).get('rows', []))
