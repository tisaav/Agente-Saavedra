# Erro na confirmação NFSe FLORIANOPOLIS - Erro na resposta do webservice

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16969328188311-Erro-na-confirma%C3%A7%C3%A3o-NFSe-FLORIANOPOLIS-Erro-na-resposta-do-webservice](https://ajuda.sankhya.com.br/hc/pt-br/articles/16969328188311-Erro-na-confirma%C3%A7%C3%A3o-NFSe-FLORIANOPOLIS-Erro-na-resposta-do-webservice)  
> **ID:** `16969328188311` | **Última Atualização:** 2026-07-22T14:54:05Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969328179479)

 **MENSAGEM:**

Erro na resposta do webservice: The content of elements must consist of well-formed character data or markup. Não foi retornado um xml válido. Uma das possíveis causas para esse erro, é algum erro que ocorreu no servidor(SEFAZ) e foi redirecionado para uma página HTML.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969361046551)

CAUSA:**

Para emitir NFS-e para Florianópolis foi criado o campo Código ID CNAE dentro do cadastro do serviço, quando o mesmo não é preenchido corretamente, ao confirmar a nota é apresentado o erro. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969337573527)

SOLUÇÃO:**

Como se trata de um erro genérico, pode haver demais informações a serem validadas, mas uma das opções seria:

Verifique em um XML emitido diretamente na Prefeitura de Florianópolis a tag idCNAE

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16969622676247)

 

Consulte no cadastro do Serviço, como esta preenchido o campo Código ID CNAE, deve conter a mesma informação do XML emitido na Prefeitura, caso esteja diferente, altere e gere uma nova NFS-e.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16969357952151)