import re

with open('modelos_safra/Boleto_Itau.jrxml', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

print('Length:', len(content))
images = re.findall(r'<image.*?</image>', content, re.DOTALL)
print('Images count:', len(images))
for i, img in enumerate(images):
    print(f'Image {i}:', img)

for word in ['banco', 'itau', 'safra', 'logo', 'header', 'cabecalho', '341', '422']:
    matches = re.findall(rf'.{{0,40}}{word}.{{0,40}}', content, re.IGNORECASE)
    print(f'Word "{word}": count {len(matches)}')
    for m in matches[:3]:
        print('  ', repr(m.strip()))
