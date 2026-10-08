import xml.etree.ElementTree as ET

tree = ET.parse('modelos_safra/Bol_Safra_COM_LOGO.jrxml')
root = tree.getroot()

for img in root.iter('{http://jasperreports.sourceforge.net/jasperreports}image'):
    re = img.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    ie = img.find('{http://jasperreports.sourceforge.net/jasperreports}imageExpression')
    if re is not None:
        print("Image attrs:", re.attrib)
    if ie is not None:
        print("Image expr starts with:", ie.text[:80] if ie.text else "None")
