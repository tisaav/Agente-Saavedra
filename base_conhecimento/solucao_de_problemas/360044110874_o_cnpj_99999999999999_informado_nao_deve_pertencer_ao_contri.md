# O CNPJ '99999999999999' informado não deve pertencer ao contribuinte declarante

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110874-O-CNPJ-99999999999999-informado-n%C3%A3o-deve-pertencer-ao-contribuinte-declarante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110874-O-CNPJ-99999999999999-informado-n%C3%A3o-deve-pertencer-ao-contribuinte-declarante)  
> **ID:** `360044110874` | **Última Atualização:** 2026-07-22T15:52:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416242793495)

 MENSAGEM:**

Erro MS1029 - O CNPJ '99999999999999' informado não deve pertencer ao contribuinte declarante. Localização: - Campo: cnpjPrestador - XPATH: /Reinf/evtServTom/infoServTom/ideEstabObra/idePrestServ/cnpjPrestador

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416242796695)

 SITUAÇÃO:**

Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416242800023)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416242802327)

 Identifique dentre as notas de prestação de serviços registradas, os parceiros utilizados. Caso no cadastro do parceiro o CNPJ seja igual ao da empresa declarante da nota de prestação, o mesmo deverá ser ajustado ou substituído por um outro parceiro que não seja o da empresa declarante.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416264771351)

 Após os ajustes, gere os movimentos e envie novamente os eventos.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416242807191)

 CAUSA:**

Problema ocorre devido ao CNPJ do parceiro informado na nota de prestação de serviços ser o mesmo CNPJ da empresa que tomou o serviço.