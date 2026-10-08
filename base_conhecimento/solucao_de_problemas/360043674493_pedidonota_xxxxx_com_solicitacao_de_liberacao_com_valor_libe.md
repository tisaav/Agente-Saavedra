# Pedido/Nota XXXXX com solicitação de liberação com valor liberado inferior ao valor solicitado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043674493-Pedido-Nota-XXXXX-com-solicita%C3%A7%C3%A3o-de-libera%C3%A7%C3%A3o-com-valor-liberado-inferior-ao-valor-solicitado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043674493-Pedido-Nota-XXXXX-com-solicita%C3%A7%C3%A3o-de-libera%C3%A7%C3%A3o-com-valor-liberado-inferior-ao-valor-solicitado)  
> **ID:** `360043674493` | **Última Atualização:** 2026-07-22T16:03:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142049221143)

 MENSAGEM**:

[CORE_E03069] Pedido/Nota XXXXX com solicitação de liberação com valor liberado inferior ao valor solicitado. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142058535575)

 SOLUÇÃO**:

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142058538007)

 Acesse a rotina **"Liberação de Limites"** *(Caminho de acesso: Configurações » Avançado)** *com o usuário que efetuou a liberação anteriormente, através do duplo-clique, o evento ficará disponível novamente para nova Liberação.

 

![Pedido-Nota_XXXXX_com_solicita__o_de_libera__o_com_valor_liberado_inferior_ao_valor_solicitado.png](https://ajuda.sankhya.com.br/hc/article_attachments/14685878940695)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142058540439)

 Após a liberação o pedido/nota poderá ser confirmado/faturado.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16142049229463)

CAUSA**:

Ocorre quando já houve liberação para o evento e após esta liberação houve alteração no lançamento, deixando o valor solicitado atual maior que o liberado anteriormente, sendo necessário que o usuário liberador realize a liberação do evento novamente.