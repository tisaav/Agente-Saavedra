import xml.etree.ElementTree as ET

tree = ET.parse('modelos_safra/Boleto_Itau.jrxml')
root = tree.getroot()

print("=== ITAU HEADER RECIBO DO PAGADOR (y < 40) ===")
for band in root.iter('{http://jasperreports.sourceforge.net/jasperreports}band'):
    for child in band:
        re = child.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
        if re is not None:
            y = int(re.attrib.get('y', 0))
            if y < 40:
                tag = child.tag.split('}')[-1]
                print(f"<{tag}>", ET.tostring(child, encoding='utf-8').decode('utf-8'))

print("\n=== ITAU HEADER FICHA DE COMPENSACAO (260 <= y <= 310) ===")
for band in root.iter('{http://jasperreports.sourceforge.net/jasperreports}band'):
    for child in band:
        re = child.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
        if re is not None:
            y = int(re.attrib.get('y', 0))
            if 260 <= y <= 300:
                tag = child.tag.split('}')[-1]
                print(f"<{tag}>", ET.tostring(child, encoding='utf-8').decode('utf-8'))
