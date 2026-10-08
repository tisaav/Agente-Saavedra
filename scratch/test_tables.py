import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
rows = res.get('responseBody', {}).get('rows', [])
print(f"Total tables: {len(rows)}")
rem_tables = [r[0] for r in rows if any(k in r[0].upper() for k in ['REM', 'LAY', 'REC', 'IRE', 'EDI', 'FORMAT'])]
print("Matching tables:", rem_tables)
