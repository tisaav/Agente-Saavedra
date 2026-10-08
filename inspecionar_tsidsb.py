from sankhya_client import SankhyaClient
import json

client = SankhyaClient()

res = client.execute_query("SELECT TOP 5 * FROM TSIDSB")
fields = [f.get("name") for f in res.get("responseBody", {}).get("fieldsMetadata", [])]
print("Colunas de TSIDSB:", fields)

# Vamos procurar 2302 ou CONTRATOS em TSIDSB
res2 = client.execute_query("SELECT * FROM TSIDSB WHERE TITULO LIKE '%2302%' OR TITULO LIKE '%CONTRATO%' OR NUDSB = 2302 OR TITULO LIKE '%LICITA%'")
fields2 = [f.get("name") for f in res2.get("responseBody", {}).get("fieldsMetadata", [])]
rows2 = res2.get("responseBody", {}).get("rows", [])
print(f"Total encontrados em TSIDSB: {len(rows2)}")
for r in rows2:
    d = dict(zip(fields2, r))
    # Remove campos muito longos para não poluir
    for k in list(d.keys()):
        if isinstance(d[k], str) and len(d[k]) > 100:
            d[k] = d[k][:100] + "..."
    print(d)
