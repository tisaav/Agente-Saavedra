import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
import base64
import io

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

# Sample real values from test boleto 25355-1
def evaluate_expression(expr):
    e = expr.strip()
    if 'razsoc' in e:
        return 'SAAVEDRA REPRESENTACOES LTDA - 92.666.817/0001-11'
    if 'endemp' in e:
        return 'R JOAO BERUTTI, 482'
    if 'dat2vct01' in e:
        return '02/09/2026'
    if 'dataneg' in e:
        return '03/08/2026'
    if 'datsis' in e:
        return '06/10/2026'
    if 'RETORNA_RENEG_OU_NOTA' in e:
        return '25355 - 1'
    if 'nosnum' in e:
        return '000000060'
    if '01' in e and len(e) <= 4:
        return '01'
    if 'TotDupl' in e:
        return '5.130,16'
    if 'AGENCIA' in e:
        return '00007 / 005843919'
    if 'lindig' in e:
        return '42297.00002 70058.439194 00000.006015 9 15570000513016'
    if 'razcli' in e:
        if 'Pagador' in e:
            return 'Pagador: HOSPITAL DE CLINICAS DE PORTO ALEGRE - 87.020.517/0001-20\nR RAMIRO BARCELOS, 2350\n90.035-003-Porto Alegre-RS\nSacador/Avalista'
        return 'HOSPITAL DE CLINICAS DE PORTO ALEGRE - 87.020.517/0001-20'
    if 'Instru' in e:
        return 'Instruções (Todas as informações deste bloqueto são de exclusiva responsabilidade do Beneficiário)'
    if 'TAXADIAATRASO' in e or 'cobrar mora' in e:
        return 'Após o vencimento cobrar mora de R$ 0,17 ao dia e Multa de 0,00% - Cobrança Escritural'
    if e.startswith('"') and e.endswith('"'):
        return e[1:-1]
    return e

# 1. First pass: Draw all rectangles and lines
for el in root.iter():
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        tag = el.tag.split('}')[-1]
        x = left_m + int(re.attrib.get('x', 0)) * scale
        y = top_m + int(re.attrib.get('y', 0)) * scale
        w = int(re.attrib.get('width', 0)) * scale
        h = int(re.attrib.get('height', 0)) * scale
        
        if tag == 'rectangle':
            draw.rectangle([x, y, x + w, y + h], outline=(0, 0, 0), width=1)
        elif tag == 'line':
            ge = el.find('{http://jasperreports.sourceforge.net/jasperreports}graphicElement')
            pen = ge.find('{http://jasperreports.sourceforge.net/jasperreports}pen') if ge is not None else None
            is_dashed = pen is not None and pen.attrib.get('lineStyle') == 'Dashed'
            if is_dashed:
                dash_len = 4 * scale
                gap_len = 3 * scale
                curr_x = x
                while curr_x < x + w:
                    draw.line([curr_x, y, min(curr_x + dash_len, x + w), y], fill=(120, 120, 120), width=1)
                    curr_x += dash_len + gap_len
            else:
                draw.line([x, y, x + w, y + h], fill=(0, 0, 0), width=1)

# 2. Second pass: Draw images
for el in root.iter('{http://jasperreports.sourceforge.net/jasperreports}image'):
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    ie = el.find('{http://jasperreports.sourceforge.net/jasperreports}imageExpression')
    if re is not None and ie is not None and ie.text:
        x = left_m + int(re.attrib.get('x', 0)) * scale
        y = top_m + int(re.attrib.get('y', 0)) * scale
        w = int(re.attrib.get('width', 0)) * scale
        h = int(re.attrib.get('height', 0)) * scale
        
        import re as re_mod
        m = re_mod.search(r'decode\("([^"]+)"\)', ie.text)
        if m:
            b64_data = m.group(1)
            img_data = base64.b64decode(b64_data)
            sub_img = Image.open(io.BytesIO(img_data)).convert('RGBA')
            sub_resized = sub_img.resize((w, h), Image.Resampling.LANCZOS)
            img.paste(sub_resized, (x, y), sub_resized)

