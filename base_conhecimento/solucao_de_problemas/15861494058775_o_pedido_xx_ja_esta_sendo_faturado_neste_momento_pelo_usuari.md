# O pedido XX ja esta sendo faturado neste momento pelo usuário X

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15861494058775-O-pedido-XX-ja-esta-sendo-faturado-neste-momento-pelo-usu%C3%A1rio-X](https://ajuda.sankhya.com.br/hc/pt-br/articles/15861494058775-O-pedido-XX-ja-esta-sendo-faturado-neste-momento-pelo-usu%C3%A1rio-X)  
> **ID:** `15861494058775` | **Última Atualização:** 2026-07-22T14:55:58Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15861445221143)

 MENSAGEM:**

[CORE_E04682] O pedido XX ja esta sendo faturado neste momento pelo usuário X.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15861450918295)

 CAUSA:**

Pode ocorre por alguma instabilidade ou faturamento "preso" na aplicação.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15861461601815)

 SOLUÇÃO:**

O sistema geralmente costuma apresentar essa mensagem quando algum procedimento de faturamento acaba ficando "preso" na aplicação após algum problema de conexão ou instabilidade, ou até mesmo em função de alguma encerramento de sessão indevido. 
Por mais que o usuário não esteja acessando o sistema naquele momento, pode ser que o processo de faturamento esteja vinculado na sessão e por isso a execução da rotina esteja impedida de ser concluída.
 Para solucionar o problema, é possível reinicializar o sistema através da tela Administração do Servidor, na aba Geral.
 
* Administração do Servidor (Configurações » Avançado » Administração do Servidor)
* Aba Geral » Descartar Cache
* Aba Geral » Reinicializar Sistema

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15861429106071)