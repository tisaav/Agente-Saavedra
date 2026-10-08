with open('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml', 'r', encoding='utf-8') as f:
    c = f.read()

import re
m = re.search(r'<variable name="CONTA9DIG".*?</variable>', c, re.DOTALL)
if m:
    print(m.group(0))
