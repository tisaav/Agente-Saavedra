# E0710 Rejeição: Para MEI pTotTribSN nunca poderá ser informado

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37228348906135-E0710-Rejei%C3%A7%C3%A3o-Para-MEI-pTotTribSN-nunca-poder%C3%A1-ser-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37228348906135-E0710-Rejei%C3%A7%C3%A3o-Para-MEI-pTotTribSN-nunca-poder%C3%A1-ser-informado)  
> **ID:** `37228348906135` | **Última Atualização:** 2026-09-18T19:33:15Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228302186263)

 **MENSAGEM**

E0710 Rejeição: Para MEI pTotTribSN nunca poderá ser informado.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228302187671)

 **SITUAÇÃO**

Ao emitir uma **NFS-e **para um destinatário cadastrado como **Microempreendedor Individual (MEI)**, o sistema preencheu automaticamente o campo **pTotTribSN** (valor aproximado total de tributos do Simples Nacional) no documento fiscal. Ao tentar transmitir o documento eletrônico, a **SEFAZ rejeitou a nota** com a mensagem de erro E0710.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228302188823)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228302189719)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348897559)

 Localize o destinatário da nota fiscal que foi rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37609065453079)

 Na aba **''Fiscal''**, verifique se o parceiro está com a marcação **''Micro empresário individual''** está habilitada.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228302193943)

 Confirme se o cadastro do parceiro está correto:

- 

Se o destinatário **realmente é MEI**, mantenha a marcação habilitada e prossiga para o próximo passo.

- 

Se o destinatário **não é MEI**, desabilite a marcação **"Micro empresário individual"** e salve o cadastro.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228302195095)

 Caso o destinatário seja MEI, verifique a **configuração tributária** utilizada na emissão do documento fiscal e certifique-se de que **não está sendo calculado ou informado o valor aproximado de tributos** (pTotTribSN) para este tipo de contribuinte.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348901015)

 Cancele a nota fiscal rejeitada e **emita novamente o documento**, garantindo que o campo **pTotTribSN não seja preenchido** quando o destinatário for MEI.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37609088841623)

 Transmita o documento fiscal novamente para a SEFAZ.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37228348903191)

 **CAUSA**

A rejeição ocorre porque, de acordo com a **legislação fiscal**, o **Microempreendedor Individual (MEI)** possui um regime tributário diferenciado e simplificado. Por essa razão, **não é permitido informar o valor aproximado de tributos do Simples Nacional (pTotTribSN)** em documentos fiscais destinados a MEI. Quando o sistema identifica que o destinatário é MEI e o campo pTotTribSN está preenchido, a **SEFAZ rejeita automaticamente** o documento com a mensagem E0710.