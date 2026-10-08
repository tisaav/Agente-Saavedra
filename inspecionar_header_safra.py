with open('modelos_safra/Bol_Safra.jrxml', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Safra' in line or '422' in line or 'image' in line or 'BANCO' in line or 'staticText-24' in line or 'staticText-55' in line:
        start = max(0, i - 5)
        end = min(len(lines), i + 15)
        print(f"=== Around line {i+1} ===")
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}", end='')
