# Vendas por vendedor no gerente online não apresenta as vendas para uma determinada TOP

> **Módulo:** Melhores Praticas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26354593831703-Vendas-por-vendedor-no-gerente-online-n%C3%A3o-apresenta-as-vendas-para-uma-determinada-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/26354593831703-Vendas-por-vendedor-no-gerente-online-n%C3%A3o-apresenta-as-vendas-para-uma-determinada-TOP)  
> **ID:** `26354593831703` | **Última Atualização:** 2026-07-22T14:42:30Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26429477770007)

  **SITUAÇÃO:**

Mesmo a top de vendas estando configurada como apoio a decisão 'Vendas', não estão sendo apresentados os registros das vendas no Dash **"Vendas por vendedor"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/26354593825303)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26354593826199)

SOLUÇÃO:**

Esse problema ocorre quando a top de vendas está marcada como bonificação.

Nesse caso, desmarque a opção **"Bonificação"**. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/26354572613015)

 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26354572614551)

CAUSA:**

Na query de Vendas por vendedor no gerente online tem uma condição para o campo de 'TOTAL',  'CASE WHEN TGFTOP.BONIFICACAO = 'S' THEN 0 ELSE 1 END * TGFTOP.GOLDEV). Esse campo na TOP é histórico, quando é alterado só surgirá efeito para os novos lançamentos.