# Tipo de Financeiro "Usar da Natureza Padrão" não está sendo respeitado no Financeiro. Saiba como resolver

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35099765891095-Tipo-de-Financeiro-Usar-da-Natureza-Padr%C3%A3o-n%C3%A3o-est%C3%A1-sendo-respeitado-no-Financeiro-Saiba-como-resolver](https://ajuda.sankhya.com.br/hc/pt-br/articles/35099765891095-Tipo-de-Financeiro-Usar-da-Natureza-Padr%C3%A3o-n%C3%A3o-est%C3%A1-sendo-respeitado-no-Financeiro-Saiba-como-resolver)  
> **ID:** `35099765891095` | **Última Atualização:** 2026-07-22T14:26:01Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35099734856599)

 **SITUAÇÃO:**

Ao configurar um **Tipo de Negociação** para que gere uma linha no Financeiro como **Despesa**, sendo que a **TOP** é de **Receita** (ou vice-versa), utilizando a opção de **Tipo de Financeiro = "Usar da Natureza Padrão" **na aba **"Parcelas"** do Tipo de Negociação**,** o lançamento continua sendo gerado incorretamente, sem respeitar a configuração esperada.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35099765882519)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35099734857495)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35099765884311)

 Acesse a tela **Preferências** (Caminho: Configurações » Avançado » Preferências)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35099734858519)

 Localize e verifique se o parâmetro **USACRPROJNATCAB** está habilitado.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35099734858775)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35099765885847)

 Ajuste conforme a necessidade do processo:

- 

**Habilitado:** O Financeiro seguirá sempre a configuração do cabeçalho da nota.

- 

**Desabilitado:** O Financeiro respeitará a natureza definida individualmente na Aba Parcelas do Tipo de Negociação.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35099734857367)

CAUSA:**

Esse comportamento ocorre devido ao parâmetro:

**"Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB"**

Quando **habilitado**, ele força que os campos **Projeto, Natureza e Centro de Resultado** do Financeiro sejam sempre iguais ao cabeçalho da nota.

Se houver qualquer alteração nesses campos no cabeçalho, o Financeiro será automaticamente atualizado.

Quando **desabilitado**, o sistema não altera esses dados no Financeiro, mesmo que sejam modificados no cabeçalho.

Assim, mesmo que uma natureza específica seja informada diretamente no Financeiro, o sistema sobrescreve essa informação com a **Natureza do cabeçalho da nota**, gerando o título incorretamente (sem considerar a informação **Tipo de Natureza** do cadastro de Naturezas de Receitas e Despesas).