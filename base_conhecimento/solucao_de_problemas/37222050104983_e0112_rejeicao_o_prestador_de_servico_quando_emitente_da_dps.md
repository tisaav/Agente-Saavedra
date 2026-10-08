# E0112 Rejeição: O prestador de serviço, quando emitente da DPS, não pode ser identificado pelo NIF.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222050104983-E0112-Rejei%C3%A7%C3%A3o-O-prestador-de-servi%C3%A7o-quando-emitente-da-DPS-n%C3%A3o-pode-ser-identificado-pelo-NIF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222050104983-E0112-Rejei%C3%A7%C3%A3o-O-prestador-de-servi%C3%A7o-quando-emitente-da-DPS-n%C3%A3o-pode-ser-identificado-pelo-NIF)  
> **ID:** `37222050104983` | **Última Atualização:** 2026-07-22T14:18:10Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222050087319)

 **MENSAGEM**

E0112 Rejeição: O prestador de serviço, quando emitente da DPS, não pode ser identificado pelo NIF.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222065962903)

 **SITUAÇÃO**

Ao emitir uma **DPS (Documento de Prestação de Serviços)** na qual a empresa emitente é o **prestador de serviço**, o sistema identificou que o prestador foi cadastrado utilizando **NIF (Número de Identificação Fiscal)** ao invés de **CNPJ ou CPF**. Neste cenário, a **Sefaz rejeitou o documento** com a mensagem E0112.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222065966231)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222065967255)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222050092823)

 Localize e selecione a **empresa emitente da DPS** que está atuando como prestadora de serviço.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222050096407)

 Verifique o campo de **identificação fiscal** da empresa e certifique-se de que está preenchido com **CNPJ** (para pessoa jurídica) ou **CPF** (para pessoa física).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222050097431)

 Caso o campo esteja preenchido com **NIF**, substitua pela **identificação fiscal brasileira válida** (CNPJ ou CPF).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37833743645847)

 Salve as alterações realizadas no cadastro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222050101143)

 Retorne à tela de **emissão da DPS** e gere novamente o documento fiscal. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222065975191)

 **CAUSA**

A rejeição ocorre porque, de acordo com as **regras de validação da Sefaz** estabelecidas pela **Reforma Tributária (Lei Complementar nº 214/2025)**, quando o **prestador de serviço é o emitente da DPS**, ele deve ser identificado obrigatoriamente por **CNPJ ou CPF**. A utilização de **NIF (Número de Identificação Fiscal estrangeiro)** não é permitida neste contexto, pois o prestador emitente deve possuir **identificação fiscal brasileira válida**. O sistema valida essa informação no momento da transmissão do documento e, ao detectar o uso de NIF, a Sefaz rejeita automaticamente a DPS com a mensagem E0112.