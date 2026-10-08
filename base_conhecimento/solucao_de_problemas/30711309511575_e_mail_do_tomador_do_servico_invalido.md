# E-mail do tomador do serviço inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30711309511575-E-mail-do-tomador-do-servi%C3%A7o-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/30711309511575-E-mail-do-tomador-do-servi%C3%A7o-inv%C3%A1lido)  
> **ID:** `30711309511575` | **Última Atualização:** 2026-09-15T21:04:10Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/30711299281815)

** Mensagem**

[E126] E-mail do tomador do serviço inválido. O campo e-mail do tomador do serviço deverá ter tamanho máximo de 80 caracteres.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39450918564503)

** Situação**

Ao tentar criar o rascunho de uma **"Nota Fiscal de Serviço Eletrônica (NFS-e)"**, o sistema apresenta a mensagem de erro indicando que o e-mail do tomador do serviço é inválido. Esta validação ocorre quando o campo de e-mail cadastrado no parceiro excede o limite de caracteres aceitos pela prefeitura ou quando há múltiplas informações de e-mail no cadastro.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/30711299282967)

** Solução**

Este erro ocorre pois algumas prefeituras, conforme manual de integração de NFSe, possuem restrições quanto ao tamanho da tag <Email> ou não permitem o envio de múltiplos endereços de e-mail no XML. Para resolver, siga as orientações abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39450901642007)

 Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros) e localize o tomador do serviço.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39450901646743)

 Verifique o campo **"E-mail"** cadastrado. Certifique-se de que o texto não ultrapasse o limite de caracteres permitido pela sua prefeitura (geralmente 80 caracteres).

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39450918578199)

 Se o e-mail contiver caracteres especiais que não são aceitos pelo sistema da prefeitura, substitua-os ou remova-os.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30711299283991)

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39450901651479)

 Caso o problema persista devido ao envio de múltiplos e-mails, acesse a tela de **"Preferências"** (Configurações >> Avançado >> Preferências) e localize o parâmetro **"NFSEUMEMAIL - Cód. IBGE municípios aceitam um end. email tomador"**. Adicione o código do IBGE da sua cidade neste parâmetro.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30711299288087)

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39450901653527)

 Ao configurar **"NFSEUMEMAIL"**, o sistema enviará apenas o primeiro endereço de e-mail informado no cadastro do parceiro.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30742119779223)

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43518567142423)

 Após realizar os ajustes, tente criar novamente o rascunho da NFS-e. 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/30711299297943)

** Causa**

O erro ocorre devido a validações impostas pela prefeitura municipal no XML da nota, sendo as principais causas:
• O e-mail cadastrado ultrapassa o limite de caracteres (tag <Email> inválida).
• O e-mail contém caracteres especiais não aceitos pelo sistema emissor.
• O cadastro contém múltiplos endereços de e-mail que o sistema da prefeitura não processa corretamente.