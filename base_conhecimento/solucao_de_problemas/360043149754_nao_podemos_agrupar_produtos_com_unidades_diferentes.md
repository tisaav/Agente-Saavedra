# Não podemos agrupar produtos com unidades diferentes

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043149754-N%C3%A3o-podemos-agrupar-produtos-com-unidades-diferentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043149754-N%C3%A3o-podemos-agrupar-produtos-com-unidades-diferentes)  
> **ID:** `360043149754` | **Última Atualização:** 2026-07-22T16:04:01Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986426647)

 MENSAGEM:**

Não podemos agrupar produtos com unidades diferentes.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120982448791)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986429463)

 Identifique dentre os pedidos que irão originar o faturamento, quais os produtos encontram-se repetidos e possuem Unidades diferentes.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458169424663)

 Exemplo:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986431895)

Pedido Número 10

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986433815)

 Produto A » Unidade CX (Caixa)

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986433815)

 Produto B » Unidade PT (Pacote)

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986433815)

 **Produto E » Unidade KG (Kilo)**

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986431895)

Pedido Número 11

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986433815)

 Produto A » Unidade CX (Caixa)

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986433815)

 Produto B » Unidade PT (Pacote)

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986433815)

 **Produto E » Unidade CX (Caixa)**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986436631)

 Ao selecionar ambos os pedidos e realizar o faturamento, o erro será reportado, pois o **Produto E **foi lançado como **Unidade KG** e em outro momento com **Unidade CX**.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986431895)

Para solucionar o caso, ajuste um dos pedidos igualando as informações de Unidade.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16120986438551)

 CAUSA:**

Ocorre quando ao realizar faturamento agrupando mais de 1 pedido, onde exista para o mesmo Cód.Produto lançamentos com Unidades diferentes.