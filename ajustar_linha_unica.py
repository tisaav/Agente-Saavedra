import re
import xml.etree.ElementTree as ET

with open('modelos_safra/Bol_Safra_DEFINITIVO.jrxml', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Recibo Header
old_recibo = re.search(r'(<image scaleImage="RetainShape"[^>]*>\s*<reportElement key="image-safra-1"[^>]*>.*?<text><!\[CDATA\[RECIBO DO PAGADOR\]\]></text>\s*</staticText>)', text, re.DOTALL)
assert old_recibo is not None, "old_recibo pattern not found!"

# Extract Base64 from old_recibo
b64_m = re.search(r'decode\("([^"]+)"\)', old_recibo.group(1))
assert b64_m is not None, "Base64 not found!"
b64 = b64_m.group(1)

new_recibo = f"""<image scaleImage="RetainShape" hAlign="Center" vAlign="Middle" onErrorType="Blank">
					<reportElement key="image-safra-1" x="6" y="2" width="24" height="26"/>
					<imageExpression class="java.io.InputStream"><![CDATA[new java.io.ByteArrayInputStream(java.util.Base64.getDecoder().decode("{b64}"))]]></imageExpression>
				</image>
				<staticText>
					<reportElement key="staticText-24" x="36" y="10" width="102" height="16"/>
					<textElement verticalAlignment="Middle">
						<font fontName="Arial" size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[BANCO SAFRA S/A]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-25" x="140" y="10" width="6" height="16"/>
					<textElement textAlignment="Right" verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-26" x="148" y="10" width="32" height="16"/>
					<textElement textAlignment="Center" verticalAlignment="Middle">
						<font fontName="Arial" size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[422-7]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-27" x="182" y="10" width="6" height="16"/>
					<textElement verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-28" x="420" y="10" width="115" height="16"/>
					<box rightPadding="2"/>
					<textElement textAlignment="Right" verticalAlignment="Middle">
						<font fontName="Arial" size="8" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[RECIBO DO PAGADOR]]></text>
				</staticText>"""

text = text.replace(old_recibo.group(1), new_recibo)
print("1. Recibo header updated!")

# 2. Update Ficha Header
old_ficha = re.search(r'(<image scaleImage="RetainShape"[^>]*>\s*<reportElement key="image-safra-2"[^>]*>.*?<textFieldExpression class="java\.lang\.String"><!\[CDATA\[\$V\{lindig\}\]\]></textFieldExpression>\s*</textField>)', text, re.DOTALL)
assert old_ficha is not None, "old_ficha pattern not found!"

new_ficha = f"""<image scaleImage="RetainShape" hAlign="Center" vAlign="Middle" onErrorType="Blank">
					<reportElement key="image-safra-2" x="6" y="474" width="24" height="26"/>
					<imageExpression class="java.io.InputStream"><![CDATA[new java.io.ByteArrayInputStream(java.util.Base64.getDecoder().decode("{b64}"))]]></imageExpression>
				</image>
				<staticText>
					<reportElement key="staticText-55" x="36" y="482" width="102" height="16"/>
					<textElement verticalAlignment="Middle">
						<font fontName="Arial" size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[BANCO SAFRA S/A]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-52" x="140" y="482" width="6" height="16"/>
					<textElement textAlignment="Right" verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-53" x="148" y="482" width="32" height="16"/>
					<textElement textAlignment="Center" verticalAlignment="Middle">
						<font fontName="Arial" size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[422-7]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-54" x="182" y="482" width="6" height="16"/>
					<textElement verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<line>
					<reportElement key="line-1" x="0" y="468" width="535" height="1"/>
					<graphicElement>
						<pen lineWidth="0.5" lineStyle="Dashed"/>
					</graphicElement>
				</line>
				<textField isStretchWithOverflow="false" pattern="" isBlankWhenNull="true">
					<reportElement key="textField-13" x="190" y="482" width="345" height="18"/>
					<box leftPadding="2" rightPadding="2">
						<topPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
						<leftPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
						<bottomPen lineWidth="0.0" lineColor="#000000"/>
						<rightPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
					</box>
					<textElement textAlignment="Right" verticalAlignment="Middle">
						<font fontName="Times-Roman" size="10" isBold="true"/>
					</textElement>
					<textFieldExpression class="java.lang.String"><![CDATA[$V{{lindig}}]]></textFieldExpression>
				</textField>"""

text = text.replace(old_ficha.group(1), new_ficha)
print("2. Ficha header updated!")

# 3. Geometric alignments
# rectangle-3: x="406" width="129" -> x="425" width="110"
text = text.replace('<reportElement key="rectangle-3" x="406" y="52" width="129" height="24"/>',
                    '<reportElement key="rectangle-3" x="425" y="52" width="110" height="24"/>')
print("3. rectangle-3 aligned!")

# rectangle-23: width="426" -> width="425"
text = text.replace('<reportElement key="rectangle-23" x="0" y="503" width="426" height="24"/>',
                    '<reportElement key="rectangle-23" x="0" y="503" width="425" height="24"/>')
print("4. rectangle-23 aligned!")

# subreport x="1" width="535" -> x="0" width="535"
text = text.replace('key="Boleto_Itau_notas" positionType="Float" x="1" y="187" width="535"',
                    'key="Boleto_Itau_notas" positionType="Float" x="0" y="187" width="535"')
print("5. subreport position adjusted to x=0 width=535!")

# Remove orphan staticText-1 (x=-571)
orphan_m = re.search(r'\s*<staticText>\s*<reportElement key="staticText-1" x="-571".*?</staticText>', text, re.DOTALL)
if orphan_m:
    text = text.replace(orphan_m.group(0), '')
    print("6. Orphan staticText-1 removed!")

# 4. XML syntax check
ET.fromstring(text.encode('utf-8'))
print("7. XML parsed and validated 100% successfully!")

# 5. Write to files
with open('modelos_safra/Bol_Safra_LINHA_UNICA.jrxml', 'w', encoding='utf-8') as f:
    f.write(text)

with open('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml', 'w', encoding='utf-8') as f:
    f.write(text)

print("8. Saved to C:/Users/SAAV166/Downloads/Bol_Safra.jrxml successfully!")
