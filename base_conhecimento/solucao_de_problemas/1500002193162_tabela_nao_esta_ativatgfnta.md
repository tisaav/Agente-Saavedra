# Tabela não está Ativa.(TGFNTA)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002193162-Tabela-n%C3%A3o-est%C3%A1-Ativa-TGFNTA](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002193162-Tabela-n%C3%A3o-est%C3%A1-Ativa-TGFNTA)  
> **ID:** `1500002193162` | **Última Atualização:** 2026-07-22T15:25:44Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302205477783)

 MENSAGEM:**

[ORA-20101]: Tabela não está Ativa.(TGFNTA)
[ORA-06512]: em "TESTE.TRG_INC_TGFTAB", line 90
[ORA-04088]: erro durante a execução do gatilho 'TESTE.TRG_INC_**TGFTAB**'

 

***

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302205479319)

 OBSERVAÇÃO:** Neste caso a tabela que não esta ativa é a Tabela de Preços (TGFTAB), como mencionado na descrição do erro.*

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302205480983)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302202221847)

 Acesse a rotina de Tabela de Preços em: *Comercial » Arquivo » Tabelas de Preços*

Verifique a tabela de preço que incidiu nos itens da nota e verifique se o campo **"Ativo"** está: **sim**.

Marque a tabela como **ativo, **ou verifique com a área responsável se os produtos da nota deveriam ter recebido outra tabela de preço, efetue o ajuste necessário.

 

![Tabela_n_o_est__Ativa._TGFNTA__1.png](https://ajuda.sankhya.com.br/hc/article_attachments/15027304475287)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302202223127)

 Após os ajustes, confirme novamente o documento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302202224279)

 CAUSA:**

Ocorre porque no momento da confirmação da nota a tabela de preço a ser utilizada não ativa.