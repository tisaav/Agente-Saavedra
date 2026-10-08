import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

for t in root.iter('{http://jasperreports.sourceforge.net/jasperreports}text'):
    if t.text:
        # Check if contains any unusual chars
        for ch in t.text:
            if ord(ch) > 127 and ch not in 'ÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÄËÏÖÜÇáéíóúàèìòùãõâêîôûäëïöüçºª§°|':
                print(f"Non-standard char: {repr(ch)} (ord {ord(ch)}) in '{t.text}'")

print("Text audit complete!")
