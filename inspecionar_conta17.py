from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT NOMETAB, NOMECAMPO, DESCRCAMPO
FROM TDDFLD 
WHERE NOMECAMPO IN ('TIPOBOLETO', 'INDNOSSONUM')
""")
for r in res.get('responseBody', {}).get('rows', []):
    print(r)
