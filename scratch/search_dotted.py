import sys
sys.path.append(r'c:\Users\SAAV166\Documents\Agente')
from sankhya_client import SankhyaClient

c = SankhyaClient()
sql = """
SELECT TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE DATA_TYPE IN ('varchar', 'nvarchar', 'char', 'nchar')
"""
res = c.execute_query(sql)
cols = res.get('responseBody', {}).get('rows', [])
print(f"Total string cols: {len(cols)}")

# Let's search columns that might be layout/formatador
for tbl, col in cols:
    if any(k in tbl.upper() for k in ['REM', 'LAY', 'REC', 'IRE', 'EDI', 'FOR', 'CTA', 'BCO', 'BAN', 'CNAB', 'ARQ']):
        try:
            check_q = f"SELECT TOP 1 {col} FROM {tbl} WHERE {col} LIKE '%HEADER SAFRA%' OR {col} LIKE '%27.01.00.00%'"
            r = c.execute_query(check_q)
            rows = r.get('responseBody', {}).get('rows', [])
            if rows:
                print(f"FOUND IN {tbl}.{col} -> {rows[0]}")
        except:
            pass
