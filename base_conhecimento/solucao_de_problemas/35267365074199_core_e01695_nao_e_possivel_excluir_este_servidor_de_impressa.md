# CORE_E01695 - Não é possível excluir este servidor de impressão, pois ele ainda possui X trabalho(s) de impressão

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35267365074199-CORE-E01695-N%C3%A3o-%C3%A9-poss%C3%ADvel-excluir-este-servidor-de-impress%C3%A3o-pois-ele-ainda-possui-X-trabalho-s-de-impress%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/35267365074199-CORE-E01695-N%C3%A3o-%C3%A9-poss%C3%ADvel-excluir-este-servidor-de-impress%C3%A3o-pois-ele-ainda-possui-X-trabalho-s-de-impress%C3%A3o)  
> **ID:** `35267365074199` | **Última Atualização:** 2026-07-22T14:25:45Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35267359573655)

 **MENSAGEM**

[CORE_E01695] Não é possível excluir este servidor de impressão, pois ele ainda possui X trabalho(s) de impressão.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656084055575)

 **SITUAÇÃO**

Na tela **"Servidores de Impressão"** (Configurações » Avançado » Impressão » Servidores de Impressão), ao tentar excluir um servidor de impressão, o sistema apresenta a mensagem de erro informando que ainda existem trabalhos de impressão pendentes vinculados ao servidor.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35267359577367)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656059474199)

 Acesse a tela **"Trabalhos de Impressão"** (Configurações » Avançado » Impressão » Trabalhos de Impressão).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656059476119)

 Localize os **trabalhos pendentes** vinculados ao servidor que deseja excluir.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656084066071)

 Aguarde até que todas as **impressões pendentes** sejam concluídas.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656059480215)

 Caso a impressora configurada esteja **indisponível**, utilize uma impressora substituta para finalizar o trabalho de impressão.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35656084068887)

 Após não haver mais impressões pendentes, retorne à tela **"Servidores de Impressão"** e realize a exclusão do servidor.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35267365069719)

 **CAUSA**

Este erro ocorre quando se tenta excluir um **servidor de impressão** que ainda possui trabalhos de impressão associados a ele. O sistema impede a exclusão para manter a **integridade referencial dos dados** e evitar que trabalhos de impressão fiquem órfãos no sistema.