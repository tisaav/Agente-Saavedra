import xml.etree.ElementTree as ET

tree_itau = ET.parse('modelos_safra/Boleto_Itau.jrxml')
root_itau = tree_itau.getroot()

tree_safra = ET.parse('modelos_safra/Bol_Safra.jrxml')
root_safra = tree_safra.getroot()

def get_elements_summary(root):
    summary = []
    for el in root.iter():
        tag = el.tag.split('}')[-1]
        re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
        if re is not None:
            k = re.attrib.get('key', '')
            x = re.attrib.get('x', '')
            y = re.attrib.get('y', '')
            w = re.attrib.get('width', '')
            h = re.attrib.get('height', '')
            txt = ""
            for sub in ['text', 'textFieldExpression', 'imageExpression']:
                s = el.find(f'{{http://jasperreports.sourceforge.net/jasperreports}}{sub}')
                if s is not None and s.text:
                    txt = s.text.strip().replace('\n', ' ')[:40]
            summary.append(f"{tag:12} k={k:15} x={x:4} y={y:4} w={w:4} h={h:4} | {txt}")
    return summary

sum_itau = get_elements_summary(root_itau)
sum_safra = get_elements_summary(root_safra)

print(f"Total elements: Itau={len(sum_itau)}, Safra={len(sum_safra)}")
print("\n--- FIRST 20 ELEMENTS IN ITAU ---")
for s in sum_itau[:20]:
    print(" ", s)

print("\n--- FIRST 20 ELEMENTS IN SAFRA ---")
for s in sum_safra[:20]:
    print(" ", s)
