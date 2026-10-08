import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
try:
    r = c.execute_query("SELECT 1 FROM DUAL")
    print("ORACLE! Result:", r.get('responseBody', {}).get('rows'))
except Exception as e:
    print("Not Oracle:", e)

try:
    r = c.execute_query("SELECT @@version")
    print("SQL SERVER! Result:", r.get('responseBody', {}).get('rows'))
except Exception as e:
    print("Not SQL Server:", e)
