# 1156 Rejeição: Data de Previsão de Entrega informada e Finalidade de Emissão diferente de "1 - NF-e normal" ou "4 - Devolução de mercadoria".

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35935282146583-1156-Rejei%C3%A7%C3%A3o-Data-de-Previs%C3%A3o-de-Entrega-informada-e-Finalidade-de-Emiss%C3%A3o-diferente-de-1-NF-e-normal-ou-4-Devolu%C3%A7%C3%A3o-de-mercadoria](https://ajuda.sankhya.com.br/hc/pt-br/articles/35935282146583-1156-Rejei%C3%A7%C3%A3o-Data-de-Previs%C3%A3o-de-Entrega-informada-e-Finalidade-de-Emiss%C3%A3o-diferente-de-1-NF-e-normal-ou-4-Devolu%C3%A7%C3%A3o-de-mercadoria)  
> **ID:** `35935282146583` | **Última Atualização:** 2026-07-22T14:24:19Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935282116503)

 **MENSAGEM**

1156 Rejeição: Data de Previsão de Entrega informada e Finalidade de Emissão diferente de "1 - NF-e normal" ou "4 - Devolução de mercadoria".

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935282117399)

 **SITUAÇÃO**

A mensagem de erro é apresentada ao tentar transmitir uma nota fiscal eletrônica (NF-e) que possui o campo **"Data de Previsão de Entrega"** preenchido, porém a **"Finalidade de Emissão"** está configurada com valor diferente de **"1 - NF-e normal"** ou **"4 - Devolução de mercadoria"**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935243237655)

 **SOLUÇÃO**

Siga o passo a passo abaixo para corrigir a rejeição:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935282122903)

 Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935282124311)

 Selecione a nota fiscal que apresentou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935282129431)

 Na grade **''Cabeçalho''**, verifique o campo **''Tipo de Operação''** e identifique o TOP usado na nota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935243246871)

 Acesse a tela **"****Tipos de Operação - TOP****" **(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935243248535)

 Busque e selecione o TOP identificado no passo 3.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935282137751)

 Na aba **“NF-e/NFC-e/CF-e”**, verifique a configuração do campo **“NF-e”**, confirmando qual opção está selecionada e se ela está de acordo com o tipo de operação que está sendo realizada.

 

![1156.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935282134935)

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35987922222231)

 Retorne ao passo 1, na grade ''Cabeçalho'', verifique o campo **"Previsão de Entrega"**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38470444291991)

 Corrija a inconsistência conforme o cenário identificado:

- 

Se a nota fiscal deveria ser **Normal** ou de **Devolução**, altere a **TOP** utilizada, selecionando uma TOP correspondente ao tipo correto de operação.

- 

Se a finalidade da nota fiscal for **Complementar** ou **Ajuste**, remova o valor informado no campo “Previsão de Entrega” e salve a alteração.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38470451674263)

 Após realizar a correção, transmita novamente a nota fiscal para a **Sefaz**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35935243251351)

 **CAUSA**

A rejeição ocorre porque a legislação permite informar a **"Data de Previsão de Entrega"** apenas quando a **"Finalidade de Emissão"** da nota fiscal for **"1 - NF-e normal"** ou **"4 - Devolução de mercadoria"**. Se a finalidade for diferente, o preenchimento desse campo não é permitido.