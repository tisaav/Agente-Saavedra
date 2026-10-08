# 1001 Rejeição: NF-e com finalidade de débito ou crédito somente para IBS/CBS

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36076049422743-1001-Rejei%C3%A7%C3%A3o-NF-e-com-finalidade-de-d%C3%A9bito-ou-cr%C3%A9dito-somente-para-IBS-CBS](https://ajuda.sankhya.com.br/hc/pt-br/articles/36076049422743-1001-Rejei%C3%A7%C3%A3o-NF-e-com-finalidade-de-d%C3%A9bito-ou-cr%C3%A9dito-somente-para-IBS-CBS)  
> **ID:** `36076049422743` | **Última Atualização:** 2026-07-24T16:47:31Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076003407127)

 **MENSAGEM**

1001 Rejeição: NF-e com finalidade de débito ou crédito somente para IBS/CBS

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076003408151)

 **SITUAÇÃO**

A mensagem de erro é apresentada ao tentar transmitir uma NF-e cuja **"Finalidade da NF-e"** está definida como **"Débito"** ou **"Crédito"** (finNFe=5 ou 6), porém há impostos informados nos itens da nota. O erro pode ocorrer tanto na emissão manual quanto na importação do XML da NF-e.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076049402775)

 **SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076003418007)

 Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou** ****''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076003420823)

 Localize e selecione a nota fiscal que apresentou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076049406999)

 Na grade **''Cabeçalho''**, verifique o campo **''Tipo Operação'' **e identifique o TOP usada na nota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076049410327)

 Acesse a tela **"****Tipos de Operação - TOP****" **(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP identificado no passo anterior.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076003429655)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique o campo **"NF-e". **

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076049413015)

 **Se estiver selecionada as opções ''**Crédito''** ou** ''Débito'', **siga as ações abaixo:

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076333328663)

 Retorne à nota que recebeu a rejeição, e confira se nos itens ou na aba **"Impostos" **está informado algum dos seguintes impostos:

- 

**ICMS**

- 

**IPI**

- 

**PIS**

- 

**COFINS**

- 

**ISSQN**

- 

**II**

- 

**ICMS UF Destino**

- 

**Imposto Devolvido**

- 

**PIS ST**

- 

**COFINS ST**

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076304088471)

 Corrija a nota fiscal:

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076049413015)

 Se a nota foi gerada manualmente:**

- Remova todos os impostos acima dos itens da nota;

- 

Mantenha apenas **IBS/CBS**, se aplicável;

- 

Salve e gere novamente o XML.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076049413015)

 Se a nota foi importada via XML: **

- 

Edite o XML antes de importar;

- 

Remova as tags de impostos: **<ICMS>**, **<IPI>**, **<PIS>**, **<COFINS>**, **<ISSQN>**, **<II>**, **<ICMSUFDest>**, **<impostoDevol>**, **<PISST>**, **<COFINSST>**;

- 

Mantenha apenas as tags de **IBS/CBS**, se existirem.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076304089879)

 Após corrigir a nota, transmita novamente para a Sefaz.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38471556817943)

 Verifique se a rejeição foi solucionada.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38471569643671)

 ****IMPORTANTE**: Se não for uma operação de IBS/CBS, não utilize as finalidades **Débito** ou **Crédito**. Se for, garanta que apenas **IBS/CBS** está informado.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36076049415575)

 **CAUSA**

A rejeição ocorre porque, para NF-e com **"Finalidade"** igual a **"Débito"** ou **"Crédito"** (finNFe=5 ou 6), não é permitido informar impostos como **"ICMS"**, **"IPI"**, **"PIS"**, **"COFINS"**, **"ISSQN"**, **"II"**, **"ICMS UF Destino"**, **"Imposto Devolvido"**, **"PIS ST"** ou **"COFINS ST"** nos itens da nota ou no XML. Apenas **"IBS/CBS"** pode ser informado, se aplicável.