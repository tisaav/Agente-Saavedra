# 745 Rejeição: O tipo de transportador não pode ser informado quando não estiver informado proprietário do veículo de tração

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35122715417623-745-Rejei%C3%A7%C3%A3o-O-tipo-de-transportador-n%C3%A3o-pode-ser-informado-quando-n%C3%A3o-estiver-informado-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/35122715417623-745-Rejei%C3%A7%C3%A3o-O-tipo-de-transportador-n%C3%A3o-pode-ser-informado-quando-n%C3%A3o-estiver-informado-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o)  
> **ID:** `35122715417623` | **Última Atualização:** 2026-07-22T14:25:59Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35122715401623)

 **MENSAGEM**

745 Rejeição: O tipo de transportador não pode ser informado quando não estiver informado proprietário do veículo de tração

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35712523739415)

 **SITUAÇÃO**

Ao emitir um MDF-e (modelo 58) com modal rodoviário, o usuário preencheu o campo **"Tipo de Transportador"** sem informar o grupo **"Proprietário do Veículo de Tração"**. A mensagem de rejeição foi apresentada durante a validação do documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35122725604759)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35712523740567)

  Quando for emitido um **MDF-e cujo o veículo informado seja de propriedade da empresa emitente** **do MDF-e**, não poderá ser gerado a TAG: <tpTransp>. Para isso, acesse a tela **"Veículos"** (Configurações » Cadastros » Veículos), na aba **"Propriedades"**, marque a opção **"Veículo da empresa"** se o veículo for de propriedade da empresa emitente.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35712533177239)

  Caso o **veículo não seja da empresa emitente**, desmarque a opção **"Veículo da empresa"** e preencha o campo **"Parceiro ou Empresa"**.
 

![745 Rejeição O tipo de transportador não pode ser informado quando 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/35712533179287)

 

**Observação:** caso seja preciso, para gerar o grupo de Tag **<prop>**, o veículo não pode ser da empresa emitente. Neste caso, desabilite o campo **"Veículo da empresa"** e preencha **"Parceiro ou Empresa"**.

 

![745 Rejeição O tipo de transportador não pode ser informado quando 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/35712533179799)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35122725610775)

 **CAUSA**

A rejeição ocorre quando, ao emitir um MDF-e (modelo 58) com modal rodoviário, o campo **"Tipo de Transportador"** é preenchido sem informar o grupo **"Proprietário do Veículo de Tração"** (**Tag: prop**). O sistema exige que, para informar o tipo de transportador, o proprietário do veículo de tração também seja informado.