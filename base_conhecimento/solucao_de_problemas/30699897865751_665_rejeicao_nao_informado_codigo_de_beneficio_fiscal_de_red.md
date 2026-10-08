# 665 Rejeição: Não informado código de benefício fiscal de redução de BC (cBenefRBC)

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30699897865751-665-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-c%C3%B3digo-de-benef%C3%ADcio-fiscal-de-redu%C3%A7%C3%A3o-de-BC-cBenefRBC](https://ajuda.sankhya.com.br/hc/pt-br/articles/30699897865751-665-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-c%C3%B3digo-de-benef%C3%ADcio-fiscal-de-redu%C3%A7%C3%A3o-de-BC-cBenefRBC)  
> **ID:** `30699897865751` | **Última Atualização:** 2026-07-22T14:35:01Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30699897850007)

 **MENSAGEM:**

665 Rejeição: Não informado código de benefício fiscal de redução de BC (cBenefRBC)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30699838784791)

SOLUÇÃO:**

Essa rejeição ocorre quando o** CST de ICMS = 51 (diferimento)** e o campo de **percentual de redução de Base de Cálculo (pRedBC)** são maior que zero, **mas o código de benefício fiscal de redução de BC (cBenefRBC)** não foi informado no grupo de tributação de ICMS. O código **cBenefRBC** é obrigatório quando há redução de base de cálculo em operações de diferimento.

**Exceções:**
**1. Devolução de Mercadoria:** a regra não se aplica caso a finalidade de emissão da NF-e for devolução de mercadoria e a operação for interestadual ou com o exterior.
**2. Aplicação a critério da UF:** a regra também pode não ser aplicada em operações de devolução de mercadoria, conforme a regulamentação da UF.

 

**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/30703056190615)

No Sankhya, certifique as seguintes configurações: **

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30703103981463)

 Tela **"Empresa"** *(Comercial » Preferências » Empresa)*, na aba **"Documentos Fiscais Eletrônicos"**, Sub abas** "NF-e/NFC-e >> Nota Técnica NF-e", **certifique-se de que a Versão: "**Nota Técnica 2019.001 - v.1.64"** está ativa. 

 

![Não informado código de benefício fiscal de redução de BC (cBenefRBC) 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/30703160284055)

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30703056195607)

** Acesse a tela **"Aliquotas de ICMS"** *(Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS)* e no cadastro da Aliquota de ICMS que foi atribuída a Nota Fiscal rejeitada, na aba **"Geral" **verifique se os campos abaixo estão devidamente cadastrados: 

- **Tributação**

- **Aliquotas**

- **% de Outorga/Diferimento**

- **Cód. Benefício Diferimento **

 

![Não informado código de benefício fiscal de redução de BC (cBenefRBC) 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/30703207954327)

 

**Observação:** dúvidas referentes aos valores a serem preenchidos nos campos acima deverão ser verificadas com o setor de contabilidade da empresa. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30699897854615)

CAUSA:**

A rejeição será gerada quando houver uma redução de base de cálculo para diferimento (CST 51), mas **o código de benefício fiscal (cBenefRBC)** não for informado.

****[NT2019_001_v1_64](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=pGfPgyEaNGg=)