from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT NUMCONTRATO, CODPROD, QTDEPREVISTA 
FROM LGH_LICITECON 
WHERE QTDEPREVISTA = 1800
"""
res = client.execute_query(sql)
print("Contratos com previsto 1800:", res.get("responseBody", {}).get("rows", []))
