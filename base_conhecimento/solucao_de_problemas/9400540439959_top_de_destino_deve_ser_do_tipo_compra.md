# TOP de destino deve ser do tipo compra

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9400540439959-TOP-de-destino-deve-ser-do-tipo-compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/9400540439959-TOP-de-destino-deve-ser-do-tipo-compra)  
> **ID:** `9400540439959` | **Última Atualização:** 2026-07-22T15:08:06Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18926175180567)

 MENSAGEM:**

[CORE_E02569] TOP de destino deve ser do tipo compra.

[CORE_E02571] TOP de Destino deve ser do tipo COMPRA ou DEVOLUÇÃO DE COMPRA.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18926175189911)

 SITUAÇÃO:**

Em uma TOP com o TIPMOV ='O' , ao tentar configurar o campo "TOP P/ Faturamento" na Aba Geral, informando uma outra TOP com o mesmo TIPO DE MOVIMENTO, a mensagem "TOP de Destino deve ser do tipo COMPRA " será apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18926175197719)

SOLUÇÃO:**

Para que seja possível 'faturar' uma TOP para outra com o mesmo TIPMOV, usuário deverá utilizar o seguinte procedimento:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18926236861079)

 Acesse as configurações da TOP, selecione **Outras opções' -> "Restrições/Exceções";**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18926175205783)

 Em TOP Destino, selecione **"Restrições' **e realize a inclusão da TOP de Pedido desejada;

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14597628977175)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18926236868375)

 OBSERVAÇÃO:**

Esta mesma validação pode ocorrer para TOP's com outros TIPMOV (EX: Pedido de venda) porém, o procedimento a ser adotado é o mesmo.
 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18926236877463)

CAUSA:**

Ocorre devido a TOP de origem com o tipo de movimento = O - Pedido de Compra estar selecionada, sendo necessário que o tipo de movimento da TOP selecionada para faturamento seja C- Compra.