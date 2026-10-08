# Esse produto possui unidades alternativas cadastradas e o controle adicional não pode ser alterado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109654-Esse-produto-possui-unidades-alternativas-cadastradas-e-o-controle-adicional-n%C3%A3o-pode-ser-alterado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109654-Esse-produto-possui-unidades-alternativas-cadastradas-e-o-controle-adicional-n%C3%A3o-pode-ser-alterado)  
> **ID:** `360044109654` | **Última Atualização:** 2026-07-22T15:54:46Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16784254052887)

 MENSAGEM:**

[CORE_E03864]: Esse produto possui unidades alternativas cadastradas e o controle adicional não pode ser alterado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16784254058519)

 SOLUÇÃO:**

- O sistema valida a alteração de controle adicional caso o controle anterior ou novo seja do tipo "Lista" ou "Livre" e exista alguma unidade alternativa cadastrada para o produto.

- Essa validação ocorre visto que para os dois casos tratam-se de controles que normalmente ficam registrados em cadastros e não apenas nas movimentações. Dessa forma, a liberação de alterações de controle poderão gerar inconsistências caso existam unidades alternativas com controle informado.

- Por exemplo, em um controle por lista, seria possível registrar uma unidade alternativa sendo "Caixa Azul" e outra "Caixa Vermelha", e uma mudança no tipo do controle deixaria estes cadastros de unidade alternativa inconsistentes.

Suponhamos que a empresa sempre trabalhou com "Canetas" controladas por Lista (Azul/Vermelha), e a partir de agora esse controle não irá mais existir. Para esse cenário é necessário compreender os detalhes que geram essa validação e avaliar junto ao implantador da empresa a aplicação das **práticas recomendadas** abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16784254065303)

 Caso não existam movimentações para as unidades alternativas cadastradas, será permitido a exclusão de seus cadastros, e consequentemente a alteração do controle adicional. Para os demais casos, avaliar os próximos tópicos;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16784246605975)

 Inventariar os produtos que sofrerão a alteração, zerando seu estoque e finalizando todos os movimentos em aberto para evitar inconsistências;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16784246610071)

 Inative os respectivos produtos e realize novos cadastros desses, informando o controle adicional correto e desejado;

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16784246612503)

 Realize os ajustes de estoque de entrada para os novos produtos, conforme controle adicional atual cadastrado para os mesmos;

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16784246618775)

 Para relatórios ou análises de períodos anteriores, é importante considerar que os produtos foram alterados.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16784246625815)

 CAUSA:**

Ao tentar alterar o controle adicional de um produto, caso o controle anterior ou novo seja do tipo "Lista" ou "Livre" e exista alguma unidade alternativa cadastrada, essa alteração não será permitida.