# E0113 Rejeição: O NIF ou cNaoNIF do prestador deve ser informado quando o grupo de informações de endereço no exterior do prestador de serviços foi informado.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222053575575-E0113-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-prestador-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-prestador-de-servi%C3%A7os-foi-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222053575575-E0113-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-prestador-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-prestador-de-servi%C3%A7os-foi-informado)  
> **ID:** `37222053575575` | **Última Atualização:** 2026-07-22T14:18:09Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222053563415)

 **MENSAGEM**

E0113 Rejeição: O NIF ou cNaoNIF do prestador deve ser informado quando o grupo de informações de endereço no exterior do prestador de serviços foi informado.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222069418391)

 **SITUAÇÃO**

Ao emitir uma **NF-e ou NFC-e** com prestador de serviços residente no exterior, onde foram informados os **dados de endereço no exterior** do prestador, mas **não foi preenchido o NIF** (Número de Identificação Fiscal) ou o **código de não preenchimento do NIF** (cNaoNIF), o sistema apresenta a rejeição.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222069421207)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222069425559)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **cadastro do prestador de serviços** residente no exterior.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222053565847)

 Na aba **"Identificação"**, localize o campo **"Identificação de Estrangeiro"** e verifique se está preenchido.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222053566743)

 Na aba **"Fiscal"**, localize a seção **"Informações para REINF"** e preencha uma das seguintes informações: 

- 

**"Nro. do NIF - Número de Identificação Fiscal''**: informe o número de identificação fiscal do prestador no país de residência, quando disponível.

- 

**"Indicativo do NIF"** (cNaoNIF): selecione o código apropriado quando o NIF não puder ser informado, conforme as opções disponíveis no sistema.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222069432855)

 Certifique-se de que o **endereço no exterior** do prestador esteja corretamente preenchido na aba **"Endereços"**, com a **UF** configurada como **"EX"** (Exterior).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222053567895)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222069435287)

 Realize um **novo lançamento** da NF-e ou NFC-e e tente transmitir o documento novamente. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222053571735)

 **CAUSA**

A rejeição ocorre quando o documento fiscal contém o **grupo de informações de endereço no exterior do prestador de serviços**, mas **não foi informado o NIF** (Número de Identificação Fiscal) ou o **código de não preenchimento do NIF** (cNaoNIF). Conforme as regras de validação da Sefaz, quando há endereço no exterior informado, é **obrigatório** preencher pelo menos uma dessas informações para identificação fiscal do prestador estrangeiro.