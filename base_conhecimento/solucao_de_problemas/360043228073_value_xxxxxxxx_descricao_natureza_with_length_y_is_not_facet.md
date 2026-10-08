# Value 'XXXXXXXX - Descrição Natureza' with length = 'Y' is not facet-valid with respect to maxLength '60' . of element 'natOp' is not valid [...]

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043228073-Value-XXXXXXXX-Descri%C3%A7%C3%A3o-Natureza-with-length-Y-is-not-facet-valid-with-respect-to-maxLength-60-of-element-natOp-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043228073-Value-XXXXXXXX-Descri%C3%A7%C3%A3o-Natureza-with-length-Y-is-not-facet-valid-with-respect-to-maxLength-60-of-element-natOp-is-not-valid)  
> **ID:** `360043228073` | **Última Atualização:** 2026-07-22T16:06:17Z

---

** 

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087245456791)

 MENSAGEM:**

cvc-maxLength-valid: Value 'XXXXXXXX - Descrição Natureza' with length = 'Y' is not facet-valid with respect to maxLength '60' for type '#AnonType_natOpideinfNFeTNFe'.
cvc-type.3.1.3: The value 'XXXXXXXX - Descrição Natureza' of element 'natOp' is not valid.

 

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087226757783)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087245462295)

 Ajuste a descrição utilizada para a respectiva 'Natureza da Operação', de forma que seja respeitado o limite máximo de 60 caracteres:

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087245466391)

 Acesse o cadastro do **["Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** *(Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), *na aba **"Livro Fiscal"** e verifique se existem informações inseridas no campo "**Natureza da Operação (SPED)"**. Em caso positivo, ajuste/abrevie essa informação para que o limite de caracteres seja aceito. Inutilize/exclua a nota emitida e refaça o lançamento.

Caso não existam informações inseridas no campo mencionado acima, siga para as próximas etapas:

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087245468951)

 Acesse a tela "**[CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714)"** *(Caminho de acesso: Comercial » Arquivo » Cadastros)*, localize a CFOP utilizada/rejeitada, conforme mencionado na respectiva rejeição.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087245470999)

 Ajuste o campo "**Descrição da CFOP"**, de forma que o limite de 60 caracteres seja respeitado.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087245472919)

 Realizado o ajuste, redigite o cabeçalho da nota e gere um novo lote. Caso a informação não seja atualizada, recomenda-se inutilização/exclusão da nota e geração de um novo lançamento.

 

** 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087226777367)

 CAUSA:**

Mensagem apresentada ao realizar emissão de uma NF-e, onde a descrição da 'Natureza da Operação' utilizada é superior ao limite aceito de 60 caracteres.


---

### 🔗 Links e Referências Internas:

- ["Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714)