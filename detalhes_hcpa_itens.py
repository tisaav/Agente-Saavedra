from sankhya_client import SankhyaClient
import json

client = SankhyaClient()

def print_table(sql, title):
    print(f"\n{'='*20} {title} {'='*20}")
    res = client.execute_query(sql)
    f_meta = [f.get("name") for f in res.get("responseBody", {}).get("fieldsMetadata", [])]
    rows = res.get("responseBody", {}).get("rows", [])
    print(f"Total registros: {len(rows)}")
    for r in rows:
        row_dict = dict(zip(f_meta, r))
        print(row_dict)

# 1. Itens do Contrato 8 e 332
print_table("""
SELECT 
    NUMCONTRATO, CODPROD, CODVOL, VLRUNIT, QTDEPREVISTA, QTDENTREGUE, CONTROLE
FROM LGH_LICITECON 
WHERE NUMCONTRATO IN (8, 332)
""", "LGH_LICITECON (Contrato 8 e 332)")

# 2. Itens de Contrato nativo TCSCON (se houver na TCSITE)
print_table("""
SELECT 
    NUMCONTRATO, CODPROD, CODVOL, VLRUNIT, QTDPREV
FROM TCSITE 
WHERE NUMCONTRATO IN (8, 332)
""", "TCSITE (Contrato 8 e 332)")

# 3. Licitações LGH_LICCAB e LGH_LICITE para 27 e 1304
print_table("""
SELECT 
    NULIC, NUMCONTRATO, CODPARC, DTABERTURA, PROCESSO, PREGAO, NUMODALIDADE, SITUACAO
FROM LGH_LICCAB 
WHERE NULIC IN (27, 1304)
""", "LGH_LICCAB (Proposta 27 e Aditivo 1304)")

print_table("""
SELECT 
    NULIC, ITEM, CODPROD, QUANTIDADE, VLRUNIT, VLRDESCONTO, SITUACAO
FROM LGH_LICITE 
WHERE NULIC IN (27, 1304)
""", "LGH_LICITE (Itens da Proposta 27 e 1304)")
