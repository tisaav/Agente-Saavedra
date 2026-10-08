import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT NOMETAB, DESCRTAB
FROM TDDTAB
WHERE DESCRTAB LIKE '%REMESSA%' OR DESCRTAB LIKE '%FORMATADOR%' OR DESCRTAB LIKE '%LAYOUT%'
""")
print("=== TABLES LIKE REMESSA/LAYOUT ===")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
