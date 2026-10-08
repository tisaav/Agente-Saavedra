# The value 'XXXXXXX' of element 'xNome' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042723354-The-value-XXXXXXX-of-element-xNome-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042723354-The-value-XXXXXXX-of-element-xNome-is-not-valid)  
> **ID:** `360042723354` | **Última Atualização:** 2026-07-22T16:06:54Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511664278039)

 MENSAGEM:**

cvc-pattern-valid: Value 'XXXX' is not facet-valid with respect to pattern '[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}' for type '#AnonType_xNomeTLocal'.
cvc-type.3.1.3: The value 'XXXXXXX' of element '**xNome**' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511664282903)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511676909463)

 Identifique na mensagem/rejeição retornada a qual cadastro refere-se a descrição do nome mencionado.

- No exemplo: The value **'XXXXXXX'** of element **'xNome**' is not valid, a descrição rejeitada trata-se do 'XXXXXXX'.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511676912919)

Acesse a tela **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho de acesso:* Configurações » Cadastros*).

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511676919063)

 Busque pelo cadastro mencionado na rejeição, conforme identificado no item 1.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511676925719)

 Para os campos "**Nome Parceiro"** e **'Razão Social"** apague toda a informação digitada e digite novamente. Certifique-se que não existe espaço em branco no início da descrição e evite ctrl+c, ctrl+v, para não copiar espaços ou caracteres indevidos:

 

![The_value__XXXXXXX__of_element__xNome__is_not_valid.png](https://ajuda.sankhya.com.br/hc/article_attachments/14610996920343)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511676927383)

 Realizado o ajuste, busque autorização para que a NF-e fique 'Aguardando Correção', posteriormente, redigite a informação 'Parceiro' no cabeçalho da nota e gere um novo lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511664301591)

 CAUSA:**

Rejeição apresentada quando a descrição de determinado 'Nome' enviado nas tag's do XML possuem espaço em branco, duplicidade de informações e/ou caracteres especiais. 

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511676934295)

 OBSERVAÇÃO:**

Verificar o parâmetro **"*****RAZDESTINADANFE-Razão Social do destinatário p/impressão no DANFE"**, *caso esteja com a opção 'Razão Social e Nome', levará as duas informações no DANFE e caso seja extenso demais o nome e razão social, irá extrapolar o limite do campo no XML.


---

### 🔗 Links e Referências Internas:

- [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)