import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
print("Count TDDOPC:", c.execute_query("SELECT COUNT(*) FROM TDDOPC").get('responseBody', {}).get('rows'))
print("Count TDDFLD:", c.execute_query("SELECT COUNT(*) FROM TDDFLD").get('responseBody', {}).get('rows'))
