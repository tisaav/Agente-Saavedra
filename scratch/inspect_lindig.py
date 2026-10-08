with open('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml', 'r', encoding='utf-8') as f:
    c = f.read()

import re
m = re.search(r'<variable name="lindig".*?</variable>', c, re.DOTALL)
if m:
    print(m.group(0))

# Also let's check textField $V{lindig} font and width:
m2 = re.search(r'<reportElement[^>]*>[^<]*</reportElement>[^<]*<textElement[^>]*>.*?</textElement>[^<]*<textFieldExpression[^>]*>\$V\{lindig\}</textFieldExpression>', c, re.DOTALL)
if m2:
    print("TextField lindig:\n", m2.group(0))
