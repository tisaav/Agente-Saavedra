from sankhya_client import SankhyaClient

client = SankhyaClient()

res = client.execute_query("SELECT CONFIG FROM TSIGDG WHERE NUGDG = 210")
config = res.get("responseBody", {}).get("rows", [[None]])[0][0]
if config:
    # Mostra os primeiros 1500 caracteres da query
    start_pos = config.find("<expression")
    end_pos = config.find("</expression>")
    if start_pos != -1 and end_pos != -1:
        print("SQL Gadget 210:")
        print(config[start_pos:start_pos+1500])
