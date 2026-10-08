# Importador de Dados - Erro: Registro já existente na Tabela de Preços para esta Data de Vigor

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30653008420119-Importador-de-Dados-Erro-Registro-j%C3%A1-existente-na-Tabela-de-Pre%C3%A7os-para-esta-Data-de-Vigor](https://ajuda.sankhya.com.br/hc/pt-br/articles/30653008420119-Importador-de-Dados-Erro-Registro-j%C3%A1-existente-na-Tabela-de-Pre%C3%A7os-para-esta-Data-de-Vigor)  
> **ID:** `30653008420119` | **Última Atualização:** 2026-08-01T02:38:22Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30698298456599)

 MENSAGEM:**

Registro já existente na Tabela de Preços para esta Data de Vigor. Cód.Produto: X Cód.Local: Y Controle: Z

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30698340696215)

 SITUAÇÃO:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653008386583)

 Ao realizar uma importação de dados usando como modelo a "**Tabela de preço por produto**", ocorre o erro abaixo. A mesma lógico pode ser aplicada para o mesmo erro na importação de outros modelos.

 

![Importador de dados - Erro Registro já existente na 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/30698255524631)

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653008386583)

 Este artigo tem como objetivo apresentar a solução para o erro acima, partindo do pressuposto de que o usuário já possui conhecimento sobre a criação, preenchimento e importação de arquivos **CSV** no sistema. Por isso, não serão abordadas as etapas de importação nem as regras necessárias para esse processo.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653008386583)

Antes de ir para solução, é necessário entender se a importação está **inserindo** novos produtos na tabela em questão ou está **alterando** o preço dos produtos já existentes na tabela de preços, pois o preenchimento do arquivo CSV muda dependendo da ação realizada.  

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653015193623)

SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653008392599)

 Se os dados inseridos no arquivo CSV tem o objetivo de inserir novos produtos, a lógica abaixo deve ser seguida.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653015196823)

**Identifique o número único da tabela de preço onde o produto deve ser incluído. 

 

![Importador de dados - Erro Registro já existente na 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/30698255527319)

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653015196823)

**No arquivo CSV informamos o código do produto, o número da tabela e o valor de venda.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30653015201943)

 

**Observação:** O campo **AD_IDEXTERNO** pode ficar em branco, por se tratar de uma inserção de dados. Mas lembrando que esse campo deve existir na tabela **TGFEXC**. Já, o campo **CODLOCAL,** só deve ser preenchido se o parâmetro **PRECOPORLOC** estiver ligado.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653008400407)

 Se o objetivo é apenas alterar valores de produtos já existentes na tabela de preço, seguimos essa lógica.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30653015196823)

 **Siga a mesma lógica do passo 1, porém a diferença é que será necessário informar não só no arquivo CSV mas também na tela tabela de preços o campo **AD_IDEXTERNO**, caso contrário resultará no erro.

 

![Importador de dados - Erro Registro já existente na 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/30698255528727)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30653008409239)

 

**Observação:** o código informado na tela deverá ser o mesmo código informado no arquivo.