with open('modelos_safra/Boleto_Itau.jrxml', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

# Find all elements around y <= 35 and y between 260 and 310
elements = re.findall(r'<(staticText|textField|image|line)[^>]*>.*?</\1>', text, re.DOTALL)
print("Total elements:", len(elements))

print("\n--- ELEMENTS IN TOP HEADER (Recibo do Pagador) ---")
for el in elements:
    if re.search(r'y="([0-9]|1[0-9]|2[0-9])"', el):
        # clean print
        lines = [l.strip() for l in el.splitlines() if l.strip()]
        print(" ".join(lines)[:150])

print("\n--- ELEMENTS IN MIDDLE HEADER (Ficha de Compensacao) ---")
for el in elements:
    if re.search(r'y="(26[0-9]|27[0-9]|28[0-9]|29[0-9]|30[0-9])"', el):
        lines = [l.strip() for l in el.splitlines() if l.strip()]
        print(" ".join(lines)[:150])
