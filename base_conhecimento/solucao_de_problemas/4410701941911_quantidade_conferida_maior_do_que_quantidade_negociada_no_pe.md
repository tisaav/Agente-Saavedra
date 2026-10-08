# Quantidade conferida maior do que quantidade negociada no pedido/nota

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4410701941911-Quantidade-conferida-maior-do-que-quantidade-negociada-no-pedido-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410701941911-Quantidade-conferida-maior-do-que-quantidade-negociada-no-pedido-nota)  
> **ID:** `4410701941911` | **Última Atualização:** 2026-07-22T15:21:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/15993307074199)

 MENSAGEM: **

[CORE_E01284] Quantidade conferida maior do que quantidade negociada no pedido/nota.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16121320010391)

 CAUSA:**

O erro ocorre quando existe uma divergência, na qual a quantidade que foi conferida é maior que o pedido/nota. Outra causa para o erro em questão é quando o cód. de barras da unidade padrão do produto está igual ao da unidade alternativa. Deste modo, quando o sistema tenta buscar na fila de conferência o produto, não consegue identificar qual das unidades é a correta. Portanto, ao colocar cod. de barras diferentes nos casos, é possível realizar a conferência pela unidade desejada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/15993188371735)

 SOLUÇÃO: **

Ao realizar a conferência, use a mesma unidade utilizada durante a negociação. Por exemplo, ao realizar uma negociação com a opção **"Unidade Alternativa"**, o processo de conferência deverá ser realizado nesta mesma unidade. Caso contrário o sistema emitirá a mensagem:

**"Quantidade conferida maior do que quantidade negociada no pedido/nota."**

 

**

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416686868375)

**