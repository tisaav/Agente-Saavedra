# E0462 Rejeição: NF-e não existe na base de dados do autorizador de NF-e nacional. Informe uma chave de NF-e existente.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225665038743-E0462-Rejei%C3%A7%C3%A3o-NF-e-n%C3%A3o-existe-na-base-de-dados-do-autorizador-de-NF-e-nacional-Informe-uma-chave-de-NF-e-existente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225665038743-E0462-Rejei%C3%A7%C3%A3o-NF-e-n%C3%A3o-existe-na-base-de-dados-do-autorizador-de-NF-e-nacional-Informe-uma-chave-de-NF-e-existente)  
> **ID:** `37225665038743` | **Última Atualização:** 2026-07-22T14:15:47Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225665022871)

 **MENSAGEM**

E0462 Rejeição: NF-e não existe na base de dados do autorizador de NF-e nacional. Informe uma chave de NF-e existente.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225665023127)

 **SITUAÇÃO**

Ao emitir uma **NF-e de devolução** ou um **CT-e** que referencia uma NF-e, o sistema apresenta a rejeição informando que a **chave de acesso da NF-e referenciada não existe** na base de dados do autorizador nacional da SEFAZ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225649062423)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225649063575)

 Verifique se a **chave de acesso da NF-e referenciada** foi digitada corretamente no documento fiscal que está sendo emitido, conferindo todos os 44 dígitos.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225649064599)

 Acesse o ****[''Portal Nacional da NF-e''](http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx)** **e consulte a chave de acesso informada. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225649066391)

 Se a consulta retornar que a NF-e não existe ou está **inexistente**, verifique as seguintes possibilidades:

- 

A NF-e original **foi cancelada** ou **inutilizada**.

- 

A **chave de acesso** informada está incorreta ou incompleta.

- 

A NF-e original **não foi autorizada** pela SEFAZ.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225649068823)

 Se a NF-e original foi **autorizada**, mas não está sendo localizada no **Portal Nacional**, consulte também o **Portal da SEFAZ do estado emissor**:

- 

Acesse o site da SEFAZ do estado correspondente.

- 

Localize a opção de **consulta de NF-e**.

- 

Informe a chave de acesso e verifique o status do documento.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225649070487)

 Caso a NF-e esteja **autorizada** nos portais da SEFAZ, aguarde alguns minutos e tente transmitir novamente o documento fiscal, pois pode haver **delay na sincronização** entre as bases de dados.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225665033239)

 Se a NF-e original **não foi autorizada** ou está **cancelada**, corrija a referência no documento fiscal que está sendo emitido, informando uma **chave de acesso válida** de uma NF-e autorizada.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225649074199)

 Após realizar as correções necessárias, tente **gerar o lote** e **transmitir** novamente o documento fiscal. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225649075479)

 **CAUSA**

A rejeição ocorre porque a **chave de acesso da NF-e informada** como referência no documento fiscal (NF-e de devolução, CT-e ou outro) **não foi localizada** na base de dados do autorizador nacional da SEFAZ. Isso pode acontecer quando a chave está **digitada incorretamente**, quando a NF-e original **não foi autorizada**, foi **cancelada**, **inutilizada** ou ainda não foi **sincronizada** entre as bases de dados da SEFAZ.