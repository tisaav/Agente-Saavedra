import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

# Collect all printable elements (rectangles, lines, texts, textFields, images, subreports)
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
                txt = s.text.strip().replace('\n', ' ')[:40]
                
        elements.append({
            'tag': tag, 'key': k, 'x': x, 'y': y, 'w': w, 'h': h,
            'x2': x + w, 'y2': y + h, 'txt': txt, 'el': el
        })

print(f"Total elements: {len(elements)}")

# Check elements out of printable page bounds (pageWidth=595, leftMargin=30, rightMargin=30 -> printable width = 535)
print("\n--- BOUNDS CHECK (printable width = 535, height = 790 in band) ---")
for e in elements:
    if e['x'] < 0:
        print(f"Negative X: {e['tag']} k={e['key']} x={e['x']} | {e['txt']}")
    if e['x2'] > 535:
        print(f"Exceeds printable width 535: {e['tag']} k={e['key']} x={e['x']} w={e['w']} x2={e['x2']} | {e['txt']}")
    if e['y2'] > 790:
        print(f"Exceeds band height 790: {e['tag']} k={e['key']} y={e['y']} h={e['h']} y2={e['y2']} | {e['txt']}")

# Check text-on-text overlaps (excluding background rectangles/lines)
print("\n--- TEXT-ON-TEXT OVERLAPS ---")
text_elements = [e for e in elements if e['tag'] in ('staticText', 'textField') and e['x'] >= 0]
for i in range(len(text_elements)):
    e1 = text_elements[i]
    for j in range(i + 1, len(text_elements)):
        e2 = text_elements[j]
        # Check bounding box collision
        # overlap in x:
        x_overlap = max(0, min(e1['x2'], e2['x2']) - max(e1['x'], e2['x']))
        y_overlap = max(0, min(e1['y2'], e2['y2']) - max(e1['y'], e2['y']))
        if x_overlap > 5 and y_overlap > 3:
            print(f"Overlap between:\n  1) [{e1['tag']}] k={e1['key']} (x={e1['x']}..{e1['x2']}, y={e1['y']}..{e1['y2']}) | '{e1['txt']}'\n  2) [{e2['tag']}] k={e2['key']} (x={e2['x']}..{e2['x2']}, y={e2['y']}..{e2['y2']}) | '{e2['txt']}'\n")
