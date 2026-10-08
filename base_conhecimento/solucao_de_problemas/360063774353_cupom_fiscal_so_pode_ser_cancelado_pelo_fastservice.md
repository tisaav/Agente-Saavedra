# Cupom Fiscal só pode ser cancelado pelo FastService

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360063774353-Cupom-Fiscal-s%C3%B3-pode-ser-cancelado-pelo-FastService](https://ajuda.sankhya.com.br/hc/pt-br/articles/360063774353-Cupom-Fiscal-s%C3%B3-pode-ser-cancelado-pelo-FastService)  
> **ID:** `360063774353` | **Última Atualização:** 2026-07-22T15:25:07Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334673448087)

 MENSAGEM:**

Cupom Fiscal só pode ser cancelado pelo FastService. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334673449495)

 SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo: 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334712060055)

 Acesse a configuração da TOP e verifique o controle de numeração;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334673451799)

 Se estiver com série = CF,  somente poderá ser cancelada pelo FastService, pois esta série é exclusiva de Cupom Fiscal.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334673452439)

 Se for uma NFC-e, altere a série para a adequada.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334712065047)

 Verifique também se o cod.mod.doc esta = '59 - Cupom Fiscal Eletrônico'. Sendo que este modelo somente deverá ser usado em localidades que utilizam SAT e, com isso, somente será cancelado pelo Fast Service.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334712065815)

 CAUSA:**

Esta validação ocorre em duas situações, se a série utilizada no lançamento for 'CF' ou for lançamento SAT onde na configuração da TOP o cod.mod.doc = 59.