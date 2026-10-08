# Unknown user name or password

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109794-Unknown-user-name-or-password](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109794-Unknown-user-name-or-password)  
> **ID:** `360044109794` | **Última Atualização:** 2026-07-22T15:54:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584947301015)

 MENSAGEM:**

Unknown user name or password.

Login failed for user 'SANKHYA'.

Login incorrect.

Alias: DBNSiade.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584947308311)

 SITUAÇÃO:**

Ao tentar acessar algum modulo do MGE, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584979387287)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584979395735)

 Solicite que a área de TI ou Administrador de Banco de Dados, revise a senha do banco, seguindo as seguintes considerações para a senha:

- Máximo de 10 caracteres;

- Uso apenas de caracteres minúsculos;

- Não pode ser utilizado o número 0;

- São aceitos apenas alguns caracteres especiais: !, *, $, | e &

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584979399063)

 Depois de usar uma senha dentro do padrão, será preciso gerar novo arquivo 'license.dat', e inserir este arquivo dentro da pasta do executável do MGE.

Caso utilize o Sankhya W, será necessário refazer a conexão com o banco de dados pelo gerenciador de pacotes e atualizar a senha no arquivo de configuração do SAS também. (SAS.CFG).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18584947332503)

 CAUSA:**

Ocorre quando a senha do banco de dados está incorreta. A senha padrão é 'tecsis', se o cliente altera essa senha, é necessário ter o arquivo 'license.dat' na pasta onde estão os executáveis do MGE.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18857211355031)

 OBSERVAÇÃO:**

Veja também artigo relacionado: [Não conectado ao ORACLE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616613)

 

 **Abaixo o link para baixar o aplicativo:**


---

### 🔗 Links e Referências Internas:

- [Não conectado ao ORACLE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616613)