# SQL-50001 - A base e o valor de IPI devem ser zero (0) para o produto: XXXXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16477401076759-SQL-50001-A-base-e-o-valor-de-IPI-devem-ser-zero-0-para-o-produto-XXXXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/16477401076759-SQL-50001-A-base-e-o-valor-de-IPI-devem-ser-zero-0-para-o-produto-XXXXXX)  
> **ID:** `16477401076759` | **Última Atualização:** 2026-07-22T14:55:09Z

---

**  

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16477401056023)

  MENSAGEM:**

SQL-50001 - A base e o valor de IPI devem ser zero (0) para o produto: XXXXXX.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16477354888471)

 CAUSA:**

Ocorre devido ao cadastro do Produto a opção do **IPI** estar desmarcada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16477371917463)

 SOLUÇÃO:**

-  Verifique se no XML o produto possui IPI;

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16481289986583)

  No cadastro do Produto pode ser que o produto tenha informações do valor de IPI, porém no cadastro do produto não está marcado para **"Calcular IPI"**. Esse processo vale para ambos (compra e venda). Então acesse:

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16481289993623)

 *Configurações » Cadastros » Produtos » Produtos:*

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16481289998743)

Aba **"Imposto"**, campo **"Tem IPI"**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16480663297815)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16481281863063)

  Verifique se na aba** Impostos / Informações por empresa** possui cadastro para empresa que está sendo importado XML.

Se essa aba estiver preenchida deverá ser preenchido também as configurações dos impostos pois a mesma sobrepõe as informações da aba **Impostos**.

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16481289993623)

 *Configurações » Cadastros » Produtos » Produtos:*

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16481289998743)

Aba **Impostos / Informações por empresa **campo**: "**IPI na Entrada" "IPI na Saída"

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16481012874647)

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16481290015895)

 Após realizar os ajustes deverá importar o XML novamente e Processar Arquivo.