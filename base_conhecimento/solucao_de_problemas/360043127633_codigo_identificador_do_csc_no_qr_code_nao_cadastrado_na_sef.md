# Código Identificador do CSC no QR-Code não cadastrado na SEFAZ(NT2016.002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043127633-C%C3%B3digo-Identificador-do-CSC-no-QR-Code-n%C3%A3o-cadastrado-na-SEFAZ-NT2016-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043127633-C%C3%B3digo-Identificador-do-CSC-no-QR-Code-n%C3%A3o-cadastrado-na-SEFAZ-NT2016-002)  
> **ID:** `360043127633` | **Última Atualização:** 2026-07-22T16:07:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16483332089111)

 MENSAGEM:**

[462 - Rejeição]: Código Identificador do CSC no QR-Code não cadastrado na SEFAZ.(NT2016.002)

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16483309691415)

 **SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16483309694487)

 Acesse: *Comercial » Preferências » Empresa*

Aba: **"NF-e/NFC-e"**

Campos: 

- 
**"Sequencial do Token NFC-e": **Informe o código de 6 digital, extraído da Sefaz Estadual

- 
**"Token NFC-e":** Informe o código alfanumérico, extraído da Sefaz Estadual

 

![C_digo_Identificador_do_CSC_no_QR-Code_n_o_cadastrado_na_SEFAZ..png](https://ajuda.sankhya.com.br/hc/article_attachments/14550251717015)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16483332109079)

 Acesse: *Configurações » Avançado » Preferências*

Parâmetros:

- 
**"GERARQRCODEXML":** Ligado

- 
**"UFSQRCODEXML-UFs com QRCODE no XML da NFC-e?":** Informe a UF's, separado por vírgula se houve mais de 1(um).

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16483332115223)

 Após o ajustes, gere novamente o cupom Eletrônico.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16483309706775)

 CAUSA:**

Quando for emitida uma NFC-e e o parâmetro CSC (Token) do emitente, no QR-Code não estiver cadastrado na Sefaz, será retornado a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16483309709207)

 OBSERVAÇÃO:**

(**NT2016.002**) - Nota Técnica 

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)