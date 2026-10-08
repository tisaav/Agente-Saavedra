import base64
import xml.etree.ElementTree as ET
import shutil

# Read Base64 of the clean shield
with open('safra_escudo_clean.png', 'rb') as f:
    b64_shield = base64.b64encode(f.read()).decode('ascii')

# Read Bol_Safra_CORRIGIDO.jrxml
with open('modelos_safra/Bol_Safra_CORRIGIDO.jrxml', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace the top header (Recibo do Pagador)
old_recibo_block = """				<image scaleImage="RetainShape" onErrorType="Blank">
					<reportElement key="image-safra-1" x="1" y="2" width="110" height="25"/>
					<imageExpression class="java.lang.String"><![CDATA["https://logospng.org/wp-content/uploads/banco-safra.png"]]></imageExpression>
				</image>
				<staticText>
					<reportElement key="staticText-25" x="116" y="12" width="8" height="15"/>
					<textElement textAlignment="Right" verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-26" x="124" y="12" width="33" height="15"/>
					<textElement textAlignment="Center" verticalAlignment="Middle">
						<font size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[422-7]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-27" x="157" y="12" width="8" height="15"/>
					<textElement verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-28" x="435" y="13" width="100" height="15"/>
					<box rightPadding="2"/>
					<textElement textAlignment="Right" verticalAlignment="Middle">
						<font size="8" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[Recibo do Pagador]]></text>
				</staticText>"""

new_recibo_block = """				<image scaleImage="RetainShape" hAlign="Center" vAlign="Middle" onErrorType="Blank">
					<reportElement key="image-safra-1" x="10" y="2" width="24" height="26"/>
					<imageExpression class="java.io.InputStream"><![CDATA[new java.io.ByteArrayInputStream(java.util.Base64.getDecoder().decode("__B64__"))]]></imageExpression>
				</image>
				<staticText>
					<reportElement key="staticText-24" x="40" y="10" width="150" height="16"/>
					<textElement verticalAlignment="Middle">
						<font fontName="Arial" size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[BANCO SAFRA S/A]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-25" x="198" y="10" width="8" height="16"/>
					<textElement textAlignment="Right" verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-26" x="208" y="10" width="32" height="16"/>
					<textElement textAlignment="Center" verticalAlignment="Middle">
						<font fontName="Arial" size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[422-7]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-27" x="242" y="10" width="8" height="16"/>
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
				</staticText>""".replace("__B64__", b64_shield)

assert old_recibo_block in text, "old_recibo_block not found in text!"
text = text.replace(old_recibo_block, new_recibo_block)
print("1. Recibo do Pagador block replaced successfully!")

# 2. Replace the bottom header (Ficha de Compensação)
old_ficha_block = """				<staticText>
					<reportElement key="staticText-52" x="116" y="484" width="8" height="15"/>
					<textElement textAlignment="Right"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-53" x="124" y="484" width="33" height="15"/>
					<textElement textAlignment="Center" verticalAlignment="Middle">
						<font size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[422-7]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-54" x="157" y="484" width="8" height="15"/>
					<textElement/>
					<text><![CDATA[|]]></text>
				</staticText>
				<line>
					<reportElement key="line-1" x="0" y="468" width="535" height="1"/>
					<graphicElement>
						<pen lineWidth="0.5" lineStyle="Dashed"/>
					</graphicElement>
				</line>
				<textField isStretchWithOverflow="true" pattern="" isBlankWhenNull="true">
					<reportElement key="textField-13" x="165" y="481" width="370" height="20"/>
					<box leftPadding="2" rightPadding="2">
						<topPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
						<leftPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
						<bottomPen lineWidth="0.0" lineColor="#000000"/>
						<rightPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
					</box>
					<textElement textAlignment="Right" verticalAlignment="Bottom">
						<font fontName="Times-Roman" size="12" isBold="true"/>
					</textElement>
					<textFieldExpression class="java.lang.String"><![CDATA[$V{lindig}]]></textFieldExpression>
				</textField>"""

new_ficha_block = """				<image scaleImage="RetainShape" hAlign="Center" vAlign="Middle" onErrorType="Blank">
					<reportElement key="image-safra-2" x="10" y="474" width="24" height="26"/>
					<imageExpression class="java.io.InputStream"><![CDATA[new java.io.ByteArrayInputStream(java.util.Base64.getDecoder().decode("__B64__"))]]></imageExpression>
				</image>
				<staticText>
					<reportElement key="staticText-55" x="40" y="482" width="150" height="16"/>
					<textElement verticalAlignment="Middle">
						<font fontName="Arial" size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[BANCO SAFRA S/A]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-52" x="198" y="482" width="8" height="16"/>
					<textElement textAlignment="Right" verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-53" x="208" y="482" width="32" height="16"/>
					<textElement textAlignment="Center" verticalAlignment="Middle">
						<font fontName="Arial" size="10" isBold="true" pdfFontName="Helvetica-Bold"/>
					</textElement>
					<text><![CDATA[422-7]]></text>
				</staticText>
				<staticText>
					<reportElement key="staticText-54" x="242" y="482" width="8" height="16"/>
					<textElement verticalAlignment="Middle"/>
					<text><![CDATA[|]]></text>
				</staticText>
				<line>
					<reportElement key="line-1" x="0" y="468" width="535" height="1"/>
					<graphicElement>
						<pen lineWidth="0.5" lineStyle="Dashed"/>
					</graphicElement>
				</line>
				<textField isStretchWithOverflow="true" pattern="" isBlankWhenNull="true">
					<reportElement key="textField-13" x="248" y="480" width="287" height="20"/>
					<box leftPadding="2" rightPadding="2">
						<topPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
						<leftPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
						<bottomPen lineWidth="0.0" lineColor="#000000"/>
						<rightPen lineWidth="0.0" lineStyle="Solid" lineColor="#000000"/>
					</box>
					<textElement textAlignment="Right" verticalAlignment="Bottom">
						<font fontName="Times-Roman" size="11" isBold="true"/>
					</textElement>
					<textFieldExpression class="java.lang.String"><![CDATA[$V{lindig}]]></textFieldExpression>
				</textField>""".replace("__B64__", b64_shield)

assert old_ficha_block in text, "old_ficha_block not found in text!"
text = text.replace(old_ficha_block, new_ficha_block)
print("2. Ficha de Compensação block replaced successfully!")

# 3. Remove stray old image-safra-2 near line 1590
old_stray_img = """				<image scaleImage="RetainShape" onErrorType="Blank">
					<reportElement key="image-safra-2" x="1" y="474" width="110" height="25"/>
					<imageExpression class="java.lang.String"><![CDATA["https://logospng.org/wp-content/uploads/banco-safra.png"]]></imageExpression>
				</image>"""
if old_stray_img in text:
    text = text.replace(old_stray_img, "")
    print("3. Stray old image-safra-2 removed successfully!")

# 4. Validate XML
ET.fromstring(text.encode('utf-8'))
print("4. XML is 100% syntactically valid!")

# 5. Save to destinos
out_path_modelos = 'modelos_safra/Bol_Safra_DEFINITIVO.jrxml'
out_path_downloads = 'C:/Users/SAAV166/Downloads/Bol_Safra.jrxml'

with open(out_path_modelos, 'w', encoding='utf-8') as f:
    f.write(text)

with open(out_path_downloads, 'w', encoding='utf-8') as f:
    f.write(text)

shutil.copy('safra_escudo_clean.png', 'C:/Users/SAAV166/Downloads/safra_logo.png')

print("5. Saved successfully to:\n  -", out_path_modelos, "\n  -", out_path_downloads, "\n  - C:/Users/SAAV166/Downloads/safra_logo.png")
