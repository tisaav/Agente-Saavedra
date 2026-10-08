# Nota já Confirmada, liberação não pode ser reprovada

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14522438394519-Nota-j%C3%A1-Confirmada-libera%C3%A7%C3%A3o-n%C3%A3o-pode-ser-reprovada](https://ajuda.sankhya.com.br/hc/pt-br/articles/14522438394519-Nota-j%C3%A1-Confirmada-libera%C3%A7%C3%A3o-n%C3%A3o-pode-ser-reprovada)  
> **ID:** `14522438394519` | **Última Atualização:** 2026-07-22T14:58:35Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16843137617687)

 MENSAGEM:**

[CORE_E02837]: Nota já Confirmada, liberação não pode ser reprovada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16843137619863)

SOLUÇÃO:**

O evento de liberação ocorre antes da confirmação, toda validação realizada pela rotina é antes da confirmação do pedido, tanto que pra conseguir confirmar o pedido tem que ser realizada a liberação para o evento solicitado. Neste caso foi realizada a liberação e o pedido foi confirmado, por isso a mensagem é apresentada. Assim, o que pode ser feito é um cancelamento ou exclusão do pedido, mas negar a liberação não será possível.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16843150674455)

CAUSA:**

Ocorre ao tentar negar a liberação de um pedido que já foi confirmado.