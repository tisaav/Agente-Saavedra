with open('modelos_safra/Boleto_Itau.jrxml', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'image-1' in line or 'image-2' in line or 'BANCO ITAU' in line:
        start = max(0, i - 10)
        end = min(len(lines), i + 25)
        print(f"=== Around line {i+1} ===")
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}", end='')
