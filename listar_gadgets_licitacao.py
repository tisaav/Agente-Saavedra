from sankhya_client import SankhyaClient

client = SankhyaClient()

# Vamos listar todos os gadgets relacionados a licitações em TSIGDG
res = client.execute_query("SELECT NUGDG, TITULO, DHALTER FROM TSIGDG WHERE TITULO LIKE '%230%' OR TITULO LIKE '%LICITA%' OR TITULO LIKE '%CONTRATO%'")
rows = res.get("responseBody", {}).get("rows", [])
for r in rows:
    print(r)
