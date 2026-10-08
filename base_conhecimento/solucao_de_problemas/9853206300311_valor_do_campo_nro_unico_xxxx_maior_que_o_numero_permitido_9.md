# Valor do campo nro. único [XXXX] maior que o número permitido: 999999

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9853206300311-Valor-do-campo-nro-%C3%BAnico-XXXX-maior-que-o-n%C3%BAmero-permitido-999999](https://ajuda.sankhya.com.br/hc/pt-br/articles/9853206300311-Valor-do-campo-nro-%C3%BAnico-XXXX-maior-que-o-n%C3%BAmero-permitido-999999)  
> **ID:** `9853206300311` | **Última Atualização:** 2026-07-22T15:05:42Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16779161972759)

 MENSAGEM:**

[CORE_E01416]: Valor do campo nro. único [XXXX] maior que o número permitido: 999999.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16779181261847)

 SITUAÇÃO:**

Ao tentar emitir um boleto a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16779161979927)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16779161982359)

 Para solução dessa mensagem, revise (com apoio do gerente e/ou manual do banco) os seguintes campos :

Tela **"Contas"** *(Caminho de acesso à tela: Configurações » Cadastros » Bancários » Contas)*

- Campo : "**Carteira"**

- Campo : "**Convênio"**

Considerando as seguintes regras :

Se o Convênio for maior que 999999 (seis dígitos) o campo Carteira deve ser: 12, 17, 18, 19.

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16779181270167)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16779181273367)

CAUSA:**

Quando o campo convênio possui mais de seis dígitos e o campo carteira é diferente de 12, 17, 18, 19..