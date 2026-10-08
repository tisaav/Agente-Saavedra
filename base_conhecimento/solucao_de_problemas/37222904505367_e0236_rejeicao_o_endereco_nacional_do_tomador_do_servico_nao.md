# E0236 Rejeição: O endereço nacional do tomador do serviço não deve ser informado na DPS quando o próprio tomador do serviço for o emitente da DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222904505367-E0236-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-tomador-do-servi%C3%A7o-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-pr%C3%B3prio-tomador-do-servi%C3%A7o-for-o-emitente-da-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222904505367-E0236-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-tomador-do-servi%C3%A7o-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-pr%C3%B3prio-tomador-do-servi%C3%A7o-for-o-emitente-da-DPS)  
> **ID:** `37222904505367` | **Última Atualização:** 2026-07-22T14:17:15Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222885934103)

 **MENSAGEM**

E0236 Rejeição: O endereço nacional do tomador do serviço não deve ser informado na DPS quando o próprio tomador do serviço for o emitente da DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222885934999)

 **SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviço (DPS)**, o usuário informou os **dados de endereço nacional do tomador do serviço**, sendo que o **próprio emitente da DPS é o tomador do serviço**. Nesta situação, a SEFAZ rejeitou o documento com a mensagem E0236.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222870937751)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222870940439)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222885938967)

 Na grade **''Cabeçalho''**, verifque se o campo **''Parceiro'' (Tomador de Serviço)**, está preenchido com a mesma empresa emitente da DPS.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222885941143)

 **Remova as informações de endereço nacional** do tomador do serviço, uma vez que estes dados **não devem ser informados** quando o tomador for o próprio emitente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222885941655)

 Realize novamente a **transmissão da DPS** para a SEFAZ. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222885942295)

 **CAUSA**

A rejeição ocorre porque a **regra de validação da SEFAZ** determina que, quando o **tomador do serviço for o próprio emitente da DPS**, os **dados de endereço nacional do tomador não devem ser informados** no documento fiscal. Esta validação visa **evitar redundância de informações**, uma vez que os dados do emitente já constam no documento. Ao preencher o endereço do tomador nesta situação, o sistema identifica a **inconsistência** e rejeita a DPS com a mensagem E0236.