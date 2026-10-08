# E0281 Rejeição: O NIF ou cNaoNIF do intermediário deve ser informado quando o grupo de informações de endereço no exterior do intermediário de serviços foi informado.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223202875287-E0281-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-intermedi%C3%A1rio-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-intermedi%C3%A1rio-de-servi%C3%A7os-foi-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223202875287-E0281-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-intermedi%C3%A1rio-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-intermedi%C3%A1rio-de-servi%C3%A7os-foi-informado)  
> **ID:** `37223202875287` | **Última Atualização:** 2026-07-22T14:16:57Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223202864279)

 **MENSAGEM**

E0281 Rejeição: O NIF ou cNaoNIF do intermediário deve ser informado quando o grupo de informações de endereço no exterior do intermediário de serviços foi informado.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223217801879)

 **SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** com intermediário de serviços estrangeiro, o usuário informou o **endereço no exterior do intermediário**, porém **não preencheu o NIF** (Número de Identificação Fiscal) ou o **código de não preenchimento do NIF** (cNaoNIF) do intermediário. Com isso, a nota fiscal foi rejeitada pela Sefaz com a mensagem de erro E0281.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223217804567)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223202865943)

 Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223217805591)

 Localize o cadastro do interdiário estrangeiro utilizado na operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223217806615)

 Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o número do passaporte ou documento estrangeiro do intermediário.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223202870167)

 Caso o intermediário possua **NIF** (Número de Identificação Fiscal no país de residência), informe este número no campo apropriado do cadastro.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223217809175)

 Caso o intermediário **não possua NIF**, informe o **código de não preenchimento do NIF** (cNaoNIF) conforme as opções disponíveis: 

- 

**''1 - Dispensado do NIF''**

- 

**''2 - Não obrigado a inscrição''**

- 

**''3 - Outros''**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223202871831)

 Salve as alterações realizadas no cadastro do parceiro.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37784833053591)

 Retorne à **NF-e** ou **NFC-e** que apresentou a rejeição e realize um **novo lançamento** do documento fiscal. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223202872599)

 **CAUSA**

A rejeição ocorre quando é emitida uma **NF-e** ou **NFC-e** com **intermediário de serviços estrangeiro** e o sistema identifica que foi informado o **grupo de endereço no exterior do intermediário**, porém **não foi preenchido o NIF** (Número de Identificação Fiscal) ou o **código de não preenchimento do NIF** (cNaoNIF). Conforme as regras de validação da Sefaz, quando há informações de endereço no exterior do intermediário, é **obrigatório informar o NIF ou justificar sua ausência** através do código cNaoNIF, garantindo a correta identificação fiscal do intermediário estrangeiro na operação.