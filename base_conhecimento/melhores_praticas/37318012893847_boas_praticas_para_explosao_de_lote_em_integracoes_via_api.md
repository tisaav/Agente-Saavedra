# Boas práticas para explosão de lote em integrações via API

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37318012893847-Boas-pr%C3%A1ticas-para-explos%C3%A3o-de-lote-em-integra%C3%A7%C3%B5es-via-API](https://ajuda.sankhya.com.br/hc/pt-br/articles/37318012893847-Boas-pr%C3%A1ticas-para-explos%C3%A3o-de-lote-em-integra%C3%A7%C3%B5es-via-API)  
> **ID:** `37318012893847` | **Última Atualização:** 2026-07-22T14:13:23Z

---

Durante integrações de pedidos de venda via API, podem surgir dúvidas ou inconsistências relacionadas à explosão de lote, especialmente quando o comportamento **difere entre pedidos lançados manualmente e pedidos integrados**.

Essas inconsistências geralmente estão associadas à forma como a integração gerencia a inclusão e a posterior alteração dos itens do pedido, em conjunto com a configuração da** TOP** (**Tipo de Operação**) utilizada.

 

#### **Procedimento**:

**Quando utilizar TOP com Validar Estoque p/ Reservar = Ligado**

##### **Fluxo obrigatório:**

##### 
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37323835642391)

 ****Inclua **o pedido via `CACSP.incluirNota`

- 

A explosão de lote ocorre automaticamente na inclusão.

- 

Não é necessário enviar requisição de alteração do item, para que ocorra a explosão do lote.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37323871895191)

 OBSERVAÇÃO:**

- 

O sistema pode desmembrar o item em múltiplas linhas, de acordo com o estoque disponível para cada local.

- 

Caso seja necessário enviar uma alteração via `**CACSP.incluirAlterarItemNota**`, é fundamental mapear previamente o pedido, verificando se houve alterações na estrutura, como explosão de lote e sequenciamento dos itens.
 

**Quando utilizar TOP com Validar Estoque p/ Reservar = Desligado**

##### **Fluxo obrigatório:**

##### 
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37323835642391)

 Inclua **o pedido via `CACSP.incluirNota`

##### 
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37323835642391)

 Confirme **o pedido via `CACSP.confirmarNota`

##### 
**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37323835642391)

 Altere** o item via `CACSP.incluirAlterarItemNota`.

- 

##### Nesse momento ocorre a **explosão de lote.**

#####  

##### **

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37324497830551)

 ATENÇÃO:**

- 

A explosão de lote **não acontece** sem a execução das chamadas **CACSP.confirmarNota** e **CACSP.incluirAlterarItemNota**.

- 

Todo o fluxo deve ser seguido integralmente pela integração para garantir o comportamento correto do sistema.
 

##### **

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37323871896855)

 INFORMAÇÕES ADICIONAIS:**

- 

Valide previamente a configuração da TOP utilizada na integração.

- 

Evite chamadas desnecessárias de alteração quando a TOP já realiza a reserva estoque.

- 

Mapeie corretament os itens e suas sequências após a explosão de lote.

- 

Realize testes em homologação sempre que houver alterações na TOP ou no fluxo da integração.