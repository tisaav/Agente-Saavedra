from sankhya_client import SankhyaClient
import xml.etree.ElementTree as ET

client = SankhyaClient()

# Lê o XML recém-criado
with open("gadget_57_dash2302_CORRIGIDO.xml", "r", encoding="utf-8") as f:
    xml_content = f.read()

# Valida se o XML é bem formado
root = ET.fromstring(xml_content)
print("[OK] XML sintaticamente válido!")

# Extrai o SQL
expr_node = root.find(".//expression")
sql = expr_node.text.strip()

# Simula com parâmetros reais do HCPA (Contrato 8 e 332)
sql_test = sql.replace(":PERIODO.INI", "'2022-01-01'")
sql_test = sql_test.replace(":PERIODO.FIN", "'2028-12-31'")
sql_test = sql_test.replace(":CODPARC", "221")
sql_test = sql_test.replace(":NUMCONTRATO", "NULL")
sql_test = sql_test.replace(":CODPROD", "NULL")
sql_test = sql_test.replace(":SITUACAO", "'T'")

res = client.execute_query(sql_test)
rows = res.get("responseBody", {}).get("rows", [])
print(f"[OK] Query executada com sucesso absoluto! Total de linhas retornadas: {len(rows)}")
for r in rows:
    # Mostra Contrato, Produto, Previsto, Faturado, Saldo
    contrato = r[0]
    pregao = r[2]
    codprod = r[9]
    prev = r[15]
    prog = r[17]
    fat = r[18]
    sld = r[20]
    print(f"Contrato: {contrato} | Pregão: {pregao} | Prod: {codprod} | Prev: {prev} | Prog: {prog} | Fat: {fat} | Saldo: {sld}")
