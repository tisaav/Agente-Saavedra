# Erro de Estoque Insuficiente ao Faturar Pedido de Venda.

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39353397688215-Erro-de-Estoque-Insuficiente-ao-Faturar-Pedido-de-Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/39353397688215-Erro-de-Estoque-Insuficiente-ao-Faturar-Pedido-de-Venda)  
> **ID:** `39353397688215` | **Última Atualização:** 2026-08-01T01:24:53Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39353397682455)

  MENSAGEM**

Estoque insuficiente para o produto XXX no local XXX

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39353405248279)

  SITUAÇÃO**

Ao tentar faturar um pedido de venda já conferido, o sistema apresenta mensagem de estoque insuficiente, mesmo quando há saldo físico disponível. Esta situação ocorre frequentemente quando:

- 

O pedido utiliza reserva de estoque

- 

A **"TOP"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) está configurada para adiar atualização de estoque

- 

Há produtos com controle de lote na conferência

- 

O estoque disponível está negativo devido a excesso de reservas

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39353405249303)

  SOLUÇÃO**

Para resolver o erro de estoque insuficiente, siga os passos abaixo:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39353397683735)

  Verifique o saldo real do produto acessando a tela **"Gerência de Produtos"** (Comercial Consultas Gerência de Produtos). Confirme se há estoque físico disponível no local indicado na mensagem de erro.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39353405250839)

  Verifique as configurações da **"TOP"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) do pedido de venda. Certifique-se de que:
 

- 

A opção **"Reserva de Estoque"** está configurada adequadamente

- 

A opção **"Detalhamento de Lote na Conferência"** está compatível com o controle de lote dos produtos

- 

A configuração de **"Atualização de Estoque"** não está em conflito com a conferência

 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39353405251351)

  Se o produto possui controle de lote, verifique se os lotes foram informados corretamente na conferência do pedido. Acesse o pedido de venda e confirme se os lotes estão devidamente apontados.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39353397684887)

  Verifique se há excesso de reservas que estejam comprometendo o estoque disponível. Acesse **"Consulta de Reservas"** (Comercial Consultas Consulta de Reservas) e analise as reservas ativas para o produto em questão.

 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39353405251607)

 Caso utilize a funcionalidade **"Faturar pelo Estoque"** no **"Portal de Vendas"** (Comercial Portal de Vendas), verifique se a configuração da **"Nota Fiscal"** está definida para atualizar o estoque apenas após confirmação. Esta funcionalidade deve desconsiderar a reserva e validar apenas o saldo físico.
 

 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39353397685271)

 Se necessário, realize um ajuste de estoque para corrigir divergências entre o saldo físico e o saldo no sistema. Utilize uma TOP de ajuste, devidamente configurada para a ação.

 

**Obs: Sempre utilize a base de homologação para realizar as correções, e posteriormente replique para produção, isso evita divergências e cenários não previstos. **