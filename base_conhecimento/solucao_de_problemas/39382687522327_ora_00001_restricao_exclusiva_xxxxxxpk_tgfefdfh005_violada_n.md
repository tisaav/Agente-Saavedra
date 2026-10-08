# ORA-00001: restrição exclusiva (XXXXXX.PK_TGFEFDFH005) violada na geração do relatório EFD - Bloco H

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39382687522327-ORA-00001-restri%C3%A7%C3%A3o-exclusiva-XXXXXX-PK-TGFEFDFH005-violada-na-gera%C3%A7%C3%A3o-do-relat%C3%B3rio-EFD-Bloco-H](https://ajuda.sankhya.com.br/hc/pt-br/articles/39382687522327-ORA-00001-restri%C3%A7%C3%A3o-exclusiva-XXXXXX-PK-TGFEFDFH005-violada-na-gera%C3%A7%C3%A3o-do-relat%C3%B3rio-EFD-Bloco-H)  
> **ID:** `39382687522327` | **Última Atualização:** 2026-07-22T13:32:14Z

---

### 

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382687516695)

 **MENSAGEM**

Ora-00001: restrição exclusiva (xxxxxx.pk_tgfefdfh005) violada

 

### 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712685591)

 **SITUAÇÃO**

Ao tentar gerar o relatório **"EFD - Fiscal"** (Livros Fiscais Conexão EFD - Fiscal), o sistema apresenta um erro de restrição exclusiva no banco de dados, impedindo a geração do arquivo.

 

### 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382687516951)

 **SOLUÇÃO**

Para resolver o erro, verifique o preenchimento do campo **"Data de Inventario em substituição ao Bloco K"** na tela de geração do EFD. Existem duas situações possíveis:

 

**Situação 1: Quando não é necessário gerar o Bloco K**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712686103)

  Acesse a tela **"**EFD - Fiscal ICMS/IPI**"** (Livros Fiscais » Conexão » EFD - Fiscal ICMS/IPI).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712688663)

  Localize o campo **"Data de Inventario em substituição ao Bloco K"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712688919)

  Remova a data preenchida neste campo, deixando-o em branco.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712689175)

  Gere novamente o arquivo EFD. O sistema processará corretamente sem apresentar o erro.

 

 

**Situação 2: Quando é necessário gerar o Bloco K**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712686103)

  Acesse a tela **"EFD - Fiscal"** (Livros Fiscais Conexão EFD - Fiscal).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712688663)

  Verifique se o campo **"Data de Inventario em substituição ao Bloco K"** está preenchido.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712688919)

  Certifique-se de que foi realizada a cópia do estoque para a data informada.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382712689175)

  Preencha também o campo **"Contagem para o K200"** com a mesma data do inventário de substituição.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382687519511)

  Gere novamente o arquivo EFD. O sistema processará corretamente o Bloco H e o Bloco K sem apresentar erros.

 

 

### 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39382687519639)

 **CAUSA**

O erro citado, pode ter muitas causas, no caso citado nesse artigo, ocorre devido à duplicidade no insert do registro H005. Quando o campo "Data de Inventario em substituição ao Bloco K" está preenchido, mas a configuração para geração do Bloco K está incompleta ou incorreta, o sistema tenta inserir o mesmo registro duas vezes na tabela TGFEFDFH005, violando a chave primária (PK_TGFEFDFH005).

Isso acontece porque o sistema identifica a necessidade de gerar informações de inventário, mas encontra inconsistências entre o preenchimento do campo **"Data do inventário de substituição"** e o campo **"Contagem para o K200"**, causando o processamento duplicado do registro.

Obs: O campo "**Data de Inventario em substituição ao Bloco K" só ficará visível caso o parâmetro GERBLHSUBSK estiver ligado.**