# 1137 Rejeição: Valor total do Item (vItem) não informado

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141563909143-1137-Rejei%C3%A7%C3%A3o-Valor-total-do-Item-vItem-n%C3%A3o-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141563909143-1137-Rejei%C3%A7%C3%A3o-Valor-total-do-Item-vItem-n%C3%A3o-informado)  
> **ID:** `37141563909143` | **Última Atualização:** 2026-07-22T14:19:03Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38158709457559)

 MENSAGEM**

1137 Rejeição: Valor total do Item (vItem) não informado

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141563890199)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e), o documento foi rejeitado pela SEFAZ porque o valor total do item (vItem) não foi informado no XML do documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141563890455)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141563891223)

 Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas). 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141563895959)

 Localize o documento fiscal que foi rejeitado. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141548031383)

 Clique em **"Gerar Arquivo XML"** para verificar o arquivo XML gerado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141563899159)

 Abra o XML gerado e verifique se o campo vItem está preenchido para todos os itens da nota fiscal. 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141563899927)

 Caso o campo não esteja preenchido, acesse a tela **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas). 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141563901079)

 Localize a nota fiscal rejeitada e abra-a para edição. 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141563901719)

 Verifique nos seguintes campos garantindo que:

- 

O **"Vlr. Unitário"** (vItem) esteja preenchido;

- 

A **"Quantidade"** (qFaturada) esteja preenchida;

- 

O **"Vlr. Total''** (vProd) seja igual a vItem × qFaturada.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141548035223)

 Corrija os valores conforme necessário e salve as alterações. 

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141548038551)

 Tente emitir a nota fiscal novamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141548039191)

 **CAUSA**

A rejeição 1137 ocorre quando o sistema não consegue calcular ou informar o valor total do item (vItem) no XML da nota fiscal. Conforme as regras de totalização da NF-e/NFC-e, o sistema deve calcular o valor total de cada item (vItem) seguindo fórmulas específicas:

Para a **Regra Geral** (quando tpOp ≠ 2 ou nulo):

```text
vItem = vProd - vDesc - vICMSDeson (se indDeduzDeson=1) + vICMSST + vICMSMonoReten + vFCPST + vFrete + vSeg + vOutro + vII + vIPI + vIPIDevol + vServ + vPIS (se indSomaPISST=1) + vCofins (se indSomaCOFINSST=1) + vIBS + vCBS + vIS + vTotIBSMonoItem + vTotCBSMonoItem
```

 

Para **Faturamento Direto** (quando tpOp = 2):

```text
vItem = vProd - vDesc - vICMSDeson (se indDeduzDeson=1) + vFrete + vSeg + vOutro + vII + vIPI + vServ + vPIS (se indSomaPISST=1) + vCofins (se indSomaCOFINSST=1) + vIBS + vCBS + vIS
```

 

Quando o sistema não consegue calcular este valor devido à falta de informações necessárias ou inconsistências nos dados, a nota é rejeitada com o código 1137.