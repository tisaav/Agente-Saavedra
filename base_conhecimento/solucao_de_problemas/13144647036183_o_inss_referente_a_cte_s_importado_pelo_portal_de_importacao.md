# O INSS referente a CTE-s importado pelo  Portal de importação de XML não foi para a Reinf

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/13144647036183-O-INSS-referente-a-CTE-s-importado-pelo-Portal-de-importa%C3%A7%C3%A3o-de-XML-n%C3%A3o-foi-para-a-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/13144647036183-O-INSS-referente-a-CTE-s-importado-pelo-Portal-de-importa%C3%A7%C3%A3o-de-XML-n%C3%A3o-foi-para-a-Reinf)  
> **ID:** `13144647036183` | **Última Atualização:** 2026-07-22T15:00:23Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17201137159191)

 SITUAÇÃO:**

O INSS referente a CTE-s importado pelo  Portal de importação de XML não foi para a Reinf.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17156644427927)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17156644431895)

 O imposto precisa estar cadastrado na tela** "Impostos",** com as devidas configurações, para que as informações do imposto ao importar o XML da CT-e sejam apresentadas  no lançamento financeiro  na **"Movimentação Financeira"**, na opção  **"Outras opções"** em **"Outros impostos"**.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17156590476951)

 Em seguida, o campo** "Classificação Cessão M.d.Obra",** da aba **"Impostos",** no cadastro de **"Serviço"** deve estar configurado. Na tela **"Preferências",** parâmetro **GERIMPINCREINF:** ligado.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/13162275448599)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17156590483991)

 CAUSA:**

Se as informações no lançamento financeiro na tela Movimentação Financeira referente a Outros Impostos não estiverem informadas, o imposto correspondente não registra na tabela  'TGFIMF' (Imposto Financeiro) e, se o serviço não estiver informado no campo Classificação Cessão M.d.Obra, o lançamento não será apresentado no EFD- Reinf para gerar o envio.