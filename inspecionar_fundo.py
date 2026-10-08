import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
for el in tree.iter():
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        y = int(re.attrib.get('y', 0))
        if y >= 685:
            tag = el.tag.split('}')[-1]
            k = re.attrib.get('key', '')
            h = int(re.attrib.get('height', 0))
            x = int(re.attrib.get('x', 0))
            w = int(re.attrib.get('width', 0))
            txt = ""
            for sub in ['text', 'textFieldExpression']:
                s = el.find('{http://jasperreports.sourceforge.net/jasperreports}' + sub)
                if s is not None and s.text:
                    txt = s.text.strip().replace('\n', ' ')[:30]
            print(f"{tag:15} k={k:15} y={y:3}..{y+h:3} (h={h:2}) x={x:3}..{x+w:3} | {txt}")
