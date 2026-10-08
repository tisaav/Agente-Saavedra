from sankhya_client import SankhyaClient

client = SankhyaClient()

# Vamos consultar as tabelas com "DSH" ou "GAD"
tables = ["TSIDSH", "TSIGAD", "TSIBIGDG", "TSIPAN", "TSILAN", "TSIBI", "TSIAPU"]

for t in tables:
    try:
        res = client.execute_query(f"SELECT TOP 1 * FROM {t}")
        f_meta = [f.get("name") for f in res.get("responseBody", {}).get("fieldsMetadata", [])]
        print(f"[OK] Tabela {t} existe! Colunas: {f_meta}")
        cnt = client.execute_query(f"SELECT COUNT(*) FROM {t}").get("responseBody", {}).get("rows", [[0]])[0][0]
        print(f"     Total registros em {t}: {cnt}")
    except Exception as e:
        print(f"[FALHA] Tabela {t}: {e}")
