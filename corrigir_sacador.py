import xml.etree.ElementTree as ET

with open('modelos_safra/Bol_Safra_LINHA_UNICA.jrxml', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update rectangle-44
text = text.replace('<reportElement key="rectangle-44" x="0" y="695" width="535" height="38"/>',
                    '<reportElement key="rectangle-44" x="0" y="695" width="535" height="40"/>')

# 2. Update rectangle-43
text = text.replace('<reportElement key="rectangle-43" x="0" y="733" width="535" height="12"/>',
                    '<reportElement key="rectangle-43" x="0" y="735" width="535" height="12"/>')

# 3. Update staticText-51
text = text.replace('<reportElement key="staticText-51" x="344" y="734" width="191" height="11"/>',
                    '<reportElement key="staticText-51" x="344" y="736" width="191" height="11"/>')

# 4. Update textField-12 in Ficha de Compensacao
# In Bol_Safra_LINHA_UNICA.jrxml, find textField-12 around y="697"
old_tf12 = """				<textField isStretchWithOverflow="true" isBlankWhenNull="false">
					<reportElement key="textField-12" x="2" y="697" width="523" height="36"/>
					<textElement>
						<font size="7"/>
					</textElement>"""

new_tf12 = """				<textField isStretchWithOverflow="false" isBlankWhenNull="false">
					<reportElement key="textField-12" x="2" y="696" width="523" height="38"/>
					<textElement>
						<font size="6"/>
					</textElement>"""

assert old_tf12 in text, "old_tf12 not found in text!"
text = text.replace(old_tf12, new_tf12)
print("textField-12 updated to font size 6 and height 38!")

# Validate XML
ET.fromstring(text.encode('utf-8'))
print("XML is 100% syntactically valid!")

# Save to destination files
with open('modelos_safra/Bol_Safra_LINHA_UNICA.jrxml', 'w', encoding='utf-8') as f:
    f.write(text)

with open('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved to C:/Users/SAAV166/Downloads/Bol_Safra.jrxml successfully!")
