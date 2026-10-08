from sankhya_client import SankhyaClient

client = SankhyaClient()

# Vamos procurar qual tabela tem o título 'DASH - ACOMPANHAMENTO CONTRATOS DE LICITACAO' ou 'ACOMPANHAMENTO CONTRATOS'
sql = """
DECLARE @SearchStr NVARCHAR(100) = '%ACOMPANHAMENTO CONTRATOS%'
SELECT 
    t.name AS TableName, 
    c.name AS ColumnName
FROM sys.tables t
JOIN sys.columns c ON t.object_id = c.object_id
JOIN sys.types ty ON c.user_type_id = ty.user_type_id
WHERE ty.name IN ('varchar', 'nvarchar', 'text', 'ntext')
"""

res = client.execute_query(sql)
rows = res.get("responseBody", {}).get("rows", [])
print(f"Total de colunas de texto no banco: {len(rows)}")

# Filtrar tabelas candidatas mais prováveis
filtered = [r for r in rows if any(k in r[0].upper() for k in ['DASH', 'GAD', 'BI', 'MOD', 'SYS', 'LAN', 'CON', 'LGH', 'AD_', 'TDD', 'TSI'])]
print(f"Candidatas filtradas: {len(filtered)}")

for tab, col in filtered:
    try:
        check_sql = f"SELECT 1 FROM [{tab}] WHERE CAST([{col}] AS NVARCHAR(MAX)) LIKE '%ACOMPANHAMENTO CONTRATOS%'"
        chk = client.execute_query(check_sql)
        found = chk.get("responseBody", {}).get("rows", [])
        if found:
            print(f">>> ENCONTRADO em: {tab}.{col} ! Total: {len(found)}")
    except Exception:
        pass
