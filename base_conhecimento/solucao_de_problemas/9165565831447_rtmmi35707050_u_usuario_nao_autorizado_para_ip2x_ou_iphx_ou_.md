# RTMMI35707050 U USUARIO NAO AUTORIZADO PARA IP2X OU IPHX ou RTMCMODELO RISKSCORING INVALIDO

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9165565831447-RTMMI35707050-U-USUARIO-NAO-AUTORIZADO-PARA-IP2X-OU-IPHX-ou-RTMCMODELO-RISKSCORING-INVALIDO](https://ajuda.sankhya.com.br/hc/pt-br/articles/9165565831447-RTMMI35707050-U-USUARIO-NAO-AUTORIZADO-PARA-IP2X-OU-IPHX-ou-RTMCMODELO-RISKSCORING-INVALIDO)  
> **ID:** `9165565831447` | **Última Atualização:** 2026-07-22T15:10:01Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16678059731223)

 MENSAGEM:**

[CORE_E02092]:

- RTMMI35707050 U USUARIO NAO AUTORIZADO PARA IP2X OU IPHX;

- RTMCMODELO RISKSCORING INVALIDO.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16678059733015)

 SITUAÇÃO:**

Ao consultar a "Análise de Risco Serasa" a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16678059737367)

 SOLUÇÃO:**

- Sobre o erro: **RTMCMODELO RISKSCORING INVALIDO**, ele ocorre devido as marcações  da tela **"Configuração Serasa"** *(Caminho de acesso: Financeiro » Preferências » Configuração Serasa)* não estarem devidamente selecionadas, são elas:

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9165061086999)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16678059738519)

 IMPORTANTE:**

Vale ressaltar que essas marcações tem a ver com o contrato firmado diretamente com o SERASA.

- Sobre o erro: **RTMMI35707050 U USUARIO NAO AUTORIZADO PARA IP2X OU IPHX,** este ocorre devido a tentativa de fazer uma consulta na tela** Análise de Risco Serasa** *(Caminho de acesso: Financeiro » Consultas » Análise de Risco Serasa)* que o contrato firmado com a SERASA não permite. Sendo assim, verifique no contrato o que foi acordado, pois essa mensagem vem direto do SERASA.

 

***

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450827941655)

*** Segue abaixo um passo a passo que deverá ser realizado para ter mais insumos no contato direto com a equipe do SERASA:

- Pegue a URLENVIO, na tabela TSERACS, nesse campo fica a URL que o sistema está gerando e mandando para o SERASA, se tiver qualquer coisa errada o SERASA irá reclamar.

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/9165416629911)

 

 

- Assim que pegar essa URL no sistema, descodifique pelo site [https://www.base64decode.org/](https://www.base64decode.org/).  Feito isso, entre em contato direto com o SERASA e solicite mais informações sobre a recusa na consulta.

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/9165440392471)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16678071523991)

 CAUSA:**

Quando é feita consulta ou acesso com as configurações diferentes do que foi acordado em contrato com o SERASA.