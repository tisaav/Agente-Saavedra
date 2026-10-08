# O Header Authorization é obrigatório para esta requisição

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32422643660951-O-Header-Authorization-%C3%A9-obrigat%C3%B3rio-para-esta-requisi%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/32422643660951-O-Header-Authorization-%C3%A9-obrigat%C3%B3rio-para-esta-requisi%C3%A7%C3%A3o)  
> **ID:** `32422643660951` | **Última Atualização:** 2026-07-22T14:31:19Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32422643642007)

 **MENSAGEM:**

O Header Authorization é obrigatório para esta requisição

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32422643642519)

SOLUÇÃO:**

Verifique a URL de login utilizada no momento da autenticação.

A API da Sankhya é sensível a letras maiúsculas e minúsculas (case sensitive). Portanto, a palavra "**login**" no endpoint deve obrigatoriamente ser informada em letras minúsculas.
Exemplo correto:

```text
https://api.sandbox.sankhya.com.br/login
```

O uso de "**Login**" (com "L" maiúsculo) resultará em falha de autenticação e erro no Header Authorization.

Após o ajuste da URL com a grafia correta, a autenticação ocorrerá normalmente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32422643644439)

CAUSA:**

A API da Sankhya diferencia maiúsculas de minúsculas na URL (case sensitive). O uso incorreto de letras maiúsculas na palavra "**login**" na URL de autenticação impede o correto processamento da requisição e ocasiona o erro de Header Authorization, mesmo quando AppKey e Token estão devidamente configurados.