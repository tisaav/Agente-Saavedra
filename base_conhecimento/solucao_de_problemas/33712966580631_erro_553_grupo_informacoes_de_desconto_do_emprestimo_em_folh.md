# Erro 553 - Grupo "Informações de desconto do empréstimo em folha' não deve ser preenchido

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33712966580631-Erro-553-Grupo-Informa%C3%A7%C3%B5es-de-desconto-do-empr%C3%A9stimo-em-folha-n%C3%A3o-deve-ser-preenchido](https://ajuda.sankhya.com.br/hc/pt-br/articles/33712966580631-Erro-553-Grupo-Informa%C3%A7%C3%B5es-de-desconto-do-empr%C3%A9stimo-em-folha-n%C3%A3o-deve-ser-preenchido)  
> **ID:** `33712966580631` | **Última Atualização:** 2026-08-18T19:54:52Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33959424293783)

 **MENSAGEM**

Erro 553 - Grupo "Informações de desconto do empréstimo em folha" não deve ser preenchido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33959424297751)

 **SITUAÇÃO**

Esta mensagem de erro é apresentada ao tentar realizar o envio do evento **S-1010** (Rubrica) pela **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33959408334999)

 **SOLUÇÃO**

Para corrigir o problema, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33959424302487)

 Acesse a **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e gere o evento **S-1010** para a rubrica **DESCONTO CRÉDITO TRABALHADOR**.
 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33959424304279)

 Ao enviar o evento, desmarque a opção **"Utilizar a data de início padrão do sistema"**, conforme indicado na imagem abaixo.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/33713144636695)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33959424306839)

 Informe a referência **05/2025** no campo correspondente.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/33713144638615)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33959424308503)

 Envie o evento com a data de validade **05/2025** para corrigir o problema.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33959408355607)

 **CAUSA**

O erro ocorre porque o início do envio da informação do **Crédito do Trabalhador** ao eSocial iniciou na referência **05/2025**, e o sistema precisa que esta rubrica seja enviada com a data de validade correspondente.