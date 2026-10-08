import os
from pypdf import PdfReader

rem_file = 'c:/Users/SAAV166/Documents/Agente/safra_auditoria/SAF_6.rem'
with open(rem_file, 'r', encoding='latin1') as f:
    rem_lines = [l.rstrip('\r\n') for l in f]

header = rem_lines[0]
details = rem_lines[1:-1]
trailer = rem_lines[-1]

folder = 'c:/Users/SAAV166/Documents/Agente/safra_auditoria'
pdf_files = ['boleto.pdf', 'boleto (1).pdf', 'boleto (2).pdf', 'boleto (3).pdf']

print("=" * 60)
print("AUDITORIA COMPLETA - SAFRA CNAB 400 & BOLETOS")
print("=" * 60)
print(f"HEADER: Agencia/Conta={header[26:40]} | Banco={header[76:79]} | Razao={header[46:76].strip()}")
print(f"TRAILER: Qtd={trailer[368:374]} | Total Centavos={trailer[374:387]}")
print("-" * 60)

pdf_data = []
for name in pdf_files:
    reader = PdfReader(os.path.join(folder, name))
    text = reader.pages[0].extract_text()
    
    linha = ''
    for l in text.split('\n'):
        if '42297.' in l:
            pos = l.find('42297.')
            linha = l[pos:].strip()
            break
            
    pdf_data.append({
        'filename': name,
        'full_text': text,
        'linha_digitavel': linha
    })

for idx, d in enumerate(details):
    nosso_num = d[62:71].strip()
    doc_rem = d[110:120].strip()
    venc_rem = d[120:126] # DDMMAA
    venc_rem_fmt = f"{venc_rem[0:2]}/{venc_rem[2:4]}/20{venc_rem[4:6]}"
    valor_centavos = int(d[126:139])
    valor_fmt = f"{valor_centavos/100:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.')
    pagador = d[234:274].strip()
    
    nota_num = doc_rem.split('-')[0]
    
    print(f"\n[TITULO {idx+1}] NOTA FISCAL {nota_num} (Doc: {doc_rem})")
    print(f"  Remessa -> Nosso Num: {nosso_num} | Venc: {venc_rem_fmt} | Valor: R$ {valor_fmt}")
    print(f"  Remessa -> Ocorrencia: {d[108:110]} | Agencia/Conta: {d[17:31]} | Especie: {d[147:149]}")
    
    # Encontrar PDF correspondente
    match = None
    for p in pdf_data:
        if nota_num in p['full_text']:
            match = p
            break
            
    if match:
        print(f"  Boleto PDF -> Arquivo: {match['filename']}")
        print(f"  Boleto PDF -> Linha Digitavel: {match['linha_digitavel']}")
        has_cnpj = "92.666.817/0001-11" in match['full_text']
        has_venc = venc_rem_fmt in match['full_text']
        has_valor = valor_fmt in match['full_text']
        print(f"  Boleto PDF -> CNPJ Beneficiario completo: {'OK' if has_cnpj else 'ERRO'}")
        print(f"  Boleto PDF -> Vencimento confere ({venc_rem_fmt}): {'OK' if has_venc else 'ERRO'}")
        print(f"  Boleto PDF -> Valor confere ({valor_fmt}): {'OK' if has_valor else 'ERRO'}")
        
        # Verificar se linha digitável bate com o Nosso Número e Agência/Conta
        # Linha digitavel Safra:
        # Bloco 1: 4229 + [campo livre 1-5] + DV
        # Bloco 2: [campo livre 6-15] + DV
        # Bloco 3: [campo livre 16-25] + DV
        # Bloco 4: DV geral
        # Bloco 5: Fator Vencimento (4 digitos) + Valor (10 digitos)
        ld = match['linha_digitavel']
        print(f"  Analise Linha Digitavel: {ld}")
    else:
        print("  Boleto PDF -> NAO ENCONTRADO!")

print("\n" + "=" * 60)
print("AUDITORIA CONCLUIDA")
print("=" * 60)
