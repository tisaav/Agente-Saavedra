# Propriedade 'EventoMDF.NRORECIBO' com largura acima do limite: (15 > 1)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/18880283321239-Propriedade-EventoMDF-NRORECIBO-com-largura-acima-do-limite-15-1](https://ajuda.sankhya.com.br/hc/pt-br/articles/18880283321239-Propriedade-EventoMDF-NRORECIBO-com-largura-acima-do-limite-15-1)  
> **ID:** `18880283321239` | **Última Atualização:** 2026-07-22T14:52:01Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18880283298711)

 **MENSAGEM:**

Propriedade 'EventoMDF.NRORECIBO' com largura acima do limite: (15 > 1).

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18880290803351)

CAUSA:**

Quando há divergência entre as tabelas. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18880254764567)

SOLUÇÃO:**

Acesse a tela **DBExplorer** *(Configurações » Avançado » DBExplorer)* e busque pelas tabelas TGFMDFE e TGFEMDF, observando o campo NRORECIBO.

 

![dbexplorer 14-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19056619078935)

 

![dbexplorer 2  14-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19056619090199)

 

No exemplo acima na TGFMDFE o campo NRORECIBO está com tamanho de 15 e na TGFEMDF esta como 1. Para correção, ajuste os campos de maneira que fiquem iguais (com 15).