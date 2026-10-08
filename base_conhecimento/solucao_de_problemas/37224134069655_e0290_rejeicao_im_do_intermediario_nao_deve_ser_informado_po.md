# E0290 Rejeição: IM do intermediário não deve ser informado, pois não existem informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224134069655-E0290-Rejei%C3%A7%C3%A3o-IM-do-intermedi%C3%A1rio-n%C3%A3o-deve-ser-informado-pois-n%C3%A3o-existem-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224134069655-E0290-Rejei%C3%A7%C3%A3o-IM-do-intermedi%C3%A1rio-n%C3%A3o-deve-ser-informado-pois-n%C3%A3o-existem-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS)  
> **ID:** `37224134069655` | **Última Atualização:** 2026-07-22T14:16:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224118365719)

 **MENSAGEM**

E0290 Rejeição: IM do intermediário não deve ser informado, pois não existem informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224134053911)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)**, o usuário preencheu as **informações do intermediador** da operação, incluindo a **Inscrição Municipal (IM)** do intermediário. Porém, o **município emissor informado na DPS** (Declaração de Prestação de Serviços) **não possui registro de informações complementares** sobre este intermediador no **CNC NFS-e (Cadastro Nacional de Contribuintes)**. Como resultado, a nota foi **rejeitada pela SEFAZ** com a mensagem de erro E0290.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224118369943)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224134060311)

 Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize a **NFS-e que foi rejeitada**.

- 

Ao abrir a nota fiscal, o sistema **redirecionará automaticamente para a tela "Central de Vendas"** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224134062231)

 Verifique se a operação **realmente necessita de um intermediador**. Caso não seja necessário:

- 

Remova as **informações do intermediador**, incluindo a **Inscrição Municipal (IM)**;

- 

Salve as alterações e tente **emitir a nota novamente**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224134063511)

 Caso a operação **exija a presença de um intermediador**, verifique se o **intermediador está devidamente cadastrado** no **CNC NFS-e do município emissor**:

- 

Entre em contato com a **Prefeitura do município emissor** ou acesse o **portal da SEFAZ municipal**;

- 

Confirme se o **intermediador possui registro ativo** e se as **informações complementares estão atualizadas** no sistema.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224134064535)

 Se o intermediador **não estiver cadastrado ou com informações incompletas**, solicite ao intermediador que **regularize seu cadastro junto ao município** antes de prosseguir com a emissão da nota.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224134065303)

 Após a **regularização do cadastro do intermediador**, retorne à tela de **"Nota Fiscal de Serviço Eletrônica"** e tente **emitir a nota novamente**. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224118375319)

 **CAUSA**

A rejeição ocorre porque o sistema da **SEFAZ valida** se o **intermediador informado na NFS-e** possui **registro completo e ativo** no **CNC NFS-e do município emissor**. Quando a **Inscrição Municipal (IM) do intermediário é preenchida**, mas **não há informações complementares registradas** no cadastro nacional do município, a nota é **automaticamente rejeitada** com o código E0290, impedindo a emissão até que a situação seja regularizada.