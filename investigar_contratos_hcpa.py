from sankhya_client import SankhyaClient
import json

client = SankhyaClient()

def query(sql, label=""):
    print("=" * 80)
    print(f"--- {label} ---")
    print(f"SQL: {sql}")
    try:
        res = client.execute_query(sql)
        f_meta = res.get("responseBody", {}).get("fieldsMetadata", [])
        fields = [f.get("name") for f in f_meta]
        rows = res.get("responseBody", {}).get("rows", [])
        print(f"Colunas ({len(fields)}): {fields}")
        print(f"Total registros: {len(rows)}")
        for i, r in enumerate(rows):
            # Formata como dict para facilitar leitura
            row_dict = dict(zip(fields, r))
            print(f"[{i+1}] {json.dumps(row_dict, default=str, ensure_ascii=False)}")
        return fields, rows
    except Exception as e:
        print(f"ERRO: {e}")
        return None, None

# 1. Consultar Contratos 8 e 332 na TCSCON
query("""
SELECT 
    NUMCONTRATO, CODPARC, DTCONTRATO, DTINIC, DTFIM, ATIVO, 
    LGH_NULINC, LGH_PROCESSO, AD_PREGAO, CODMOD
FROM TCSCON 
WHERE NUMCONTRATO IN (8, 332)
""", "TCSCON: Contratos 8 e 332")

# 2. Consultar na LGH_LICCONT
query("""
SELECT * 
FROM LGH_LICCONT 
WHERE NUMCONTRATO IN (8, 332)
""", "LGH_LICCONT: Contratos 8 e 332")

# 3. Consultar na LGH_LICCAB se temos Proposta 27 ou Aditivo 1304
query("""
SELECT * 
FROM LGH_LICCAB 
WHERE NULIC IN (27, 1304) OR NUMCONTRATO IN (8, 332) OR PROCESSO LIKE '%27%' OR PREGAO LIKE '%27%'
""", "LGH_LICCAB: Proposta 27 / Aditivo 1304")
