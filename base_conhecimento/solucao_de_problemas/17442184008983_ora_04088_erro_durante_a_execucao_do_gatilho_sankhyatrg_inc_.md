# ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_TGFITE_AFTER'

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/17442184008983-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho-SANKHYA-TRG-INC-TGFITE-AFTER](https://ajuda.sankhya.com.br/hc/pt-br/articles/17442184008983-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho-SANKHYA-TRG-INC-TGFITE-AFTER)  
> **ID:** `17442184008983` | **Última Atualização:** 2026-07-22T14:53:23Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17442183944343)

 **MENSAGEM:**

[ORA-00001]: restrição exclusiva (SANKHYA.PK_TGFITE) violada
[ORA-06512]: em "SANKHYA.TRG_INC_TGFITE_AFTER", line 27
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_INC_TGFITE_AFTER'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17442192929943)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17444986455447)

 Consulte as tabelas: TGFITE_INC, TGFITE_UPD, TGFITE_DLT, TGFCAB_UPT, TGFCAB_DLT;

Se houver alguma informação nas tabelas mencionadas acima, as mesmas deverão ser excluídas, pois são tabelas temporárias.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17444986461463)

 Consulte também se no momento tem alguma trigger da TGFCAB e TGFITE desabilitada;

SELECT * FROM USER_TRIGGERS WHERE STATUS <> 'ENABLED' AND TABLE_NAME IN ('TGFCAB', 'TGFITE')

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17442161902487)

CAUSA:**

Ocorre quando existe linhas indevidamente na tabela: TGFITE_INC. Essa tabela recebe apenas o INSERT e DELETE em tempo de execução e sempre deve ficar vazia. Isso é controlado pelas triggers da TGFCAB e TGFITE, que em algum momento, podem ter sido desabilitadas e deixado os registros lá.

Esse erro pode ocorrer em qualquer rotina que envolta as tabelas TGFCAB e TGFITE.