# A linha referenciada na tabela TGFGRU, não está cadastrada, ou não está ativa, ou não é analítica

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110014-A-linha-referenciada-na-tabela-TGFGRU-n%C3%A3o-est%C3%A1-cadastrada-ou-n%C3%A3o-est%C3%A1-ativa-ou-n%C3%A3o-%C3%A9-anal%C3%ADtica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110014-A-linha-referenciada-na-tabela-TGFGRU-n%C3%A3o-est%C3%A1-cadastrada-ou-n%C3%A3o-est%C3%A1-ativa-ou-n%C3%A3o-%C3%A9-anal%C3%ADtica)  
> **ID:** `360044110014` | **Última Atualização:** 2026-07-22T15:54:00Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16949614520215)

 MENSAGEM:**

A linha referenciada na tabela TGFGRU, não está cadastrada, ou não está ativa, ou não é analítica.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16949627403287)

 SITUAÇÃO:**

Ao salvar a inclusão de um produto, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16949627408535)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16949614527255)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*

- Identifique no cadastro do produto, aba: **"Geral"**, campo **"Grupo"**, o código e nome do grupo vinculado ao produto.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16949614536983)

 Acesse: *Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços*

- Pesquise pelo grupo, após identifica-lo, verifique se o **Grupo **está **'Ativo'** e se o mesmo é **'Analítico'**. Se não estiver **Ativo**, verifique a possibilidade de ativá-lo.

- Se não for Analítico, verifique na hierarquia qual é o GRUPO a ser selecionado do tipo **'Analítico'** e informe o código ao produto.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16949627418647)

 NOTA:**

O grupo **0 - <SEM GRUPO>**, é um grupo default do sistema e deve existir na base de dados, considere não exclui-lo do sistema.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16949614543767)

 CAUSA:**

Ocorre quando o Grupo vinculado ao produto não está devidamente configurado para utilização.