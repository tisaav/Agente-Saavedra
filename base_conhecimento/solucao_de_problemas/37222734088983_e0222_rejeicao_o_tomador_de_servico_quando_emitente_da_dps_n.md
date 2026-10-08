# E0222 Rejeição: O tomador de serviço, quando emitente da DPS, não pode ser identificado pelo NIF.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222734088983-E0222-Rejei%C3%A7%C3%A3o-O-tomador-de-servi%C3%A7o-quando-emitente-da-DPS-n%C3%A3o-pode-ser-identificado-pelo-NIF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222734088983-E0222-Rejei%C3%A7%C3%A3o-O-tomador-de-servi%C3%A7o-quando-emitente-da-DPS-n%C3%A3o-pode-ser-identificado-pelo-NIF)  
> **ID:** `37222734088983` | **Última Atualização:** 2026-07-22T14:17:31Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222749957527)

 **MENSAGEM**

E0222 Rejeição: O tomador de serviço, quando emitente da DPS, não pode ser identificado pelo NIF.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222749958551)

 **SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)**, o usuário configurou o **tomador do serviço** como sendo a própria **empresa emitente** do documento. No entanto, no **cadastro deste parceiro**, o campo **"Identificação de Estrangeiro"** foi preenchido com a opção **"NIF"** (Número de Identificação Fiscal). Ao tentar transmitir o documento para a SEFAZ, a nota foi **rejeitada** com a mensagem de erro E0222.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222734077591)

 **SOLUÇÃO**

Para resolver esta rejeição, é necessário **ajustar o cadastro do parceiro** que está configurado como tomador do serviço. Siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222749960983)

  Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222734079511)

  Localize e selecione o **parceiro** que está configurado como **tomador do serviço** na DPS rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222749963927)

  Acesse a aba **"Identificação"** do cadastro do parceiro.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222749964695)

  Verifique o preenchimento do campo **"Identificação de Estrangeiro"**: 

- 

Se o tomador for uma **pessoa jurídica brasileira**, certifique-se de que este campo esteja **vazio** ou preenchido com **CNPJ válido**.

- 

Se o tomador for uma **pessoa física brasileira**, certifique-se de que este campo esteja **vazio** ou preenchido com **CPF válido**.

- 

**Remova** a identificação **"NIF"** do campo **"Identificação de Estrangeiro"**, pois quando o tomador é o próprio emitente da DPS, não é permitido utilizar identificação de estrangeiro.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222734081303)

  Salve as alterações realizadas no cadastro do parceiro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222749966487)

  Retorne ao **documento fiscal** e realize uma nova tentativa de **transmissão** para a SEFAZ. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222749967127)

 **CAUSA**

A rejeição ocorre porque a **SEFAZ não permite** que o **tomador do serviço**, quando for o **próprio emitente da DPS**, seja identificado por meio de **NIF (Número de Identificação Fiscal de estrangeiro)**. Esta validação garante que **empresas brasileiras** emitindo documentos fiscais em seu próprio nome utilizem apenas **identificações nacionais válidas**, como CNPJ ou CPF, mantendo a **conformidade fiscal** e a **integridade dos dados** no sistema tributário nacional.