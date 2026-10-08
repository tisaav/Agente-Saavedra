import xml.etree.ElementTree as ET
import base64

# Read safra_escudo_clean.png
with open('safra_escudo_clean.png', 'rb') as f:
    escudo_b64 = base64.b64encode(f.read()).decode('ascii')

# Read safra_horizontal_clean.png
with open('safra_horizontal_clean.png', 'rb') as f:
    horiz_b64 = base64.b64encode(f.read()).decode('ascii')

print(f"Escudo B64 length: {len(escudo_b64)}")
print(f"Horiz B64 length: {len(horiz_b64)}")
