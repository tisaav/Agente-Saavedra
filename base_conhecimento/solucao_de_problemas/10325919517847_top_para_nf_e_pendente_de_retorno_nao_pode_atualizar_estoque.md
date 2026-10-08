# TOP para NF-e Pendente de Retorno não pode atualizar estoque

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10325919517847-TOP-para-NF-e-Pendente-de-Retorno-n%C3%A3o-pode-atualizar-estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/10325919517847-TOP-para-NF-e-Pendente-de-Retorno-n%C3%A3o-pode-atualizar-estoque)  
> **ID:** `10325919517847` | **Última Atualização:** 2026-07-22T15:03:54Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18887649507223)

 MENSAGEM:**

[CORE_E02623] TOP para NF-e Pendente de Retorno não pode atualizar estoque.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18887626430231)

 SITUAÇÃO:**

Ao tentar incluir a Top para NF-e  pendente de retorno na aba impressão de uma outra TOP a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18887649523991)

 SOLUÇÃO:**

Verifique a configuração do** Tipo de Operação** *(Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP)* para NF-e pendente de retorno, observe o campo "Atualização do Estoque", na aba **Estoque. **Ele não pode estar configurado como 'Atualizar'. Portanto, caso necessário, faça o ajuste e realize novamente o lançamento.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/10325915696919)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18887649545879)

CAUSA:**

Ocorre quando o Tipo de Operação está atualizando estoque.