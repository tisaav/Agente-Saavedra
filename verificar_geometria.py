import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

print("=== RECTANGLES CHECK ===")
for r in root.iter('{http://jasperreports.sourceforge.net/jasperreports}rectangle'):
    re = r.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        k = re.attrib.get('key', '')
        x = int(re.attrib.get('x', 0))
        y = int(re.attrib.get('y', 0))
        w = int(re.attrib.get('width', 0))
        h = int(re.attrib.get('height', 0))
        print(f"Rectangle k={k:15} x={x:3}..{x+w:3} (w={w:3}) y={y:3}..{y+h:3} (h={h:3})")

print("\n=== LINES CHECK ===")
for l in root.iter('{http://jasperreports.sourceforge.net/jasperreports}line'):
    re = l.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        k = re.attrib.get('key', '')
        x = int(re.attrib.get('x', 0))
        y = int(re.attrib.get('y', 0))
        w = int(re.attrib.get('width', 0))
        h = int(re.attrib.get('height', 0))
        print(f"Line k={k:15} x={x:3}..{x+w:3} (w={w:3}) y={y:3}..{y+h:3} (h={h:3})")
