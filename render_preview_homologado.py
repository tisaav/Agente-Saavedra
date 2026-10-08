import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

tree = ET.parse('C:/Users/SAAV166/Downloads/Bol_Safra.jrxml')
root = tree.getroot()

scale = 2  # 2x resolution
page_w = int(root.attrib.get('pageWidth', 595)) * scale
page_h = int(root.attrib.get('pageHeight', 842)) * scale
left_m = int(root.attrib.get('leftMargin', 30)) * scale
top_m = int(root.attrib.get('topMargin', 20)) * scale

img = Image.new('RGB', (page_w, page_h), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Load fonts
try:
    f_arial_reg = lambda sz: ImageFont.truetype("arial.ttf", int(sz * scale))
    f_arial_bold = lambda sz: ImageFont.truetype("arialbd.ttf", int(sz * scale))
    f_times_reg = lambda sz: ImageFont.truetype("times.ttf", int(sz * scale))
    f_times_bold = lambda sz: ImageFont.truetype("timesbd.ttf", int(sz * scale))
except:
    f_def = ImageFont.load_default()
    f_arial_reg = lambda sz: f_def
    f_arial_bold = lambda sz: f_def
    f_times_reg = lambda sz: f_def
    f_times_bold = lambda sz: f_def

def evaluate_expression(key, expr):
    e = expr.strip()
    if key == 'textField-5':
        return 'Após o Vencimento, cobrar Multa de 2,00%(R$ 46,39)\nApós o vencimento, cobrar juros de R$ 00,77 ao dia\nProtestar após 5 dias vencidos'
    if 'razsoc' in e:
        return 'SAAVEDRA REPRESENTACOES LTDA - 92.666.817/0001-11'
    if 'endemp' in e:
        return 'R JOAO BERUTTI, 482'
    if 'dat2vct01' in e:
        return '24/06/2026'
    if 'dataneg' in e:
        return '07/10/2026'
    if 'datsis' in e:
        return '07/10/2026'
    if 'RETORNA_RENEG_OU_NOTA' in e:
        return '21222-1'
    if 'nosnum' in e:
        return '000001139'
    if '00700' in e or 'AGENCIA' in e:
        return '00700 / 005843919'
    if 'TotDupl' in e:
        return '2.319,70'
    if 'lindig' in e:
        return '42297.00705 00058.439191 00000.113928 4 14870000231970'
    if 'razcli' in e:
        if 'Pagador' in e:
            return 'Pagador: SOCIEDADE SULINA DIVINA PROVIDENCIA - 87317764001084\nR DA GRUTA, 145 - CEP 91712160, CASCATA, Porto Alegre/RS\nBeneficiário Final'
        return 'SOCIEDADE SULINA DIVINA PROVIDENCIA - 87317764001084'
    if 'Instru' in e:
        return 'Instruções (Todas as informações deste bloqueto são de exclusiva responsabilidade do Beneficiário)'
    if 'Pagável' in e or 'Sistema de Compensação' in e:
        return 'Pagável em qualquer Banco do Sistema de Compensação'
    if e.startswith('"') and e.endswith('"'):
        return e[1:-1]
    return e

# First pass: Rectangles and Lines
for el in root.iter():
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        tag = el.tag.split('}')[-1]
        x = (int(re.attrib.get('x', '0')) * scale) + left_m
        y = (int(re.attrib.get('y', '0')) * scale) + top_m
        w = int(re.attrib.get('width', '0')) * scale
        h = int(re.attrib.get('height', '0')) * scale
        
        if tag == 'rectangle':
            draw.rectangle([x, y, x + w, y + h], outline=(0, 0, 0), width=1)
        elif tag == 'line':
            draw.line([x, y, x + w, y], fill=(150, 150, 150), width=1)

# Second pass: Texts and Fields
for el in root.iter():
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        tag = el.tag.split('}')[-1]
        key = re.attrib.get('key', '')
        x = (int(re.attrib.get('x', '0')) * scale) + left_m
        y = (int(re.attrib.get('y', '0')) * scale) + top_m
        w = int(re.attrib.get('width', '0')) * scale
        h = int(re.attrib.get('height', '0')) * scale
        
        text_val = None
        if tag == 'staticText':
            t = el.find('{http://jasperreports.sourceforge.net/jasperreports}text')
            if t is not None and t.text:
                text_val = evaluate_expression(key, t.text)
        elif tag == 'textField':
            t = el.find('{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression')
            if t is not None and t.text:
                text_val = evaluate_expression(key, t.text)
                
        if text_val:
            te = el.find('{http://jasperreports.sourceforge.net/jasperreports}textElement')
            font_size = 7
            is_bold = False
            is_times = False
            align = 'left'
            if te is not None:
                align = te.attrib.get('textAlignment', 'left')
                f = te.find('{http://jasperreports.sourceforge.net/jasperreports}font')
                if f is not None:
                    font_size = int(f.attrib.get('size', '7'))
                    is_bold = f.attrib.get('isBold', 'false').lower() == 'true'
                    if 'Times' in f.attrib.get('fontName', ''):
                        is_times = True
                        
            if is_times:
                f_obj = f_times_bold(font_size) if is_bold else f_times_reg(font_size)
            else:
                f_obj = f_arial_bold(font_size) if is_bold else f_arial_reg(font_size)
                
            # Draw multi-line or single-line
            lines = text_val.split('\n')
            curr_y = y + 2
            for line in lines:
                if align == 'Right' or align == 'right':
                    bbox = draw.textbbox((0, 0), line, font=f_obj)
                    line_w = bbox[2] - bbox[0]
                    draw.text((x + w - line_w - 4, curr_y), line, fill=(0, 0, 0), font=f_obj)
                elif align == 'Center' or align == 'center':
                    bbox = draw.textbbox((0, 0), line, font=f_obj)
                    line_w = bbox[2] - bbox[0]
                    draw.text((x + (w - line_w) // 2, curr_y), line, fill=(0, 0, 0), font=f_obj)
                else:
                    draw.text((x + 4, curr_y), line, fill=(0, 0, 0), font=f_obj)
                curr_y += int((font_size + 2) * scale)

out_preview = 'c:/Users/SAAV166/Documents/Agente/preview_boleto_safra_homologado.png'
img.save(out_preview)
print(f"Preview salvo com sucesso em: {out_preview}")
