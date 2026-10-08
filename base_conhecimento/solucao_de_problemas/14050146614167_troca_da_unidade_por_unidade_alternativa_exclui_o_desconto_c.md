# Troca da unidade por unidade alternativa, exclui o desconto concedido na plataforma Mercos

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14050146614167-Troca-da-unidade-por-unidade-alternativa-exclui-o-desconto-concedido-na-plataforma-Mercos](https://ajuda.sankhya.com.br/hc/pt-br/articles/14050146614167-Troca-da-unidade-por-unidade-alternativa-exclui-o-desconto-concedido-na-plataforma-Mercos)  
> **ID:** `14050146614167` | **Última Atualização:** 2026-07-22T14:59:34Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970280625943)

SOLUÇÃO:**

Pedidos criados na plataforma Mercos que possuem desconto na origem, ao serem importados no Sankhya, perdem o desconto concedido quando a unidade do produto em questão for alterada para uma unidade alternativa, trazendo o preço de tabela do item e recalculando o valor total da nota.

Sendo assim, o desconto deve ser concedido no item novamente, na central de vendas antes da confirmação.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970248250903)

CAUSA:**

Se trata de um comportamento natural do sistema. O Sistema recalcula o preço por que entende que  uma negociação em "unidade" é diferente de uma negociação em "caixas". Portanto, se o usuário altera o pedido que veio da integração na central de vendas ele se torna responsável por essa alteração.