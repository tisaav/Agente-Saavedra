# Erro toFixed() digits argument must be between 0 and 100

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31299212340375-Erro-toFixed-digits-argument-must-be-between-0-and-100](https://ajuda.sankhya.com.br/hc/pt-br/articles/31299212340375-Erro-toFixed-digits-argument-must-be-between-0-and-100)  
> **ID:** `31299212340375` | **Última Atualização:** 2026-07-22T14:33:20Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31299212326295)

 **MENSAGEM:**

toFixed() digits argument must be between 0 and 100

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31940145752215)

 SITUAÇÃO:**

Ao acessar a tela **"Consulta de produtos" **é apresentada a mensagem de erro citada acima.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31299212332567)

SOLUÇÃO:**

Quando a tela  Consulta de produtos é acionada e essa mensagem é apresentada, significa que  um dos produtos da base possui o campo **"Decimais para quantidade"** (Aba Medidas e Estoque) com valor **superior a 100.** 
Assim, analise e ajuste o campo de todos os produtos que estejam com esta configuração. 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31299212333079)

CAUSA:**

O erro acontece quando um dos produtos da base possui um valor superior a 100 no campo Decimais para quantidade.