# Erro no envio de boletos por e-mail com destinatário inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34121059915287-Erro-no-envio-de-boletos-por-e-mail-com-destinat%C3%A1rio-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/34121059915287-Erro-no-envio-de-boletos-por-e-mail-com-destinat%C3%A1rio-inv%C3%A1lido)  
> **ID:** `34121059915287` | **Última Atualização:** 2026-07-22T14:27:42Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37667773697687)

**SITUAÇÃO:**

Ao tentar enviar boletos por e-mail, se um único destinatário estiver com e-mail incorreto, o sistema apresenta erro e nenhum boleto é enviado, mesmo que existam outros destinatários válidos.
 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34121027416471)

**SOLUÇÃO:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39659972275223)

 Acesse a tela **"Fila para Envio de Boletos"** (Configurações >> Avançado >> Envio de Mensagens >> Fila para Envio de Boletos).
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39659956014615)

 Verifique o status dos boletos. Se o status estiver com **"Erro: Não enviada"**, a consulta no **"DBExplorer"** (Configurações >> Avançado >> DBExplorer) pode mostrar no campo **"MSGERRO"**: **"already connected"**.
 

Comando:
 

SELECT * FROM TMDFMG WHERE STATUS = 'Erro: Não Enviada'
AND (DTENTRADA BETWEEN 'data aqui' AND 'data aqui')

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39659956014743)

 Em seguida, acesse a tela **"Impressão de Boleto(s)"** (Financeiro >> Relatórios >> Impressão de Boleto(s)), selecione o agrupamento e os boletos que deseja enviar.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39659956016279)

 Clique no botão **"Enviar boleto(s) por e-mail"**.
 

![Impressão de boletos.png](https://ajuda.sankhya.com.br/hc/article_attachments/36724847266967)

 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39659972281367)

 No pop-up **"Enviar boleto(s) por e-mail"**, localize o campo **"Opções"**.
 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39659956016663)

 Verifique a opção **"Enviar apenas se todos tiverem destinatários definidos"**; por padrão, ela já vem marcada.
 

![7](https://ajuda.sankhya.com.br/hc/article_attachments/36724847269527)

 Para enviar os boletos mesmo quando houver destinatários com e-mail inválido, desmarque a opção do passo anterior.
 

Ao desmarcar, o sistema enviará os boletos somente para os destinatários com e-mails válidos, ignorando aqueles que estiverem incorretos.
 

![unnamed (14).png](https://ajuda.sankhya.com.br/hc/article_attachments/34121059907351)

 

![8](https://ajuda.sankhya.com.br/hc/article_attachments/36724834978455)

 Se a opção permanecer marcada, o envio não será feito para nenhum destinatário, mesmo que alguns endereços sejam válidos.
 

![unnamed (15).png](https://ajuda.sankhya.com.br/hc/article_attachments/36724847271831)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34121059910679)

**CAUSA:**

A falha no envio ocorre porque a opção **"Enviar apenas se todos tiverem destinatários definidos"** está marcada. Nesse modo, qualquer e-mail inválido bloqueia todo o envio, impedindo que os boletos sejam enviados mesmo para destinatários válidos.