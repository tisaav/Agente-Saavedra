# 1153 Rejeição: NFC-e com data de previsão de entrega

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35815751414167-1153-Rejei%C3%A7%C3%A3o-NFC-e-com-data-de-previs%C3%A3o-de-entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/35815751414167-1153-Rejei%C3%A7%C3%A3o-NFC-e-com-data-de-previs%C3%A3o-de-entrega)  
> **ID:** `35815751414167` | **Última Atualização:** 2026-07-22T14:24:39Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/35815751393047)

**MENSAGEM**

1153 Rejeição: NFC-e com data de previsão de entrega.
 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/35815751394583)

**SITUAÇÃO**

A mensagem é apresentada ao tentar transmitir uma nota fiscal eletrônica (NFC-e) no sistema quando o campo **"Previsão de Entrega"** (**dPrevEntrega)** está preenchido. Isso ocorre durante o processo de emissão ou reenvio da nota fiscal.
 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/35815751395479)

**SOLUÇÃO**

Para solucionar, identifique a natureza do erro conforme as instruções abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35815751396375)

  Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35815689807895)

  Localize e selecione a NFC-e que apresentou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35815689810839)

  Encontre o campo **"Previsão de Entrega"** (**dPrevEntrega**).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38432846913943)

 Remova qualquer data informada no campo **"Previsão de Entrega"**, deixando-o em branco.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35815751402007)

  Salve a nota e transmita novamente para a SEFAZ.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/35815689820695)

**CAUSA**

A **Rejeição 1153: NFC-e com data de previsão de entrega** ocorre porque o sistema da SEFAZ não permite que uma Nota Fiscal de Consumidor Eletrônica (NFC-e - modelo 65) contenha data de previsão de entrega. Essa tag é exclusiva para NF-e modelo 55.