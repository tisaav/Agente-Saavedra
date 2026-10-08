# O produto XXX não pertence ao pedido/nota

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044237413-O-produto-XXX-n%C3%A3o-pertence-ao-pedido-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044237413-O-produto-XXX-n%C3%A3o-pertence-ao-pedido-nota)  
> **ID:** `360044237413` | **Última Atualização:** 2026-07-22T15:59:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16422030478999)

 MENSAGEM:**

O produto XXX não pertence ao pedido/nota.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16422030482967)

 SITUAÇÃO:**

Ao tentar executar uma tarefa no coletor a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16422030485271)

 SOLUÇÃO:**

Para correção siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16422054443671)

 Acesse *Configurações » Cadastros » Produtos » Produtos*, aba **Geral**, campo **"Referência"**

ou 

Configurações » Cadastros » Produtos » Produtos, aba **Unidade Alternativa**, campo **"Código de Barras da Unidade Alternativa".**

Identifique se existe mais de um produto que possui a mesma referência ou código de barras e faça o ajuste para que a referência entre ambos seja diferente.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16422054446103)

 Após os ajustes, execute a chamada da tarefa novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16422054448023)

 CAUSA**

Ocorre quando dois ou mais produtos possuem o mesmo código de referência ou código de barras, o sistema busca pelo produto de menor código de cadastro no sistema e se no lançamento for o outro produto, ocorre a mensagem.

Exemplo:

Produtos:
Código: 10 - Referencia: AN13911
Código: 33 - Referencia: AN13911

Se o produto 33 estiver no lançamento da execução da tarefa, apresentará a mensagem, pois o sistema tentará buscar o produto de código 10 (dez).