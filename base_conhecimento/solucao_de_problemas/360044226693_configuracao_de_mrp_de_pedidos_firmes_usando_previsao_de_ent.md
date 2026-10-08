# Configuração de MRP de Pedidos Firmes, usando 'Previsão de Entrega(Itens)

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044226693-Configura%C3%A7%C3%A3o-de-MRP-de-Pedidos-Firmes-usando-Previs%C3%A3o-de-Entrega-Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044226693-Configura%C3%A7%C3%A3o-de-MRP-de-Pedidos-Firmes-usando-Previs%C3%A3o-de-Entrega-Itens)  
> **ID:** `360044226693` | **Última Atualização:** 2026-07-22T16:00:01Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17293007557143)

 SITUAÇÃO:**

Após configurar o MRP com o tipo de demanda igual a Pedidos Firmes e configurar o campo Tipo de Período como Previsão de Entrega (Itens), não é gerado o MPS para os produtos mesmo que tenham pedidos lançados no portal.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17293007560727)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17293007575319)

 Acesse: Produção » Rotinas » Planejamento de Produção (MRP I)

- Selecione o Planejamento;

- Botão: **"Configurações"**

- Aba **"Tipo de Demanda":** Pedidos Firmes

Sub-Aba: **"Pedidos Firmes"**
Campo **"Tipo de Período":** Previsão de Entrega(Itens)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292979313943)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Aba: **"Validações"**

- Campo **"Exige previsão de entregas"**: marcado

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292979322007)

 Acesse: Comercial » Rotinas » Central de Vendas

- No Lançamento do Pedido, após inserir os itens.

- Acesse: Botão Outras Opções(...)>>Provisionar Entrega.

- Preencha a Data de Provisão de Entrega nos itens.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292979324567)

 Acesse: Produção » Rotinas » Planejamento de Produção (MRP I)

- Filtre por período, considerando o período em que foram lançado os pedidos, que tem 'provisão de entrega' nos itens. e 'Executar a MRP...'

- O sistema vai gerar o planejamento da produção de acordo com os itens que estiverem com a Provisão informada nos itens.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17293007607319)

 CAUSA:**

Configurado o MPS para usar o tipo do período igual a Previsão de Entrega (Itens) e não configurar a TOP do pedido para Exigir Provisão de Entregas.