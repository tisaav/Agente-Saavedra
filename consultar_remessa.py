from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("SELECT COUNT(*) FROM TSIREM")
print("Total TSIREM:", res.get('responseBody', {}).get('rows'))

res = c.execute_query("SELECT MAX(CODIGO) FROM TSIREM")
print("Max CODIGO TSIREM:", res.get('responseBody', {}).get('rows'))

# Let's check if there are other tables related to remessa:
res = c.execute_query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME = 'NROREMESSA'")
print("Tables with NROREMESSA:", res.get('responseBody', {}).get('rows'))
