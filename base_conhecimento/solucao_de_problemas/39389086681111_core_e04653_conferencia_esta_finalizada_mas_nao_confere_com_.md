# CORE_E04653 Conferência está finalizada, mas não confere com os itens do pedido ou nota

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39389086681111-CORE-E04653-Confer%C3%AAncia-est%C3%A1-finalizada-mas-n%C3%A3o-confere-com-os-itens-do-pedido-ou-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/39389086681111-CORE-E04653-Confer%C3%AAncia-est%C3%A1-finalizada-mas-n%C3%A3o-confere-com-os-itens-do-pedido-ou-nota)  
> **ID:** `39389086681111` | **Última Atualização:** 2026-08-27T02:18:20Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39389047866647)

 **MENSAGEM**

CORE_E04653 – Conferência está finalizada, mas não confere com os itens do pedido ou nota

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39389047868183)

 **SITUAÇÃO**

O erro ocorre na tela "Central de Vendas" (Comercial > Consulta > Central de Vendas) ao faturar um pedido cujo Tipo de Operação (TOP) exige Conferência de Mercadoria antes do faturamento. Pode acontecer em vendas, devoluções ou qualquer outro tipo de documento nessa condição.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39389047872023)

 **SOLUÇÃO**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39389047873431)

 Verifique se o pedido de origem foi alterado após a conferência ter sido finalizada (quantidade de item, inclusão ou exclusão de item).

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39389086675095)

 Solicite uma nova conferência (recontagem) para o pedido na tela de Conferência de Mercadoria, para que a quantidade conferida volte a corresponder à quantidade atual do pedido.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39389086675735)

 Se o erro for recorrente, revise a "Configuração de Conferência" vinculada à TOP (Comercial > Cadastros > Tipos de Operação - TOP), no campo **"Momento da Conferência"**, que deve estar como **"Antes do Faturamento"** para esta regra se aplicar.

- Para que pequenas divergências entre o conferido e o pedido sejam resolvidas automaticamente (sem bloquear o faturamento), habilite **"Corte Parcial"** e defina o **"Procedimento de Corte"** como:

  - 
**"Atualizar Quantidade Cortada"** ajusta o item à quantidade realmente conferida; ou

  - 
**"Gerar Devolução"** gera uma nota de devolução automática para a diferença não conferida.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39389086673175)

 **CAUSA**

A TOP do pedido está configurado para exigir conferência antes do faturamento. A conferência já foi finalizada como "Finalizada OK", mas, depois disso, o pedido foi alterado, quantidade de um item mudou, ou um item foi incluído/excluído, e a quantidade conferida não corresponde mais à quantidade pendente no pedido. O sistema identifica essa divergência ao gerar a nota e bloqueia o faturamento até que a conferência volte a bater com o pedido.