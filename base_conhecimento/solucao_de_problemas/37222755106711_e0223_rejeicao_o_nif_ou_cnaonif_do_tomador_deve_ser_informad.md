# E0223 Rejeição: O NIF ou cNaoNIF do tomador deve ser informado quando o grupo de informações de endereço no exterior do tomador de serviços foi informado.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222755106711-E0223-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-tomador-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-tomador-de-servi%C3%A7os-foi-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222755106711-E0223-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-tomador-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-tomador-de-servi%C3%A7os-foi-informado)  
> **ID:** `37222755106711` | **Última Atualização:** 2026-07-22T14:17:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222740058007)

 **MENSAGEM**

E0223 Rejeição: O NIF ou cNaoNIF do tomador deve ser informado quando o grupo de informações de endereço no exterior do tomador de serviços foi informado.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222755093399)

 **SITUAÇÃO**

Ao tentar emitir uma **NFS-e** para um **tomador de serviços localizado no exterior**, o sistema apresenta a rejeição E0223, indicando que as informações de identificação fiscal do tomador estrangeiro não foram preenchidas corretamente no cadastro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222755094423)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222740061975)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **tomador de serviços estrangeiro**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222740062999)

 Na aba **"Identificação"**, verifique se o campo **"País"** está preenchido com um país diferente do Brasil, confirmando que se trata de um parceiro do exterior.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222755097111)

 Na aba **"Fiscal"**, localize e preencha obrigatoriamente um dos seguintes campos: 

- 

**"Nro. do NIF - Número de Identificação Fiscal''**: informe o número de identificação fiscal do tomador no país de origem, quando disponível;

- 

**"Indicativo do NIF"**: caso o tomador não possua NIF, selecione o código apropriado que justifique a ausência do número de identificação fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222755098007)

 Certifique-se de que o **endereço do tomador** esteja corretamente preenchido com as informações do país de origem, incluindo cidade e país.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222755099543)

 Salve as alterações realizadas no cadastro do parceiro.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222740065943)

 Retorne à **NFS-e** e realize um novo lançamento ou gere novamente o lote da nota fiscal. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222755101463)

 **CAUSA**

A rejeição ocorre porque a **Sefaz exige** que, quando o tomador de serviços possui **endereço no exterior**, seja informado obrigatoriamente o **NIF** (Número de Identificação Fiscal) ou o **código que justifique a ausência do NIF** (cNaoNIF). Esta validação garante a **correta identificação fiscal** do tomador estrangeiro para fins de tributação e controle fiscal das operações internacionais.