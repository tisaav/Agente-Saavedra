# 269 Rejeição: CNPJ/CPF Emitente da NF-e Complementar difere do CNPJ/CPF da NF Referenciada

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36074363515415-269-Rejei%C3%A7%C3%A3o-CNPJ-CPF-Emitente-da-NF-e-Complementar-difere-do-CNPJ-CPF-da-NF-Referenciada](https://ajuda.sankhya.com.br/hc/pt-br/articles/36074363515415-269-Rejei%C3%A7%C3%A3o-CNPJ-CPF-Emitente-da-NF-e-Complementar-difere-do-CNPJ-CPF-da-NF-Referenciada)  
> **ID:** `36074363515415` | **Última Atualização:** 2026-07-22T14:23:54Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36074363496087)

 **MENSAGEM**

269 Rejeição: CNPJ/CPF Emitente da NF-e Complementar difere do CNPJ/CPF da NF Referenciada

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36074332855319)

 **SITUAÇÃO**

Ao emitir uma **NF-e Complementar** e informar uma **NF-e Referenciada**, quando o **CNPJ/CPF do emitente** da nota complementar é diferente do **CNPJ/CPF do emitente** da nota referenciada. Isso impede a autorização da nota pela Sefaz.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36074363498391)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36074332858135)

 Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36074363503127)

 Localize e selecione a nota fiscal que apresentou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38602957727639)

 Na grade **''Cabeçalho''**, verifique o campo **"Tipo de Operação" **e identifique a TOP usada na nota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36074332862743)

 Acesse a tela **"Tipos de Operação" **(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38602932359575)

 Busque e selecione a TOP identificada no passo 3.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38602957738135)

 Na aba **"NF-e/NFC-e/CF-e" **verifique se no campo **"NF-e" **está selecionada uma das opções abaixo:

- 

**''Crédito''; ou**

- 

**''Complementar''.**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/36157465699095)

 Se for uma **NF-e de Crédito**, verifique se o campo **"Tipo de Nota Fiscal de Crédito"** se está selecionada uma das opções abaixo:

- 
**''Retorno''**; ou

- 
**''Redução de valores''**.

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/36157465699095)

 Caso a Top seja de **Crédito, do tipo "Retorno" ou "Redução de valores", siga os passos abaixo**:

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36149716504727)

 Volte à nota que recebeu a rejeição e verifique **o CNPJ/CPF do emitente**. Para isso:

- 

Na grade ''Cabeçalho'', verifique o campo **"Empresa"** e veja a empresa emitente;

- 

Em seguida, acesse a tela **"Empresas" **(Configurações » Cadastros » Empresas)**, **busque e selecione a empresa identificada no cabeçalho da nota. Por fim, na aba **"Geral", **no campo **"CNPJ/CPF",** veja o CNPJ ou CPF da empresa emitente.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36149716507287)

 Retorne ao passo 1, localize a aba **"NF-e/NFS-e"** e verifique as notas que estão referenciadas no campo **"Chave NF-e referenciada"**.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38602932361751)

 Se necessário, corrija a referência:

- 

**Referência errada:** caso a **NF-e Referenciada** não tenha sido emitida pelo mesmo **CNPJ/CPF** da nota complementar, apague a chave incorreta no campo **"Chave NF-e Referenciada"** e informe a chave correta (de uma nota emitida pelo mesmo **CNPJ/CPF**).

- 

**CNPJ/CPF do emitente da nota complementar errado:** se o **CNPJ/CPF** da nota complementar estiver incorreto, acesse o cadastro da empresa (emitente) no Sankhya (Configurações » Cadastros » Empresas), corrija o **CNPJ/CPF** e reimporte ou redigite a nota com o dado correto.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38602932362775)

  Salve a nota e reenvie para a Sefaz.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36074332864023)

 **CAUSA**

A rejeição ocorre porque o **CNPJ/CPF do emitente** da **NF-e Complementar** informado é diferente do **CNPJ/CPF do emitente** da **NF-e Referenciada**, contrariando a regra da Sefaz para esse tipo de operação.