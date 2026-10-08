import xml.etree.ElementTree as ET

tree_itau = ET.parse('modelos_safra/Boleto_Itau.jrxml')
root_itau = tree_itau.getroot()

tree_safra = ET.parse('modelos_safra/Bol_Safra.jrxml')
root_safra = tree_safra.getroot()

print("--- ITAU PARAMETERS ---")
for p in root_itau.findall('{http://jasperreports.sourceforge.net/jasperreports}parameter'):
    print(p.attrib.get('name'), p.attrib.get('class'))

print("\n--- SAFRA PARAMETERS ---")
for p in root_safra.findall('{http://jasperreports.sourceforge.net/jasperreports}parameter'):
    print(p.attrib.get('name'), p.attrib.get('class'))

print("\n--- ITAU FIELDS ---")
fields_itau = [f.attrib.get('name') for f in root_itau.findall('{http://jasperreports.sourceforge.net/jasperreports}field')]
print(fields_itau)

print("\n--- SAFRA FIELDS ---")
fields_safra = [f.attrib.get('name') for f in root_safra.findall('{http://jasperreports.sourceforge.net/jasperreports}field')]
print(fields_safra)

print("\n--- ITAU VARIABLES ---")
vars_itau = [v.attrib.get('name') for v in root_itau.findall('{http://jasperreports.sourceforge.net/jasperreports}variable')]
print(vars_itau)

print("\n--- SAFRA VARIABLES ---")
vars_safra = [v.attrib.get('name') for v in root_safra.findall('{http://jasperreports.sourceforge.net/jasperreports}variable')]
print(vars_safra)
