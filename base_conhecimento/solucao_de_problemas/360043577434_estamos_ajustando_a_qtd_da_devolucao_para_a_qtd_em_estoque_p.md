# Estamos ajustando a Qtd. da Devolução para a Qtd. em estoque! Produto XXX / NF YYYY

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577434-Estamos-ajustando-a-Qtd-da-Devolu%C3%A7%C3%A3o-para-a-Qtd-em-estoque-Produto-XXX-NF-YYYY](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577434-Estamos-ajustando-a-Qtd-da-Devolu%C3%A7%C3%A3o-para-a-Qtd-em-estoque-Produto-XXX-NF-YYYY)  
> **ID:** `360043577434` | **Última Atualização:** 2026-07-22T16:01:56Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105884505623)

 MENSAGEM:**

[CORE_E04656] Estamos ajustando a Qtd. da Devolução para a Qtd. em estoque! Produto XXX / NF YYYY.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105854089495)

 **SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458182163223)

 Exemplo prático:**

Nota de Compra - Item 1 - Quantidade Comprada: 100 Unidades.
Nota de Venda - Item 1 - Quantidade Vendida: 10 Unidades.
Em estoque: 90 unidades.
Nota de Devolução de Compra (a partir da nota de Origem) - Quantidade a devolver: 100 Unidades.
Será apresentada a mensagem, ajustado a devolução para 90 unidades (Quantidade disponível no estoque).

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105854094615)

 Considere efetuar a análise do estoque físico e do sistema, para verificar exatamente qual é o estoque disponível e ajustar a quantidade devolvida dos itens para a nota de Devolução de Compra.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105884511127)

 Então, ao clicar em Devolver, clique em **"Selecionar Itens"** e efetue os ajustes das quantidades a devolver de cada item, de acordo com a quantidade em estoque.

 

![devolver_estornar.png](https://ajuda.sankhya.com.br/hc/article_attachments/14503674323479)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105884511895)

 **CAUSA:**

Ocorre quando ao tentar efetuar a devolução de uma compra, onde a quantidade disponível seja diferente da quantidade que foi adquirida na nota de compra e o campo da TOP de Devolução de compra não esta marcada a opção **"Atualizar Estoque a partir da ****Confirmação"**.