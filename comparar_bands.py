import xml.etree.ElementTree as ET

def print_bands(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    print(f"\n===== BANDS FOR {filename} =====")
    for child in root:
        tag = child.tag.split('}')[-1]
        band = child.find('{http://jasperreports.sourceforge.net/jasperreports}band')
        if band is not None:
            print(f"{tag:15} -> band height = {band.attrib.get('height')}")
        elif tag == 'group':
            name = child.attrib.get('name')
            gh = child.find('{http://jasperreports.sourceforge.net/jasperreports}groupHeader')
            gf = child.find('{http://jasperreports.sourceforge.net/jasperreports}groupFooter')
            gh_h = gh.find('{http://jasperreports.sourceforge.net/jasperreports}band').attrib.get('height') if gh is not None and gh.find('{http://jasperreports.sourceforge.net/jasperreports}band') is not None else None
            gf_h = gf.find('{http://jasperreports.sourceforge.net/jasperreports}band').attrib.get('height') if gf is not None and gf.find('{http://jasperreports.sourceforge.net/jasperreports}band') is not None else None
            print(f"Group {name:15} -> header={gh_h}, footer={gf_h}")

print_bands('modelos_safra/Boleto_Itau.jrxml')
print_bands('modelos_safra/Bol_Safra.jrxml')
