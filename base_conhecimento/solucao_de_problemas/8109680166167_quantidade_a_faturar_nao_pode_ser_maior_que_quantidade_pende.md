# Quantidade a faturar não pode ser maior que quantidade pendente

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8109680166167-Quantidade-a-faturar-n%C3%A3o-pode-ser-maior-que-quantidade-pendente](https://ajuda.sankhya.com.br/hc/pt-br/articles/8109680166167-Quantidade-a-faturar-n%C3%A3o-pode-ser-maior-que-quantidade-pendente)  
> **ID:** `8109680166167` | **Última Atualização:** 2026-07-22T15:12:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17007524190743)

 MENSAGEM**:

Quantidade a faturar não pode ser maior que quantidade pendente.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17007570432407)

 CAUSA:**

Ocorre quando a marcação **"Aceitar faturar quantidade maior que a da origem?" **não é realizada na TOP e tenta faturar com uma quantidade maior.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17007524204695)

 SOLUÇÃO:**

Com a marcação** "Aceitar faturar quantidade maior que a da origem?" **efetuada, será permitido faturar, na Central de Notas, um Pedido/Nota (compra, venda ou requisição), com a quantidade maior do que a quantidade negociada do Pedido.

Esta opção foi criada para substituir os parâmetros:        

- **Aceita faturar compra qtd maior que a do pedido? ACEITACACIMA**

- **Aceita qtd Dev. Compra maior que a compra? ACEITAEACIMA**

- **Aceita faturar venda qtd maior que a do pedido? ACEITAFATACIMA**

- **Aceita qtde Dev. Venda maior que a venda? ACEITADACIMA**

- **Aceita faturar quantidade maior que a da origem? ACEITAARMACIMA**

Por padrão, esta opção virá desmarcada.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17007399376919)

 

**Observação:** Além desta marcação, é necessário que o campo **"****Exige Pedido"** (aba Geral) esteja marcada como **"****Exige algum item"**.

O mesmo não é permitido quando na TOP de faturamento, a opção exigir pedido estiver selecionado "Exige algum item" e a opção **"Aceitar faturar quantidade maior que a origem?"** estiver desmarcada.