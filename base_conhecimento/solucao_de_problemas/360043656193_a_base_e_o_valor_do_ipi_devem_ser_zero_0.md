# A base e o valor do IPI devem ser zero (0)

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656193-A-base-e-o-valor-do-IPI-devem-ser-zero-0](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656193-A-base-e-o-valor-do-IPI-devem-ser-zero-0)  
> **ID:** `360043656193` | **Última Atualização:** 2026-07-22T16:04:38Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143358736535)

 MENSAGEM:**

ORA-20101: A base e o valor do IPI devem ser zero (0).
ORA-06512: em "SANKHYA.TRG_INC_TGFITE", line 406
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_TGFITE'
SQL-50001 - A base e o valor de IPI devem ser zero (0)

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143366443287)

 SITUAÇÃO:**

Ao realizar o faturamento de um pedido em nota pela tela **"[Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)"** no **SankhyaW**, apresenta a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143366444695)

 SOLUÇÃO:**

Para solução, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143358742039)

 Acesse: Comercial » Consulta » Portal de Vendas:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143366447127)

 Selecione o pedido/nota, acesse a grade de itens e verifique os campos de **"Base do IPI"**, **"Aliq. IPI"** e **"Vlr. IPI"**, em todos os itens da nota.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143366449687)

 Pode ser que algum produto tenha informações do valor de IPI, porém no cadastro do produto não está marcado para **"Calcular IPI na Venda"**. Então acesse:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143366447127)

 *Configurações » Cadastros » Produtos » Produtos:*

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143358751127)

Aba **"Imposto"**, campo **"Tem IPI na Venda"**

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14662051331479)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143366447127)

 Confira o % (percentual) de IPI que incide em cada item, antes de confirmar/faturar o pedido/nota.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143366447127)

 O mesmo vale para processo de compra, alterando para a opção: **"Tem IPI na Compra".**

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143358753175)

 OBSERVAÇÃO:**

Qualquer dúvida nas configurações, sobre a incidência de IPI, procure a contabilidade para esclarecimentos.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143358754967)

 Após os ajustes, redigite os itens e fature.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16143358755735)

CAUSA:**

Após o lançamento foram realizadas alterações no cadastro do produto em relação a incidência de IPI e com isso causa divergência do cálculo de IPI.


---

### 🔗 Links e Referências Internas:

- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)