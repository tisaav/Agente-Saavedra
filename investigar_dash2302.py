from sankhya_client import SankhyaClient
import json

client = SankhyaClient()

def test_query(sql, label=""):
    print("=" * 60)
    print(f"QUERY [{label}]: {sql}")
    try:
        res = client.execute_query(sql)
        f_meta = res.get("responseBody", {}).get("fieldsMetadata", [])
        fields = [f.get("name") for f in f_meta]
        rows = res.get("responseBody", {}).get("rows", [])
        print(f"Campos: {fields}")
        print(f"Total retornado: {len(rows)}")
        for i, r in enumerate(rows[:10]):
            print(f"  {i+1}: {r}")
        return fields, rows
    except Exception as e:
        print(f"ERRO: {e}")
        return None, None

# 1. Procurar onde o 2302 está cadastrado (TSILAN, TSIDSH, TSIPAN, TSIGAD, etc.)
test_query("SELECT NULAN, NOME, DESCRICAO, IDENTIFICADOR FROM TSILAN WHERE NULAN = 2302 OR IDENTIFICADOR LIKE '%2302%'", "TSILAN")
test_query("SELECT NUINST, TITULO FROM TSIPAN WHERE NUINST = 2302 OR TITULO LIKE '%2302%' OR TITULO LIKE '%CONTRATO%'", "TSIPAN")
test_query("SELECT CODGAD, TITULO FROM TSIGAD WHERE CODGAD = 2302 OR TITULO LIKE '%2302%' OR TITULO LIKE '%CONTRATO%'", "TSIGAD")
