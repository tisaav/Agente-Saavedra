import pypdf
import glob
import os

pdf_files = [
    r'C:\Users\SAAV166\Desktop\safra\boleto.pdf',
    r'C:\Users\SAAV166\Desktop\safra\boleto (1).pdf',
    r'C:\Users\SAAV166\Desktop\safra\boleto (2).pdf',
    r'C:\Users\SAAV166\Desktop\safra\boleto (3).pdf'
]

for p in pdf_files:
    print(f"\n==========================================")
    print(f"FILE: {os.path.basename(p)}")
    reader = pypdf.PdfReader(p)
    text = reader.pages[0].extract_text()
    
    # Check key lines:
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for line in lines:
        if any(k in line for k in ['422-7', '42297', '341', '00700', 'Vencimento', 'Valor', 'Nosso Número', 'Multa', 'juros', 'Protestar', 'Pagável', 'SAAVEDRA']):
            print("  ", line)
