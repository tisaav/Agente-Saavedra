import re
import xml.etree.ElementTree as ET

path = 'C:/Users/SAAV166/Downloads/Bol_Safra.jrxml'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update textField-8 width from 224 to 355
old_tf8 = '<reportElement key="textField-8" x="67" y="527" width="224" height="11" />'
new_tf8 = '<reportElement key="textField-8" x="67" y="527" width="355" height="11" />'
assert old_tf8 in content, "old_tf8 not found"
content = content.replace(old_tf8, new_tf8)

# 2. Update textField-13 (Linha digitável)
# Change font size from 10 to 9, width from 345 to 355, x from 190 to 188
old_lindig = '''<textField isStretchWithOverflow="false" pattern="" isBlankWhenNull="true">
					<reportElement key="textField-13" x="190" y="482" width="345" height="18" />
					<box leftPadding="2" rightPadding="2">
						<topPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000" />
						<leftPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000" />
						<bottomPen lineWidth="0.0" lineColor="#000000" />
						<rightPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000" />
					</box>
					<textElement textAlignment="Right" verticalAlignment="Middle">
						<font fontName="Times-Roman" size="10" isBold="true" />
					</textElement>
					<textFieldExpression class="java.lang.String">$V{lindig}</textFieldExpression>
				</textField>'''

new_lindig = '''<textField isStretchWithOverflow="false" pattern="" isBlankWhenNull="true">
					<reportElement key="textField-13" x="188" y="482" width="356" height="18" />
					<box leftPadding="0" rightPadding="0">
						<topPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000" />
						<leftPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000" />
						<bottomPen lineWidth="0.0" lineColor="#000000" />
						<rightPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000" />
					</box>
					<textElement textAlignment="Right" verticalAlignment="Middle">
						<font fontName="Times-Roman" size="9" isBold="true" />
					</textElement>
					<textFieldExpression class="java.lang.String">$V{lindig}</textFieldExpression>
				</textField>'''
assert old_lindig in content, "old_lindig not found"
content = content.replace(old_lindig, new_lindig)

# 3. Update CONTA9DIG to strip dash so it formats as 005843919
old_conta = '"sankhya.lpad(CTA.CODCTABCO,9,\'0\')"'
new_conta = '"sankhya.lpad(replace(CTA.CODCTABCO,\'-\',\'\'),9,\'0\')"'
assert old_conta in content, "old_conta not found"
content = content.replace(old_conta, new_conta)

# Validate XML
ET.fromstring(content)
print("XML is valid!")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Also copy to workspace modelos_safra for backup
with open('c:/Users/SAAV166/Documents/Agente/modelos_safra/Bol_Safra_HOMOLOGADO.jrxml', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated Bol_Safra.jrxml and Bol_Safra_HOMOLOGADO.jrxml!")
