with open('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'<variable[^>]*name=\"[^\"]*linha[^\"]*\".*?</variable>', c, re.DOTALL | re.IGNORECASE)
for m in matches:
    print(m)

# Let's search all occurrences of LINHADIGITAVEL in the file:
print("\nOccurrences of LINHADIGITAVEL:")
for m in re.finditer(r'LINHADIGITAVEL', c):
    print(c[max(0, m.start()-50):min(len(c), m.end()+150)])
    print("---")
