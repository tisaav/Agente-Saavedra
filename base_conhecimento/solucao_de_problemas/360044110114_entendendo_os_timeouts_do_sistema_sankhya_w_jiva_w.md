# Entendendo os timeouts do sistema- Sankhya-W/ Jiva-W

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110114-Entendendo-os-timeouts-do-sistema-Sankhya-W-Jiva-W](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110114-Entendendo-os-timeouts-do-sistema-Sankhya-W-Jiva-W)  
> **ID:** `360044110114` | **Última Atualização:** 2026-07-22T15:53:51Z

---

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458057611031)

 Timeout** é um termo em inglês utilizado para determinar um limite de tempo, e na computação isso é muito utilizado para limitar o tempo máximo que um procedimento ou rotina pode executar ininterruptamente.
A plataforma **SankhyaOm** possui alguns tipos de timeouts e cada um deles determina limites diferentes, como segue:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311042467735)

 Timeout de query**

Esse timeout determina o limite de tempo que o sistema espera pela resposta em consultas e outros comandos no banco de dados (select, update, insert, delete).
Ao atingir o limite de tempo, o banco de dados será notificado pela aplicação para que ele “desista” da operação e retorne um erro.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311042471959)

 No caso do Oracle esse erro é: ***"ORA-01013 user requested cancel of current operation"*** ou em português: ***"ORA-01013 o usuário solicitou o cancelamento da operação atual".***

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311042471959)

 Para o SQLServer, as mensagens a ser apresentadas são: Em inglês: "***The query has timed"*** out ou em português: ***"O tempo limite da consulta foi atingido".*** Esse timeout é definido pelo atributo -Djape.global.query.timeout (em segundos) e deve ser configurado em <WILDFLY>/bin/standalone.conf (Linux) ou <WILDFLY>/bin/standalone.conf.bat (Windows), o valor padrão para este atributo é de 600 segundos equivalendo a 10 minutos.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311010047639)

 **Timeout de sessão**

Esse tempo determina quanto tempo uma operação completa pode durar. Em uma operação completa podemos ter diversas transações e milhares de interações com o banco de dados (select/updates/inserts/deletes), portanto ela determina a janela total de tempo em uma operação. Em termos práticos, seria o tempo total decorrido entre o usuário clicar em um botão na tela, a requisição chegar ao servidor, ser totalmente processada e a resposta gerada.
Esse timeout é definido pelo atributo -Djape.session.timeout (em milisegundos) no arquivo <WILDFLY>/bin/standalone.conf (Linux) ou <WILDFLY>/bin/standalone.conf.bat (Windows). Ao atingir o limite de tempo, será apresentado ao usuário a mensagem ***“JapeSession timeout”** *Na ausência de configuração o valor padrão é de 1800000 ms, ou seja, 30 minutos.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311042475799)

 **Timeout de transação**

Esse é o tempo máximo de uma transação com o banco de dados (TRANSACTION_TIME_OUT). Uma operação no sistema pode compreender diversas transações e esse timeout determina o tempo limite de cada uma delas, não a somatória. Ao acontecer esse tipo de timeout a transação é automaticamente desfeita (rollback) e para o usuário é apresentada uma mensagem do tipo ***“Transaction is not active”*** ou "Could not commit transaction"
Se uma determinada operação compreende diversas transações e uma delas teve o limite de tempo excedido, então apenas ela vai sofrer rollback, ficando as anteriores com o status “COMMITED”. Atualmente, é possível configurar este timeout pelo sistema a partir da tela **“Administração do Servidor”**, aba **“Avançado”**, conforme imagem abaixo:

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/12463588527511)