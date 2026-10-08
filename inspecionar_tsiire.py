from sankhya_client import SankhyaClient

c = SankhyaClient()
res = c.execute_query("""
SELECT SEQUENCIA, CAMPO, TAMANHO, TIPO
FROM TSIIRE
WHERE CODIGO = 15010100
ORDER BY SEQUENCIA
""")
print("=== BRADESCO 400 HEADER (15010100) ===")
pos = 1
for r in res.get('responseBody', {}).get('rows', []):
    seq, campo, tam, tipo = r
    end_pos = pos + tam - 1
    print(f"Seq {seq:02d} | Pos {pos:03d}-{end_pos:03d} | Tam {tam:03d} | Tipo {tipo} | {campo}")
    pos = end_pos + 1
