import xml.etree.ElementTree as ET

with open('modelos_safra/Bol_Safra_LINHA_UNICA.jrxml', 'r', encoding='utf-8') as f:
    text = f.read()

root = ET.fromstring(text.encode('utf-8'))

print("=== textFields ===")
for i, el in enumerate(root.iter('{http://jasperreports.sourceforge.net/jasperreports}textField')):
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    t = el.find('{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression')
    if re is not None:
        key = re.attrib.get('key')
        y = re.attrib.get('y')
        x = re.attrib.get('x')
        if key in ['textField-5', 'textField-12', 'textField-13', 'textField-8']:
            print(f"[{i}] key={key} x={x} y={y} text={repr(t.text if t is not None else None)[:90]}")
