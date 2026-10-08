# 1027 Rejeição: NF referenciada informada indevidamente

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36156238693015-1027-Rejei%C3%A7%C3%A3o-NF-referenciada-informada-indevidamente](https://ajuda.sankhya.com.br/hc/pt-br/articles/36156238693015-1027-Rejei%C3%A7%C3%A3o-NF-referenciada-informada-indevidamente)  
> **ID:** `36156238693015` | **Última Atualização:** 2026-07-22T14:23:31Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156238658839)

 **MENSAGEM**

1027 Rejeição: NF referenciada informada indevidamente

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156238661271)

 **SITUAÇÃO**

Ao emitir uma nota fiscal de **crédito **do tipo **"Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM"**, o usuário preencheu ou manteve uma **"NF Referenciada"** na tela de edição da NF-e, isso gerou a rejeição 1027 durante o envio da nota à Sefaz.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156238663063)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156255200919)

 Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou** ****''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156238668311)

 Localize a nota fiscal que está com a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156238670999)

 Na grade **''Cabeçalho''**, verifique no campo** ''Tipo Operação'' **o TOP utilizado na nota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156238672535)

 Acesse a tela **''****Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP identificado no passo anterior.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156255210007)

 Na aba **"NF-e/NFC-e/CF-e" **e verifique se no campo **"NF-e" **está selecionada a opção **"Nota de crédito".**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156255213207)

 Em seguida, no campo **"Tipo de Nota Fiscal de Crédito", **verifique se está selecionada a opção **"Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM"**.

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156255207063)

 Caso o TOP seja de **crédito, do tipo "**Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM"** siga os passos abaixo**:

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156279643031)

 Retorne à nota fiscal que apresentou a rejeição, acesse a aba **“NF-e/NFS-e”** e remova todas as notas informadas no campo **“Chave NF-e Referenciada”**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38471220860951)

 Salve as alterações.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38471220863127)

 Após realizar as correções, transmita novamente a **NF-e** para a **Sefaz**.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36156255215127)

 **CAUSA**

A rejeição ocorre porque, para notas fiscais do tipo **"Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM"**, não é permitido informar nenhuma **"NF Referenciada"** no XML. A presença da tag **<NFref>** viola a regra da Sefaz, impedindo a transmissão da nota.