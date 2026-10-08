path = 'C:/Users/SAAV166/Downloads/Bol_Safra.jrxml'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace width="356" with width="347" so 188 + 347 = 535 (exact right border)
old_tag = '<reportElement key="textField-13" x="188" y="482" width="356" height="18" />'
new_tag = '<reportElement key="textField-13" x="188" y="482" width="347" height="18" />'

assert old_tag in content, "old_tag not found!"
content = content.replace(old_tag, new_tag)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

with open('c:/Users/SAAV166/Documents/Agente/modelos_safra/Bol_Safra_HOMOLOGADO.jrxml', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated textField-13 width to 347! Right edge is now exactly 535!")
