# Nenhum processo produtivo que permita vínculo com pedido de venda encontrado para o pedido [XXXXX]

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043723754-Nenhum-processo-produtivo-que-permita-v%C3%ADnculo-com-pedido-de-venda-encontrado-para-o-pedido-XXXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043723754-Nenhum-processo-produtivo-que-permita-v%C3%ADnculo-com-pedido-de-venda-encontrado-para-o-pedido-XXXXX)  
> **ID:** `360043723754` | **Última Atualização:** 2026-08-25T16:45:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363769026455)

**MENSAGEM**

Não é permitido especificar Pedido para OP sequência 1, pois o Processo Produtivo está configurado como "Nunca" exige pedido de venda.

[PROD_E00135] Nenhum processo produtivo que permita vínculo com pedido de venda encontrado para o pedido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42985880821527)

**SITUAÇÃO**

Este erro ocorre ao tentar lançar uma Ordem de Produção (OP) vinculada a um pedido de venda ou ao gerar a OP pelo Portal de Vendas, por meio da opção **Outras Opções » "Gerar Produção"**.

O problema ocorre quando o Processo Produtivo associado ao produto está configurado com a opção "**Exigir pedido de venda"** definida como "**Nunca"**. Nesse cenário, o sistema identifica uma incompatibilidade entre a configuração do processo produtivo e a tentativa de vincular a OP a um pedido de venda, ocasionando o bloqueio da operação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363769027863)

**SOLUÇÃO**

Para solucionar o problema, siga os passos abaixo:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16363769029911)

 Acesse a tela **"Processo Produtivo - NOVA"** **(Produção » Cadastros » Processo Produtivo - Nova) **e localize o processo produtivo utilizado pelo produto que está apresentando o erro.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/42985880826007)

 Clique no botão **"Outras Opções".**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/42985880826391)

 Localize o campo **"Exigir pedido de venda"** e verifique a configuração atual.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/42985818798615)

 Altere a configuração para **"Opcional"** ou **"Sempre"**, conforme a necessidade do seu processo produtivo:

    • **"Opcional"**: permite lançar OPs com ou sem vínculo ao pedido de venda. Com esta opção na produção de múltiplos produtos, caso algum necessite do pedido, o sistema irá gerar os devidos pedidos conforme a necessidade.

    • **"Sempre"**: exige obrigatoriamente o vínculo da OP a um pedido de venda.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/42985818801175)

 Salve as alterações realizadas no **Processo Produtivo.**

![6](https://ajuda.sankhya.com.br/hc/article_attachments/42985818801815)

 Refaça o processo de lançamento das OPs.
 

![outras configurações do processo.png](https://ajuda.sankhya.com.br/hc/article_attachments/42985880830487)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363781188503)

**CAUSA**

O erro ocorre devido a uma divergência na configuração do campo **"Exigir pedido de venda" **entre os diferentes processos produtivos utilizados nos itens do pedido.

O bloqueio pode ocorrer, por exemplo, quando o produto que aparece na primeira posição da ordenação possui um processo produtivo configurado como **"Nunca"**. Também pode ocorrer quando há pedidos com necessidade de produção e nenhum dos processos produtivos da planta está configurado com **"Exigir pedido de venda"** como **"Opcional"**.

Recomenda-se padronizar a configuração do campo “Exigir pedido de venda” entre todos os processos produtivos.