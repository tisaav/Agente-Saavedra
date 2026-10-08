# Impossível converter para uma string válida: null

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8425348813463-Imposs%C3%ADvel-converter-para-uma-string-v%C3%A1lida-null](https://ajuda.sankhya.com.br/hc/pt-br/articles/8425348813463-Imposs%C3%ADvel-converter-para-uma-string-v%C3%A1lida-null)  
> **ID:** `8425348813463` | **Última Atualização:** 2026-07-22T15:12:01Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16596637213975)

 MENSAGEM**:

Impossível converter para uma string válida: null.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16596677252119)

 SITUAÇÃO:**

Ao tentar gerar o SPED ICMS a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16596677253783)

 SOLUÇÃO:**

Acesse a tela **"****Ajuste de Apuração de ICMS e ICMS ST"** *(Caminho de acesso à tela: Livros Fiscais » Arquivos » Ajuste da Apuração de ICMS e ICMS ST)* e verifique se todos os lançamentos estão com o campo "**Dt. Docto"** preenchidos, caso não estejam faça o preenchimento e salve.

 

![Impossível converter para uma string válida null 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16596677254679)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16596637224471)

CAUSA:**

Esse erro é causado no processo de geração do EFD ICMS/IPI quando temos na tela Ajuste da apuração de icms e icms st lançamentos que, na aba "Ajuste", estejam com o campo Dt. Docto vazio.