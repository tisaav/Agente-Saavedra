# Nota já foi gerada no Livro Fiscal de ICMS/IPI, não pode ser alterada

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617073-Nota-j%C3%A1-foi-gerada-no-Livro-Fiscal-de-ICMS-IPI-n%C3%A3o-pode-ser-alterada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617073-Nota-j%C3%A1-foi-gerada-no-Livro-Fiscal-de-ICMS-IPI-n%C3%A3o-pode-ser-alterada)  
> **ID:** `360044617073` | **Última Atualização:** 2026-07-22T15:53:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585319936279)

 MENSAGEM:**

[ORA-20101]: Nota já foi gerada no Livro Fiscal de ICMS/IPI, não pode ser alterada. Nota de Nro Único: 'X'
[ORA-06512]: em "SANKHYA.TRG_UPD_TGFCAB", line 960
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_UPD_TGFCAB'.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585319944471)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585297962007)

 Anote o número único do lançamento a ser alterado;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585284490519)

 Acesse a tela **"Cadastro Livro ICMS/IPI"** *(Caminho de acesso: Livros Fiscais » Arquivos)* e filtre por esse número único:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15358723169943)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585319962519)

 **Clique em **Aplicar;**

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585305332887)

 Verifique os dados retornados pelo **"Modo grade";**

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585319967127)

 IMPORTANTE:** É retornada 1 linha por item do lançamento;

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585298005271)

 Valide se as linhas retornadas correspondem ao lançamento que será alterado;

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585335738775)

Através do botão (-) exclua tais registros;

 

**

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585284529815)

 **Retorne ao lançamento e tente realizar a alteração desejada.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585305362583)

 OBSERVAÇÃO:**

Caso seja apenas uma edição e necessite reenviar essa nota aos Livros, acesse a tela **"Geração ICMS/IPI"** e gere as notas do período novamente.

Caso deseje gerar apenas esse lançamento, ao clicar em **"Gerar agora"** informe o número único dessa.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16585305369367)

CAUSA:**

Mensagem ocorre quando para o Nro único referente ao lançamento a ser alterado existem registros na tabela de Livros Fiscais (TGFLIV).