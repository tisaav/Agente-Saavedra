# A importação não suporta devolução de compra

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31282923818263-A-importa%C3%A7%C3%A3o-n%C3%A3o-suporta-devolu%C3%A7%C3%A3o-de-compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/31282923818263-A-importa%C3%A7%C3%A3o-n%C3%A3o-suporta-devolu%C3%A7%C3%A3o-de-compra)  
> **ID:** `31282923818263` | **Última Atualização:** 2026-07-22T14:33:25Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31282897793559)

 **MENSAGEM:**

[CORE_E02898] Chave XXXXX referenciada no XML é de uma compra Nro.Único XX. A importação não suporta devolução de compras.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31939690733975)

 SITUAÇÃO:**

Ao realizar uma importação de xml de uma nota de devolução de compras que seja de terceiro a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31282897794583)

SOLUÇÃO:**

Este é um comportamento do sistema, que não realiza **importação de notas de devoluções de compra, sendo elas de terceiros.**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31282897797271)

CAUSA:**

O erro é apresentado quando se está importando o xml de uma nota de devolução de terceiro, o sistema verifica se a chave referenciada é de compras, se for o sistema faz a validação.