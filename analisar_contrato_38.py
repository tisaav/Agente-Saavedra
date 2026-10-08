from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT 
    CON.NUMCONTRATO, CON.CODPARC, PAR.NOMEPARC, CON.AD_PREGAO, CON.LGH_PROCESSO,
    CON.DTCONTRATO, CON.DTTERMINO, CON.AD_NUMEROCONTRATOCLIENTE
FROM TCSCON CON
JOIN TGFPAR PAR ON PAR.CODPARC = CON.CODPARC
WHERE CON.NUMCONTRATO = 38 OR CON.AD_PREGAO = (SELECT AD_PREGAO FROM TCSCON WHERE NUMCONTRATO = 38)
"""
res = client.execute_query(sql)
rows = res.get("responseBody", {}).get("rows", [])
for r in rows:
    print(r)
