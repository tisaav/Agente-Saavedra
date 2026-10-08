import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

rights = []
for elem in root.iter():
    re = elem.find('.//reportElement') or elem.find('.//{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        x = int(re.attrib.get('x', '0'))
        w = int(re.attrib.get('width', '0'))
        y = int(re.attrib.get('y', '0'))
        if y >= 470:
            rights.append((x + w, y, x, w, elem.tag))

rights.sort(key=lambda x: x[0], reverse=True)
print("Top 10 rightmost elements in Ficha de compensacao:")
for r in rights[:10]:
    print(f"Right={r[0]}, y={r[1]}, x={r[2]}, w={r[3]}, tag={r[4]}")
