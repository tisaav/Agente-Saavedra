from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT 
    CON.NUMCONTRATO,
    CON.AD_PREGAO,
    CON.LGH_PROCESSO,
    CON.AD_NUMEROCONTRATOCLIENTE,
    CON.DTCONTRATO,
    CON.DTTERMINO,
    PAR.NOMEPARC
FROM TCSCON CON
JOIN TGFPAR PAR ON PAR.CODPARC = CON.CODPARC
WHERE CON.NUMCONTRATO IN (181, 286, 61, 43, 1, 59, 94, 64)
ORDER BY CON.AD_PREGAO, CON.NUMCONTRATO
"""
res = client.execute_query(sql)
rows = res.get("responseBody", {}).get("rows", [])
for r in rows:
    print(r)
