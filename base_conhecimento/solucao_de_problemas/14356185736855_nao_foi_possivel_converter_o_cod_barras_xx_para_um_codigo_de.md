# Não foi possível converter o cód. barras: "''XX" para um código de produto válido

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14356185736855-N%C3%A3o-foi-poss%C3%ADvel-converter-o-c%C3%B3d-barras-XX-para-um-c%C3%B3digo-de-produto-v%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/14356185736855-N%C3%A3o-foi-poss%C3%ADvel-converter-o-c%C3%B3d-barras-XX-para-um-c%C3%B3digo-de-produto-v%C3%A1lido)  
> **ID:** `14356185736855` | **Última Atualização:** 2026-07-22T14:58:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867603692695)

 MENSAGEM:**

[CORE_E01283]: Não foi possível converter o cód. barras: "''XX" para um código de produto válido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867603694615)

SOLUÇÃO:**

Verifique na tela de configurações de Conferência, no campo **"Buscar código de barras por",** qual configuração está definida e avalie se o código informado na conferência está coerente com a configuração. 

Buscar código de barras por: o  sistema irá utilizar esse campo para identificar onde procurar o **"Produto".**  As opções são as seguintes:

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450657310615)

 Automático:** o produto será localizado através da seguinte ordem:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867572871703)

 Pelo campo **"Cód. de Barras",** da aba** "Estoque";**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867572873495)

 Pelo campo Código de Barras, da aba **"Unidades Alternativas",** ou pelo campo Cód. Barras da aba **"Código de barras"**, desde que tenha-se o campo **"Unidade de volume"** informado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867572874647)

 Pelo campo "**Referência**", do cadastro de produto, ou pelo campo Cód. Barras, da aba Código de barras, que não tenha Unidade de volume informada ou cuja Unidade de volume seja a mesma do produto.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450657310615)

 Código do produto:** o sistema pesquisará no **"Cadastro de Produtos"**, em que o Cód. de barra é igual ao Código do produto.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450657310615)

 Referência:** o sistema pesquisará pelo campo Referência, do Cadastro de Produtos ou pelo campo Cód. Barras, da aba Código de barras (também no Cadastro de Produtos), que não tenha Unidade de Volume informada ou que a Unidade de Volume, seja a mesma do produto.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450657310615)

 Unidade alternativa:** a pesquisa será feita pelo campo Código de Barras, da aba Unidades Alternativas, ou pelo campo Cód. Barras, da aba Código de barras, que tenha o campo Unidade de Volume informado e que seja diferente da Unidade de Volume do produto.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450657310615)

 Estoque:** a busca será feita pelo campo Cód. de Barras, da aba Estoque (Cadastro de Produtos).