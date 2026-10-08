# Quantidade de produto 'X' devolvido é maior que o total disponível para devolução das notas de venda

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179054-Quantidade-de-produto-X-devolvido-%C3%A9-maior-que-o-total-dispon%C3%ADvel-para-devolu%C3%A7%C3%A3o-das-notas-de-venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179054-Quantidade-de-produto-X-devolvido-%C3%A9-maior-que-o-total-dispon%C3%ADvel-para-devolu%C3%A7%C3%A3o-das-notas-de-venda)  
> **ID:** `360043179054` | **Última Atualização:** 2026-07-24T12:42:03Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162261769111)

 MENSAGEM:**

Quantidade de produto 'X' devolvido é maior que o total disponível para devolução das notas de venda.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162261770647)

 SITUAÇÃO:**

Mensagem apresentada ao importar XML de notas de devolução.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162314264983)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162261777175)

 Verifique quais são as notas de origem (venda) referenciadas no XML de devolução que está sendo importado.

Essa informação é visualizada na tag **<refNFe>**, conforme exemplo abaixo:

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14676728462359)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162314268567)

 Localize no **"[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)"** (através da chave acima) a nota de venda origem da devolução a ser importada. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162314270871)

 Abra a nota na Central e certifique-se que para os itens a serem devolvidos já existe uma nota de devolução vinculada:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162314274711)

 Outras Opções » **Documentos Relacionados** » Documentos de Destino:

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14685244561943)

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/12271637235351)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162314283031)

 Para o caso acima, não é possível realizar uma nova devolução para a nota de venda/origem referenciada. Alinhe internamente qual das notas procede, realizando as devidas tratativas. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162261802775)

 CAUSA:**

Mensagem apresentada quando para a nota referenciada na respectiva nota de devolução, não existem mais itens pendentes de devolução, visto que outra devolução já foi efetuada.


---

### 🔗 Links e Referências Internas:

- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)