import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
print("TGFFCT (Formatador Remessa por Conta):")
res = c.execute_query("SELECT * FROM TGFFCT")
print([f['name'] for f in res.get('responseBody', {}).get('fieldsMetadata', [])])
for r in res.get('responseBody', {}).get('rows', []):
    print(r)

print("TGFHGR (Historico de Geracao de Remessa Bancaria):")
res2 = c.execute_query("SELECT TOP 5 * FROM TGFHGR ORDER BY DHGERACAO DESC")
print([f['name'] for f in res2.get('responseBody', {}).get('fieldsMetadata', [])])
for r in res2.get('responseBody', {}).get('rows', []):
    print(r)
