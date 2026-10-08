# Financeiro não pode ser modificado. Já tem provisão baixada

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4410701967639-Financeiro-n%C3%A3o-pode-ser-modificado-J%C3%A1-tem-provis%C3%A3o-baixada](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410701967639-Financeiro-n%C3%A3o-pode-ser-modificado-J%C3%A1-tem-provis%C3%A3o-baixada)  
> **ID:** `4410701967639` | **Última Atualização:** 2026-07-22T15:21:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16121402739863)

 MENSAGEM: **

[CORE_E02787] Financeiro não pode ser modificado. Já tem provisão baixada.

[CORE_E03481] Financeiro não pode ser modificado. Já tem provisão baixada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16121377091095)

 SOLUÇÃO:**

É um comportamento nativo do sistema. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16121402744471)

 CAUSA: **

Os pedidos de ''compra' ou 'Venda'' geralmente são configurados para atualizar o financeiro de forma **''provisionada'',** se assim estiver na TOP.  Quando se realiza o faturamento parcial ou integral deste pedido, sua **''provisão financeira''** é baixada (parcial ou total) e um novo titulo 'REAL' é incluído na movimentação financeira. 

Ao tentar realizar alguma modificação em campos que podem interferir no financeiro dos Pedidos que já foram faturados, a mensagem de **aviso** é apresentada.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16121377101591)

 OBSERVAÇÃO:**

Campos adicionais não entram nesta regra.