# O token expirou e não conseguimos obter um novo, talvez a API tenha sido revogada. Sugerimos que faça uma nova autenticação. Código: 400

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33766936673943-O-token-expirou-e-n%C3%A3o-conseguimos-obter-um-novo-talvez-a-API-tenha-sido-revogada-Sugerimos-que-fa%C3%A7a-uma-nova-autentica%C3%A7%C3%A3o-C%C3%B3digo-400](https://ajuda.sankhya.com.br/hc/pt-br/articles/33766936673943-O-token-expirou-e-n%C3%A3o-conseguimos-obter-um-novo-talvez-a-API-tenha-sido-revogada-Sugerimos-que-fa%C3%A7a-uma-nova-autentica%C3%A7%C3%A3o-C%C3%B3digo-400)  
> **ID:** `33766936673943` | **Última Atualização:** 2026-07-22T14:28:21Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33766950114839)

 **MENSAGEM:**

O token expirou e não conseguimos obter um novo, talvez a API tenha sido revogada. Sugerimos que faça uma nova autenticação. Código: 400

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33766950115223)

 **SITUAÇÃO:**

Durante testes ou tentativas de envio de e-mails pelas telas **Servidor SMTP **ou **Contas SMTP**, o sistema exibe a mensagem de erro acima, impedindo o disparo de mensagens por contas configuradas com autenticação OAuth, como Outlook ou Office365.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33766950115735)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33970137663767)

 Pela tela** Contas SMTP: **

- 

Acesse a tela **''Contas SMTP'' **(Configurações> Avançado > Envio de Mensagens > Contas SMTP); 

- 

Selecione a conta de e-mail configurada com OAuth; 

- 

Clique no botão **''****Autenticação OAuth'';**

- 

Realize o login com a conta Microsoft autorizada; 

- 

Após autenticar, o novo token será salvo automaticamente; 

- 

Realize um teste de envio de e-mail para validar.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33970174552471)

 Pela tela **Servidor SMTP: **

- 

Acesse a tela **''Servidor SMTP''** (Configurações> Avançado > Envio de Mensagens > Servidor SMTP);

- 

Clique no botão **''****Autenticação OAuth''**;** **

- 

Realize a revalidação da conta Microsoft conforme instruções na tela.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33766950116247)

 CAUSA:**

Esse erro está relacionado à expiração do token de autenticação OAuth, utilizado pelo sistema Sankhya para se comunicar com os servidores da Microsoft (Outlook/Office365).

O token expirado refere-se a um token temporário de sessão, gerado durante a autenticação inicial, com validade limitada conforme as regras da Microsoft.

A falha ocorre quando o Sankhya não consegue renovar automaticamente esse token, devido a um dos seguintes motivos:

- 

Expiração sem renovação permitida; 

- 

Revogação de permissões pelo administrador da conta Microsoft; 

- 

Alterações na política de segurança da Microsoft;

- 

Mudanças no escopo ou configurações da aplicação no portal Azure.