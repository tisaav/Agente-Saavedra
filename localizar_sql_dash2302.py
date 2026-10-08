from sankhya_client import SankhyaClient
import json

client = SankhyaClient()

def search_text_in_db(needle):
    print(f"=== Buscando '{needle}' em sys.sql_modules ===")
    sql = f"""
    SELECT OBJECT_NAME(m.object_id) AS OBJ_NAME, o.type_desc
    FROM sys.sql_modules m
    JOIN sys.objects o ON m.object_id = o.object_id
    WHERE m.definition LIKE '%{needle}%'
    """
    try:
        res = client.execute_query(sql)
        rows = res.get("responseBody", {}).get("rows", [])
        print(f"Encontrados em sys.sql_modules: {len(rows)}")
        for r in rows:
            print(f"  • {r[0]} ({r[1]})")
    except Exception as e:
        print("Erro em sys.sql_modules:", e)

    # Buscar em tabelas que possam guardar XMLs ou SQLs de Dashboards do Sankhya (ex: TSIDSH, TSIGAD, AD_, etc.)
    print(f"\n=== Buscando '{needle}' em tabelas de Dash/Gadget do Sankhya ===")
    candidate_tables = [
        ("TSIGAD", "EXPRESSAO"),
        ("TSIGAD", "SQL"),
        ("TSIPAN", "CONFIG"),
        ("TDDSQL", "TEXTO"),
        ("TSISYS", "PARAMETROS"),
        ("TSIFAS", "EXPRESSAO")
    ]
    for tab, col in candidate_tables:
        try:
            sql_check = f"SELECT TOP 5 * FROM {tab} WHERE CAST({col} AS NVARCHAR(MAX)) LIKE '%{needle}%'"
            res = client.execute_query(sql_check)
            rows = res.get("responseBody", {}).get("rows", [])
            if rows:
                print(f"  [+] Encontrado na tabela {tab}.{col}! Total: {len(rows)}")
        except Exception:
            pass

search_text_in_db("LGH_LICITECON")
search_text_in_db("2302")
