import xml.etree.ElementTree as ET

tree = ET.parse('modelos_safra/Bol_Safra.jrxml')
for el in tree.iter():
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        y = int(re.attrib.get('y', 0))
        if 120 <= y <= 470:
            tag = el.tag.split('}')[-1]
            txt = ''
            for sub in ['text', 'textFieldExpression', 'imageExpression', 'subreportExpression']:
                s = el.find('{http://jasperreports.sourceforge.net/jasperreports}' + sub)
                if s is not None and s.text:
                    txt = s.text.strip().replace('\n', ' ')[:50]
            print(f"{tag:12} y={y:3} x={re.attrib.get('x'):3} w={re.attrib.get('width'):3} h={re.attrib.get('height'):3} | {txt}")
