# Erro no mecanismo da regra dinâmica

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9173941578007-Erro-no-mecanismo-da-regra-din%C3%A2mica](https://ajuda.sankhya.com.br/hc/pt-br/articles/9173941578007-Erro-no-mecanismo-da-regra-din%C3%A2mica)  
> **ID:** `9173941578007` | **Última Atualização:** 2026-07-22T15:09:44Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18583359570199)

 MENSAGEM:**

[CORE_E01365] Erro no mecanismo da regra dinâmica.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18583374922135)

 SITUAÇÃO:**

Mensagem é apresentada ao utilizar algumas regras de negócios.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18583374928279)

 SOLUÇÃO:**

Revisar as configurações da regra de negócio apresentada na mensagem pois não foi possível executá-la nos parâmetros definidos.

Uma situação comum para este erro é o fato do eventual liberador definido numa regra de negócio com uma evento personalizado, não ter esta alçada definida no cadastro de usuários.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9173755244823)

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18583359589015)

 CAUSA: **

Quando for encontrada alguma inconsistência na regra de negócio.