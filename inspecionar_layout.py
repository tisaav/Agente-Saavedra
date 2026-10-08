import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

print("Page width:", root.attrib.get('pageWidth'))
print("Page height:", root.attrib.get('pageHeight'))
print("Left margin:", root.attrib.get('leftMargin'))
print("Right margin:", root.attrib.get('rightMargin'))
print("Top margin:", root.attrib.get('topMargin'))
print("Bottom margin:", root.attrib.get('bottomMargin'))

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
        for sub in ['text', 'textFieldExpression', 'imageExpression']:
            s = el.find('{http://jasperreports.sourceforge.net/jasperreports}' + sub)
            if s is not None and s.text:
                txt = s.text.strip().replace('\n', ' ')[:35]
                
        font_info = ""
        te = el.find('{http://jasperreports.sourceforge.net/jasperreports}textElement')
        if te is not None:
            f = te.find('{http://jasperreports.sourceforge.net/jasperreports}font')
            if f is not None:
                fname = f.attrib.get('fontName', 'default')
                fsize = f.attrib.get('size', 'default')
                fbold = f.attrib.get('isBold', 'false')
                font_info = f"font={fname} sz={fsize} bold={fbold}"
                
        elements.append({
            'tag': tag, 'key': k, 'x': x, 'y': y, 'w': w, 'h': h,
            'x2': x + w, 'y2': y + h, 'txt': txt, 'font': font_info, 'el': el
        })

print(f"\nTotal report elements: {len(elements)}")

# Group by band / y-range
# Header Recibo: y < 30
# Recibo Body: 28 <= y < 130
# Details/subreport: 130 <= y < 470
# Header Ficha: 468 <= y < 510
# Ficha Body: 503 <= y < 700
# Barcode: y >= 680

print("\n--- HEADER RECIBO (y < 30) ---")
for e in sorted([e for e in elements if e['y'] < 30 and e['x'] >= 0], key=lambda x: x['x']):
    print(f"x={e['x']:3}..{e['x2']:3} y={e['y']:2}..{e['y2']:2} {e['tag']:11} k={e['key']:15} | {e['txt']:30} | {e['font']}")

print("\n--- HEADER FICHA (468 <= y < 505) ---")
for e in sorted([e for e in elements if 468 <= e['y'] < 505 and e['x'] >= 0], key=lambda x: x['x']):
    print(f"x={e['x']:3}..{e['x2']:3} y={e['y']:3}..{e['y2']:3} {e['tag']:11} k={e['key']:15} | {e['txt']:30} | {e['font']}")
