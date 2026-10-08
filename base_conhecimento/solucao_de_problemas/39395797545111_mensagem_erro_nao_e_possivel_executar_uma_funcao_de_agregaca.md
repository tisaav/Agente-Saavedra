# MENSAGEM ERRO: Não é possível executar uma função de agregação em uma expressão que contenha uma agregação ou subconsulta.

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39395797545111-MENSAGEM-ERRO-N%C3%A3o-%C3%A9-poss%C3%ADvel-executar-uma-fun%C3%A7%C3%A3o-de-agrega%C3%A7%C3%A3o-em-uma-express%C3%A3o-que-contenha-uma-agrega%C3%A7%C3%A3o-ou-subconsulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/39395797545111-MENSAGEM-ERRO-N%C3%A3o-%C3%A9-poss%C3%ADvel-executar-uma-fun%C3%A7%C3%A3o-de-agrega%C3%A7%C3%A3o-em-uma-express%C3%A3o-que-contenha-uma-agrega%C3%A7%C3%A3o-ou-subconsulta)  
> **ID:** `39395797545111` | **Última Atualização:** 2026-07-24T12:42:20Z

---

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39395797536535)

 SITUAÇÃO

Este erro ocorre ao tentar gerar o arquivo SPED Fiscal na tela **"EFD - Fiscal ICMS/IPI"** (Livros Fiscais » Conexão » EFD - Fiscal ICMS/IPI). O sistema apresenta a mensagem de erro relacionada a funções de agregação no banco de dados, impedindo a conclusão do processamento.

 

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39395797537815)

 SOLUÇÃO

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39395797538583)

 Atualize o **"Módulo Livros Fiscais"** para a versão **5.21.2** ou superior.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39395797538967)

 Realize a atualização primeiramente em **ambiente de teste** para validação.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39395797539479)

 Após validar o funcionamento correto, aplique a atualização em **ambiente de produção**.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39395793812119)

 Processe novamente a geração do SPED Fiscal.
 

 

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39395797540375)

 CAUSA

O erro é causado por uma **inconsistência na estrutura de consultas SQL** utilizada pelo sistema em versões anteriores à 5.21.2 do Módulo Livros Fiscais. A correção foi implementada na versão 5.21.2, que ajusta as funções de agregação utilizadas no processamento do SPED Fiscal.

 

###