# Registro C197  Tamanho do campo inválido COD_AJ - Registro/Campo não informado ou inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14687156126743-Registro-C197-Tamanho-do-campo-inv%C3%A1lido-COD-AJ-Registro-Campo-n%C3%A3o-informado-ou-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/14687156126743-Registro-C197-Tamanho-do-campo-inv%C3%A1lido-COD-AJ-Registro-Campo-n%C3%A3o-informado-ou-inv%C3%A1lido)  
> **ID:** `14687156126743` | **Última Atualização:** 2026-07-22T14:58:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806702736791)

 MENSAGEM:**

Registro C197 Tamanho do campo inválido COD_AJ - Registro/Campo não informado ou inválido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806700714775)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806700716183)

 Acesse a  tela **"Configurações de Ajustes de Apuração"** *(Caminho de acesso: Livros Fiscais » Arquivos » Configurações de Ajustes de Apuração);*

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806702742167)

 No ajuste código: 2 -  AJUSTE CREDITO DE ICMS SIMPLES NACIONAL Empresa - X;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806702743959)

 Tipo de Configuração: 1 - Ajustes de Documento, no 2 quadrante "Ajustes de Documentos - EFD Fiscal o campo: Código do ajuste: estava com a informação.: 1099050.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14686882630551)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806700722199)

 OBSERVAÇÃO: **

O código ajuste deve possuir 08 caracteres, os dois primeiros caracteres o sistema utiliza a UF da Empresa.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14686984345495)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806700723223)

 Após confirmar a alteração, acesse a tela **"Geração ICMS/IPI"** *(Caminho de acesso: Livros Fiscais » Arquivos » Geração ICMS/IPI)* e efetue a geração dos livros  fiscais novamente;

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806702749975)

 Na sequência, acesse a tela **"****EFD - Escrituração Fiscal Digital - ICMS/IPI"** *(Caminho de acesso: Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IP)* e gere o arquivo EFD-Escrituração Fiscal Digital ICMS/IPI' novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806702752279)

 CAUSA:**

Ocorre por informar o código de Ajuste incorretamente com a quantidade menor que o esperado no PVA no campo 'Código Ajuste'.

**Exemplo:** No PVA o campo espera 10 caracteres, na tela Configurações de Ajustes de Apuração o cadastro deve conter 08, sendo que os dois iniciais o sistema utiliza a UF da Empresa, ficando assim: MG10990505.