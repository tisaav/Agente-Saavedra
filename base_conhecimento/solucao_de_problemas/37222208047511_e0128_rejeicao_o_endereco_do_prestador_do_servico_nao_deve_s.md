# E0128 Rejeição: O endereço do prestador do serviço não deve ser informado na DPS quando o próprio prestador for o emitente da DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222208047511-E0128-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-do-prestador-do-servi%C3%A7o-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-pr%C3%B3prio-prestador-for-o-emitente-da-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222208047511-E0128-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-do-prestador-do-servi%C3%A7o-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-pr%C3%B3prio-prestador-for-o-emitente-da-DPS)  
> **ID:** `37222208047511` | **Última Atualização:** 2026-07-22T14:17:58Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222208037399)

 **MENSAGEM**

E0128 Rejeição: O endereço do prestador do serviço não deve ser informado na DPS quando o próprio prestador for o emitente da DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222208038423)

 **SITUAÇÃO**

Mensagem apresentada ao emitir uma **DPS (Documento de Prestação de Serviços)** em que o **prestador do serviço é o próprio emitente** do documento fiscal, mas foram informados dados de endereço do prestador no grupo específico destinado a essa finalidade.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222223023255)

 **SOLUÇÃO**

Para resolver esta rejeição, **não informe o endereço do prestador** no grupo específico da DPS quando o prestador for o próprio emitente do documento:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222208040599)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222223024791)

 Verifique se o **prestador do serviço** informado no documento é o **mesmo emitente da DPS**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222208042007)

 Certifique-se de que o **grupo de endereço do prestador** não esteja preenchido na DPS, pois quando o prestador é o próprio emitente, **essas informações não devem ser informadas**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222223026711)

 Remova qualquer informação de endereço do prestador que tenha sido preenchida indevidamente.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222208043799)

 Salve as alterações e tente emitir novamente a DPS.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222223031063)

 **CAUSA**

A rejeição ocorre porque, de acordo com as **regras de validação da Sefaz** estabelecidas pela **Lei Complementar nº 214/2025** (Reforma Tributária), quando o **prestador do serviço é o próprio emitente da DPS**, o grupo de informações de endereço do prestador **não deve ser preenchido** no documento fiscal. Isso acontece porque os dados do emitente já constam no cabeçalho do documento, tornando **redundante e incorreta** a inclusão dessas informações novamente no grupo específico do prestador. A validação visa garantir a **consistência e integridade** dos dados transmitidos à Sefaz.