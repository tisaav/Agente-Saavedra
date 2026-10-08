# Importador de dados - ORA-00001: restrição exclusiva (SANKHYA.PK_XXX) violada

> **Módulo:** Solucao de Problemas | **Subseção:** Acessos/Banco de Dados  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30460733237783-Importador-de-dados-ORA-00001-restri%C3%A7%C3%A3o-exclusiva-SANKHYA-PK-XXX-violada](https://ajuda.sankhya.com.br/hc/pt-br/articles/30460733237783-Importador-de-dados-ORA-00001-restri%C3%A7%C3%A3o-exclusiva-SANKHYA-PK-XXX-violada)  
> **ID:** `30460733237783` | **Última Atualização:** 2026-07-22T14:35:48Z

---

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31540980330775)

CAUSA:**

O erro **ORA-00001: restrição exclusiva violada** ocorre quando há uma tentativa de inserir um registro que viola a restrição de chave primária (**PK**) na tabela. Esse problema geralmente acontece devido à duplicação de valores na coluna utilizada como chave primária, impedindo a inserção do novo registro.

No contexto do **Importador de Dados**, esse erro pode surgir quando a coluna **AD_IDEXTERNO** não está corretamente preenchida ou quando um registro já existente no banco de dados está sendo inserido novamente sem a devida atualização.

 

#### **Utilização da Coluna AD_IDEXTERNO no Importador de Dados**

A coluna **AD_IDEXTERNO** funciona como uma **chave primária (PK)** para o **Importador de Dados**, determinando se a operação realizada será um **INSERT** ou um **UPDATE**. No entanto, essa funcionalidade não substitui a validação do banco de dados, que pode gerar um erro caso detecte duplicidade de **PK** na tabela.

Se o campo **AD_IDEXTERNO** estiver vazio, o **Importador de Dados** tentará realizar um **INSERT**. Entretanto, caso o arquivo **.csv** contenha um registro com uma **PK** já existente no banco, ocorrerá um erro de **PK duplicada**.

Por outro lado, se o campo **AD_IDEXTERNO** já estiver preenchido no banco de dados, o **Importador de Dados** identificará o registro e realizará um **UPDATE**, evitando a tentativa de inserção de um registro duplicado.

##  

#### **Procedimento para Atualização Correta**

Caso esteja importando um arquivo com o objetivo de atualizar algum dado já existente no sistema, e não a inserção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31540980331159)

 Crie o campo **AD_IDEXTERNO** na tabela em questão, caso ainda não exista;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31540980331415)

 Preencha o campo** AD_IDEXTERNO **nos registros existentes. Recomenda-se utilizar o mesmo valor da **PK** da tabela. Exemplo, se estamos importando um CSV para atualização de um produto, acesse o cadastro desse produto e preencha o AD_EDEXTERNO.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31541008459159)

 No arquivo CSV, preencha também o campo **AD_IDEXTERNO** com os mesmos valores preenchidos no sistema.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31541008459927)

 Execute a importação via **Importador de Dados**, utilizando o arquivo **.csv** atualizado.

- 

  - 

Mantenha marcadas as opções abaixo:

    - 

**"Atualizar os registros"**

    - 

**"Validar Regras de Negócio"**

**Observação: **diferente da inserção de novos registros, na atualização de registros existentes obrigatoriamente temos que preencher o AD_IDEXTERNO, tanto no sistema quanto no CSV.

Seguindo este procedimento evita-se a violação de restrições de **PK** no banco de dados e garante-se uma atualização eficiente dos registros sem erros de duplicidade.