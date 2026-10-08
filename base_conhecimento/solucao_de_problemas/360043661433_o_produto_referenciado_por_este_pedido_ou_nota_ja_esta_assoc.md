# O produto referenciado por este pedido ou nota já está associado a outro pedido ou nota, não se pode atualizá-lo

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043661433-O-produto-referenciado-por-este-pedido-ou-nota-j%C3%A1-est%C3%A1-associado-a-outro-pedido-ou-nota-n%C3%A3o-se-pode-atualiz%C3%A1-lo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043661433-O-produto-referenciado-por-este-pedido-ou-nota-j%C3%A1-est%C3%A1-associado-a-outro-pedido-ou-nota-n%C3%A3o-se-pode-atualiz%C3%A1-lo)  
> **ID:** `360043661433` | **Última Atualização:** 2026-07-22T16:04:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142957725207)

 MENSAGEM:**

SQL-50001 O produto referenciado por este pedido ou nota já está associado a outro pedido, ou nota, não se pode atualizá-lo.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142957728791)

 SITUAÇÃO:**

Mensagem apresentada ao tentar alterar o item de um lançamento, após faturá-lo através de um documento origem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142965809687)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142957737367)

 Se necessário altere o produto que foi faturado por um documento origem, o procedimento correto é **excluir o produto que não será mantido** na nota de destino e **inserir o produto desejado**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142957738391)

 Lembre-se que o item excluído perderá a ligação com o documento de origem e voltará a ficar ***pendente: SIM***.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142965816855)

 Para o faturamento de pedido/nota o impacto constatado é o citado no item 2. Porém, se esse processo for realizado para documentos eletrônicos que exigem a chave referenciada, é importante ressaltar que essa ligação será perdida, sendo necessário vincular e preencher esse campo no layout da nota destino, evitando possíveis rejeições.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458195496599)

 Lembramos que é importante avaliar o processo com cautela, visto que é incompreensível vender o PRODUTO A e faturar/devolver o PRODUTO B. A prática recomendada é que o ajuste seja realizado considerando todos os documentos vinculados.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142957745431)

 CAUSA:**

Mensagem apresentada ao tentar alterar o item de um lançamento, após faturá-lo através de um documento origem. A mensagem é causada pelas ligações entre os documentos, visto que as informações devem ser preservadas.