import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

elements = []
for el in root.iter():
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        tag = el.tag.split('}')[-1]
        k = re.attrib.get('key', '')
        x = int(re.attrib.get('x', 0))
        y = int(re.attrib.get('y', 0))
        w = int(re.attrib.get('width', 0))
        h = int(re.attrib.get('height', 0))
        
        txt = ""
        for sub in ['text', 'textFieldExpression', 'imageExpression', 'subreportExpression']:
            s = el.find('{http://jasperreports.sourceforge.net/jasperreports}' + sub)
            if s is not None and s.text:
                txt = s.text.strip().replace('\n', ' ')[:35]
                
        elements.append({
            'tag': tag, 'key': k, 'x': x, 'y': y, 'w': w, 'h': h,
            'x2': x + w, 'y2': y + h, 'txt': txt
        })

# Sort by y, then x
elements_sorted = sorted(elements, key=lambda e: (e['y'], e['x']))

print("=== ALL ELEMENTS BY Y POSITION ===")
for e in elements_sorted:
    if e['x'] >= 0:
        print(f"y={e['y']:3}..{e['y2']:3} x={e['x']:3}..{e['x2']:3} | {e['tag']:11} k={e['key']:16} | {e['txt']}")
