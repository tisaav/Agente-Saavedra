import xml.etree.ElementTree as ET

tree = ET.parse('modelos_safra/Boleto_Itau.jrxml')
root = tree.getroot()

ns = {'jr': 'http://jasperreports.sourceforge.net/jasperreports'}

def inspect_band(band_name):
    print(f"\n==================== BAND: {band_name} ====================")
    for band in root.iter('{http://jasperreports.sourceforge.net/jasperreports}band'):
        height = band.attrib.get('height')
        print(f"Band height: {height}")
        for child in band:
            tag = child.tag.split('}')[-1]
            re = child.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
            if re is not None:
                x = int(re.attrib.get('x', 0))
                y = int(re.attrib.get('y', 0))
                w = int(re.attrib.get('width', 0))
                h = int(re.attrib.get('height', 0))
                key = re.attrib.get('key', '')
                
                txt = ""
                text_el = child.find('{http://jasperreports.sourceforge.net/jasperreports}text')
                if text_el is not None and text_el.text:
                    txt = text_el.text.strip()
                tfe = child.find('{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression')
                if tfe is not None and tfe.text:
                    txt = f"EXPR: {tfe.text.strip()}"
                ie = child.find('{http://jasperreports.sourceforge.net/jasperreports}imageExpression')
                if ie is not None and ie.text:
                    txt = f"IMG: {ie.text.strip()}"
                    
                if y < 40 or (260 <= y <= 310) or (460 <= y <= 510):
                    print(f"  [{tag:12}] x={x:3} y={y:3} w={w:3} h={h:3} key={key:15} | {txt[:60]}")

inspect_band("ALL")
