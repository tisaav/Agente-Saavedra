# Cannot locate or connect to SQL server. Unable to connect: SQL Server is unavailable or does not exist. Unable to connect: SQL server does not exist or network acces Alias

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616433-Cannot-locate-or-connect-to-SQL-server-Unable-to-connect-SQL-Server-is-unavailable-or-does-not-exist-Unable-to-connect-SQL-server-does-not-exist-or-network-acces-Alias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616433-Cannot-locate-or-connect-to-SQL-server-Unable-to-connect-SQL-Server-is-unavailable-or-does-not-exist-Unable-to-connect-SQL-server-does-not-exist-or-network-acces-Alias)  
> **ID:** `360044616433` | **Última Atualização:** 2026-07-22T15:54:02Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815460636183)

 MENSAGEM:**

Cannot locate or connect to SQL server. Unable to connect: SQL Server is unavailable or does not exist. Unable to connect: SQL server does not exist or network acces
Alias: DBNSiade.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815452551703)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815452555031)

 Acesse o aplicativo BDE na máquina local onde está ocorrendo o erro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815460641175)

 Acesse o diretório/pasta onde está instalado o BDE: Exemplo: **C:\BDE**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815460642711)

 Execute como Administrador o executável **bdeadmin.exe**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815452566039)

 No BDE, o campo SERVER NAME que fica em Databases e que está utilizando para acessar o sistema

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815452567703)

 Pesquise no máquina do **Servidor **ou em outro Computador que está acessando o sistema normalmente, para que seja ajustado o SERVER NAME, corretamente.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815460646807)

 Salve as alterações e acesse novamente o sistema.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815452576279)

 CAUSA:**

Ocorre quando o BDE do Computador não está devidamente configurado com o endereço do Servidor do sistema.