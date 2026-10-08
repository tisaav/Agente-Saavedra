# Dados da NF-e divergentes do EPEC. (NT2014/001)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043118413-Dados-da-NF-e-divergentes-do-EPEC-NT2014-001](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043118413-Dados-da-NF-e-divergentes-do-EPEC-NT2014-001)  
> **ID:** `360043118413` | **Última Atualização:** 2026-07-22T16:07:35Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510324338071)

 **MENSAGEM:**

[467 - Rejeição]: Dados da NF-e divergentes do EPEC.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510324339607)

SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510324340887)

 Uma NF-e emitida em Contingência EPEC precisa ser transmitida à Sefaz Estadual imediatamente após cessarem os problemas técnicos no Ambiente Autorizador da Sefaz Estadual. Nesse tipo de Contingência, primeiro é enviado o Evento EPEC para a **Sefaz Nacional**, que compartilhará o mesmo com o **Ambiente Estadual**.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510310649495)

 Confira a divergência dos dados da NF-e com os dados do EPEC recebido anteriormente, para os campos: IE do Emitente, Data de Emissão, Tipo de Nota Fiscal (entrada / saída), UF do destinatário, identificação do destinatário (CNPJ/CPF/idEstrangeiro), IE do Destinatário e dados de valor (Total, ICMS e ICMS-ST).

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510310652183)

 Opcionalmente, a SEFAZ Autorizadora poderá informar na mensagem de erro o nome da tag da NF-e com valor divergente no EPEC.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510324348695)

 Localizado o campo de divergência ajuste essa informação, se possível. Caso a informação enviada em EPEC seja a incorreta, acione o seu contador para orientações.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510324352279)

 CAUSA:**

Quando uma NF-e em Contingência EPEC for recebida pela **Sefaz Estadual** com os dados divergentes do evento EPEC registrado na **Sefaz Nacional** haverá a rejeição.

Alguns dados que podem estar divergentes:

- Data e hora de Emissão (Time Zone/Fuso Horário também deve ser verificado)

- IE do Emitente

- Tipo de Nota Fiscal (entrada / saída)

- UF do destinatário

- Identificação do destinatário (CNPJ/CPF/idEstrangeiro)

- IE do Destinatário

- Dados de valor (Total, ICMS e ICMS-ST)