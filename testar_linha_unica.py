from PIL import Image, ImageDraw, ImageFont

# Canvas width = 535 * 2, height = 45 * 2
scale = 2
w = 535 * scale
h = 45 * scale
img = Image.new('RGB', (w, h), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Load fonts
font_arial_10 = ImageFont.truetype("arialbd.ttf", 10 * scale)
font_times_10 = ImageFont.truetype("timesbd.ttf", 10 * scale)
font_times_105 = ImageFont.truetype("timesbd.ttf", int(10.5 * scale))

shield = Image.open('safra_escudo_clean.png')
sh_h = 26 * scale
sh_w = int(shield.width * sh_h / shield.height)
shield_resized = shield.resize((sh_w, sh_h), Image.Resampling.LANCZOS)

# Paste shield at x=6
img.paste(shield_resized, (6 * scale, 3 * scale), shield_resized)

# Bank name at x=36
draw.text((36 * scale, 10 * scale), "BANCO SAFRA S/A", fill=(0, 0, 0), font=font_arial_10)

# Pipe at x=140
draw.text((140 * scale, 10 * scale), "|", fill=(0, 0, 0), font=font_arial_10)

# Code at x=148
draw.text((148 * scale, 10 * scale), "422-7", fill=(0, 0, 0), font=font_arial_10)

# Pipe at x=182
draw.text((182 * scale, 10 * scale), "|", fill=(0, 0, 0), font=font_arial_10)

# Test Linha Digitável
linha = "42297.00002 70058.439194 00000.013219 4 15560000155409"
bbox_times = font_times_10.getbbox(linha)
w_times = bbox_times[2] - bbox_times[0]
print(f"Linha digitavel width at 10pt: {w_times / scale:.1f} pt (available width: 345 pt)")

# Draw right-aligned within x=190..535 (width 345)
linha_x = 535 * scale - w_times
draw.text((linha_x, 10 * scale), linha, fill=(0, 0, 0), font=font_times_10)

img.save('mockup_linha_unica.png')
print('Saved mockup_linha_unica.png')
