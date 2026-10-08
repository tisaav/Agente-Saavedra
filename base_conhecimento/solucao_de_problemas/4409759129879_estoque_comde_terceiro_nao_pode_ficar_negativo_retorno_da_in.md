# Estoque com/de Terceiro não pode ficar negativo (Retorno da industrialização)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4409759129879-Estoque-com-de-Terceiro-n%C3%A3o-pode-ficar-negativo-Retorno-da-industrializa%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409759129879-Estoque-com-de-Terceiro-n%C3%A3o-pode-ficar-negativo-Retorno-da-industrializa%C3%A7%C3%A3o)  
> **ID:** `4409759129879` | **Última Atualização:** 2026-07-22T15:21:25Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16091139436439)

 MENSAGEM**:

SQL-500001 Estoque com/de Terceiro não pode ficar negativo.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16091125422743)

 SOLUÇÃO:**

Após constatar o erro e verificar que não deveria ter uma linha do produto na tgfest, limpe a linha na tgfest para o produto produzido que está retornando da industrialização. Tal serviço** é feito via banco de dados,** pois pelo sistema não é possível tirar essa linha criada. Ao se deparar com tal mensagem, acione o Service Desk.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16091125426711)

 CAUSA:**

Quando se faz o retorno da industrialização é normal vir o produto que foi industrializado, e como esse produto não existe na nota que originou a devolução, o campo** "ATUALESTTERC"** ficará como 'N', mesmo com a top estando configurada para atualizar estoque de terceiro. O sistema leva em consideração para deixar o campo como 'N' quando não existe uma linha na tgfest para esse produto e para o parceiro em questão.

Se por algum motivo existir uma linha na tgfest desse produto para esse parceiro, vai apresentar o erro que o estoque não pode ficar negativo. Um dos motivos de ter sido criada a linha para produto na tgfest é por algum erro do usuário, que em algum momento movimentou esse produto na entrada, mesmo que o saldo esteja zerado já é  suficiente para que o sistema entenda que no retorno da industrialização esse produto tenha que ficar com o **ATUALESTTERC diferente de 'N'.**