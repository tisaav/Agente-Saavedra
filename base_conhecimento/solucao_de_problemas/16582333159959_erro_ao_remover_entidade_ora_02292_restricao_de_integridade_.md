# Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.AD_FK_XXXXXXXXXXXXX) violada - registro filho localizado"

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16582333159959-Erro-ao-remover-entidade-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-AD-FK-XXXXXXXXXXXXX-violada-registro-filho-localizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/16582333159959-Erro-ao-remover-entidade-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-AD-FK-XXXXXXXXXXXXX-violada-registro-filho-localizado)  
> **ID:** `16582333159959` | **Última Atualização:** 2026-07-22T14:55:03Z

---

** 

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582297238423)

  MENSAGEM:**

Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.AD_FK_XXXXXXXXXXXXX) violada - registro filho localizado

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582272915735)

 CAUSA:**

Ocorre quando a tabela adicional a qual a FK está relacionada impossibilita o cancelamento.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582304226711)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582333148951)

 Acesse a tela **DBExplorer** (*Configurações » Avançado » DBExplorer)*

 

Realize o SELECT a seguir na FK que o Sankhya está indicando o erro.

Copie o **AD_FK_XXXXXXXXXXXX** e cole onde está essa mesma informação no SELECT:

 

**Query para Banco de Dados Oracle:**

SELECT TABLE_NAME AS TABELA, COLUMN_NAME AS COLUNA, CONSTRAINT_NAME AS FK 
FROM USER_CONS_COLUMNS
WHERE CONSTRAINT_NAME LIKE '%AD_FK_XXXX%'

**Query para Banco de Dados SQL Server:**

SELECT TABLE_NAME AS TABELA, COLUMN_NAME AS COLUNA, CONSTRAINT_NAME AS FK
FROM INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
WHERE CONSTRAINT_NAME LIKE '%AD_FK_XXXX%'

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16583716247447)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16583733408535)

 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582288328983)

 Acesse a tela **Construtor de Telas** (*Configurações » Avançado » Construtor de Telas)*

-  Filtre o resultado da TABLE_NAME "TABELA" no campo Nome da Tabela que foi apresentado no DBExplorer:

- Selecione a linha e acesse o botão *Outras opções » Lançador » Localizar lançador*

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16583742127127)

 

-  Logo será aberto o caminho em que NUNOTA se encontra:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16583743410839)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582304232343)

 Acesse o caminho que foi apresentado e filtre pelo Nro Único da nota que está apresentado o erro. Exclua o registro, retorne ao Portal e Cancele a nota novamente.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585141368599)

 OBSERVAÇÃO: **

O erro pode aparecer em qualquer outra tela do sistema, não somente no cancelamento de notas e não necessariamente a tabela relacionada em questão poderá estar vinculada a uma tela especificamente.