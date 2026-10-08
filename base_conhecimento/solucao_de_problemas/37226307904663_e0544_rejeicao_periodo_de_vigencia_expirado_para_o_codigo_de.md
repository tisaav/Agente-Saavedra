# E0544 Rejeição: Período de vigência expirado para o código de identificação do Benefício Municipal no município de incidência do ISSQN para a data de competência informada na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226307904663-E0544-Rejei%C3%A7%C3%A3o-Per%C3%ADodo-de-vig%C3%AAncia-expirado-para-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-no-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-para-a-data-de-compet%C3%AAncia-informada-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226307904663-E0544-Rejei%C3%A7%C3%A3o-Per%C3%ADodo-de-vig%C3%AAncia-expirado-para-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-no-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-para-a-data-de-compet%C3%AAncia-informada-na-DPS)  
> **ID:** `37226307904663` | **Última Atualização:** 2026-07-22T14:15:06Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226291253015)

 **MENSAGEM**

E0544 Rejeição: Período de vigência expirado para o código de identificação do Benefício Municipal no município de incidência do ISSQN para a data de competência informada na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226307890071)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** ou enviar um **RPS (Recibo Provisório de Serviços)** para conversão, o documento é **rejeitado pela prefeitura** com a mensagem de erro E0544, indicando que o **código do benefício municipal informado está com o período de vigência expirado** para a data de competência utilizada.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226307890711)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226291256471)

 Verifique junto à **prefeitura do município** qual é o **código de benefício fiscal municipal vigente** para a data de competência da nota fiscal que está sendo emitida.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226291257751)

 Acesse a tela **"Serviços"** (Configurações » Cadastros » Produtos » Serviço) e localize o **serviço utilizado** na nota fiscal rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38295029879831)

 Na aba **''Impostos''**, verifique o campo **"Cód. Trib. Município NFS-e" **e confirme se:

- 

O código informado está **correto e atualizado** conforme orientação da prefeitura;

- 

O **período de vigência** do código abrange a **data de competência** da nota fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226291259287)

 Caso o código esteja **expirado ou incorreto**, atualize o campo com o código vigente fornecido pela prefeitura.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226291259927)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226291260183)

 Retorne à tela de emissão da **NFS-e** e **gere novamente** o documento fiscal com as informações atualizadas.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226291260823)

 Caso a rejeição persista, entre em contato com a **administração pública municipal** para validar se há alguma **restrição adicional** ou atualização necessária no cadastro do benefício fiscal.
 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226307900695)

 **CAUSA**

A rejeição ocorre quando o **código de identificação do benefício fiscal municipal** informado no cadastro do serviço está com o **período de vigência expirado** em relação à **data de competência** utilizada na emissão da NFS-e ou no RPS. Isso acontece porque as prefeituras estabelecem **períodos específicos de validade** para cada código de benefício, e ao tentar emitir uma nota com data de competência **fora desse período**, o sistema municipal rejeita o documento automaticamente.