# Produto deve ser negociado em múltiplos de XX

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9678465387287-Produto-deve-ser-negociado-em-m%C3%BAltiplos-de-XX](https://ajuda.sankhya.com.br/hc/pt-br/articles/9678465387287-Produto-deve-ser-negociado-em-m%C3%BAltiplos-de-XX)  
> **ID:** `9678465387287` | **Última Atualização:** 2026-07-22T15:06:35Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19572724990359)

 MENSAGEM:**

[CORE_E01987] Produto deve ser negociado em múltiplos de XX.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19572787002263)

 SITUAÇÃO:**

Ao confirmar o produto de unidade alternativa no portal a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19572725012119)

 CAUSA:**

Quando o produto possui agrupamento mínimo e é informada uma quantidade diferente das múltiplas permitidas.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19572787007255)

 SOLUÇÃO:**

Esse aviso acontece porque na tela Cadastro de **Produtos** *(Caminho de acesso à tela: Configurações » Cadastros » Produtos)* está cadastrado o agrupamento mínimo exemplo de 5,40. Desta forma, ele somente permitirá colocar na quantidade da nota múltiplos de 5,40 e não deixará colocar a quantidade 2/4/9, por exemplo. Assim, colocando um valor diferente será gerado esse aviso de erro. 

![produtos 05-12.png](https://ajuda.sankhya.com.br/hc/article_attachments/19572725018263)

O campo "Agrupamento mínimo" comporta os dados pertinentes ao agrupamento mínimo para a venda ou compra do produto, ou seja, a negociação desse produto só poderá ser feita com quantidades múltiplas do valor (4 casas decimais) informado nesse campo.

***Exemplo:*** *Temos o produto "Ovo" com sua Unidade padrão: unidade e para ele é definido um agrupamento mínimo de 12. Na inserção do item na nota, o campo "Quantidade" deverá ser preenchido com um múltiplo de 12.*

**

![7ee58381fa59853aa1aa73e570094f15067dd97a_2_500x500.gif](https://ajuda.sankhya.com.br/hc/article_attachments/9678442058775)

 Informando no campo Agrupamento mínimo o valor 0 (zero), será aceita qualquer quantidade na compra.**

Desta forma, caso queira que seja digitado o valor diferente de múltiplos de 5,40, por exemplo, é necessário deixar o campo em branco ou inserir o número 0. Assim, será possível digitar a quantidade desejada.