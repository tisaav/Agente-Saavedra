# Lock time out. SQL Server connection timed out

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360053148034-Lock-time-out-SQL-Server-connection-timed-out](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053148034-Lock-time-out-SQL-Server-connection-timed-out)  
> **ID:** `360053148034` | **Última Atualização:** 2026-07-22T15:28:44Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585757963927)

 MENSAGEM**:

Lock time out. SQL Server connection timed out.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585757971607)

 CAUSA**:

Mensagem apresentada devido ao timeout padrão do BDE para SQL Server que é de 300 segundos.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585757982999)

 SOLUÇÃO**:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585757988503)

 Acesse o BDE no diretório de instalação como 'Administrador'
Aba: Configuration>>Drivers>>Native>>MSSQL

-**MAX QUERY TIME** = 900 [Altere de 300 para 900]

Salve clicando na seta azul para direita(Apply)

![bde_max.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360091393493)

O valor configurado por padrão é de 300 segundos, pode-se aumentá-lo para 900 de modo a ter maior tempo para a resposta.

**Nota**: Caso não tenha permissões, solicite ao Administrador, que execute o procedimento.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585757990423)

Após os ajustes, acesse novamente o sistema.