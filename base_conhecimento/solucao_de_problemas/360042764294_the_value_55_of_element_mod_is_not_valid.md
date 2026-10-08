# The value '55' of element 'mod' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042764294-The-value-55-of-element-mod-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042764294-The-value-55-of-element-mod-is-not-valid)  
> **ID:** `360042764294` | **Última Atualização:** 2026-07-22T16:05:55Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514737913623)

 MENSAGEM:**

The value '55' of element 'mod' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514721330071)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514737917335)

 Localize a nota de compra que originou a devolução, verifique o 'Tipo de Operação' utilizado na mesma. Através dessa TOP acesse a tela "[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)" (*Caminho de acesso: Comercial » Arquivo » Cadastros/Financeiro » Arquivos » Cadastros)* e inicie as análises abaixo:

- Aba **"NF-e/NFC-e"** » "**Modelo do Documento"**: 55 - Nota Fiscal Eletrônica.

- Aba **"NF-e/NFC-e"** » campo "**NF-e"**: Terceiros.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514737918999)

 Abra a nota de origem através da Central de Compras e verifique se existe "**Chave NF-e"** informada. Em caso negativo, insira essa informação.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514721337111)

 Caso a TOP possua informações que diferem do item 1, realize os devidos ajustes e relance a nota de entrada. Para isso, inutilize/exclua a devolução que gerou esse incidente.

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514721342103)

 **Por fim, refaça o lançamento da nota de entrada, em seguida emita a devolução.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514721344151)

CAUSA:**

Rejeição apresentada, em sua maioria, na emissão de devoluções, onde a nota de origem possui informações diferentes do definido abaixo:

- "**NF-e**" = [Normal]

- "**Modelo do documento**" = [55]

- "**Chave NF-e**" = [Preenchida e existente na SEFAZ].

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16514737928855)

 IMPORTANTE:**

Mesmo que atualmente as informações acima estejam corretas, o ajuste pode ter sido realizado após lançamento da nota. Dessa forma indicamos a realização das etapas 3 e 4.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)