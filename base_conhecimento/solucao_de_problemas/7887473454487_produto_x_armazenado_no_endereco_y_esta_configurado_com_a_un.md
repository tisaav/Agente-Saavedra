# Produto: X armazenado no endereço: Y está configurado com a unidade alternativa, a quantidade negociada no Pedido/Nota não é multiplo dessa unidade

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7887473454487-Produto-X-armazenado-no-endere%C3%A7o-Y-est%C3%A1-configurado-com-a-unidade-alternativa-a-quantidade-negociada-no-Pedido-Nota-n%C3%A3o-%C3%A9-multiplo-dessa-unidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/7887473454487-Produto-X-armazenado-no-endere%C3%A7o-Y-est%C3%A1-configurado-com-a-unidade-alternativa-a-quantidade-negociada-no-Pedido-Nota-n%C3%A3o-%C3%A9-multiplo-dessa-unidade)  
> **ID:** `7887473454487` | **Última Atualização:** 2026-07-22T15:12:54Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541730320791)

MENSAGEM**:

"Produto: X armazenado no endereço: Y está configurado com a unidade alternativa, a quantidade negociada no Pedido/Nota não é multiplo dessa unidade.
O Envio não foi concluído para não fracionar o Estoque.
Pedido: X"

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541730323095)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541747089431)

 Verifique na tela de **"Produto"**, na aba **"WMS"**, o endereço de picking vinculado ao produto.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450903872663)

 Verifique na tela **"Estoque/endereçamento WMS"** se o endereço picking vinculado está com o produto correto.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450903872663)

 Caso não esteja, corrija  o endereço de picking vinculado no produto para o picking correto com o produto no estoque, ou faça o inventário dos endereços para ficarem corretos com o vinculo.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541747091479)

 Verifique na tela tela **"Estoque/endereçamento WMS"** se tem mais de uma unidade armazenada no  endereço picking. Caso tenha, corrija para a unidade correta.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541747094039)

CAUSA:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541747089431)

  Produto com endereço X de picking vinculado no produto e o estoque está no endereço Y de picking sem vinculo com o produto.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16541747091479)

 Produto com mais de uma unidade armazenada no mesmo endereço picking.