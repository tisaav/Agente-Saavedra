# LINE 679 - PL/SQL: erro: precisão de número grande demais numérico ou de valor ORA-06512: em "SANKHYA.SNK_MATGIRCALCSUG"

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26585839620375-LINE-679-PL-SQL-erro-precis%C3%A3o-de-n%C3%BAmero-grande-demais-num%C3%A9rico-ou-de-valor-ORA-06512-em-SANKHYA-SNK-MATGIRCALCSUG](https://ajuda.sankhya.com.br/hc/pt-br/articles/26585839620375-LINE-679-PL-SQL-erro-precis%C3%A3o-de-n%C3%BAmero-grande-demais-num%C3%A9rico-ou-de-valor-ORA-06512-em-SANKHYA-SNK-MATGIRCALCSUG)  
> **ID:** `26585839620375` | **Última Atualização:** 2026-07-22T14:41:08Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26585839604375)

 **MENSAGEM:**

[ORA-06502] PL/SQL: erro: precisão de número grande demais numérico ou de valor ORA-06512: em "SANKHYA.SNK_MATGIRCALCSUG", line 679 ORA-06512: em line 1 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26585839605271)

SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26585839607063)

 O erro ocorre quando algum Estoque Mínimo foi cadastrado com uma quantidade errada no cadastro do Produto, aba **"Medidas e Estoque".**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450222894359)

 Para facilitar a busca, a consulta abaixo pode ser realizada por meio da tela DBexplorer, usando a query abaixo.

 

```text
SELECT CODPROD, ESTMIN FROM TGFEST WHERE ESTMIN IS NOT NULL ORDER BY ESTMIN DESC
```

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26585800059799)

 Caso algum valor no campo ESTMIN (estoque mínimo) esteja extremamente alto, isso pode ocasionar em problemas nos cálculos quando é realizado o processo da matriz, resultando no erro. Neste caso, realize a correção no cadastro do produto e faça novamente o processamento da matriz.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26585839613719)

CAUSA:**

Ocorre quando um valor de estoque mínimo/máximo é informado de forma errada.