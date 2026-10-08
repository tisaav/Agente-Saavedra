# Data de Faturamento deve ser maior ou igual a data de Negociação

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178154-Data-de-Faturamento-deve-ser-maior-ou-igual-a-data-de-Negocia%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178154-Data-de-Faturamento-deve-ser-maior-ou-igual-a-data-de-Negocia%C3%A7%C3%A3o)  
> **ID:** `360043178154` | **Última Atualização:** 2026-08-18T20:31:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165048400407)

 MENSAGEM:**

[CORE_E01846] Data de Faturamento deve ser maior ou igual a data de Negociação.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165066956183)

 SITUAÇÃO:**

Ao tentar efetuar o faturamento de uma Nota, a seguinte mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165048410263)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165066965783)

 Verifique a data de Faturamento e se estiver menor que a data de Negociação, deverá ser ajustada.

Caso realmente se faz necessário que o Faturamento seja menor que a data de Negociação, considere ligar o parâmetro "**PERDTFATANDTNEG - Permitir Dt. Faturamento anterior Dt. Negociação?"**

 

![parametro3.png](https://ajuda.sankhya.com.br/hc/article_attachments/14712981951127)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165048417431)

 Após os ajustes, tente faturar novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16165048420375)

 CAUSA:**

Ocorre quando a data de Faturamento é menor que a data de negociação, caso o parâmetro esteja desligado, será apresentada a mensagem impeditiva.