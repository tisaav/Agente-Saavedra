# Não é possível inserir o produto sem informar o lote quando o parâmetro LOTAUTCENT estiver ligado e o grupo de produtos não estiver validando estoque

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9034634432151-N%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-o-produto-sem-informar-o-lote-quando-o-par%C3%A2metro-LOTAUTCENT-estiver-ligado-e-o-grupo-de-produtos-n%C3%A3o-estiver-validando-estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/9034634432151-N%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-o-produto-sem-informar-o-lote-quando-o-par%C3%A2metro-LOTAUTCENT-estiver-ligado-e-o-grupo-de-produtos-n%C3%A3o-estiver-validando-estoque)  
> **ID:** `9034634432151` | **Última Atualização:** 2026-09-16T14:19:39Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672473941271)

 MENSAGEM:**

[CORE_E01165]: Não é possível inserir o produto sem informar o lote quando o parâmetro LOTAUTCENT estiver ligado e o grupo de produtos não estiver validando estoque.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672476520855)

 SITUAÇÃO:**

- Ao emitir NF-e a mensagem é apresentada;

- Ao iniciar a operação de produção.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672473947671)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672473948439)

 Na emissão da nota, verifique se o local e o lote estão sendo informados no lançamento. Caso esses campos não estejam visíveis, inclua no layout, pela tela **"Configurador de layout da nota"**;

 

***OU***

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672476527127)

 Identifique o grupo de produto que não está fazendo a validação corretamente do estoque, analise o processo produtivo e identifique a MP que está configurada com esse grupo de produto. Em seguida, corrija o grupo de produto.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16672473951639)

 CAUSA:**

Quando é lançada a NF-e sem informar lote e local, ou utilizar um grupo de produto que não está fazendo a validação corretamente do estoque.