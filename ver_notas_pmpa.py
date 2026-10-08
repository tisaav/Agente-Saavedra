from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT TGFCAB.NUMCONTRATO, TGFCAB.CODTIPOPER, COUNT(*) AS QTD, SUM(TGFITE.QTDNEG) AS TOTAL_QTD
FROM TGFCAB
JOIN TGFITE ON TGFITE.NUNOTA = TGFCAB.NUNOTA
WHERE TGFCAB.CODPARC = 336 AND TGFITE.CODPROD = 324
GROUP BY TGFCAB.NUMCONTRATO, TGFCAB.CODTIPOPER
"""
res = client.execute_query(sql)
for r in res.get("responseBody", {}).get("rows", []):
    print(r)
