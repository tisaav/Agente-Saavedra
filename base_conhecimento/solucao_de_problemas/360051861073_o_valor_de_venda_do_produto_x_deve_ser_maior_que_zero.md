# O valor de venda do produto 'X' deve ser maior que ZERO

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360051861073-O-valor-de-venda-do-produto-X-deve-ser-maior-que-ZERO](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051861073-O-valor-de-venda-do-produto-X-deve-ser-maior-que-ZERO)  
> **ID:** `360051861073` | **Última Atualização:** 2026-07-22T15:30:12Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15936103722647)

 MENSAGEM:**

[CORE_E01699] O valor de venda do produto 'X' deve ser maior que ZERO.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15936125748887)

 CAUSA:**

Ao tentar confirmar uma nota de compra com Tipo de Operação que atualize 'preço de venda', e o preço "calculado" seja menor que o preço de tabela atual, a mensagem poderá ser apresentada.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15936103724695)

 SOLUÇÃO:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15936103725719)

 Sintonize com os usuários certificados da sua empresa, que possuam detalhes dos processos internos, se de fato o Tipo de Operação utilizado deverá ter o campo 'Precifica' definido com a opção para atualização de preço de venda:

**Tela: **Tipos de Operação - TOP >> **Aba**: Geral >> **Campo:** Precifica:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15936116499991)

 Caso a configuração acima esteja incorreta, realize os devidos ajustes e refaça o lançamento.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15936103727255)

 Caso a atualização de preço de venda deva ocorrer, possivelmente a mensagem está sendo apresentada pois considerando sua Fórmula de precificação atual, diante valor informado para o item, o preço que está sendo calculado é MENOR que o preço de tabela atual.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15936125754007)

 **Caso em sua empresa, esse cenário seja permitido, o parâmetro **DIMINUIPRECO ***(Tela Preferências/Configurações/Avançado)*** **deve ser ajustado para **LIGADO**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15936103493271)

**

![4](https://ajuda.sankhya.com.br/hc/article_attachments/15936103729431)

 **Realizado o ajuste, teste a confirmação da nota. Valide a atualização de preço gerada através da tela 'Variação de Preços de Produtos' e alinhe sobre a permanência do parâmetro ligado para situações futuras.