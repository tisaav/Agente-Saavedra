# Pedido de Compra, Compra ou Devolução de Compra não podem impactar na análise de giro

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615593-Pedido-de-Compra-Compra-ou-Devolu%C3%A7%C3%A3o-de-Compra-n%C3%A3o-podem-impactar-na-an%C3%A1lise-de-giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615593-Pedido-de-Compra-Compra-ou-Devolu%C3%A7%C3%A3o-de-Compra-n%C3%A3o-podem-impactar-na-an%C3%A1lise-de-giro)  
> **ID:** `360044615593` | **Última Atualização:** 2026-07-22T15:55:03Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589532230295)

 **MENSAGEM:**

Pedido de Compra, Compra ou Devolução de Compra não podem impactar na análise de giro.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589532233239)

 SOLUÇÃO:**

Para 'Tipos de Operação' com tipo de movimento = 'Pedido de Compra', 'Compra' ou 'Devolução de Compra', defina o campo **'Análise de Giro'** da aba **'Geral', **como **"Desconsiderar":**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15298865318807)

 

**Análise de Giro:** este campo define se as movimentações realizadas com esta TOP deverão ser consideradas na análise de giro e qual sinal será aplicado a estas movimentações. O campo apresenta as seguintes opções:

- Desconsiderar: aponta que esta TOP não participará da composição do Giro. Deve ser escolhida para operações de Compras, Pedidos e outras movimentações que não representam giro de mercadorias;

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589532234519)

 CAUSA:**

Ao salvar alterações e/ou o lançamento de um novo 'Tipo de Operação', a mensagem é apresentada quando 'Top's' com tipo de movimento = 'Pedido de Compra', 'Compra' ou 'Devolução de Compra' tem o campo 'Análise de Giro' diferente de 'Desconsiderar'.