# ORA-28001: the password has expired

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616373-ORA-28001-the-password-has-expired](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616373-ORA-28001-the-password-has-expired)  
> **ID:** `360044616373` | **Última Atualização:** 2026-07-22T15:54:05Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782953379095)

 MENSAGEM:**

[ORA-28001]: the password has expired.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782953387415)

 CAUSA:**

Ocorre quando a senha do usuário do banco de dados SANKHYA tenha expirado. Sendo necessário que um DBA Master acesse o banco de dados com permissões de administrador e execute o reset da senha.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782984570135)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782953383191)

 Solicite que a equipe de TI/DBA da Empresa acesse com um aplicativo de gerenciamento de banco de dados, com o usuário **SYS** (*A senha para acesso ao Banco de Dados é de responsabilidade do DBA*).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16782953384727)

 Execute os comandos abaixo:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458084706583)

 Comando para definir que a senha nunca mais expire:

**ALTER PROFILE DEFAULT LIMIT PASSWORD_LIFE_TIME UNLIMITED;**

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458084706583)

 Comando para passar ao banco uma nova senha:
**ALTER USER SANKHYA IDENTIFIED BY novasenha**

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458084706583)

 Em seguida, restaure a senha já utilizada para o usuário:
**ALTER USER SANKHYA IDENTIFIED BY  senha do usuário sankhya**