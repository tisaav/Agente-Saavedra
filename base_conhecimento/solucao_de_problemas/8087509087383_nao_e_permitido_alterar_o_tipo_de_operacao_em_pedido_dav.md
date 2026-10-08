# Não é permitido alterar o tipo de operação em pedido "DAV" 

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8087509087383-N%C3%A3o-%C3%A9-permitido-alterar-o-tipo-de-opera%C3%A7%C3%A3o-em-pedido-DAV](https://ajuda.sankhya.com.br/hc/pt-br/articles/8087509087383-N%C3%A3o-%C3%A9-permitido-alterar-o-tipo-de-opera%C3%A7%C3%A3o-em-pedido-DAV)  
> **ID:** `8087509087383` | **Última Atualização:** 2026-07-22T15:12:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361687163543)

 MENSAGEM:**

CORE_E01841 Não é permitido alterar o tipo de operação em pedido "DAV".

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361672048151)

SOLUÇÃO:**

Quando se usa faturamento lateral (quando se fatura de um orçamento para pedido, pedido para pedido), configure na TOP de origem, no botão **"Outras Opções"** a opção **"Restrições/Exceções"** parametrizando as TOPs de destino, conforme imagem abaixo:*
*

 

*

![Imagem](/attachments/token/arW0774uojoYPnmol8CQuERp1/?name=image.png)

*

 

Definindo as TOPs que deseja que sejam listadas no momento do faturamento do seu pedido/orçamento o sistema será forçado a permitir o faturamento de orçamento para pedido ou pedido para pedido não apresentando a mensagem de erro:

Não é permitido alterar o tipo de operação em pedido "DAV" Código: CORE_E01841

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361687172759)

CAUSA:
**

Por se tratar de um faturamento lateral de orçamento para um pedido DAV e/ou pedido de venda para pedido o sistema entende que o faturamento seria para uma TOP do tipo venda por isso a necessidade da parametrização descrita acima.