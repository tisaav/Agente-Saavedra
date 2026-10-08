# Tipos de Liberação de Limites Evento 2

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/5772652795543-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites-Evento-2](https://ajuda.sankhya.com.br/hc/pt-br/articles/5772652795543-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites-Evento-2)  
> **ID:** `5772652795543` | **Última Atualização:** 2026-07-22T15:17:41Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361377868695)

 SITUAÇÃO:**

Tipos de Liberação de Limites Evento 2, quando configurado no cadastro de Produto, na aba **"Venda",** o  campo: **"% Desconto Máximo"**, em seguida ao realizar uma Nota ou Pedido de Venda em que foi aplicado um desconto maior do que o permitido, dependendo do preço do produto na tabela de Preço, o sistema apresentará no Pop-up da solicitação de liberação de limite na tela da Central o campo: **"Percentual Limite"** um valor diferente do que foi configurado no campo: % Desconto Máximo do Cadastro do Produto. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14679237303575)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14679238138775)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361377869719)

SOLUÇÃO:**

Para que esse comportamento não ocorra independente do Preço de Venda do Produto na tabela de Preço, configure no cadastro do produto, na aba: Medidas e Estoque o campo: Decimais para Valor, informando um valor de casas decimais a ser considerada para Preços de Vendas. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14679198155543)

 

Feito isso, o sistema levará corretamente o valor do Percentual Limite na validação do Evento 2. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14679244700695)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361338204055)

CAUSA:**

Quando não é informado no cadastro do Produto o campo: **"Decimais para Valor"** na aba **"Medidas e Estoque"** o sistema ao realizar o cálculo, na validação da liberação do limite, não interpreta de forma correta e apresenta o valor no campo: **"Percentual Limite de forma incorreta".**