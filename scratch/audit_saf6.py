with open(r'C:\Users\SAAV166\Desktop\safra\SAF_6.rem', 'r', encoding='latin1') as f:
    lines = [line.rstrip('\r\n') for line in f if line.strip()]

print(f"Total lines in SAF_6.rem: {len(lines)}")
for i, l in enumerate(lines):
    print(f"Line {i+1}: length={len(l)}")

header = lines[0]
print("\n=== HEADER ===")
print("Pos 001-009:", header[0:9])
print("Pos 010-026:", header[9:26])
print("Pos 027-040 (Ag/Conta):", header[26:40])
print("Pos 047-076 (Cedente):", header[46:76])
print("Pos 077-079 (Banco):", header[76:79])
print("Pos 080-094 (Nome Banco):", header[79:94])
print("Pos 095-100 (Data):", header[94:100])
print("Pos 395-400 (Seq):", header[394:400])

print("\n=== DETALHES ===")
for i, d in enumerate(lines[1:-1]):
    print(f"\n--- Detalhe {i+1} ---")
    print(f"Tipo Reg: {d[0:1]}")
    print(f"CNPJ Cedente: {d[3:17]}")
    print(f"Ag/Conta: '{d[17:31]}'")
    print(f"NUFIN (pos 38-62): '{d[37:62].strip()}'")
    print(f"Nosso Número (pos 63-71): '{d[62:71]}'")
    print(f"Carteira (pos 108): '{d[107:108]}'")
    print(f"Ocorrência (pos 109-110): '{d[108:110]}'")
    print(f"Seu Número / Nota (pos 111-120): '{d[110:120]}'")
    print(f"Vencimento (pos 121-126): '{d[120:126]}'")
    print(f"Valor (pos 127-139): '{d[126:139]}'")
    print(f"Banco (pos 140-142): '{d[139:142]}'")
    print(f"Agência (pos 143-147): '{d[142:147]}'")
    print(f"1a Instrução (pos 157-158): '{d[156:158]}'")
    print(f"2a Instrução (pos 159-160): '{d[158:160]}'")
    print(f"Juros (pos 161-173): '{d[160:173]}'")
    print(f"Data Multa (pos 206-211): '{d[205:211]}'")
    print(f"Perc Multa (pos 212-215): '{d[211:215]}'")
    print(f"Zeros Multa (pos 216-218): '{d[215:218]}'")
    print(f"CNPJ Pagador (pos 221-234): '{d[220:234]}'")
    print(f"Nome Pagador (pos 235-274): '{d[234:274].strip()}'")
    print(f"Endereço (pos 275-314): '{d[274:314].strip()}'")
    print(f"CEP (pos 327-334): '{d[326:334]}'")
    print(f"Cidade/UF (pos 335-351): '{d[334:351].strip()}'")
    print(f"Num Remessa (pos 392-394): '{d[391:394]}'")
    print(f"Seq Registro (pos 395-400): '{d[394:400]}'")

trailer = lines[-1]
print("\n=== TRAILER ===")
print("Tipo Reg:", trailer[0:1])
print("Qtd Registros (pos 395-400):", trailer[394:400])
