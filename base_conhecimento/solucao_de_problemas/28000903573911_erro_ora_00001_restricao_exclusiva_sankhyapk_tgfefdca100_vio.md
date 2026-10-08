# [ERRO: ORA-00001] restrição exclusiva (SANKHYA.PK_TGFEFDCA100) violada

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/28000903573911--ERRO-ORA-00001-restri%C3%A7%C3%A3o-exclusiva-SANKHYA-PK-TGFEFDCA100-violada](https://ajuda.sankhya.com.br/hc/pt-br/articles/28000903573911--ERRO-ORA-00001-restri%C3%A7%C3%A3o-exclusiva-SANKHYA-PK-TGFEFDCA100-violada)  
> **ID:** `28000903573911` | **Última Atualização:** 2026-07-22T14:38:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30649050094743)

 MENSAGEM:**

[ERRO: ORA-00001] restrição exclusiva (SANKHYA.PK_TGFEFDCA100) violada

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36883086784023)

 SOLUÇÃO: **

Esse erro ocorre durante o processamento do **EFD Contribuições**, no momento em que o sistema grava os registros **A100 (Documentos de Serviço)** na tabela **TGFEFDCA100**.

A chave primária dessa tabela é composta pelos seguintes campos:

- CODEMP

- DTREF

- REGNIV1

- CODEMPESTAB

- CHAVE

Durante o processamento, o sistema exclui e recria os registros do período. Quando ocorre a violação da chave primária, significa que o **SELECT responsável pela geração está retornando duas ou mais linhas com a mesma combinação desses campos**, ocasionando a tentativa de inserir registros duplicados.

Para identificar a origem da duplicidade, siga os passos abaixo:

#####  

##### **

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36883543673495)

 Monitoramento do Processamento**

- 

Acesse a tela **Monitor de Consultas** (**Configurações > Avançado**).

- 

 Clique em **Iniciar monitoramento**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42013106955287)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36883543675287)

 **Geração do arquivo**

- 

Acesse a tela **EFD - Contribuições PIS/COFINS** (**Livros Fiscais > Conexão**).

- 

Clique em **Processar**.

- 

Quando o erro for apresentado, retorne ao **Monitor de Consultas**, clique em **Parar monitoramento** e, em seguida, em **Baixar arquivos de Log**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42013106955799)

##### **

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42028225271447)

 Identificação do Problema**

No arquivo de monitoramento, localize o comando que apresentou o erro. Para facilitar a pesquisa, procure pela palavra **"ERRO:"**.

O trecho correspondente será um **INSERT** realizado a partir de um **SELECT**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42026797039383)

O trecho correspondente será um **INSERT** realizado a partir de um **SELECT**.

Execute esse **SELECT** no **DBExplorer**.

Como a consulta retorna todos os registros que seriam inseridos, recomenda-se adaptá-la para exibir apenas os registros duplicados.

Para isso:

- mantenha no **GROUP BY** apenas os campos que compõem a chave primária;

- adicione uma cláusula **HAVING COUNT(*) > 1** para listar somente as combinações repetidas.

**Observação:** para que o **HAVING** funcione corretamente, o **GROUP BY** deve conter apenas os campos da chave primária. Caso outros campos permaneçam na cláusula, eles poderão impedir a identificação das duplicidades, pois tornam cada agrupamento único.

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42028225272343)

 Correção dos Registros Duplicados**

Após identificar os registros duplicados, realize o ajuste necessário, conforme o cenário:

- excluir o registro indevido;

- ajustar a **CHAVE** para um valor único;

- ou consolidar as informações quando houver registros redundantes.

Após a correção, processe novamente o **EFD Contribuições**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36883086785431)

 **CAUSA:**

A ocorrência é causada pela existência de registros que geram a mesma combinação dos campos que compõem a chave primária da tabela **TGFEFDCA100** (**CODEMP, DTREF, REGNIV1, CODEMPESTAB e CHAVE**).

Como consequência, durante a gravação do registro **A100**, o banco de dados impede a inserção de registros com chave duplicada e retorna o erro:

```text
[ERRO: ORA-00001] restrição exclusiva (SANKHYA.PK_TGFEFDCA100) violada
```

Portanto, é necessário identificar a origem das duplicidades e corrigi-las antes de executar novamente o processamento do **EFD Contribuições**.

 

![Erro ao gerar SPED por causa notas de serviço duplicadas  1.png](https://ajuda.sankhya.com.br/hc/article_attachments/30649050097559)