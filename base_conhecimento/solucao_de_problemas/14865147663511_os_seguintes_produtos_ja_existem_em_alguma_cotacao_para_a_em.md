# Os seguintes produtos já existem em alguma cotação para a empresa  com o situação igual a "Aberta", portanto não é possível incluí-los. Produtos: XXXXXX - Altere o produto ou volte para a rotina de cotação

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14865147663511-Os-seguintes-produtos-j%C3%A1-existem-em-alguma-cota%C3%A7%C3%A3o-para-a-empresa-com-o-situa%C3%A7%C3%A3o-igual-a-Aberta-portanto-n%C3%A3o-%C3%A9-poss%C3%ADvel-inclu%C3%AD-los-Produtos-XXXXXX-Altere-o-produto-ou-volte-para-a-rotina-de-cota%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/14865147663511-Os-seguintes-produtos-j%C3%A1-existem-em-alguma-cota%C3%A7%C3%A3o-para-a-empresa-com-o-situa%C3%A7%C3%A3o-igual-a-Aberta-portanto-n%C3%A3o-%C3%A9-poss%C3%ADvel-inclu%C3%AD-los-Produtos-XXXXXX-Altere-o-produto-ou-volte-para-a-rotina-de-cota%C3%A7%C3%A3o)  
> **ID:** `14865147663511` | **Última Atualização:** 2026-08-05T15:23:20Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16620955475351)

 MENSAGEM:**

[CORE_E00275]: Os seguintes produtos já existem em alguma cotação para a empresa com o situação igual a "Aberta", portanto não é possível incluí-los. Produtos: XXXXXX - Altere o produto ou volte para a rotina de cotação.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16620943747991)

SOLUÇÃO:**

Caso o produto a ser inserido seja repetido na mesma cotação e o parâmetro esteja configurado para não permitir a inserção; tem-se a exibição da seguinte mensagem:

***"Os seguintes produtos já existem em alguma cotação para a empresa X com o situação igual a "Aberta", portanto não é possível incluí-los. Produtos:***

***Y - "NOMEDOPRODUTO"***

Através do parâmetro **"Código p/ produto genérico na cotação - CODPRODGENCOT"**, o comprador permite ou não o lançamento de produtos repetidos na cotação. O parâmetro pode ser configurado com três valores:

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450600597399)

 -1 (menos um):** caso seja informado este valor, todo e qualquer produto poderá se repetir no lançamento da cotação;

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450600597399)

 0 (zero):** informando este valor, nenhum produto poderá se repetir no lançamento da cotação;

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450600597399)

 Valor maior que 0:** neste caso, deve-se informar o código do produto que poderá se repetir, sendo permitida repetição somente para este produto no lançamento da cotação.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16620943750039)

 **OBSERVAÇÃO:**

Caso o produto esteja sendo inserido com o mesmo controle, codvol e codlocal iguais, a aplicação entende que se trata do mesmo produto. Então, este só pode ter um fornecedor aprovado associado ao mesmo produto. Caso o produto possua controle ou codlocal diferentes, o sistema não barra o processo.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14865242862231)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16620955484567)

CAUSA:**

Ocorre quando o produto é repetido e o parâmetro CODPRODGENCOT  não permite produto repetido.