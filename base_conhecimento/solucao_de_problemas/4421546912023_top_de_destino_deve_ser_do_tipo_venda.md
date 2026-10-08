# TOP de Destino deve ser do tipo VENDA

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4421546912023-TOP-de-Destino-deve-ser-do-tipo-VENDA](https://ajuda.sankhya.com.br/hc/pt-br/articles/4421546912023-TOP-de-Destino-deve-ser-do-tipo-VENDA)  
> **ID:** `4421546912023` | **Última Atualização:** 2026-07-22T15:19:25Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305191896471)

 MENSAGEM: **

[CORE_E02568] Em uma TOP com o TIPMOV ='P', ao tentar configurar o campo "TOP P/ Faturamento", informando uma outra TOP com o mesmo TIPO DE MOVIMENTO, a mensagem "TOP de Destino deve ser do tipo VENDA " será apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305187998487)

 SOLUÇÃO:**
Para que seja possível 'faturar' uma TOP para outra com o mesmo TIPMOV, faça o seguinte procedimento:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305191910039)

 Nas configurações da TOP de Orçamento, selecione Outras opções' -> "Restrições/Exceções";

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305191913623)

 Em TOP Destino, selecione** "Restrições'** e realize a inclusão da TOP de Pedido desejada;

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15752235350551)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305191916695)

 OBSERVAÇÃO:**

Esta mesma validação pode ocorrer para TOP´s com outros TIPMOV (EX: Pedido de compra) porém, o procedimento a ser adotado é o mesmo.
 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16305188012823)

 CAUSA: **
Para TOP de origem com o tipo de movimento P-Pedido de Venda, é necessário que o tipo de movimento da TOP selecionada para faturamento seja V- Venda.