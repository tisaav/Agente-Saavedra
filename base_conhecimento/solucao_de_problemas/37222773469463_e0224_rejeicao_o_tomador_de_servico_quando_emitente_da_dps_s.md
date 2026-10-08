# E0224 Rejeição: O tomador de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222773469463-E0224-Rejei%C3%A7%C3%A3o-O-tomador-de-servi%C3%A7o-quando-emitente-da-DPS-somente-pode-ser-identificado-pelo-CNPJ-ou-CPF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222773469463-E0224-Rejei%C3%A7%C3%A3o-O-tomador-de-servi%C3%A7o-quando-emitente-da-DPS-somente-pode-ser-identificado-pelo-CNPJ-ou-CPF)  
> **ID:** `37222773469463` | **Última Atualização:** 2026-07-22T14:17:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222773436439)

 **MENSAGEM**

E0224 Rejeição: O tomador de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222789571351)

 **SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)** em que a própria empresa é o **tomador do serviço**, o sistema identifica que o tomador foi preenchido com informações diferentes de **CNPJ ou CPF**, como por exemplo, utilizando o campo **"Identificação de Estrangeiro"**. Nesta situação, a Sefaz rejeita o documento com a mensagem E0224.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222773444759)

 **SOLUÇÃO**

Para corrigir a rejeição E0224, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222789578391)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222773448599)

 Localize e selecione o **parceiro** que está cadastrado como **tomador do serviço** no DPS rejeitado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222773449623)

 Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222789581079)

 Caso o tomador seja uma **pessoa jurídica brasileira**, certifique-se de que o campo **"CNPJ / CPF"** esteja corretamente preenchido e remova qualquer informação do campo "Identificação de Estrangeiro".

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222773452567)

 Caso o tomador seja uma **pessoa física brasileira**, certifique-se de que o campo **"CNPJ / CPF"** esteja corretamente preenchido e remova qualquer informação do campo "Identificação de Estrangeiro".

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222789583511)

 Salve as alterações realizadas no cadastro do parceiro.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222773460887)

 Retorne ao **DPS** e atualize os dados do tomador, ou exclua o documento e emita novamente com as informações corretas.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222773461783)

 **CAUSA**

A rejeição ocorre porque a **Sefaz exige** que, quando a empresa emitente do DPS for também o **tomador do serviço**, este deve ser identificado exclusivamente por **CNPJ ou CPF**. A utilização de outros tipos de identificação, como o campo **"Identificação de Estrangeiro"**, não é permitida neste cenário, resultando na rejeição do documento fiscal.