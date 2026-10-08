# Escolher a série do imobilizado no lançamento da Ordem de Serviço

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007367962-Escolher-a-s%C3%A9rie-do-imobilizado-no-lan%C3%A7amento-da-Ordem-de-Servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007367962-Escolher-a-s%C3%A9rie-do-imobilizado-no-lan%C3%A7amento-da-Ordem-de-Servi%C3%A7o)  
> **ID:** `1500007367962` | **Última Atualização:** 2026-07-22T15:24:53Z

---

Confira abaixo o passo a passo para escolher a série do imobilizado no lançamento da Ordem de Serviço (lembrando que série não é o controle de estoque por serie (TGFSER) e sim o código da série informada no contrato):

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913684154135)

 Ligue os parâmetros **"****HABMULTSERCONT"** e **"****SERVIMOBILI"**;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913700200855)

 Tendo realizado a nota de compra comum de um bem imobilizado, não informe nesse momento a série;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913684157719)

 Em seguida, crie um contrato, mas não informe o produto, ele será inserido quando vincular a nota de remessa ao contrato;

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913700203287)

 No **"Cadastro de naturezas"**, aba **"Serviços autorizados"**, adicione os serviços que serão usados no lançamento da Ordem de serviço;

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913684159767)

 Faça o lançamento da nota de remessa para o produto imobilizado com as configurações da top abaixo:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451142754455)

 TOP de Venda, da baixa no estoque: XXX

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451142754455)

 Atualiza imobilizado como Transf. Remessa

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451142754455)

 **"Informar Contrato na Nota":** Obrigatório
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451142754455)

"Integ. Série ao Contrato":** Entrada

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451142754455)

**Nota de vendas de Nro Unico:** XXX

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17032692042519)

 Empresa X

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17032692042519)

 Parceiro XX

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17032692042519)

 Contrato: XXXX

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17032692042519)

 TOP: XXX

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451142754455)

 **Produto XX:** Qtd 2

 

Nesta nota, clique no botão **"Outras opções",** existente na grade de itens da nota, e escolha a opção: **"Transferência de bens"** para escolher os bens que farão parte do contrato, depois confirme a nota.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913684161687)

 No cadastro do contrato XXXX utilize a opção **"Selecionar produtos/serviços do pedido"** existente no botão Outras opções. Escolha a nota de remessa lançada anteriormente e o produto informado nesta nota e clique no botão** "Confirmar"**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913684165143)

 Acesse o lançamento da ordem de serviço escolhendo o parceiro, contrato, produto e serviço definidos nos passos anteriores e escolha o executante e a a série do produto.