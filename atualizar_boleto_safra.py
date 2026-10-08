import xml.etree.ElementTree as ET

tree = ET.parse('modelos_safra/Bol_Safra_LINHA_UNICA.jrxml')
root = tree.getroot()

ET.register_namespace('', 'http://jasperreports.sourceforge.net/jasperreports')

# 1. Local de Pagamento (staticText-29)
for el in root.iter('{http://jasperreports.sourceforge.net/jasperreports}staticText'):
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None and re.attrib.get('key') == 'staticText-29':
        t = el.find('{http://jasperreports.sourceforge.net/jasperreports}text')
        if t is not None:
            t.text = 'Pagável em qualquer Banco do Sistema de Compensação'
            print("1. staticText-29 ajustado!")

# 2. textField-12 (remover Sacador/Avalista)
for el in root.iter('{http://jasperreports.sourceforge.net/jasperreports}textField'):
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None and re.attrib.get('key') == 'textField-12':
        t = el.find('{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression')
        if t is not None and t.text and 'Sacador/Avalista' in t.text:
            cleaned_lines = []
            for line in t.text.split('\n'):
                if 'Sacador/Avalista' not in line:
                    cleaned_lines.append(line)
            expr = '\n'.join(cleaned_lines).rstrip()
            if expr.endswith('+'):
                expr = expr[:-1].rstrip()
            t.text = expr
            print("2. textField-12 (Sacador/Avalista removido) ajustado!")

# 3. textField-5 (Instruções: Multa, Juros, Protesto)
new_inst_expr = (
    '"Após o Vencimento, cobrar Multa de 2,00%(R$ " + new java.text.DecimalFormat("#,##0.00").format($V{Vars.TotDupl}.doubleValue() * 0.02) + ")\\n" +\n'
    '"Após o vencimento, cobrar juros de R$ " + new java.text.DecimalFormat("#,##0.00").format($V{Vars.TotDupl}.doubleValue() * 0.00033) + " ao dia\\n" +\n'
    '"Protestar após 5 dias vencidos"'
)

for el in root.iter('{http://jasperreports.sourceforge.net/jasperreports}textField'):
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None and re.attrib.get('key') == 'textField-5':
        t = el.find('{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression')
        if t is not None:
            t.text = new_inst_expr
            print("3. textField-5 atualizado para novo padrão de instruções!")

# 4. Agência / Código Beneficiário:
for el in root.iter('{http://jasperreports.sourceforge.net/jasperreports}textField'):
    t = el.find('{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression')
    if t is not None and t.text and '$V{AGENCIA}' in t.text:
        t.text = '"00700 / " + $V{CONTA9DIG}'
        print("4. Campo de Agência/Código Beneficiário ajustado para '00700 / ' + $V{CONTA9DIG}!")

# Salvar
tree.write('modelos_safra/Bol_Safra_HOMOLOGADO.jrxml', encoding='utf-8', xml_declaration=True)
tree.write('modelos_safra/Bol_Safra_LINHA_UNICA.jrxml', encoding='utf-8', xml_declaration=True)
tree.write('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml', encoding='utf-8', xml_declaration=True)
print("Arquivos salvos com sucesso!")
