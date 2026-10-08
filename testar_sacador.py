from PIL import Image, ImageDraw, ImageFont

scale = 2
w = 535 * scale
h = 100 * scale

img = Image.new('RGB', (w, h), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Font 6pt (12px at scale 2)
font_6 = ImageFont.truetype("arial.ttf", 6 * scale)
font_8_bold = ImageFont.truetype("arialbd.ttf", 8 * scale)

# Box 1: Pagador rectangle at y=0, height=39*scale (ends at 39*scale)
draw.rectangle([0, 0, w - 1, 39 * scale], outline=(0, 0, 0), width=1)

# Box 2: Ficha de compensacao / Autenticacao at y=39*scale, height=12*scale (ends at 51*scale)
draw.rectangle([0, 39 * scale, w - 1, 51 * scale], outline=(0, 0, 0), width=1)

# Text: Ficha de compensacao / Autenticacao Mecanica right-aligned
auth_txt = "Ficha de Compensação/Autenticação Mecânica"
bbox_auth = font_8_bold.getbbox(auth_txt)
draw.text((w - (bbox_auth[2] - bbox_auth[0]) - 5*scale, 40 * scale), auth_txt, fill=(0, 0, 0), font=font_8_bold)

# Draw 4 lines of Pagador inside Box 1
lines = [
    "Pagador: HOSPITAL DE CLINICAS DE PORTO ALEGRE - 87.020.517/0001-20",
    "R RAMIRO BARCELOS, 2350",
    "90.035-003-Porto Alegre-RS",
    "Sacador/Avalista"
]

y_curr = 2 * scale
line_h = int(8.2 * scale)
for line in lines:
    draw.text((3 * scale, y_curr), line, fill=(0, 0, 0), font=font_6)
    y_curr += line_h

# Draw Barcode below Box 2 (at y=56*scale)
bc_y = 56 * scale
bc_h = 36 * scale
curr_bc_x = 2 * scale
import random
random.seed(422)
pattern = []
for _ in range(70):
    pattern.extend([random.choice([2, 4, 1, 3]) * scale, random.choice([2, 3, 1]) * scale])
for i, bar in enumerate(pattern):
    if i % 2 == 0:
        draw.rectangle([curr_bc_x, bc_y, curr_bc_x + bar, bc_y + bc_h], fill=(0, 0, 0))
    curr_bc_x += bar
    if curr_bc_x > w - 100 * scale:
        break

img.save('test_sacador_corrigido.png')
print("Saved test_sacador_corrigido.png!")
