with open('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '$V{lindig}' in line:
        print(f"lindig around line {i+1}:")
        for j in range(max(0, i-15), min(len(lines), i+10)):
            print(f"{j+1}: {lines[j]}", end='')
        print("="*40)
    if 'textField-8' in line:
        print(f"textField-8 around line {i+1}:")
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"{j+1}: {lines[j]}", end='')
        print("="*40)
    if '0584391' in line or '00700' in line:
        print(f"Agencia/Conta around line {i+1}:")
        for j in range(max(0, i-5), min(len(lines), i+10)):
            print(f"{j+1}: {lines[j]}", end='')
        print("="*40)
