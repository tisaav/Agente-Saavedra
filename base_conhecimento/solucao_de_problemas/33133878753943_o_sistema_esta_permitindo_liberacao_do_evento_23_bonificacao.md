# O sistema está permitindo liberação do evento 23 - Bonificação mesmo tendo atingido o limite de liberação no período para o liberador

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33133878753943-O-sistema-est%C3%A1-permitindo-libera%C3%A7%C3%A3o-do-evento-23-Bonifica%C3%A7%C3%A3o-mesmo-tendo-atingido-o-limite-de-libera%C3%A7%C3%A3o-no-per%C3%ADodo-para-o-liberador](https://ajuda.sankhya.com.br/hc/pt-br/articles/33133878753943-O-sistema-est%C3%A1-permitindo-libera%C3%A7%C3%A3o-do-evento-23-Bonifica%C3%A7%C3%A3o-mesmo-tendo-atingido-o-limite-de-libera%C3%A7%C3%A3o-no-per%C3%ADodo-para-o-liberador)  
> **ID:** `33133878753943` | **Última Atualização:** 2026-07-22T14:29:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33181896425111)

 **MENSAGEM:**

[CORE_E03924] Valor acima do permitido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33133842572567)

 **SITUAÇÃO:**

Quando um pedido de venda do tipo bonificação é lançado e passa pela liberação do evento 23, o sistema bloqueia novas liberações ao atingir o limite configurado, exibindo a mensagem: "Valor acima do permitido". No entanto, se um dos pedidos liberados for faturado, o sistema permite novas liberações, possibilitando que o valor total ultrapasse o limite definido para o período.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33133842573335)

CAUSA:**

Esse cenário geralmente ocorre quando a TOP utilizada no faturamento não está configurada como **"Bonificação"**. Nesse caso, o valor do pedido deixa de ser considerado entre os pedidos pendentes de liberação, e o valor da nota fiscal também não é contabilizado como liberado, justamente porque a TOP utilizada no faturamento não corresponde ao tipo **"Bonificação".**

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33133842573847)

SOLUÇÃO: **

Verifique se a TOP utilizada no faturamento está corretamente configurada. Para que a bonificação seja considerada no saldo de liberações do evento 23 – Bonificação, é necessário utilizar uma TOP com o campo "Bonificação" marcado na aba "Geral" do seu cadastro.

 

![tipos de operação.png](https://ajuda.sankhya.com.br/hc/article_attachments/33181886985111)