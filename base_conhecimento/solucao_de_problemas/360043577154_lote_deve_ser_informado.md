# Lote deve ser informado

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577154-Lote-deve-ser-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577154-Lote-deve-ser-informado)  
> **ID:** `360043577154` | **Última Atualização:** 2026-07-22T16:01:59Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107145270551)

 **MENSAGEM**:

[ORA-20101]: Lote deve ser informado. 
[ORA-06512]: em "SANKHYA.TRG_UPT_TGFITE", line 703
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_UPT_TGFITE'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107129546519)

 SOLUÇÃO**:

Considere o Comportamento da Aplicação conforme abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107145279127)

 Quando o produto possuir controle adicional de LOTE, no ato da Compra informe o número de lote (geralmente seguido de data de Fabricação e Validade).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107145280407)

 A principal premissa é que esse produto não sofra alteração em seu cadastro, ou seja, não alterar a configuração do controle adicional.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458182242071)

 Vejamos:**
No ato da Compra ou Produção um produto com controle adicional de estoque deverá informar o número de Lote.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107145286807)

 Se houver devolução de compra, informe o número de Lote.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107145286807)

 Se houver venda, informe o número de Lote.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107145286807)

 Se houver devolução da venda, informe o número de lote.

Esse controle é imprescindível para que não ocorra a mensagem (ORA-20101: Lote deve ser informado. ), em algum documento.

Recomendações caso ocorre a mensagem: **"ORA-20101: Lote deve ser informado".**

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107129567383)

 Verifique o histórico do produto em **"[Gerência de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111253-Ger%C3%AAncia-de-Produtos)"**, para observar as movimentações do produto (atentar-se para Local, Controle).

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107145294487)

 Verifique o cadastro do produto, aba **"[Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque)"**, sub-aba **"Controle Adicional"**, campo **"Controlar por:" "Numero de Lote"**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16107129570711)

 CAUSA:**

Ocorre quando o produto tem controle adicional por lote e o lote não foi informado.


---

### 🔗 Links e Referências Internas:

- [Gerência de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111253-Ger%C3%AAncia-de-Produtos)
- [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque)