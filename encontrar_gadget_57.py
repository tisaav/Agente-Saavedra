from sankhya_client import SankhyaClient

client = SankhyaClient()

# Procurar tabelas com GAD ou GDG
sql = """
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME LIKE '%GDG%' OR TABLE_NAME LIKE '%GAD%' OR TABLE_NAME LIKE '%DSB%'
"""
res = client.execute_query(sql)
tables = [r[0] for r in res.get("responseBody", {}).get("rows", [])]
print("Tabelas encontradas:", tables)

for t in tables:
    try:
        r = client.execute_query(f"SELECT * FROM [{t}] WHERE 1=0")
        f_meta = [f.get("name") for f in r.get("responseBody", {}).get("fieldsMetadata", [])]
        print(f"Tabela {t} colunas: {f_meta}")
        
        # Testa se tem id 57
        id_cols = [c for c in f_meta if 'GDG' in c or 'GAD' in c or 'ID' in c]
        for c in id_cols:
            chk = client.execute_query(f"SELECT COUNT(*) FROM [{t}] WHERE [{c}] = 57").get("responseBody", {}).get("rows", [[0]])[0][0]
            if chk > 0:
                print(f"  >>> ENCONTRADO GADGET 57 em {t}.{c}!")
    except Exception as e:
        pass
