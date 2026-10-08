# E0232 Rejeição: IM do tomador não deve ser informado, pois não existem informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222824324631-E0232-Rejei%C3%A7%C3%A3o-IM-do-tomador-n%C3%A3o-deve-ser-informado-pois-n%C3%A3o-existem-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222824324631-E0232-Rejei%C3%A7%C3%A3o-IM-do-tomador-n%C3%A3o-deve-ser-informado-pois-n%C3%A3o-existem-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS)  
> **ID:** `37222824324631` | **Última Atualização:** 2026-07-22T14:17:22Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222809440535)

 **MENSAGEM**

E0232 Rejeição: IM do tomador não deve ser informado, pois não existem informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222824308375)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)**, o usuário informou a **Inscrição Municipal (IM) do tomador** do serviço no cadastro do parceiro. Porém, ao transmitir a nota, o sistema retornou a rejeição acima, indicando que a IM não deveria ter sido informada, pois **não existem informações complementares** registradas no **CNC NFS-e (Cadastro Nacional de Contribuintes)** do município emissor para aquele tomador.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222824309783)

 **SOLUÇÃO**

Para resolver esta rejeição, remova a **Inscrição Municipal (IM)** do cadastro do tomador do serviço antes de emitir a NFS-e. Siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222824310167)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222809444119)

 Localize e selecione o **parceiro tomador do serviço** que está apresentando a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222809444887)

 Na aba **''Identificação''**, verifique o campo ''Cad.Mun.Contribuintes'' e remova o valor informado, deiaxando o campo em branco.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222809446167)

 Salve as alterações.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222809447063)

 Retorne à tela de emissão da **NFS-e** e realize novamente a **transmissão da nota**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222809448471)

 **CAUSA**

A rejeição ocorre porque a **Inscrição Municipal (IM) do tomador** foi informada na DPS (Declaração de Prestação de Serviços), porém **não existem informações complementares** deste contribuinte registradas no **CNC NFS-e do município emissor**. A SEFAZ valida se o tomador possui cadastro complementar no município e, caso não possua, a IM não deve ser preenchida no documento fiscal. Esta validação garante a **consistência dos dados** entre o cadastro municipal e as informações declaradas na nota fiscal de serviços.