# Sistema recalcula valor dos itens ao faturar um lançamento

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26676492863511-Sistema-recalcula-valor-dos-itens-ao-faturar-um-lan%C3%A7amento](https://ajuda.sankhya.com.br/hc/pt-br/articles/26676492863511-Sistema-recalcula-valor-dos-itens-ao-faturar-um-lan%C3%A7amento)  
> **ID:** `26676492863511` | **Última Atualização:** 2026-07-22T14:40:50Z

---

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450237698583)

Ao realizar o faturamento de um lançamento, os valores do item são recalculados de acordo com a tabela de preço.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26676505222039)

SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26676492835095)

 Caso trabalhe com o parâmetro **RECPRECOTPV** como **"Nunca"**, porém atenda a alguma dessas condições, ocorrerá o recalculo.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450237698583)

Se no cadastro do produto o campo **"Digitação na nota"** estiver como quantidade, permitirá o recalculo.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450237698583)

Se for uma venda e trabalhar com um dos parâmetros abaixo **ligado** permitirá o recalculo:

- 
**DESCFOB** - Usa desconto FOB

- 
**PERCDESCFOB** - Usar % Desc.por região p/Frete FOB ?

- 
**USASIMFORMAPGTO** - Simula formas de pagamento na Central?

- 
**PERCDESCFOBCAB** - Usa Perc. Desc. FOB no rodap (Venda)?

- 
**USAPRECPELATOP** - Usa precificação de produtos/serviços pela TOP

- 
**USAPRECTOPPDV** - Usa precificação pela TOP no PDV Web

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26676505232791)

CAUSA:**

Caso algum dos parâmetros acima estejam habilitados, resulta no recalculo do valor unitário do item ao faturar.