# 1003 Rejeição: NF-e de crédito faz referência a documento fiscal diferente de NF-e modelo 55

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36077711672087-1003-Rejei%C3%A7%C3%A3o-NF-e-de-cr%C3%A9dito-faz-refer%C3%AAncia-a-documento-fiscal-diferente-de-NF-e-modelo-55](https://ajuda.sankhya.com.br/hc/pt-br/articles/36077711672087-1003-Rejei%C3%A7%C3%A3o-NF-e-de-cr%C3%A9dito-faz-refer%C3%AAncia-a-documento-fiscal-diferente-de-NF-e-modelo-55)  
> **ID:** `36077711672087` | **Última Atualização:** 2026-07-22T14:23:49Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077711640215)

 **MENSAGEM**

1003 Rejeição: NF-e de crédito faz referência a documento fiscal diferente de NF-e modelo 55.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077711643031)

 **SITUAÇÃO**

Ao emitir uma NF-e de crédito, ao selecionar a **"Finalidade da NF-e"** como **"Crédito"** (finNFe = 5), foi referenciado um documento fiscal cuja chave não corresponde a uma NF-e modelo 55. Isso ocorre quando, na seção **"NF-e Referenciada"**, é informada uma chave de acesso de outro modelo, como NFC-e (modelo 65), nota em papel (modelo 01), CT-e (modelo 57), entre outros.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077706050583)

 **SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077711646615)

 Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou** ''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077711649047)

  Localize e selecione a nota fiscal que apresentou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077706058263)

 Na grade **''Cabeçalho''**, verifique o campo **''Tipo Operação''** e identifique o TOP utilizado na nota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38471677296919)

 Acesse a tela **"Tipos de Operação - TOP" **(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP identificado no passo anterior.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077711656471)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique o campo** ''NF-e''**.** **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077706060951)

 Caso esteja selecionada a opção **"Crédito", **realize as ações a seguir:

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077706067351)

 Retorne à nota que recebeu a rejeição, vá até a aba **"NF-e/NFS-e"** e verifique os documentos informados no campo **" Chave NF-e Referenciada"**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36119625441815)

 Para cada chave referenciada, confira se corresponde a uma NF-e modelo 55. O modelo está nos dígitos 21 e 22 da chave de acesso (valor **"55"** indica NF-e modelo 55). 

- 

Por exemplo: NFe 3519 **55 **12345678901234567890123456789012345678901234 (os dígitos 21-22 em negrito indicam o modelo).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36119625442839)

 Remova qualquer referência a documentos que não sejam NF-e modelo 55:

- 

Exclua a linha ou registro da nota referenciada incorreta e adicione apenas chaves de acesso de NF-e modelo 55.

- 

Se não houver uma NF-e modelo 55 para referenciar, deixe o campo de referência vazio (se permitido para o seu caso).

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38471677300887)

 Salve a nota fiscal e realize nova tentativa de transmissão para a **Sefaz**.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36077711661079)

 **CAUSA**

A rejeição ocorre porque, ao emitir uma NF-e de crédito, foi referenciada uma chave de acesso que não pertence a uma NF-e modelo 55. Apenas este modelo é aceito para referência em operações de crédito, conforme exigência da Sefaz.