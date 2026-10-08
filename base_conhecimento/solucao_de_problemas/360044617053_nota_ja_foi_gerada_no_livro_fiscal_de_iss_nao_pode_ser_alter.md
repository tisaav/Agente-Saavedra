# Nota já foi gerada no Livro Fiscal de ISS, não pode ser alterada

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617053-Nota-j%C3%A1-foi-gerada-no-Livro-Fiscal-de-ISS-n%C3%A3o-pode-ser-alterada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617053-Nota-j%C3%A1-foi-gerada-no-Livro-Fiscal-de-ISS-n%C3%A3o-pode-ser-alterada)  
> **ID:** `360044617053` | **Última Atualização:** 2026-07-22T15:53:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814600257303)

 MENSAGEM:**

[ORA-20101]: Nota já foi gerada no Livro Fiscal de ISS, não pode ser alterada. Nota de Nro Único: 'X'.

[ORA-06512]: em "SANKHYA.TRG_UPD_TGFCAB", line 937

[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_UPD_TGFCAB'.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814623295383)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814600268567)

 Anote o número único do lançamento a ser excluído/alterado;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814600275351)

 Acesse a tela "**Cadastro Livro ISS"** *(Livros Fiscais » Arquivos)* e filtre por esse Número único;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814623310103)

 Clique em **aplicar;**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814623314711)

 Verifique os dados retornados pelo Modo Grade;

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814600292631)

 IMPORTANTE:**

É retornada 1 linha por item do lançamento.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814623323671)

 Valide se as linhas retornadas correspondem ao lançamento que será editado/excluído;

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814600303895)

 Através do botão **"Remover"** exclua tais registros;

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814600314391)

 Retorne ao lançamento e tente realizar a alteração/exclusão novamente.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814623345943)

 OBSERVAÇÕES:**

Caso seja apenas uma edição e necessite enviar essa nota novamente aos Livros, acesse a tela **"Geração ISS"** e gere as notas do período novamente.

Caso deseje gerar apenas esse lançamento, ao clicar em **"Gerar agora"** informe o número único dessa.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16814600328215)

 CAUSA:**

Mensagem ocorre quando para o Nro único referente ao lançamento a ser excluído existem registros na tabela de Livros Fiscais (TGFLIV).