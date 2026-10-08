# Não foi possível localizar a tabela de preços

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9404930495511-N%C3%A3o-foi-poss%C3%ADvel-localizar-a-tabela-de-pre%C3%A7os](https://ajuda.sankhya.com.br/hc/pt-br/articles/9404930495511-N%C3%A3o-foi-poss%C3%ADvel-localizar-a-tabela-de-pre%C3%A7os)  
> **ID:** `9404930495511` | **Última Atualização:** 2026-07-22T15:08:00Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861145879)

 MENSAGEM:**

[COM_E00176]  Não foi possível localizar a tabela de preços.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612868650391)

 SITUAÇÃO:**

Ao tentar buscar o produto através da consulta de produtos ou pela central de vendas a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861166615)

 CAUSA:**

Quando o produto está vinculado a uma tabela de preços inexistente.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612868667415)

 SOLUÇÃO:**

Verifique qual tabela de preço está sendo usado pelo usuário que está realizando o lançamento.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612868669847)

 Acesse a Tela **Portal de Vendas** *(Comercial » Consulta » Portal de Vendas);*

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612868678679)

 Busque pelo Pedido de Venda Número único da nota;

![portal de vendas.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612868686871)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861196823)

 Dê um duplo clique o sistema abrirá a **Central de Vendas** *(Comercial » Rotinas » Central de Vendas);*

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861203223)

 Clique no Botão Produtos, abrirá a Consulta de Produtos;

![produtos.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861207831)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861212311)

 O sistema contextualizou o parceiro e a empresa e traz tabela de preço;

![tabela.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861217175)

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612868723479)

 Informe o produto xxxx o sistema emite a mensagem: Não foi possível localizar a tabela de preços.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861237015)

 Clique no Botão 'Configurações do painel de resultados

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612868740503)

 Nota-se que possui uma tabela cadastrada xxxx 

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861277207)

 Essa tabela não existe no Banco de Dados

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612868753047)

 Exclua essa Tabela

![11 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612861296919)

 Nota-se que agora o sistema permite realizar a busca do produto xxxx sem evidências de erros.