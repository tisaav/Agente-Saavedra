# Item X do pedido/nota YYYY já foi faturado. Não pode ser excluído.

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360058522254-Item-X-do-pedido-nota-YYYY-j%C3%A1-foi-faturado-N%C3%A3o-pode-ser-exclu%C3%ADdo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058522254-Item-X-do-pedido-nota-YYYY-j%C3%A1-foi-faturado-N%C3%A3o-pode-ser-exclu%C3%ADdo)  
> **ID:** `360058522254` | **Última Atualização:** 2026-08-01T01:31:44Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16273175167255)

**MENSAGEM**

[CORE_E01541] Erro ao remover entidade: item do pedido/nota já foi faturado. não pode ser excluído.
 

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/42388429872919)

**SITUAÇÃO**

Esta mensagem aparece ao tentar excluir um pedido de venda no Portal de vendas. Isso ocorre quando o sistema identifica que o item possui um faturamento vinculado ou uma quantidade entregue preenchida, impedindo a exclusão do documento por questões de integridade de dados.
 

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16273175178775)

**SOLUÇÃO**

A exclusão não será permitida até que as notas de destino sejam tratadas. Siga os passos abaixo para analisar e corrigir o cenário:
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16273175180823)

 Identifique o documento de destino. acesse o pedido de venda, selecione o item e clique em **"Outras Opções"** > **"Documentos Relacionados"**. na grade inferior, dê um duplo clique no documento de destino para visualizá-lo.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16273168008215)

 Analise o documento e verifique se o item possui **"Quantidade Entregue"** preenchida indevidamente, mesmo que não haja uma nota fiscal ativa vinculada.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/16273168009239)

 Realize a tratativa necessária:
 

- 

Nota destino não confirmada ou NF-e de terceiros: exclua o lançamento.
 

1. 

Nota fiscal eletrônica dentro do prazo: proceda com o cancelamento da mesma.
 

1. 

Desligar a Nota: na Central de Vendas, utilize a opção **"Outras Opções"** > **"Desligar a Nota dos Pedidos"** para remover a vinculação entre a nota e o pedido.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/16273175185431)

 Caso excepcional (quantidade entregue preenchida sem nota): se confirmado que não existe nota fiscal, mas o campo **"QTDENTREGUE"** permanece preenchido, realize uma intervenção via banco de dados.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/42388429875479)

 Após a execução da correção, tente novamente excluir o pedido.
 

**Observação:** se o erro for recorrente, abra um chamado técnico para verificar possíveis falhas em triggers (como a **"TRG_UPT_TGFITE"**) ou customizações que impactem o preenchimento indevido da quantidade entregue.
 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16273175189527)

**CAUSA**

O sistema bloqueia a exclusão para manter a integridade dos dados ao detectar que o item foi faturado ou possui movimentação registrada. isso pode ser causado por:
 

- 

Existência de nota fiscal de destino vinculada;
 

1. 

Falha na trigger de atualização de estoque ou quantidade entregue;
 

1. 

Exclusão de notas fiscais sem atualização do pedido original;
 

1. 

Interrupções no processo de faturamento ou customizações indevidas.