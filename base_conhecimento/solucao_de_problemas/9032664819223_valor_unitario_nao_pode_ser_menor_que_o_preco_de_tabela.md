# Valor unitário não pode ser menor que o preço de tabela

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9032664819223-Valor-unit%C3%A1rio-n%C3%A3o-pode-ser-menor-que-o-pre%C3%A7o-de-tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/9032664819223-Valor-unit%C3%A1rio-n%C3%A3o-pode-ser-menor-que-o-pre%C3%A7o-de-tabela)  
> **ID:** `9032664819223` | **Última Atualização:** 2026-07-22T15:11:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447187143959)

 MENSAGEM: **

[CORE_E01549]  Valor unitário não pode ser menor que o preço de tabela.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447162799511)

 SITUAÇÃO: **

Ao processar importação no Portal de Importação XML ou fazer o lançamento manualmente direto nos portais a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447162801943)

 SOLUÇÃO: **

Essa é uma validação feita pelo sistema que é controlada pelo parâmetro **"Bloquear valor menor que o preço de tabela? - BLOQVLRMENORTAB".**

Quando este parâmetro estiver ativado, o sistema não permitirá informar um valor unitário menor que o preço de tabela nas Vendas.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447187159447)

 **OBSERVAÇÃO:**

O parâmetro Bloquear valor menor que o preço de tabela? - BLOQVLRMENORTAB, bloqueia apenas para **vendas, pedidos e devoluções**. Não bloqueia transferências, ou seja, para transferências está liberado para que o preço seja menor preço de tabela.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447187164951)

 CAUSA:**

Ao importar um XML ou fazer o lançamento de vendas, pedidos e/ou devoluções com o preço menor que o preço de tabela, com o parâmetro Bloquear valor menor que o preço de tabela? - BLOQVLRMENORTAB habilitado.