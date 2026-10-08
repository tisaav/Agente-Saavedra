# O serviço não será finalizado pois o limite de rejeições foi alcançado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9859065199127-O-servi%C3%A7o-n%C3%A3o-ser%C3%A1-finalizado-pois-o-limite-de-rejei%C3%A7%C3%B5es-foi-alcan%C3%A7ado](https://ajuda.sankhya.com.br/hc/pt-br/articles/9859065199127-O-servi%C3%A7o-n%C3%A3o-ser%C3%A1-finalizado-pois-o-limite-de-rejei%C3%A7%C3%B5es-foi-alcan%C3%A7ado)  
> **ID:** `9859065199127` | **Última Atualização:** 2026-07-22T15:05:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357465630871)

 MENSAGEM:**

[CORE_E05991] O serviço não será finalizado pois o limite de rejeições foi alcançado. Foram repetições da rejeição para o mesmo xml dessa NF-e.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357510051991)

 SITUAÇÃO:**

Ao gerar lote da NF-e a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357510054423)

 CAUSA:**

O sistema grava um histórico dos motivos das rejeições apresentadas ao tentar Gerar o Lote, e quando ocorre de esgotar uma grande quantidade de rejeição apresentada em uma única NF, necessita deletar esse histórico para conseguir tentar gerar o lote novamente.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19357510064535)

 SOLUÇÃO:**

Quando esse erro ocorrer acione o suporte para análise e intervenção.

OBS: Acessar o banco de dados e deletar o registro das tabelas TGFACT e TGFREJNFE)