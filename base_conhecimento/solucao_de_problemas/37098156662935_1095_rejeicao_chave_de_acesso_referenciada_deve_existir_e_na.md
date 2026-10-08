# 1095 Rejeição: Chave de acesso referenciada deve existir e não estar cancelada [nRef: xxx]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098156662935-1095-Rejei%C3%A7%C3%A3o-Chave-de-acesso-referenciada-deve-existir-e-n%C3%A3o-estar-cancelada-nRef-xxx](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098156662935-1095-Rejei%C3%A7%C3%A3o-Chave-de-acesso-referenciada-deve-existir-e-n%C3%A3o-estar-cancelada-nRef-xxx)  
> **ID:** `37098156662935` | **Última Atualização:** 2026-08-25T15:12:46Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098156650135)

 **MENSAGEM**

1095 Rejeição: Chave de acesso referenciada deve existir e não estar cancelada [nRef: xxx]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098147949591)

 **SITUAÇÃO**

Ao tentar transmitir uma **NF-e que faz referência a outra nota fiscal** (como em casos de devolução, complemento ou substituição), a SEFAZ rejeita a operação porque a **chave de acesso referenciada não existe na base de dados** da SEFAZ ou está com status de cancelada.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098156650903)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098147950999)

 Verifique se a **chave de acesso referenciada** está correta. Para isso, consulte a nota fiscal original no **Portal Nacional da NF-e**:

- 

Acesse o site do ********[''Portal Nacional da NF-e''](http://www.nfefazenda..gov.br/portal/consultaRecaptcha.aspx?AspxAutoDetectCookieSupport=1);

- 

Informe a **chave de acesso** da nota referenciada;

- 

Confirme o **status** do documento fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098156651799)

 Caso a consulta indique que a **nota fiscal está cancelada**, utilize uma **nota válida** para referência ou, se aplicável, **emita a NF-e sem informar referência**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098147952791)

 Se a consulta retornar **"Chave de acesso inexistente"**, verifique se a chave foi digitada corretamente. Para isso:

- Acesse a nota original no sistema

- Confira a chave de acesso no XML da nota

- Compare com a chave informada na nota que está sendo rejeitada

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37989614204951)

 Para corrigir a chave na nota que está sendo rejeitada:

- Acesse a tela ****[''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas);

- Localize a nota rejeitada;

- Na aba **''NF-e''**, verifique o campo **"Chave NF-e Referenciada"** e corrija a informação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098156656023)

 Caso a nota esteja sendo gerada por meio de **devolução automática**, verifique se a **nota fiscal original** encontra-se **autorizada pela SEFAZ** e se o **XML correspondente foi corretamente importado no sistema**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098156659991)

 Após realizar os ajustes, **gere um novo lote da NF-e** e **reenvie o documento para autorização**.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098156660119)

 **CAUSA**

Esta rejeição ocorre quando uma NF-e faz referência a outra nota fiscal através da chave de acesso, mas a SEFAZ não consegue localizar esta nota referenciada em sua base de dados ou a encontra com status de cancelada. Isso pode acontecer por diversos motivos:

- A chave de acesso foi digitada incorretamente;

- A nota referenciada foi cancelada após sua emissão;

- A nota referenciada nunca foi autorizada pela SEFAZ;

- A nota referenciada foi emitida em contingência e não foi transmitida posteriormente;

- A nota referenciada pertence a outra UF e não está disponível na base nacional.

De acordo com as regras de validação da SEFAZ, para que uma nota fiscal possa referenciar outra, a nota referenciada deve existir na base de dados e estar com status diferente de cancelada.


---

### 🔗 Links e Referências Internas:

- [''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)