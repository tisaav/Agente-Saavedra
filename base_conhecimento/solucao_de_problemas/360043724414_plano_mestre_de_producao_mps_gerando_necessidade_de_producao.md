# Plano Mestre de Produção (MPS) gerando necessidade de produção duplicada do PA

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043724414-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS-gerando-necessidade-de-produ%C3%A7%C3%A3o-duplicada-do-PA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043724414-Plano-Mestre-de-Produ%C3%A7%C3%A3o-MPS-gerando-necessidade-de-produ%C3%A7%C3%A3o-duplicada-do-PA)  
> **ID:** `360043724414` | **Última Atualização:** 2026-07-22T15:59:59Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290802413975)

 SITUAÇÃO:**

Plano Mestre de Produção (MPS) gerando necessidade de produção duplicada do PA.

** **

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290814425367)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290802431895)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:

- Efetue conferência nas TOP's de 'Pedido de Venda' se estão configuradas para 'Reservar' estoque.
Se SIM, considere se a necessidade de Produção irá suprir o estoque além do que a necessidade à produzir.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290802438295)

 Efetue a configuração conforme a necessidade do processo, acessando: Produção » Rotinas » Planejamento de Produção (MRP I):

- Botão: **"Configuração"**

- Selecione a Configuração desejada

Aba: **"Filtros de Estoque"**
Sub-Aba: **"Produtos Acabados (PA)"**
Campo: **"Estoque Atual"**

Opção **"****Não Considera":** usado quando as TOPs de Pedido de Venda precisam reservar o estoque. Desta forma, a Necessidade de Produção será gerada apenas para atender os Pedidos e não o estoque faltante.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290802441111)

 CAUSA:**
Quando a TOP para geração de Pedido está configurado para 'Reservar Estoque' e as Configurações do MPS(Produção » Rotinas » Planejamento de Produção (MRP I)) está considerando o estoque das Matérias Primas (MP's), gerando duplicidade de informação.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458141703959)

 Caso de Uso:**
Quando um pedido para um determinado Produto (PA-Produto Acabado), que é de 20 unidades e ao gerar a Necessidade de compra pelo MRP I calcula-se que é preciso produzir 40 unidades, mas o correto é apenas 20.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290814469015)

 OBSERVAÇÃO:**

Mais detalhes sobre configuração de Plano Mestre de Produção, acesse o HELP do Sistema.