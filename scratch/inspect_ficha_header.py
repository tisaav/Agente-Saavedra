import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

ns = {'j': 'http://jasperreports.sourceforge.net/jasperreports'}
# or no namespace
for elem in root.iter():
    tag = elem.tag.split('}')[-1]
    if tag in ['textField', 'staticText']:
        re = elem.find('.//reportElement') or elem.find('.//{http://jasperreports.sourceforge.net/jasperreports}reportElement')
        if re is not None:
            y = int(re.attrib.get('y', '0'))
            if 460 <= y <= 510:
                x = int(re.attrib.get('x', '0'))
                w = int(re.attrib.get('width', '0'))
                h = int(re.attrib.get('height', '0'))
                expr = elem.find('.//textFieldExpression')
                if expr is None:
                    expr = elem.find('.//{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression')
                txt = elem.find('.//text')
                if txt is None:
                    txt = elem.find('.//{http://jasperreports.sourceforge.net/jasperreports}text')
                content = (expr.text if expr is not None else '') or (txt.text if txt is not None else '')
                print(f"y={y:3d}, x={x:3d}, w={w:3d}, h={h:2d} | tag={tag} | {content.strip()}")
