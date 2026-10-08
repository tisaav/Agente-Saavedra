# E0291 Rejeição: O endereço nacional do intermediário do serviço não deve ser informado na DPS quando o próprio tomador do serviço for o emitente da DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224192814103-E0291-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-intermedi%C3%A1rio-do-servi%C3%A7o-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-pr%C3%B3prio-tomador-do-servi%C3%A7o-for-o-emitente-da-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224192814103-E0291-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-intermedi%C3%A1rio-do-servi%C3%A7o-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-pr%C3%B3prio-tomador-do-servi%C3%A7o-for-o-emitente-da-DPS)  
> **ID:** `37224192814103` | **Última Atualização:** 2026-07-22T14:16:50Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224192804887)

 **MENSAGEM**

E0291 Rejeição: O endereço nacional do intermediário do serviço não deve ser informado na DPS quando o próprio tomador do serviço for o emitente da DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224177173399)

 **SITUAÇÃO**

Mensagem apresentada ao tentar emitir uma **DPS (Documento de Prestação de Serviços)** quando o **tomador do serviço é o próprio emitente** do documento e foram informados dados de endereço nacional do intermediário do serviço.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224192807191)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224192807703)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224177176599)

 Na grade** ''Cabeçalho''**, nos campos **''Empresa''** e **''Parceiro''**, verifique se o tomador de serviço informado é o mesmo que o emitente do documento.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224192809367)

 Caso o tomador seja o próprio emitente, **não preencha** as informações de **endereço nacional do intermediário** do serviço.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224192811159)

 Remova os dados de endereço do intermediário que foram informados indevidamente, incluindo:

- 

**CEP**

- 

**Logradouro**

- 

**Número**

- 

**Complemento**

- 

**Bairro**

- 

**Município**

- 

**UF**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38196047820311)

 Após remover as informações do intermediário, **salve as alterações** e tente emitir novamente a DPS.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224177179543)

 **CAUSA**

Esta rejeição ocorre quando, na emissão de uma **DPS**, o **tomador do serviço é identificado como o próprio emitente** do documento e, ao mesmo tempo, são informados **dados de endereço nacional do intermediário** do serviço. Conforme as **regras de validação da Sefaz** estabelecidas pela **Lei Complementar nº 214/2025**, quando o tomador e o emitente são a mesma entidade, **não deve haver intermediário** na operação, portanto, o preenchimento do endereço do intermediário é indevido e gera a rejeição do documento.