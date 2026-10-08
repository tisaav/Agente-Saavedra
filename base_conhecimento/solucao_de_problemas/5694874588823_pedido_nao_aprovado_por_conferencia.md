# Pedido não aprovado por conferência

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/5694874588823-Pedido-n%C3%A3o-aprovado-por-confer%C3%AAncia](https://ajuda.sankhya.com.br/hc/pt-br/articles/5694874588823-Pedido-n%C3%A3o-aprovado-por-confer%C3%AAncia)  
> **ID:** `5694874588823` | **Última Atualização:** 2026-07-22T15:17:48Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16306102527383)

 MENSAGEM:**

Pedido não aprovado por conferência.

 

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16306130492439)

SOLUÇÃO:**

Quando ativo esse parâmetro exige que o pedido esteja aprovado para seguir com o faturamento e não existe código no sistema que aprove automaticamente o pedido quando o parâmetro está ativo. Esse parâmetro veio do MGE, pois lá não tinha a rotina de conferência, havendo a necessidade desse parâmetro estar ativo. Para o **Sankhya Om** não é necessário o uso desse parâmetro, pois o próprio sistema já faz essa validação de acordo com as novas configurações da fila de conferencia.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16306102557463)

 CAUSA:**

Quando o parâmetro **"EXIGECONFPEDVDA"** está ligado é feita a validação, pois no delphi usa essa opção mas no **Sankhya Om** ela não precisa ficar marcada.