import base64
import xml.etree.ElementTree as ET

# Read Base64 of the clean shield
with open('safra_escudo_clean.png', 'rb') as f:
    b64_shield = base64.b64encode(f.read()).decode('ascii')

# Read Bol_Safra_CORRIGIDO.jrxml
with open('modelos_safra/Bol_Safra_CORRIGIDO.jrxml', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new Recibo do Pagador header elements
recibo_header_old_pattern = r'<image onErrorType="Blank">\s*<reportElement key="image-safra-1".*?</staticText>'
# Let's inspect the exact lines around image-safra-1 in Bol_Safra_CORRIGIDO.jrxml
