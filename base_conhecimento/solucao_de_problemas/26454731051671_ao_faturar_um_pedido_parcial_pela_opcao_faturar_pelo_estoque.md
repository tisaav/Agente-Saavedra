# Ao faturar um pedido parcial pela opção  faturar pelo estoque, o restante do pedido está ficando como não pendente

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26454731051671-Ao-faturar-um-pedido-parcial-pela-op%C3%A7%C3%A3o-faturar-pelo-estoque-o-restante-do-pedido-est%C3%A1-ficando-como-n%C3%A3o-pendente](https://ajuda.sankhya.com.br/hc/pt-br/articles/26454731051671-Ao-faturar-um-pedido-parcial-pela-op%C3%A7%C3%A3o-faturar-pelo-estoque-o-restante-do-pedido-est%C3%A1-ficando-como-n%C3%A3o-pendente)  
> **ID:** `26454731051671` | **Última Atualização:** 2026-07-22T14:42:06Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26456188084503)

 **SITUAÇÃO:**

Ao faturar um pedido parcial pela opção faturar pelo estoque, o restante do pedido está ficando como não pendente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26454716743319)

SOLUÇÃO:**

Isso é um comportamento do sistema. Para deixar o restante do pedido como pendente, use a opção de faturar pelo estoque deixando pendente. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/26454716753431)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26454731048215)

CAUSA:**

Essa particularidade é quando usa a opção de faturar pelo estoque, na qual tem casos que só serão faturados os itens que realmente tem no estoque. Essa opção não olha os parâmetros **FATCORTITNS** e **ZERARQTDCONF,** pois temos a opção de Faturar pelo estoque deixando pendente que resolve o problema.