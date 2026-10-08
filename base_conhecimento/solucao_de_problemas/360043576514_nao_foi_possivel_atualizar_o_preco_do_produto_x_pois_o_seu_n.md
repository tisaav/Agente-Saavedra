# Não foi possível atualizar o preço do produto "X" pois o seu novo preço "R$" é menor que o preço "R$" da regra da tabela "0"

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043576514-N%C3%A3o-foi-poss%C3%ADvel-atualizar-o-pre%C3%A7o-do-produto-X-pois-o-seu-novo-pre%C3%A7o-R-%C3%A9-menor-que-o-pre%C3%A7o-R-da-regra-da-tabela-0](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043576514-N%C3%A3o-foi-poss%C3%ADvel-atualizar-o-pre%C3%A7o-do-produto-X-pois-o-seu-novo-pre%C3%A7o-R-%C3%A9-menor-que-o-pre%C3%A7o-R-da-regra-da-tabela-0)  
> **ID:** `360043576514` | **Última Atualização:** 2026-07-22T16:02:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192155820183)

 MENSAGEM:**

Não foi possível atualizar o preço do produto "X" pois o seu novo preço "R$" é menor que o preço "R$" da regra da tabela "0". Verifique as configurações do item "X" na nota "Y".

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192155824407)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192164840855)

 Sintonize com os usuários certificados da sua empresa, que possuam detalhes dos processos internos, se de fato o Tipo de Operação utilizado deverá ter o campo **"Precifica"** definido com a opção para atualização de preço de venda:

Tela: **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** » Aba: **Geral** » Campo: Precifica:

 

![top8.png](https://ajuda.sankhya.com.br/hc/article_attachments/14684309671959)

 

Caso a configuração acima esteja incorreta, realize os devidos ajustes e refaça o lançamento.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192164842007)

 Caso a atualização de preço de venda deva ocorrer, possivelmente a mensagem está sendo apresentada pois considerando sua fórmula de precificação atual, diante do valor informado para o item, o preço que está sendo calculado é MENOR que o preço de tabela atual.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192164843031)

 Caso em sua empresa, esse cenário seja permitido, o parâmetro "**DIMINUIPRECO" **na tela** "[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)" **(Caminho de acesso: *Configurações » Avançado » Preferências*)** **deve ser ajustado para ligado.

 

![preferencias10.png](https://ajuda.sankhya.com.br/hc/article_attachments/14684265627927)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192164847767)

 Realizado o ajuste, teste a confirmação da nota. Valide a atualização de preço gerada através da tela **"[Variação de Preços de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753)"** e alinhe sobre a permanência do parâmetro ligado para situações futuras.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192155830167)

 CAUSA:**

Ao tentar confirmar uma nota de compra com Tipo de Operação que atualize 'preço de venda', e o preço 'calculado' seja menor que o preço de tabela atual, a mensagem poderá ser apresentada.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)
- [Variação de Preços de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753)