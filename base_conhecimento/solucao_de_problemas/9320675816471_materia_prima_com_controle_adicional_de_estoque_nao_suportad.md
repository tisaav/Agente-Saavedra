# Matéria-prima com controle adicional de estoque não suportado: Código XXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9320675816471-Mat%C3%A9ria-prima-com-controle-adicional-de-estoque-n%C3%A3o-suportado-C%C3%B3digo-XXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/9320675816471-Mat%C3%A9ria-prima-com-controle-adicional-de-estoque-n%C3%A3o-suportado-C%C3%B3digo-XXXX)  
> **ID:** `9320675816471` | **Última Atualização:** 2026-07-22T15:08:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702130250263)

 MENSAGEM:**

[PROD_E00017]: Matéria-prima com controle adicional de estoque não suportado: XX Código XXXX.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702103396375)

 SITUAÇÃO:**

Ao configurar a composição de produto e informar uma matéria prima que tenha controle adicional como data de validade a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702103400983)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702103405719)

 O módulo Manufatura só trabalha com produtos com controle adicional, controlados por série, lista ou lote.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702103423127)

 Caso deseje utilizar data de validade nas matérias primas, o produto deve trabalhar com o tipo de controle igual a lote. Sendo assim, é necessário acesse o cadastro do **Produto** *(Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), *na aba **"Medidas e estoque"**, sub-aba **"Controle adicional"** e verifique se o campo "**Controlar por" **está definido como número de lote.

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702130285975)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702103432855)

 Selecione também a marcação **"Utiliza data de validade",** juntamente com o parâmetro **"LOTEDTVAL",** habilitado na tela **"Preferências"*** (Caminho de acesso: Configurações » Avançado » Preferências).*

 

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702130298135)

 

![3.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702103444887)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16702130316055)

 CAUSA:**

Ao tentar informar um produto que trabalha com controle adicional diferente de Série, Lote ou Lista no cadastro do produto.