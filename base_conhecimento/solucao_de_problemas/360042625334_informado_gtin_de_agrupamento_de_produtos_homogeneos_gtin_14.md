# Informado GTIN de agrupamento de produtos homogêneos (GTIN-14) no GTIN da unidade tributável [nItem: 999](NT2017/001)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625334-Informado-GTIN-de-agrupamento-de-produtos-homog%C3%AAneos-GTIN-14-no-GTIN-da-unidade-tribut%C3%A1vel-nItem-999-NT2017-001](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625334-Informado-GTIN-de-agrupamento-de-produtos-homog%C3%AAneos-GTIN-14-no-GTIN-da-unidade-tribut%C3%A1vel-nItem-999-NT2017-001)  
> **ID:** `360042625334` | **Última Atualização:** 2026-07-22T16:08:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16487743899159)

 MENSAGEM:**

[887 - Rejeição]: Informado GTIN de agrupamento de produtos homogêneos (GTIN-14) no GTIN da unidade tributável [nItem: 999](NT2017/001).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16487743902231)

 SOLUÇÃO:**

Considere o comportamento da aplicação, conforme abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16487699203351)

 Se a operação for realizada com a 'Unidade Padrão' e **NÃO** possuirmos uma 'Unidade Alternativa' marcada como 'Unidade de Tributação', no XML as tags cEAN e cEANTrib serão preenchidas conforme aba Impostos, campo 'EAN/GTIN Produto p/ NF-e'.

As tag's **<cEAN>** e **<cEANTrib>**, serão preenchidas conforme o campo abaixo:

Tela: **"Produtos"**

Aba: **"Impostos"**
Campo **"EAN/GTIN" Produto p/ NF-e":** d*e acordo com a Definição das opções*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16487699205527)

 A operação é feita com a 'Unidade de Tributação', porém **EXISTE** uma 'Unidade Alternativa' cadastrada e na mesma marcada como 'Unidade de Tributação', dessa forma a tag cEAN será preenchida conforme a configuração do campo 'EAN/GTIN Produto p/ NF-e'. Já a tag cEANTrib conforme campo 'EAN/GTIN Unid.Tributação' da aba 'Unidade Alternativa'.

O campo **"Unidade Tributação"** fica na aba: **"Unidade Alternativa"**, opção "**Unid. Tributação"**

A tag **<cEAN>**, será preenchida conforme o campo abaixo:
Aba: **"Impostos"**
Campo **"EAN/GTIN Produto p/ NF-e:"** de acordo com a Definição das opções

A tag <**cEANTrib**>, será preenchida conforme o campo abaixo
Aba: **"Unidade Alternativa"**
Campo **"EAN/GTIN Unid.Tributação":**  de acordo com a Definição das opções

Conforme o comportamento acima, efetue os ajustes necessários, segundo o processo da empresa,. Considere sempre consultar a área Fiscal da Empresa, caso haja dúvidas. Após os ajustes lance novamente os produtos ou fature a Nota e gere Lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16487743910423)

 CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65), e o Código de Barras da Unidade Tributável (tag: cEANTrib) informado seja de um agrupamento de produtos homogêneos (GTIN-14), haverá a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16487743914135)

 OBSERVAÇÃO:**

([NT2017/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=4DaFPH8v5ac=)) - Nota Técnica.