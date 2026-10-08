# 1157 Rejeição: Data de previsão de entrega não permitida para a modalidade de frete informada

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35944511260439-1157-Rejei%C3%A7%C3%A3o-Data-de-previs%C3%A3o-de-entrega-n%C3%A3o-permitida-para-a-modalidade-de-frete-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/35944511260439-1157-Rejei%C3%A7%C3%A3o-Data-de-previs%C3%A3o-de-entrega-n%C3%A3o-permitida-para-a-modalidade-de-frete-informada)  
> **ID:** `35944511260439` | **Última Atualização:** 2026-08-25T00:08:52Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944511234071)

 **MENSAGEM**

1157 Rejeição: Data de previsão de entrega não permitida para a modalidade de frete informada.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944518914583)

 **SITUAÇÃO**

A rejeição é apresentada ao emitir uma nota fiscal quando o campo **“Previsão de Entrega”** está preenchido e a **Modalidade de Frete** selecionada é uma das seguintes opções: **1 – Contratação do Frete por conta do Destinatário (FOB)**; **4 – Transporte Próprio por conta do Destinatário**; **9 – Sem Ocorrência de Transporte**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944518915223)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944518915863)

 Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou** ''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944511240215)

 Identifique e selecione a nota fiscal que apresentou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944511243671)

 Na aba **"Transporte", **verifique a opção selecionada no campo **"CIF / FOB":**

- 

**''Terceiros''**

- 

**''Transp. próprio remetente''**

- 

**''Sem frete''**

- 

**''Transporte próprio destinatário''**

- 

**''CIF - Contratação do frente por conta do remetente''**

- 

**''FOB - Contratação do frete por conta do destinatário''**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944518922263)

 Corrija a inconsistência conforme o cenário identificado:

Localize o campo “Previsão de Entrega” e remova a data informada caso a modalidade selecionada no campo “CIF/FOB” seja uma das seguintes:

- 

''FOB – Contratação do frete por conta do destinatário'';

- 

''Transp. próprio destinatário'';

- 

''Sem frete''.

Caso a modalidade de transporte correta seja diferente das opções acima, altere o campo **“CIF/FOB”** conforme a necessidade. Nessa situação, a data informada em **“Previsão de Entrega”** poderá ser mantida.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944511249815)

 Salve as alterações realizadas na nota fiscal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944518924951)

 Transmita novamente a nota fiscal para a SEFAZ.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35944511252887)

 **CAUSA**

Conforme as regras da Sefaz, o preenchimento do campo **"Previsão de Entrega"** não é permitido nas seguintes modalidades de frete:

- 

FOB - Contratação do frete por conta do destinatário

- 

Transporte próprio destinatário

- 

Sem frete