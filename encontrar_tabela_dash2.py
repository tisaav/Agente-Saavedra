from sankhya_client import SankhyaClient

client = SankhyaClient()

sql = """
SELECT t.name AS TableName, c.name AS ColumnName
FROM sys.tables t
JOIN sys.columns c ON t.object_id = c.object_id
JOIN sys.types ty ON c.user_type_id = ty.user_type_id
WHERE ty.name IN ('varchar', 'nvarchar', 'text', 'ntext')
  AND (t.name LIKE 'TSI%' OR t.name LIKE 'TDD%' OR t.name LIKE 'AD_%' OR t.name LIKE 'LGH_%')
"""

res = client.execute_query(sql)
rows = res.get("responseBody", {}).get("rows", [])
print(f"Colunas de texto encontradas: {len(rows)}")

found_any = False
for tab, col in rows:
    try:
        check_sql = f"SELECT TOP 1 [{col}] FROM [{tab}] WHERE CAST([{col}] AS NVARCHAR(MAX)) LIKE '%ACOMPANHAMENTO%CONTRATO%'"
        chk = client.execute_query(check_sql)
        f_rows = chk.get("responseBody", {}).get("rows", [])
        if f_rows:
            print(f">>> ENCONTRADO em: {tab}.{col}")
            found_any = True
            # Mostra dados da linha
            full_sql = f"SELECT * FROM [{tab}] WHERE CAST([{col}] AS NVARCHAR(MAX)) LIKE '%ACOMPANHAMENTO%CONTRATO%'"
            det = client.execute_query(full_sql)
            f_meta = [f.get("name") for f in det.get("responseBody", {}).get("fieldsMetadata", [])]
            for r in det.get("responseBody", {}).get("rows", []):
                print("  Linha:", dict(zip(f_meta, r)))
    except Exception as e:
        pass

if not found_any:
    print("Nenhum match com '%ACOMPANHAMENTO%CONTRATO%'")
