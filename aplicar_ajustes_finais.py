import xml.etree.ElementTree as ET
import shutil

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

ns = {'jr': 'http://jasperreports.sourceforge.net/jasperreports'}

# 1. Update Recibo Header elements
for el in root.iter():
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        key = re.attrib.get('key')
        
        # Recibo
        if key == 'image-safra-1':
            re.attrib['x'] = '6'
            re.attrib['y'] = '2'
            re.attrib['width'] = '24'
            re.attrib['height'] = '26'
        elif key == 'staticText-24':
            re.attrib['x'] = '36'
            re.attrib['y'] = '10'
            re.attrib['width'] = '102'
            re.attrib['height'] = '16'
        elif key == 'staticText-25':
            re.attrib['x'] = '140'
            re.attrib['y'] = '10'
            re.attrib['width'] = '6'
            re.attrib['height'] = '16'
        elif key == 'staticText-26':
            re.attrib['x'] = '148'
            re.attrib['y'] = '10'
            re.attrib['width'] = '32'
            re.attrib['height'] = '16'
        elif key == 'staticText-27':
            re.attrib['x'] = '182'
            re.attrib['y'] = '10'
            re.attrib['width'] = '6'
            re.attrib['height'] = '16'
        elif key == 'staticText-28':
            re.attrib['x'] = '420'
            re.attrib['y'] = '10'
            re.attrib['width'] = '115'
            re.attrib['height'] = '16'
            
        # Ficha de Compensacao
        elif key == 'image-safra-2':
            re.attrib['x'] = '6'
            re.attrib['y'] = '474'
            re.attrib['width'] = '24'
            re.attrib['height'] = '26'
        elif key == 'staticText-55':
            re.attrib['x'] = '36'
            re.attrib['y'] = '482'
            re.attrib['width'] = '102'
            re.attrib['height'] = '16'
        elif key == 'staticText-52':
            re.attrib['x'] = '140'
            re.attrib['y'] = '482'
            re.attrib['width'] = '6'
            re.attrib['height'] = '16'
        elif key == 'staticText-53':
            re.attrib['x'] = '148'
            re.attrib['y'] = '482'
            re.attrib['width'] = '32'
            re.attrib['height'] = '16'
        elif key == 'staticText-54':
            re.attrib['x'] = '182'
            re.attrib['y'] = '482'
            re.attrib['width'] = '6'
            re.attrib['height'] = '16'
        elif key == 'textField-13':
            re.attrib['x'] = '190'
            re.attrib['y'] = '482'
            re.attrib['width'] = '345'
            re.attrib['height'] = '18'
            el.attrib['isStretchWithOverflow'] = 'false'
            # Adjust font to Times-Roman size 10 bold
            te = el.find('{http://jasperreports.sourceforge.net/jasperreports}textElement')
            if te is not None:
                te.attrib['textAlignment'] = 'Right'
                te.attrib['verticalAlignment'] = 'Middle'
                f = te.find('{http://jasperreports.sourceforge.net/jasperreports}font')
                if f is not None:
                    f.attrib['fontName'] = 'Times-Roman'
                    f.attrib['size'] = '10'
                    f.attrib['isBold'] = 'true'
                    
        # Geometric alignments
        elif key == 'rectangle-3':
            # Was x=406, w=129 -> Align to right column x=425, w=110
            re.attrib['x'] = '425'
            re.attrib['width'] = '110'
        elif key == 'rectangle-23':
            # Was x=0, w=426 -> Align to left column w=425
            re.attrib['width'] = '425'
        elif key == 'Boleto_Itau_notas':
            # subreport was w=536, overflow 1px -> w=534
            re.attrib['width'] = '534'

# Remove orphan staticText-1 (x=-571)
for band in root.iter('{http://jasperreports.sourceforge.net/jasperreports}band'):
    to_remove = []
    for child in band:
        re = child.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
        if re is not None and re.attrib.get('key') == 'staticText-1' and int(re.attrib.get('x', 0)) < 0:
            to_remove.append(child)
    for r in to_remove:
        band.remove(r)
        print("Removed orphan staticText-1 (x=-571)!")

# Write updated XML
out_downloads = 'C:/Users/SAAV166/Downloads/Bol_Safra.jrxml'
out_modelos = 'modelos_safra/Bol_Safra_LINHA_UNICA.jrxml'

# JasperReports standard XML declaration
tree.write(out_downloads, encoding='utf-8', xml_declaration=True)
tree.write(out_modelos, encoding='utf-8', xml_declaration=True)
print("Updated XML written successfully!")
