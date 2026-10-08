import xml.etree.ElementTree as ET

with open('modelos_safra/Bol_Safra_LINHA_UNICA.jrxml', 'r', encoding='utf-8') as f:
    text = f.read()

root = ET.fromstring(text.encode('utf-8'))
for el in root.iter('{http://jasperreports.sourceforge.net/jasperreports}variable'):
    name = el.attrib.get('name')
    if name in ['AGENCIA', 'CONTA9DIG', 'numctam']:
        expr = el.find('{http://jasperreports.sourceforge.net/jasperreports}variableExpression')
        print(f"Variable {name}: {expr.text if expr is not None else 'None'}")
