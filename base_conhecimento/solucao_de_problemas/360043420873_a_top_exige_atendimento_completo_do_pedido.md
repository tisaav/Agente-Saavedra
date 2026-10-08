# A TOP exige atendimento completo do pedido

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043420873-A-TOP-exige-atendimento-completo-do-pedido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043420873-A-TOP-exige-atendimento-completo-do-pedido)  
> **ID:** `360043420873` | **Última Atualização:** 2026-08-25T18:47:01Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117988064279)

 MENSAGEM:**

[CORE_E02687]  A TOP Exige atendimento completo do pedido.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001259799)

 SITUAÇÃO:**

Ao criar uma nota, na confirmação a seguinte mensagem é apresentada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001289495)

 CAUSA:**

Ocorre ao emitir NF-e com TOP configurada para **"Exigir completo"** sem que exista a ligação de todos os itens do pedido  com a respectiva nota.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001261719)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001268759)

 Acesse o cadastro do Tipo de Operação utilizado e verifique como encontra-se a configuração abaixo:

Aba **"Geral"** » Campo** "Exigir Pedido"**:

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14610662485527)

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001272087)

 Não exigir:** Não exigirá nenhum tipo de origem, ou seja, a Nota não precisará estar vinculada a um Pedido.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001272087)

 Exigir algum item:** Exigirá que pelo menos um item da Nota tenha uma origem (Pedido).

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001272087)

 Exigir completo**: Exigirá que todos os itens da Nota estejam ligados a uma origem (Pedido).

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001275287)

 **Caso a configuração acima esteja como "**Exigir completo**" é obrigatório que um pedido tenha sido selecionado para esse faturamento e todos os itens tenham sido faturados.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001280535)

 Caso não deseje faturar todos os itens do pedido é necessário que a configuração acima seja revista, e definida como **"Exigir algum item"** ou **"Não exigir"**.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118001284631)

 Se a alteração na TOP for realizada um novo lançamento deve ser feito.