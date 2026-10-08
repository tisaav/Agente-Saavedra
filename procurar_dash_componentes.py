from sankhya_client import SankhyaClient
import json

client = SankhyaClient()

def query(sql, label=""):
    print("=" * 80)
    print(f"--- {label} ---")
    try:
        res = client.execute_query(sql)
        f_meta = res.get("responseBody", {}).get("fieldsMetadata", [])
        fields = [f.get("name") for f in f_meta]
        rows = res.get("responseBody", {}).get("rows", [])
        print(f"Colunas: {fields}")
        print(f"Total registros: {len(rows)}")
        for r in rows:
            print(" ", dict(zip(fields, r)))
        return fields, rows
    except Exception as e:
        print(f"ERRO: {e}")
        return None, None

# 1. LGH_LICMENU
query("SELECT * FROM LGH_LICMENU", "LGH_LICMENU")

# 2. Procurar em TSILAN por '2302' ou 'Contrato'
query("SELECT NULAN, NOME, DESCRICAO, IDENTIFICADOR FROM TSILAN WHERE NOME LIKE '%2302%' OR NOME LIKE '%CONTRATO%' OR DESCRICAO LIKE '%2302%' OR DESCRICAO LIKE '%CONTRATO%'", "TSILAN")

# 3. Procurar em TSIPAN (Painéis)
query("SELECT NUINST, TITULO, DESCRICAO FROM TSIPAN WHERE TITULO LIKE '%2302%' OR TITULO LIKE '%CONTRATO%' OR TITULO LIKE '%LICITA%'", "TSIPAN")

# 4. Procurar em TSIGAD (Gadgets)
query("SELECT CODGAD, TITULO FROM TSIGAD WHERE TITULO LIKE '%2302%' OR TITULO LIKE '%CONTRATO%' OR TITULO LIKE '%LICITA%'", "TSIGAD")
