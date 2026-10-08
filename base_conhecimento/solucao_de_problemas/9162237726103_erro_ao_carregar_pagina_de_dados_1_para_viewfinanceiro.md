# Erro ao carregar página de dados 1 para ViewFinanceiro

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9162237726103-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-ViewFinanceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/9162237726103-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-ViewFinanceiro)  
> **ID:** `9162237726103` | **Última Atualização:** 2026-09-03T14:15:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033134286743)

 MENSAGEM:**

[CORE_E00358] Erro ao carregar página de dados 1 para ViewFinanceiro.
A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, <, <= , >, >= ou quando ela é usada como uma expressão.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033149365911)

 SITUAÇÃO:**

Ao tentar acessar as telas Movimentação financeira ou Compensação financeira a mensagem abaixo é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033134313367)

 CAUSA: **

Quando o filtro possui alguma condição incorreta ou incompleta.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033149386135)

 SOLUÇÃO:**

- Necessário verificar se a tela possui algum filtro, sendo o padrão ou algum criado. Caso possua algum filtro, faça o teste retirando o filtro. Se o erro deixar de ocorrer verifique a expressão utilizada nesse filtro;

- Para visualizar o filtro padrão é necessário acessar o sistema com o usuário SUP;

![filtros 13-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033149394327)

- Identificado o filtro é necessário revisar o mesmo, pois alguma condição do filtro ficou incorreta ou incompleta causando o erro apresentado na tela. Se o erro persistir, verificar se existe campo adicional calculado na tabela. 

![assistente de filtro 13-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033134335511)