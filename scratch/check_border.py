with open('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml', 'r', encoding='utf-8') as f:
    c = f.read()

import re
# Check borders and table lines at the right
# The table borders usually have width = 535 or x + width = 535
matches = re.findall(r'<reportElement[^>]*x=\"([0-9]+)\"[^>]*width=\"([0-9]+)\"[^>]*y=\"504\"', c)
for x, w in matches:
    print(f"y=504: x={x}, w={w}, right={int(x)+int(w)}")

# Let's check the line at the top of the table:
for m in re.finditer(r'<line[^>]*>.*?</line>', c, re.DOTALL):
    line_str = m.group(0)
    if 'y="503"' in line_str or 'y="504"' in line_str or '53' in line_str:
        print(line_str)
