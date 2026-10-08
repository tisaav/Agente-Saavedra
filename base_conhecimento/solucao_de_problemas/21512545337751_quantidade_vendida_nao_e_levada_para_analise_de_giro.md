# Quantidade vendida não é levada para Análise de Giro

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/21512545337751-Quantidade-vendida-n%C3%A3o-%C3%A9-levada-para-An%C3%A1lise-de-Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/21512545337751-Quantidade-vendida-n%C3%A3o-%C3%A9-levada-para-An%C3%A1lise-de-Giro)  
> **ID:** `21512545337751` | **Última Atualização:** 2026-07-22T14:50:08Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891439286423)

 **SITUAÇÃO:**

Quando a quantidade de venda dos produtos na análise de giro é 0 (zero) ou apresenta divergências em relação ao portal de vendas/gerência de produtos. É necessário verificar alguns pontos para garantir que a quantidade correta seja levada após o processo da matriz.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21512545329047)

CAUSA:**

Ocorre quando a nota de venda não atende aos requisitos acima, onde ela é desconsiderada ou pode ocasionar no travamento do Job consolidador responsável por coletar as informações de quantidades vendidas (giro) e levar para Análise de Giro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21512545303831)

 **SOLUÇÃO:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450440623511)

 Os requisitos informados abaixo, devem ser seguidos, pois caso contrário, a quantidade vendida não será levada para análise de giro, o que pode resultar em divergências nos cálculos da sugestão de compra giro.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450440623511)

 Para realizar os testes, utilize uma nota de venda como exemplo, que tenha sido negociada dentro do período informado na Análise de giro.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454158999)

 A nota deverá estar confirmada;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891439335063)

 O valor total da nota (cabeçalho) e o valor unitário do item vendido, precisam ser maior que zero;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454188439)

 A TOP de venda deverá ter a configuração de Análise de Giro;

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/21891439360023)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454204951)

 No cadastro do produto deverá ter a marcação 'Calcula Giro pelo Agendador'* (**Produto » aba Medidas e Estoque**);*

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/21891439389847)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454244503)

 Obrigatoriamente o produto vendido precisar ter **CUSTO** com data igual ou anterior a nota de venda realizada;

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454269207)

 O **tipo** e o **tamanho** dos campos entre as tabelas TGFPRO e TGFGIR devem ser idênticas ao banco de dados. Segue abaixo consulta que auxiliará na comparação:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450440623511)

 SQL:

```text
SELECT PRO.NAME AS COLUNA,

TYPE_NAME(PRO.XTYPE) AS TIPO_PRO,

PRO.LENGTH AS TAMANHO_PRO,

TYPE_NAME(GIR.XTYPE) AS TIPO_GIR,

GIR.LENGTH AS TAMANHO_GIR

FROM SYSCOLUMNS PRO, SYSCOLUMNS GIR WHERE PRO.ID = OBJECT_ID('TGFPRO') AND GIR.ID = OBJECT_ID('TGFGIR')

AND PRO.NAME = GIR.NAME

AND (TYPE_NAME(PRO.XTYPE) <> TYPE_NAME(GIR.XTYPE) OR PRO.LENGTH <> GIR.LENGTH)
```

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450440623511)

 ORACLE:

```text
SELECT * FROM (SELECT PRO.COLUMN_NAME AS COLUNA,

PRO.DATA_TYPE AS TIPO_PRO,

CAST(PRO.DATA_LENGTH AS NUMBER) AS TAMANHO_PRO,

GIR.DATA_TYPE AS TIPO_GIR,

CAST(GIR.DATA_LENGTH AS NUMBER) AS TAMANHO_GIR

FROM USER_TAB_COLUMNS PRO, USER_TAB_COLUMNS GIR WHERE PRO.TABLE_NAME = 'TGFPRO'

AND GIR.TABLE_NAME = 'TGFGIR' AND PRO.COLUMN_NAME = GIR.COLUMN_NAME) X

WHERE X.TAMANHO_PRO <> X.TAMANHO_GIR
```

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454284311)

 O produto não poderá ter o custo duplicado, ou seja, custo com a mesma data para o mesmo produto. Segue abaixo consulta que auxiliará na identificação do custo duplicado, que pode ocasionar o travamento do Job consolidador: 

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450440623511)

 Execute a consulta abaixo referente ao parâmetro CUSTOPORCONT (Custo por controle):

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454293655)

Se estiver desligado:

```text
SELECT CODPROD , CODEMP , DTATUAL, COUNT(1) FROM TGFCUS GROUP BY CODPROD , CODEMP , DTATUAL HAVING COUNT(1) > 1 ORDER BY DTATUAL DESC, CODPROD
```

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454293655)

Se estiver ligado:

```text
SELECT CODPROD,DTATUAL,CONTROLE,COUNT(1) FROM TGFCUS GROUP BY CODPROD,DTATUAL,CONTROLE HAVING COUNT(1) > 1
```

 

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891439475991)

 É necessário existir uma referência de Custo Variável para cada empresa analisada. Na tela Gerente On-Line - GOL (*Comercial » Gerente*), abra as configurações e acesse a aba *Margem de contribuição*.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450440623511)

 O ano de referência deve ser anterior ao período de negociação da nota utilizada.

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454327831)

 

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891439502359)

 Verifique se a Matriz analisada possui algum filtro que impeça o item de levar sua quantidade vendida. Na tela Análise de Giro (*Comercial » Rotinas*), abra as configurações e acesse a aba *Outras Configurações. *

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/21891439516951)

 

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891454390551)

 Após verificar os itens acima, certifique-se de que o Job de consolidação da Análise de giro esteja rodando. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/21891454407831)

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21891439567511)

**IMPORTANTE:**

Se após seguir as orientações e aguardar o horário agendado o problema persistir, acione o time de Service Desk.

**Observação: ** Existem operações que, apesar de ser uma saída (baixa no estoque) não devem ser consideradas no processo de ANALISE DE  GIRO  (Ex:  Doações,  registros de Perdas, Ajustes etc.)