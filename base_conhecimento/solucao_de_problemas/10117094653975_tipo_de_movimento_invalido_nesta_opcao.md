# Tipo de movimento inválido nesta opção

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10117094653975-Tipo-de-movimento-inv%C3%A1lido-nesta-op%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/10117094653975-Tipo-de-movimento-inv%C3%A1lido-nesta-op%C3%A7%C3%A3o)  
> **ID:** `10117094653975` | **Última Atualização:** 2026-07-22T15:04:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18975663300631)

 MENSAGEM:**

[CORE_E01860] Tipo de Movimento inválido nesta opção.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18975663318295)

 SITUAÇÃO:**

Ao tentar confirmar uma nota na central de vendas ou tentar cadastrar um modelo de nota para uma TOP financeiro a mensagem é apresentada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18975663344279)

CAUSA:**

Ocorre quando se utiliza uma TOP com tipo de movimento diferente do realizado ou a TOP não vincula no modelo de nota.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18975663328919)

 SOLUÇÃO:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450774587799)

 Lançamento de notas:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18975647565591)

 Acesse a tela do Tipo de operação utilizado na central de vendas e verifique se o campo *'Tipo de movimento' *está preenchido com a opção: 'VENDA'.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/10116892767767)

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450774587799)

 Criação do modelo de nota (existem duas maneiras diferentes):

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18975663339927)

 Crie um **Tipo de operação TOP** *(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)* do tipo compras caso queira apenas uma nota para CT-e. No financeiro insira despesas, para que o sistema gere notas "avulsas" apenas para CT-e e, assim, consequentemente possa vê-las no portal de compras ou;

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/10116985402391)

 

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18975663339927)

 No** portal de importação XML** *(Comercial » Rotinas » Portal de importação de XML)* vá até 'Outras opções', em seguida clique em 'Preferências para importar CT-e' e associe sua TOP financeira de CT-e à uma nota. Vale destacar que essa ação fará a junção e não será possível ver separado.

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/10117046459799)