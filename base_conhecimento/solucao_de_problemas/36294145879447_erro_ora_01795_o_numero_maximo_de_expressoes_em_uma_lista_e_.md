# Erro: "ORA-01795: o número máximo de expressões em uma lista é de 1000"

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36294145879447-Erro-ORA-01795-o-n%C3%BAmero-m%C3%A1ximo-de-express%C3%B5es-em-uma-lista-%C3%A9-de-1000](https://ajuda.sankhya.com.br/hc/pt-br/articles/36294145879447-Erro-ORA-01795-o-n%C3%BAmero-m%C3%A1ximo-de-express%C3%B5es-em-uma-lista-%C3%A9-de-1000)  
> **ID:** `36294145879447` | **Última Atualização:** 2026-07-22T14:23:12Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36294145849239)

 **MENSAGEM:**

**ORA-01795: o número máximo de expressões em uma lista é de 1000**

 

![image (28).png](https://ajuda.sankhya.com.br/hc/article_attachments/36493822655511)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36294155897879)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36493851984407)

 **Revise a requisição** para garantir que a cláusula **IN** não ultrapasse o limite máximo de **1000 valores, **imposto pelo Oracle.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36493851985815)

 Se for necessário tratar um volume maior de registros, utilize alternativas como **paginação**, **filtros de faixa** ou **divisão da consulta** em blocos menores.

Essas abordagens evitam que o limite do Oracle seja excedido e asseguram que a consulta seja executada corretamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36294155898135)

CAUSA:**

O erro ocorre pois o banco Oracle possui uma limitação de até 1000 valores na clausula **IN**.

Neste cenário, a consulta enviada pela requisição via API continha mais de 1000 códigos de produto, ultrapassando o limite e gerando a falha.