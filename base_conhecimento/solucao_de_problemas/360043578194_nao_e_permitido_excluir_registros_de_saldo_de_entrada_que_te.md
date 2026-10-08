# Não é permitido excluir registros de saldo de entrada que tenham movimentações associadas

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043578194-N%C3%A3o-%C3%A9-permitido-excluir-registros-de-saldo-de-entrada-que-tenham-movimenta%C3%A7%C3%B5es-associadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043578194-N%C3%A3o-%C3%A9-permitido-excluir-registros-de-saldo-de-entrada-que-tenham-movimenta%C3%A7%C3%B5es-associadas)  
> **ID:** `360043578194` | **Última Atualização:** 2026-07-22T16:01:48Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16172211099799)

 MENSAGEM:**

ORA-20101: Não é permitido excluir registros de saldo de entrada que tenham movimentações associadas.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16172194727063)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16172211111575)

 Compreender que a mensagem acima é apresentada, visto que a nota a ser excluída/cancelada gerou registros de entrada para 'Rastreamento de Estoque (ST)'. 

A implementação do rastreamento do Estoque necessita de **integridade das informações**. Ao atribuir uma saída tomando como rastreamento determinada entrada **não é possível excluir nem cancelar** este lançamento, pois todas as informações da saída foram geradas com base nesta entrada, como valores de impostos e controle do estoque.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16172194736535)

 Dessa forma, será necessário sintonias com o Contador da Empresa para avaliar a melhor solução para o respectivo problema/incidente. Visto que essa exclusão/cancelamento não será permitido.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16172211123351)

 CAUSA:**

Quando existe o rastreamento de estoque (ST), ao atribuir uma saída tomando como rastreamento determinada entrada, não é possível excluir nem cancelar este lançamento, pois todas as informações da saída foram geradas com base nesta entrada, como valores de impostos e controle do estoque.