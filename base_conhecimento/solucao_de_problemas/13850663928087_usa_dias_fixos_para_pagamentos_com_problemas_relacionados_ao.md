# Usa dias fixos para pagamentos, com problemas relacionados aos meses de 31 dias

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/13850663928087-Usa-dias-fixos-para-pagamentos-com-problemas-relacionados-aos-meses-de-31-dias](https://ajuda.sankhya.com.br/hc/pt-br/articles/13850663928087-Usa-dias-fixos-para-pagamentos-com-problemas-relacionados-aos-meses-de-31-dias)  
> **ID:** `13850663928087` | **Última Atualização:** 2026-07-22T14:59:45Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913052841879)

 SITUAÇÃO:**
Cliente possui dias fixos para pagamento. No tipo de negociação foi determinado a condição de 30 dias para pagamento. Entretanto, ao emitir um faturamento cujo o o mês possui 31 dias, foi observado que o sistema se perde no calculo. Considera-se que o cliente utiliza a data de entrada/saída como base dos vencimentos.
 

**Exemplo:** Quando emitido um faturamento no dia 01/03/2023, o sistema automaticamente calcula o vencimento para o dia 01/03/2023, ignorando a regra do sistema, que deveria somar 30 dias ou a data prox. de pagamento.
 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913036178967)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970559174423)

 Para esta situação, observe em especifico se o parâmetro: **"Posterga vencimento com dia fixo (CALDIAFIXOVCT)? - POSVENCDIAFIX"**, está ativado.
Caso não, ative o mesmo e ser fique atento as seguintes configurações:

- 
Tipo negociação > Características > Campo Prazo mínimo = 30

- 
Tipo negociação > Parcelas > Prazo: 30

- 
Tipo negociação > Características > Base do prazo: A partir do dia

- 
Tipo negociação > Parcelas > Vencimento não útil: Vencimento original

- 
Parceiro > Crédito > Campo prazo médio pagamento = 30

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450681787927)

 Entretanto, vale destacar que que além deste, outros parâmetros impactam o funcionamento dos "Dias Fixos" e devem estar devidamente configurados para seu correto funcionamento.

 

- 
**POSVENCDIAFIX ** - Ligado

- 
**DIASMAXPRAZEXTR** - 0

- 
**RECALVENCFAT** - Ligado

- 
**DTCALCVENC ** - saída

- 
**TRANSFVENC** - Desligado

- 
**USARDIAFIXOVCT** - Ligado

- 
**POSVENCDIAFIX** - Desligado

- 
**ACVENDIAFIXOVCT ** - Ligado

- 
**CALDIAFIXOVCT ** - Ligado

- 
**HABTIPALTDTVENC ** - Desligado

- 
**FP_FOLGADOM** e **FOLGADOM** - Ligado

- 
**DIASMAXPRAZEXTR** - 0

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16913052848535)

 CAUSA:**
Problemas relacionados ao cálculo de vencimento utilizando dias fixos para meses com 31 dias.