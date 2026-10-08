# 254 Rejeição: NF-e complementar não possui NF referenciada

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36063692527127-254-Rejei%C3%A7%C3%A3o-NF-e-complementar-n%C3%A3o-possui-NF-referenciada](https://ajuda.sankhya.com.br/hc/pt-br/articles/36063692527127-254-Rejei%C3%A7%C3%A3o-NF-e-complementar-n%C3%A3o-possui-NF-referenciada)  
> **ID:** `36063692527127` | **Última Atualização:** 2026-07-30T13:27:12Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063669372567)

 **MENSAGEM**

254 Rejeição: NF-e complementar não possui NF referenciada
 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063669374743)

 **SITUAÇÃO**

A mensagem de erro é apresentada ao tentar transmitir uma **NF-e** marcada como **"Complementar"** ou de **"Crédito"** no sistema, sem informar uma **"Nota Fiscal Referenciada" **ou seja não foi preenchida a referência à nota original.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063692494999)

 **SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063692496791)

 Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063692498327)

 Localize e selecione a nota fiscal que apresentou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063669380247)

 Na grade **''Cabeçalho''**, verifique o campo **''Tipo Operação''** e identifique a TOP usada na nota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063669381911)

 Acesse a tela **"Tipos de Operação - TOP" **(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e busque a TOP identificada no passo anterior.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38610088103319)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e" **está selecionada uma das opções abaixo:

- 

**''Crédito''**, ou

- 

**''Complementar''.**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063669385367)

 Se for uma **NF-e de Crédito**, verifique no campo **"Tipo de Nota Fiscal de Crédito"** se está selecionada uma das opções abaixo:

- **''Multa e Juros''**

- **''Retorno''**

- **''Redução de valores''**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063669388311)

 Feitas as verificações acima, caso a TOP usada seja **Complementar ou Crédito (do tipo Multa e Juros, Retorno ou Redução de valores)**, adicione uma **Chave NF-e Referenciada. **Para isso:

- 

Retorne no passo 1.

- 

Na aba **"NF-e/NFS-e"**, informe no campo **"Chave NF-e referenciada" **a chave de acesso da **NF-e original.**

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063669391511)

  Clique em **"Salvar"** e, em seguida, transmita novamente a NF-e para a SEFAZ.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38610088107927)

 Aguarde o retorno da SEFAZ e confirme a autorização da nota.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36063692512023)

 **CAUSA**

A rejeição ocorre porque toda **NF-e complementar** ou de **crédito **(do tipo Multa e Juros, Retorno ou Redução de valores) deve obrigatoriamente referenciar a nota fiscal original que está sendo complementada. Quando a **"Nota Fiscal Referenciada"** não é informada, o sistema impede a transmissão da NF-e.