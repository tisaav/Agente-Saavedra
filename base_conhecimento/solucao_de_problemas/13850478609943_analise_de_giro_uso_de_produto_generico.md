# Analise de Giro: Uso de produto genérico

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/13850478609943-Analise-de-Giro-Uso-de-produto-gen%C3%A9rico](https://ajuda.sankhya.com.br/hc/pt-br/articles/13850478609943-Analise-de-Giro-Uso-de-produto-gen%C3%A9rico)  
> **ID:** `13850478609943` | **Última Atualização:** 2026-07-22T14:59:47Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867656916887)

 SITUAÇÃO:**
Ao realizar o uso de **"Produto Genérico"** em um novo produto e agrupar a este outros produtos pela aba de **"Produtos Específicos"**, gostaria que ao processar uma matriz de análise de giro para os produtos de forma agrupada, traga a mesma **Sugestão de Compra**, quando os produtos estiverem desagrupados.
 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867664047383)

SOLUÇÃO:**
 

**Produtos Desagrupados:** estes são analisados de maneira **individual**, linha a linha;

**Produtos Agrupados:** este é apresentado em uma única linha,  utilizando o Produto genérico, trazendo consigo:
 
***

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867656923543)

 *Cálculos: **

**Estoque mínimo:** soma de todos os **Estoque mínimo **dos produtos vinculados ao **Produto genérico**;
 

**Estoque:**  soma de todos o **Estoque** dos  produtos vinculados ao Produto genérico;
 

**Sug. Compra:** total do Est. mínimo + % acréscimo de compras - total do Estoque + Vendas Pendentes - Compras Pendentes.
 

***

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867664051479)

 ***Diferenças entre a** "Sugestão de Compra" **dos produtos agrupados e desagrupados:
 
As diferenças são devido a que o sistema compreende a situação analisando os **estoques**.
 
As diferenças na totalização ocorre por conta do **estoque **de cada produto.

- 
Quando a Matriz de Análise de giro analisa os **produtos separados**, ele considera o Estoque de forma individual (um a um) e gera a sugestão de compra 

- 
Quando a Matriz de Análise de giro analisa os **produtos de forma conjunta**, ele **soma **os estoques de todos os produtos e isso causará uma diferença final entre as sugestões de compra.

**Exemplo:**
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13850388452887)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13850438402583)

 
***

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867664055959)

 *Análise desagrupada:**
 
Se realizar o seguinte cálculo de linha a linha de cada produto, a aba **"Sug. Compra"**, irá conferir com o cálculo.
 
Prod. 12 > 1017,00 + 20% - 0,54 = 1.219,86 (No sistema arredonda, pois não conseguimos comprar produtos "fracionado").
 
Prod. 673 > 346,86 + 20% - 695,09 = -278,85 (Não há sugestão, pois o meu estoque é maior que que estoque mínimo).
 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867664057623)

CAUSA:**
A diferença que ocorre entre as Sugestões de Compra se trata de comportamento do sistema, conforme foi apresentado os cálculos abaixo.