# Nota Fiscal sem a informação do QR-Code (NT2015/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042561654-Nota-Fiscal-sem-a-informa%C3%A7%C3%A3o-do-QR-Code-NT2015-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042561654-Nota-Fiscal-sem-a-informa%C3%A7%C3%A3o-do-QR-Code-NT2015-002)  
> **ID:** `360042561654` | **Última Atualização:** 2026-07-22T16:09:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473862387735)

 MENSAGEM:**

[394- Rejeição]: Nota Fiscal sem a informação do QR-Code (NT2015/002)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473862391063)

 SOLUÇÃO:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458227819031)

 SankhyaOM / JivaEVO:

Acesse: Tela **"Preferências"** (Caminho de acesso:* Configurações » Avançado*):

- 
**"GERARQRCODEXML** **- Gerar QRCODE no XML da NFC-e?": **ligado

- 
**"UFSQRCODEXML** **- UFs com QRCODE no XML da NFC-e?": **Informe a UF da empresa EMITENTE da NFC-e. No campo se faz necessário informar todas as UF’s utilizadas na emissão das notas e que necessitam da informação do QR-Code.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458227819031)

 Fast Service:

*Avançado » Preferências » Todas Preferências* » aba "**Parâmetro de Telas**":

- 
**"Gerar QR-CODE no XML do NFCe?": **marcado

- 
**"UF's com QR-CODE no XML do NFCe:" **informe a UF da empresa EMITENTE da NFC-e;

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360087650074)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473862392855)

 CAUSA:**

Quando for emitida uma NFC-e e o QR-Code (Campo: qrCode - ID: ZX02) não for informado, será retornada a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16473862394775)

 OBSERVAÇÃO:**
([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=v9JbkEY7evI=)) - Nota Técnica.