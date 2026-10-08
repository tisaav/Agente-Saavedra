# E0280 Rejeição: O intermediário de serviço, quando emitente da DPS, não pode ser identificado pelo NIF.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223163734167-E0280-Rejei%C3%A7%C3%A3o-O-intermedi%C3%A1rio-de-servi%C3%A7o-quando-emitente-da-DPS-n%C3%A3o-pode-ser-identificado-pelo-NIF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223163734167-E0280-Rejei%C3%A7%C3%A3o-O-intermedi%C3%A1rio-de-servi%C3%A7o-quando-emitente-da-DPS-n%C3%A3o-pode-ser-identificado-pelo-NIF)  
> **ID:** `37223163734167` | **Última Atualização:** 2026-07-22T14:16:58Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223199005719)

 **MENSAGEM**

E0280 Rejeição: O intermediário de serviço, quando emitente da DPS, não pode ser identificado pelo NIF.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223199008023)

 **SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)**, o usuário configurou a empresa emitente como **intermediária do serviço** e, no cadastro desta empresa, preencheu o campo **"Identificação de Estrangeiro"** com o código **"NIF"** (Número de Identificação Fiscal). Durante a validação do documento pela Sefaz, a rejeição foi apresentada, pois o intermediário de serviço, quando é o próprio emitente da DPS, não pode ser identificado pelo NIF.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223163714199)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223163714967)

 Acesse a tela **''Empresas''** (Configurações » Cadastros » Empresas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223199010583)

 Localize o cadastro da empresa emitente do DPS que está atuando como intermediária do serviço.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223199013143)

 Na aba **"Identificação"**, verifique o campo **"Identificação de Estrangeiro"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223199016087)

 Caso o campo esteja preenchido com **"NIF"**, remova esta informação ou altere para um tipo de identificação válido, conforme a legislação vigente. O intermediário de serviço, quando emitente da DPS, **não pode ser identificado pelo NIF**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223199017111)

 Salve as alterações realizadas no cadastro da empresa.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37784947222167)

 Emita novamente o **Documento de Prestação de Serviços (DPS)** e transmita para a Sefaz. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223199017751)

 **CAUSA**

A rejeição ocorre quando o **intermediário de serviço**, sendo o próprio **emitente da DPS**, possui o campo **"Identificação de Estrangeiro"** preenchido com o código **"NIF"** no cadastro da empresa. Conforme as regras de validação da Sefaz estabelecidas pela **Lei Complementar nº 214/2025**, o intermediário de serviço, quando emitente do documento, **não pode ser identificado pelo NIF**, devendo utilizar outros tipos de identificação fiscal válidos no território nacional.