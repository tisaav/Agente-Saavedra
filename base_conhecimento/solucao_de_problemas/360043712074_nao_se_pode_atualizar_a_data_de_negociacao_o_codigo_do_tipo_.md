# Não se pode atualizar a data de negociação, o código do tipo de negociação ou o valor da nota de uma nota que já foi baixada no financeiro

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712074-N%C3%A3o-se-pode-atualizar-a-data-de-negocia%C3%A7%C3%A3o-o-c%C3%B3digo-do-tipo-de-negocia%C3%A7%C3%A3o-ou-o-valor-da-nota-de-uma-nota-que-j%C3%A1-foi-baixada-no-financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712074-N%C3%A3o-se-pode-atualizar-a-data-de-negocia%C3%A7%C3%A3o-o-c%C3%B3digo-do-tipo-de-negocia%C3%A7%C3%A3o-ou-o-valor-da-nota-de-uma-nota-que-j%C3%A1-foi-baixada-no-financeiro)  
> **ID:** `360043712074` | **Última Atualização:** 2026-07-22T16:00:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290440023063)

 MENSAGEM:**

[ORA-20101]: Não se pode atualizar a data de negociação, o código do tipo de negociação ou o valor da nota de uma nota que já foi baixada no financeiro.Nota de Nro Único: 'X'
[ORA-06512]: em "SANKHYA.TRG_UPD_TGFCAB", line 960
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_UPD_TGFCAB'

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290425090327)

  SITUAÇÃO:**

Ao tentar alterar informações de lançamentos na Central, é apresentada a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290440030743)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290425098135)

 Acesse: Financeiro » Rotinas » Movimentação Financeira

Localize os financeiros gerados pelo respectivo lançamento e proceda com o **estorno **dos mesmos.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290425105815)

 Realizado o estorno, teste uma nova alteração dos dados desejados na respectiva 'Central'.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290425108759)

 CAUSA:**

Mensagem apresentada ao tentar alterar informações de lançamentos que possuem financeiros baixados.