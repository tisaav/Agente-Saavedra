# Informado CST de diferimento sem as informações de diferimento [nItem: xxx]

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8337704977431-Informado-CST-de-diferimento-sem-as-informa%C3%A7%C3%B5es-de-diferimento-nItem-xxx](https://ajuda.sankhya.com.br/hc/pt-br/articles/8337704977431-Informado-CST-de-diferimento-sem-as-informa%C3%A7%C3%B5es-de-diferimento-nItem-xxx)  
> **ID:** `8337704977431` | **Última Atualização:** 2026-08-05T19:02:18Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361691542807)

 MENSAGEM:**

[929 - Rejeição]: Informado CST de diferimento sem as informações de diferimento [nItem: xxx]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361676423447)

SOLUÇÃO: **

Caso se trate de uma NF-e (modelo 55) ou NFC-e (modelo 65) e o CST for igual a 51 - Diferimento, deve informe os seguintes campos de valores: 

Valor do ICMS de operação - Tag vICMSOp
Modalidade BC ICMS - Tag modBC
Redução de BC ICMS - Tag pRedBC
Valor da BC do ICMS - Tag vBC
Alíquota de ICMS - Tag pICMS
Valor do ICMS - Tag vICMS 
Valor do ICMS de operação - Tag vICMSOp
Percentual do diferimento - Tag pDif 
Valor do ICMS diferido - Tag vICMSDif

 

De acordo com a NT(Nota Técnica 2019.001) temos algumas exceções para a regra de validação:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361676423959)

 A regra não se aplica quando a Finalidade de emissão da NFe (tag: finNFe) é igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361691544727)

 A critério da UF, a regra não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361691546135)

 A critério da UF, a regra não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste;

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361676430487)

 A critério da UF, a regra não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361691547159)

CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e o CST - Código da Situação Tributária de ICMS for igual a 51 - Diferimento, deve informar todos os valores de diferimento;