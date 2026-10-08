import xml.etree.ElementTree as ET
import re

with open('modelos_safra/Bol_Safra_CORRIGIDO.jrxml', 'r', encoding='utf-8') as f:
    text = f.read()

for key in ['staticText-24', 'staticText-25', 'staticText-26', 'staticText-27', 'staticText-28',
            'staticText-55', 'staticText-52', 'staticText-53', 'staticText-54', 'textField-13',
            'image-safra-1', 'image-safra-2']:
    m = re.search(rf'<[^>]*key="{key}"[^>]*>.*?</(staticText|textField|image)>', text, re.DOTALL)
    if m:
        print(f"=== KEY: {key} ===\n{m.group(0)}\n")
