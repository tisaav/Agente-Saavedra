# WMS_E00135: o ajuste só poderá ser desfeito após a deleção da nota de ajuste

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35043761919383-WMS-E00135-o-ajuste-s%C3%B3-poder%C3%A1-ser-desfeito-ap%C3%B3s-a-dele%C3%A7%C3%A3o-da-nota-de-ajuste](https://ajuda.sankhya.com.br/hc/pt-br/articles/35043761919383-WMS-E00135-o-ajuste-s%C3%B3-poder%C3%A1-ser-desfeito-ap%C3%B3s-a-dele%C3%A7%C3%A3o-da-nota-de-ajuste)  
> **ID:** `35043761919383` | **Última Atualização:** 2026-07-22T14:26:06Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35043761910679)

 **MENSAGEM**

[WMS_E00135] O ajuste só poderá ser desfeito após a deleção da nota de ajuste.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35471397511191)

 **SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta desfazer um ajuste de inventário que já possui **notas de ajuste** (falta ou sobra) geradas e vinculadas ao processo.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35043761911959)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35471365934231)

 Acesse a tela **"Histórico de Ajuste de Estoque"** (WMS » Inventário » Histórico de Ajuste de Estoque) e verifique qual o **"Tipo de divergência"** gerada:** "Falta" ou "Sobra".**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35471365937047)

 Se existir mais de um ajuste para o mesmo inventário, valide **todos os ajustes** gerados.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35471365940887)

 Caso o tipo de ajuste seja **Falta:**

- 

Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas)

- 

Filtre a nota de ajuste de saída gerada para os produtos e exclua essa nota

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35471397519895)

 Caso o tipo de ajuste seja **Sobra:**

- 

Acesse a tela **"Portal de Compras"** (Comercial » Consulta » Portal de Compras)

- 

Filtre a nota de ajuste de sobra gerada para os produtos  e exclua essa nota

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35471365948439)

 Retorne à tela **"Histórico de Ajuste de Estoque"** (WMS » Inventário » Histórico de Ajuste de Estoque) e desfaça o ajuste gerado, agora sem as notas vinculadas.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35043785271703)

 **CAUSA**

O erro ocorre quando um ajuste de inventário já teve as notas de sobra ou falta geradas e vinculadas ao ajuste, impedindo que o processo seja desfeito diretamente.