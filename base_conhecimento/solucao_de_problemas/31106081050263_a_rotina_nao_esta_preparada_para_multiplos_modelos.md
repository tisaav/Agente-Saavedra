# A rotina não está preparada para múltiplos modelos

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31106081050263-A-rotina-n%C3%A3o-est%C3%A1-preparada-para-m%C3%BAltiplos-modelos](https://ajuda.sankhya.com.br/hc/pt-br/articles/31106081050263-A-rotina-n%C3%A3o-est%C3%A1-preparada-para-m%C3%BAltiplos-modelos)  
> **ID:** `31106081050263` | **Última Atualização:** 2026-07-30T11:48:00Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31106081046679)

 **MENSAGEM:**

[CORE_E05182] A rotina não está preparada para múltiplos modelos.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31286331513367)

 SITUAÇÃO:**

Esse erro pode causar o não envio do PDF da NFS-e no envio automático de e-mails. Nessa situação, o sistema encaminha apenas o XML e o boleto, sem anexar o PDF da nota fiscal.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31106081047447)

SOLUÇÃO:**

Este erro ocorre devido a uma configuração inadequada na TOP, especificamente na aba **"E-mails da TOP"**. Quando são atribuídos dois modelos diferentes simultaneamente, o sistema não consegue processar corretamente o envio de e-mails, resultando nesse erro.

Para corrigir o problema, siga os passos abaixo:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31291124328471)

 Verifique a configuração da TOP:**

- 

  - 

Acesse a aba **"E-mails da TOP"** e verifique se há mais de um modelo configurado.

  - 

Caso existam dois modelos atribuídos (por exemplo, um modelo de nota e um modelo de boleto), remova um deles, deixando apenas o necessário para o envio correto.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31291124330647)

 Teste o envio manualmente:**

- 

  - 

Utilize a opção **"Outras opções" > "Enviar e-mails com seleção de destinatário"**, localizada no **"Portal de vendas"**.

  - 

Caso o erro ocorra, ajuste as configurações conforme necessário e teste novamente

Após realizar esses ajustes, o sistema deverá encaminhar os e-mails corretamente. O XML e o boleto da nota serão enviados em um e-mail, enquanto o PDF e o boleto serão enviados em outro.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31106106648983)

CAUSA:**

O erro ocorre porque a rotina não suporta múltiplos modelos configurados simultaneamente na aba E-mails da TOP. Quando essa configuração indevida está presente, o envio automático pode falhar sem exibir mensagens de erro, impedindo o envio do PDF corretamente. Ajustar a configuração da TOP para conter apenas um modelo por vez resolve o problema e permite que os e-mails sejam enviados corretamente.