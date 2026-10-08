from sankhya_client import SankhyaClient

client = SankhyaClient()

res = client.execute_query("SELECT NUGDG, TITULO, DESCRICAO, CONFIG FROM TSIGDG WHERE NUGDG = 57")
rows = res.get("responseBody", {}).get("rows", [])
if rows:
    nugdg, titulo, desc, config = rows[0]
    print(f"Gadget: {nugdg} - {titulo}")
    with open("gadget_57_dash2302_config.xml", "w", encoding="utf-8") as f:
        f.write(config)
    print("Salvo com sucesso em 'gadget_57_dash2302_config.xml'! Tamanho:", len(config))
else:
    print("Gadget 57 não encontrado!")
