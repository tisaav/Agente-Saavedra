# 255 Rejeição: NF-e possui mais de uma NF referenciada

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36069259293463-255-Rejei%C3%A7%C3%A3o-NF-e-possui-mais-de-uma-NF-referenciada](https://ajuda.sankhya.com.br/hc/pt-br/articles/36069259293463-255-Rejei%C3%A7%C3%A3o-NF-e-possui-mais-de-uma-NF-referenciada)  
> **ID:** `36069259293463` | **Última Atualização:** 2026-07-24T12:42:56Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069259277079)

 **MENSAGEM**

255 Rejeição: NF-e possui mais de uma NF referenciada.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069259277591)

 **SITUAÇÃO**

A mensagem de erro é apresentada ao tentar transmitir uma **NF-e complementar** ou **NF-e de crédito** no Sankhya OM, quando há mais de uma nota fiscal referenciada informada no documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069262075287)

 **SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069262076055)

 Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069259278743)

 Localize e selecione a nota fiscal que apresentou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069262078103)

 Na grade** ''Cabeçalho''**, localize o campo **''Tipo Operação''** e identifique a TOP usada na nota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38436038696215)

 Acesse a tela **"Tipos de Operação - TOP" **(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069259283991)

 Busque e selecione o TOP identificado no passo 3.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069470039831)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se no campo **"NF-e" **está selecionada uma das opções abaixo:

- 

**Crédito**

- 

**Complementar**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069259283223)

 Se a nota for uma **NF-e de Crédito**, verifique no campo **“Tipo de Nota Fiscal de Crédito”** se está selecionada uma das seguintes opções:

- Multa e Juros;

- Retorno;

- Redução de valores.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069656381207)

 Feitas as verificações acima, caso a TOP usada seja **Complementar ou Crédito (do tipo Multa e Juros, Retorno ou Redução de valores)**, execute as ações abaixo:

- 

Retorne ao passo 1 e localize a nota que foi rejeitada;

- 

Na aba **"NF-e/NFS-e''**, verifique se o campo **"Chave NF-e referenciada" **tenha somente uma nota referenciada. Caso haja mais de uma, remova as demais até que permaneça somente uma nota referenciada.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38436094087959)

 Clique em **"Salvar"** e, em seguida, transmita novamente a NF-e para a SEFAZ.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38436094088855)

 Aguarde o retorno da SEFAZ e confirme a autorização da nota.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36069259287063)

 **CAUSA**

O erro ocorre porque, para **NF-e complementar** ou **NF-e de crédito **(do tipo Multa e Juros, Retorno ou Redução de valores), a legislação permite referenciar apenas uma nota fiscal. Ao informar mais de uma nota referenciada nesses casos, o sistema rejeita a transmissão.