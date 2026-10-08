# Tipo de negociação não encontrada

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360058228934-Tipo-de-negocia%C3%A7%C3%A3o-n%C3%A3o-encontrada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058228934-Tipo-de-negocia%C3%A7%C3%A3o-n%C3%A3o-encontrada)  
> **ID:** `360058228934` | **Última Atualização:** 2026-07-22T15:26:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16272245153303)

 MENSAGEM**:

[CORE_E04654]  Tipo de negociação não encontrada: 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16272282907415)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16272282908055)

 Solicite a Equipe de TI da sua empresa ou Terceiro que se certifique de que o horário do servidor de banco de dados não está adiantado. Caso esteja, solicite o devido ajuste.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16272282909463)

 Após os ajustes feitos, efetue o lançamento do documento novamente.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16272282910359)

 OBSERVAÇÃO:**

Caso não tenha um especialista de TI ou DBA, entre em contato com a Unidade ou aloque horas com a Equipe de TI da Sankhya para os devidos ajustes.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16272282911767)

 CAUSA:**

Ao tentar efetuar algum lançamento ou faturamento que utilize determinado 'Tipo de Negociação', caso o cadastro desse tipo de negociação esteja com **horário superior** ao horário do lançamento que está sendo realizado, o tipo de negociação não será "encontrado", apresentando a mensagem. 

- Suponhamos o cadastro do tipo de negociação X;

- O tipo de negociação exemplificado foi cadastrado considerando a data/hora do computador: **29/10 às 15:00.** 

- Porém, o **servidor de banco de dados está 2 horas adiantado**, salvando a data/hora desse cadastro: **29/10 às 17:00.**

- Dessa forma, antes que o computador local aponte 17:00h, não será possível utilizar esse cadastro. Justificando a necessidade de ajuste/correção do horário do servidor de banco.