# A TOP exige que tenha pelo menos 1 item Pedido/Nota de origem

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043578454-A-TOP-exige-que-tenha-pelo-menos-1-item-Pedido-Nota-de-origem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043578454-A-TOP-exige-que-tenha-pelo-menos-1-item-Pedido-Nota-de-origem)  
> **ID:** `360043578454` | **Última Atualização:** 2026-08-28T18:14:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363216734743)

 MENSAGEM:**

[CORE_E05433] A TOP exige que tenha pelo menos 1 item Pedido/Nota de origem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363216737687)

SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363222480535)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:

Aba Geral » Campo 'Exigir Pedido':

- 
**Não exigir:** Não exigirá nenhum tipo de origem, ou seja, a Nota não precisará estar vinculada a um Pedido.

- 
**Exigir algum item**: Exigirá que pelo menos um item da Nota tenha uma origem (Pedido).

- 
**Exigir completo:** Exigirá que todos os itens da Nota estejam ligados a uma origem (Pedido).

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14359719500823)

 

**Nota:** Se a TOP for do tipo de movimento "Devolução de Venda" o nome do campo é ; **"****Exigir Nota de Venda",** que no caso deverá estar como **"Não exigir"** quando estiver lançando a nota sem ligação com a origem.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363216744727)

 Caso a configuração acima esteja como **"Exigir algum item"** é obrigatório que um pedido de venda tenha sido selecionado para esse faturamento.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363216745879)

 Caso deseje lançar a NF-e avulsa, sem ligação com pedidos, a marcação acima precisa ser revista, e definido a opção "**Não exigir**".

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363216747159)

 **Se a alteração na TOP for realizada um novo lançamento deve ser feito.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363222488471)

CAUSA:**

Ocorre quando ao emitir NF-e com TOP configurada para **"Exigir algum item"** sem que exista a ligação dos seus itens com o pedido de venda, a mensagem será apresentada.