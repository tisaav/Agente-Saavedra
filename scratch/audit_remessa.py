remessa_text = """01REMESSA01COBRANCA       00700005843919      SAAVEDRA REPRESENTACOES LTDA  422BANCO SAFRA    081026                                                                                                                                                                                                                                                                                                   005000001
1029266681700011100700005843919      0000000000000000000111173109000261                              000 0510124985-1   13112600000002325114220000701N160726161000000000000770000000000000000000000000000000013112602000000287317764001084SOCIEDADE SULINA DIVINA PROVIDENCIA     R DA GRUTA, 145                         CASCATA     91712160Porto Alegre   RS                                     422005000002
1029266681700011100700005843919      0000000000000000000111172109000261                              000 0510124983-1   13112600000001310154220000701N160726161000000000000430000000000000000000000000000000013112602000000287317764001084SOCIEDADE SULINA DIVINA PROVIDENCIA     R DA GRUTA, 145                         CASCATA     91712160Porto Alegre   RS                                     422005000003
1029266681700011100700005843919      0000000000000000000111385000000612                              000 0510125054-1   17112600000001606804220000701N200726161000000000000530000000000000000000000000000000017112602000000288625686002443ASSOCIACAO EDUCADORA SAO CARLOS - AESC  R JOSE DE ALENCAR, 286                  MENINO DEU  90880481Porto Alegre   RS                                     422005000004
1029266681700011100700005843919      0000000000000000000111181000000604                              000 0510124993-1   13112600000002964634220000701N160726161000000000000980000000000000000000000000000000013112602000000288625686002443ASSOCIACAO EDUCADORA SAO CARLOS - AESC  R JOSE DE ALENCAR, 286                  MENINO DEU  90880481Porto Alegre   RS                                     422005000005
9                                                                                                                                                                                                                                                                                                                                                                               00000004000000000820669005000006"""

lines = remessa_text.strip().split('\n')
print(f"Total lines: {len(lines)}")
for i, l in enumerate(lines):
    print(f"Line {i+1} length: {len(l)}")

header = lines[0]
print("\n=== HEADER AUDIT ===")
print("Pos 001-009 (Identif):", header[0:9])
print("Pos 010-026 (Literal):", header[9:26])
print("Pos 027-040 (Ag/Conta):", f"'{header[26:40]}'")
print("Pos 041-046 (Brancos):", f"'{header[40:46]}'")
print("Pos 047-076 (Razão Social):", f"'{header[46:76]}'")
print("Pos 077-079 (Código Banco):", f"'{header[76:79]}'")
print("Pos 080-094 (Nome Banco):", f"'{header[79:94]}'")
print("Pos 095-100 (Data Gravação):", f"'{header[94:100]}'")
print("Pos 395-400 (Sequencial):", f"'{header[394:400]}'")

print("\n=== DETALHE LINES AUDIT ===")
for i, d in enumerate(lines[1:5]):
    print(f"\n--- Detalhe {i+1} (Nota) ---")
    print("Pos 001-001 (Tipo Reg):", d[0:1])
    print("Pos 002-003 (Tipo Inscr):", d[1:3])
    print("Pos 004-017 (CNPJ Cedente):", d[3:17])
    print("Pos 018-031 (Ag/Conta):", f"'{d[17:31]}'")
    print("Pos 038-062 (Nosso Controle / NUFIN):", f"'{d[37:62]}'")
    print("Pos 063-071 (Nosso Número):", f"'{d[62:71]}'")
    print("Pos 106-107 (Dias Protesto):", f"'{d[105:107]}'")
    print("Pos 108-108 (Carteira):", f"'{d[107:108]}'")
    print("Pos 109-110 (Ocorrência):", f"'{d[108:110]}'")
    print("Pos 111-120 (Seu Número):", f"'{d[110:120]}'")
    print("Pos 121-126 (Vencimento):", f"'{d[120:126]}'")
    print("Pos 127-139 (Valor Título):", f"'{d[126:139]}'")
    print("Pos 140-142 (Banco):", f"'{d[139:142]}'")
    print("Pos 143-147 (Agência):", f"'{d[142:147]}'")
    print("Pos 148-149 (Espécie):", f"'{d[147:149]}'")
    print("Pos 150-150 (Aceite):", f"'{d[149:150]}'")
    print("Pos 151-156 (Emissão):", f"'{d[150:156]}'")
    print("Pos 157-158 (1a Instrução):", f"'{d[156:158]}'")
    print("Pos 159-160 (2a Instrução):", f"'{d[158:160]}'")
    print("Pos 161-173 (Juros diários):", f"'{d[160:173]}'")
    print("Pos 206-211 (Data Multa):", f"'{d[205:211]}'")
    print("Pos 212-215 (Perc Multa):", f"'{d[211:215]}'")
    print("Pos 216-218 (Zeros Multa):", f"'{d[215:218]}'")
    print("Pos 219-220 (Tipo Inscr Pagador):", f"'{d[218:220]}'")
    print("Pos 221-234 (CNPJ/CPF Pagador):", f"'{d[220:234]}'")
    print("Pos 235-274 (Nome Pagador):", f"'{d[234:274]}'")
    print("Pos 275-314 (Endereço Pagador):", f"'{d[274:314]}'")
    print("Pos 315-326 (Bairro Pagador):", f"'{d[314:326]}'")
    print("Pos 327-334 (CEP Pagador):", f"'{d[326:334]}'")
    print("Pos 335-349 (Cidade Pagador):", f"'{d[334:349]}'")
    print("Pos 350-351 (UF Pagador):", f"'{d[349:351]}'")
    print("Pos 392-394 (Num Remessa):", f"'{d[391:394]}'")
    print("Pos 395-400 (Sequencial Registro):", f"'{d[394:400]}'")