# 3. Third pass: Draw staticTexts and textFields
for el in root.iter():
    re = el.find('{http://jasperreports.sourceforge.net/jasperreports}reportElement')
    if re is not None:
        tag = el.tag.split('}')[-1]
        if tag in ('staticText', 'textField'):
            x = left_m + int(re.attrib.get('x', 0)) * scale
            y = top_m + int(re.attrib.get('y', 0)) * scale
            w = int(re.attrib.get('width', 0)) * scale
            h = int(re.attrib.get('height', 0)) * scale
            
            text_val = ""
            if tag == 'staticText':
                t_el = el.find('{http://jasperreports.sourceforge.net/jasperreports}text')
                if t_el is not None and t_el.text:
                    text_val = t_el.text
            elif tag == 'textField':
                tfe = el.find('{http://jasperreports.sourceforge.net/jasperreports}textFieldExpression')
                if tfe is not None and tfe.text:
                    text_val = evaluate_expression(tfe.text)
                        
            if not text_val:
                continue
                
            te = el.find('{http://jasperreports.sourceforge.net/jasperreports}textElement')
            font_size = 8
            font_name = 'Arial'
            is_bold = False
            align = 'left'
            valign = 'top'
            
            if te is not None:
                align = te.attrib.get('textAlignment', 'left').lower()
                valign = te.attrib.get('verticalAlignment', 'top').lower()
                f_el = te.find('{http://jasperreports.sourceforge.net/jasperreports}font')
                if f_el is not None:
                    font_size = float(f_el.attrib.get('size', 8))
                    font_name = f_el.attrib.get('fontName', 'Arial')
                    is_bold = f_el.attrib.get('isBold', 'false').lower() == 'true'
                    
            if 'times' in font_name.lower():
                font = f_times_bold(font_size) if is_bold else f_times_reg(font_size)
            else:
                font = f_arial_bold(font_size) if is_bold else f_arial_reg(font_size)
                
            lines = text_val.split('\n')
            line_h = int((font_size + 3) * scale)
            
            for line_idx, line_str in enumerate(lines):
                bbox = font.getbbox(line_str) if hasattr(font, 'getbbox') else (0, 0, len(line_str)*6*scale, line_h)
                line_w = bbox[2] - bbox[0]
                
                if align in ('right', 'end'):
                    draw_x = x + w - line_w - (2 * scale)
                elif align in ('center', 'centre'):
                    draw_x = x + (w - line_w) // 2
                else:
                    draw_x = x + (2 * scale)
                    
                if valign in ('middle', 'center'):
                    draw_y = y + (h - len(lines) * line_h) // 2 + line_idx * line_h
                elif valign in ('bottom',):
                    draw_y = y + h - len(lines) * line_h + line_idx * line_h - (1 * scale)
                else:
                    draw_y = y + (1 * scale) + line_idx * line_h
                    
                draw.text((draw_x, draw_y), line_str, fill=(0, 0, 0), font=font)

# 4. Draw realistic FEBRABAN Code 128 / Interleaved 2 of 5 barcode (y=750..787)
bc_y = top_m + 747 * scale
bc_h = 38 * scale
curr_bc_x = left_m + 2 * scale
# FEBRABAN barcode 2 of 5 interleaved pattern
import random
random.seed(422)
pattern = []
for _ in range(70):
    pattern.extend([random.choice([2, 4, 1, 3]) * scale, random.choice([2, 3, 1]) * scale])
for i, bar in enumerate(pattern):
    if i % 2 == 0:
        draw.rectangle([curr_bc_x, bc_y, curr_bc_x + bar, bc_y + bc_h], fill=(0, 0, 0))
    curr_bc_x += bar
    if curr_bc_x > left_m + 420 * scale:
        break

# Save full A4 preview
out_preview = 'c:/Users/SAAV166/Documents/Agente/preview_boleto_safra_completo.png'
img.save(out_preview, quality=95)

# Save zoom sections
zoom_ficha = img.crop((left_m - 5*scale, top_m + 465*scale, left_m + 540*scale, top_m + 540*scale))
zoom_ficha.save('c:/Users/SAAV166/Documents/Agente/preview_zoom_ficha.png')

zoom_recibo = img.crop((left_m - 5*scale, top_m, left_m + 540*scale, top_m + 110*scale))
zoom_recibo.save('c:/Users/SAAV166/Documents/Agente/preview_zoom_recibo.png')

# Save zoom of bottom barcode area
zoom_codigo_barras = img.crop((left_m - 5*scale, top_m + 690*scale, left_m + 540*scale, top_m + 795*scale))
zoom_codigo_barras.save('c:/Users/SAAV166/Documents/Agente/preview_zoom_barcode.png')

print("All realistic previews generated successfully!")
