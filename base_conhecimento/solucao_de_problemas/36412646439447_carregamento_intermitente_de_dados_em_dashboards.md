# Carregamento intermitente de dados em dashboards

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36412646439447-Carregamento-intermitente-de-dados-em-dashboards](https://ajuda.sankhya.com.br/hc/pt-br/articles/36412646439447-Carregamento-intermitente-de-dados-em-dashboards)  
> **ID:** `36412646439447` | **Última Atualização:** 2026-07-22T14:23:01Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36412646429591)

 **SITUAÇÃO:**

Ao aplicar filtros em relatórios e dashboards do BI, os dados não são exibidos na primeira tentativa.

Nesses casos, é preciso **clicar** mais de uma vez em ''**Aplicar Filtro''** ou ''**Atualizar''** para que as informações apareçam. 

Esse comportamento ocorre de forma intermitente, ou seja, alguns componentes de BI são afetados, enquanto outros funcionam normalmente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36412646431511)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36492822963607)

 Revise as consultas SQL utilizadas nos componentes de BI.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36492929307799)

 Em seguida, remova as conversões de datas desnecessárias como **TO_DATE**, **TO_TIMESTAMP**, **CAST**, ou outras manipulações manuais aplicadas nos parâmetros.

(O Sankhya já envia parâmetros de data devidamente tratados pela aplicação. Quando a consulta realiza uma nova conversão sobre esses valores, pode ocorrer arredondamentos ou interpretações divergentes, resultando no comportamento intermitente.)

- 

Em vez de usar conversões como:

 

```text
BETWEEN TO_DATE(CAST(TO_TIMESTAMP(:PERIODO.INI, 'yyyy-mm-dd') AS DATE), 'DD/MM/YYYY')
```

 

- 

Utilize diretamente os parâmetros fornecidos pelo sistema:

 

```text
BETWEEN :PERIODO.INI AND :PERIODO.FIN
```

 

Caso a consulta tenha sido construída pela unidade, é necessário que o autor revise o código.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36492793393303)

 OBSERVAÇÃO:**
Esse mesmo problema pode ser reproduzido no **DBExplorer, **quando a consulta aplica conversões adicionais. Porém, ao executar diretamente no banco de dados, o comportamento não ocorre, o que reforça que a aplicação já trata corretamente as datas e que a duplicidade de conversões é o ponto crítico da inconsistência.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36412646431895)

CAUSA:**

A intermitência ocorre porque os parâmetros de período enviados pela aplicação já chegam ao banco com o tratamento adequado. Quando a consulta SQL aplica conversões adicionais, como **TO_DATE**, **TO_TIMESTAMP**, **CAST** ou manipulações manuais, o valor pode ser truncado, arredondado ou interpretado de forma diferente, gerando resultados inconsistentes.