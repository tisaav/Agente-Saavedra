# Financeiros não encontrados para imprimir boleta

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9038402484247-Financeiros-n%C3%A3o-encontrados-para-imprimir-boleta](https://ajuda.sankhya.com.br/hc/pt-br/articles/9038402484247-Financeiros-n%C3%A3o-encontrados-para-imprimir-boleta)  
> **ID:** `9038402484247` | **Última Atualização:** 2026-08-27T11:38:59Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672326309911)

 MENSAGEM:**

[CORE_E01378]: Financeiros não encontrados para imprimir boleta!

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672342159767)

 SITUAÇÃO:**

Ao tentar emitir boletos a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672342163991)

 SOLUÇÃO:**

Verifique se a 'PROCEDURE  STP_CONFIRMANOTA2' e a 'TRIGGER  TRG_UPD_TGFCAB' existem no banco de dados. Caso não existam, realize a atualização de versão para que as mesmas sejam criadas. Elas são responsáveis por confirmar a nota e inserir corretamente o número da nota no financeiro.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672326319255)

 CAUSA: **

Ao tentar fazer a impressão de boletos e por algum motivo o financeiro fica sem o número da nota.