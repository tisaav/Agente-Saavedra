import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
# Let's search columns with varchar/char that might contain 'HEADER SAFRA'
sql = """
DECLARE @SearchStr NVARCHAR(100) = '%HEADER SAFRA%'
SELECT t.name AS TableName, c.name AS ColumnName
FROM sys.tables t
JOIN sys.columns c ON t.object_id = c.object_id
JOIN sys.types ty ON c.user_type_id = ty.user_type_id
WHERE ty.name IN ('varchar', 'nvarchar', 'char', 'nchar', 'text')
  AND t.name NOT LIKE 'sys%'
"""
res = c.execute_query(sql)
cols = res.get('responseBody', {}).get('rows', [])
print(f"Total string columns: {len(cols)}")

# Let's filter candidate tables
candidate_tables = set()
for r in cols:
    tname, cname = r[0], r[1]
    if any(k in tname.upper() for k in ['REM', 'EDI', 'BAN', 'CTA', 'LAY', 'REC', 'IRE', 'FOR', 'MOD', 'CAD']):
        candidate_tables.add(tname)

print("Candidate tables:", candidate_tables)

for t in candidate_tables:
    try:
        q = f"SELECT TOP 1 * FROM {t} WHERE 1=0"
        # Just check
        res2 = c.execute_query(f"SELECT COUNT(*) FROM {t}")
        cnt = res2.get('responseBody', {}).get('rows', [[0]])[0][0]
        if cnt > 0:
            # check if header safra is in any column
            t_cols = [r[1] for r in cols if r[0] == t]
            where_clauses = [f"{col} LIKE '%HEADER SAFRA%'" for col in t_cols[:10]]
            check_q = f"SELECT TOP 1 {t_cols[0]} FROM {t} WHERE {' OR '.join(where_clauses)}"
            r3 = c.execute_query(check_q)
            if r3.get('responseBody', {}).get('rows'):
                print(f"FOUND IN TABLE {t}!!!")
    except Exception as e:
        pass
