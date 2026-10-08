from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT 
    CON.AD_PREGAO,
    COUNT(DISTINCT CON.NUMCONTRATO) AS QTD_CONTRATOS,
    STRING_AGG(CAST(CON.NUMCONTRATO AS VARCHAR), ', ') AS CONTRATOS,
    PAR.NOMEPARC
FROM TCSCON CON
JOIN TGFPAR PAR ON PAR.CODPARC = CON.CODPARC
WHERE CON.AD_PREGAO IS NOT NULL AND LTRIM(RTRIM(CON.AD_PREGAO)) <> ''
GROUP BY CON.AD_PREGAO, PAR.NOMEPARC
HAVING COUNT(DISTINCT CON.NUMCONTRATO) > 1
ORDER BY QTD_CONTRATOS DESC
"""
res = client.execute_query(sql)
rows = res.get("responseBody", {}).get("rows", [])
print(f"Total de pregões com mais de 1 contrato: {len(rows)}")
for r in rows:
    print(r)
