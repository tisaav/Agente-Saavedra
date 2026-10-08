# Total deve ser diferente de zero

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042916974-Total-deve-ser-diferente-de-zero](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042916974-Total-deve-ser-diferente-de-zero)  
> **ID:** `360042916974` | **Última Atualização:** 2026-08-05T19:51:42Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117073901591)

 MENSAGEM:**

[CORE_E03242] Total deve ser diferente de zero.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117073905047)

 SITUAÇÃO:**

Ao tentar confirmar um pedido/nota a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117073907479)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117073913239)

 **Analise o lançamento verificando se o valor do produto ou da nota devem ser zerados. Caso não seja necessário, ajuste os valores informados e realize a confirmação novamente. 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117073915671)

 Se for realmente necessário que esses campos sejam zerados, para que o sistema permita finalizar o lançamento, habilite os parâmetros** "ACEITARVLRZERO - ****Aceitar valor total igual a zero" **e **"ACEITARUNITZERO - Aceitar valor unitário igual a zero na venda"**, disponíveis na tela "Preferências" *(Caminho de acesso: Configurações » Avançado).*

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14605520196375)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117089570071)

 CAUSA**:

Ocorre quando no lançamento de pedidos/notas, os campos de Vlr.Unitário e/ou Vlr.Total encontram-se zerados.