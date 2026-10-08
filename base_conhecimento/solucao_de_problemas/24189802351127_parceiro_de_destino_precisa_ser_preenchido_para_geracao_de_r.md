# Parceiro de Destino precisa ser preenchido para geração de Remessa

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24189802351127-Parceiro-de-Destino-precisa-ser-preenchido-para-gera%C3%A7%C3%A3o-de-Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/24189802351127-Parceiro-de-Destino-precisa-ser-preenchido-para-gera%C3%A7%C3%A3o-de-Remessa)  
> **ID:** `24189802351127` | **Última Atualização:** 2026-07-22T14:47:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189802317335)

 **MENSAGEM: **

[CORE_E03217] Parceiro de Destino precisa ser preenchido para geração de Remessa

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189802324375)

 SITUAÇÃO:**

**Explicando o comportamento:** O **parceiro destinatário** é utilizado pelo sistema para preencher o campo **"Parceiro"** no lançamento de remessa gerado. **Seguindo a ordem abaixo**, conforme a configuração utilizada:

**Campo "Gerar se parc. Destinatário preenchido" - marcado:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189753866519)

 Caso tenha **"Parceiro Destinatário" preenchido** ele é **usado** na remessa;

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189753872791)

 Se **não preencher o "Parceiro Destinatário"** no lançamento, o sistema **permite confirmar mas não gera a remessa**, apresenta a mensagem:
Parceiro de Destino precisa ser preenchido para geração de Remessa
Código: CORE_E03217

**Campo "Gerar se parc. Destinatário preenchido" - desmarcado:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189753866519)

 Caso tenha **"Parceiro Destinatário"** preenchido ele é **usado** na remessa;

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189753872791)

 Se não **preencher o "Parceiro Destinatário"** no lançamento, o sistema **usa o parceiro do modelo**;

![3.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189802333975)

 Se **não preencher o "Parceiro Destinatário"** e não tiver "**Parceiro" no modelo** o sistema **não gera a remessa**, apresenta a mensagem:
Parceiro p/gerar Remessa indefinido.
Código: CORE_E03218

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189753884183)

**SOLUÇÃO:**

Observe qual configuração está aplicada: Campo "Gerar se parc. Destinatário preenchido" - **marcado** ou Campo "Gerar se parc. Destinatário preenchido" - **desmarcado**. Em seguida, faça a tratativa de acordo com o comportamento do sistema citado acima. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24189753889559)

**CAUSA:**

Ao tentar gerar uma nota de remessa, tendo as configurações e os dados inseridos em desacordo, a mensagem é apresentada.