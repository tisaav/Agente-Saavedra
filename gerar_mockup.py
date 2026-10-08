from PIL import Image, ImageDraw, ImageFont

# Create a mockup canvas of width 535 * 2 (for high dpi) and height 40 * 2
scale = 2
w = 535 * scale
h = 45 * scale
img = Image.new('RGB', (w, h), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Load fonts
try:
    font_bold = ImageFont.truetype("arialbd.ttf", 10 * scale)
    font_bold_lg = ImageFont.truetype("arialbd.ttf", 11 * scale)
    font_times = ImageFont.truetype("timesbd.ttf", 11 * scale)
except:
    font_bold = ImageFont.load_default()
    font_bold_lg = font_bold
    font_times = font_bold

# Paste shield at x=15*scale, y=4*scale, height=25*scale
shield = Image.open('safra_escudo_clean.png')
sh_h = 26 * scale
sh_w = int(shield.width * sh_h / shield.height)
shield_resized = shield.resize((sh_w, sh_h), Image.Resampling.LANCZOS)
img.paste(shield_resized, (15 * scale, 3 * scale), shield_resized)

# Draw Bank Name at x=(15*scale + sh_w + 10*scale), y=12*scale
bank_x = 15 * scale + sh_w + 12 * scale
draw.text((bank_x, 10 * scale), "BANCO SAFRA S/A", fill=(0, 0, 0), font=font_bold)

# Draw Pipe at x=202*scale
draw.text((202 * scale, 10 * scale), "|", fill=(0, 0, 0), font=font_bold)

# Draw Bank Code at x=209*scale
draw.text((210 * scale, 10 * scale), "422-7", fill=(0, 0, 0), font=font_bold_lg)

# Draw Pipe at x=239*scale
draw.text((239 * scale, 10 * scale), "|", fill=(0, 0, 0), font=font_bold)

# Draw Linha digitavel at x=247*scale
draw.text((247 * scale, 9 * scale), "42297.00002 70058.439194 00000.006015 9 15570000513016", fill=(0, 0, 0), font=font_times)

img.save('mockup_header_safra.png')
print('Saved mockup_header_safra.png')
