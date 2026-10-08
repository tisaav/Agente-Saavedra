# Não foi possível carregar a lista de funcionários. Motivo: A subconsulta retornou mais de 1 valor

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/28148339768599-N%C3%A3o-foi-poss%C3%ADvel-carregar-a-lista-de-funcion%C3%A1rios-Motivo-A-subconsulta-retornou-mais-de-1-valor](https://ajuda.sankhya.com.br/hc/pt-br/articles/28148339768599-N%C3%A3o-foi-poss%C3%ADvel-carregar-a-lista-de-funcion%C3%A1rios-Motivo-A-subconsulta-retornou-mais-de-1-valor)  
> **ID:** `28148339768599` | **Última Atualização:** 2026-07-29T13:19:00Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28150146281623)

 MENSAGEM:**

Não foi possível carregar a lista de funcionários. 

Motivo: A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, <, <= , >, >= ou quando ela é usada como uma expressão.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28150150873623)

 SITUAÇÃO:**

Ao realizar o Reajuste Salarial por meio do caminho:

**Pessoal+ » Rotinas Folha » Reajuste Salarial**, após preencher todos os campos necessários, ocorre um erro ao tentar carregar a lista de funcionários.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/28148339753623)

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28150146290711)

** SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28150146293271)

 Identifique ****os funcionários com aviso prévio duplicado, siga os passos abaixo:**

1. Acesse a tela Configurações » Avançado » DBExplorer.

1. Execute a seguinte consulta:

*SELECT CODFUNC, COUNT(*) FROM TFPAVI*

*WHERE CODEMP = ‘xx’*

*GROUP BY CODFUNC*

*HAVING COUNT(*) > 1*

***** Trocar o 'xx' pelo código da empresa.***

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28150150883223)

 Realize o cancelamento do aviso incoerente.**

1. Acesse a tela Pessoal+ » Cadastros » Aviso Prévio;

1. Faça a busca pelo funcionários encontrado;

1. Preencha os campos de cancelamento do aviso.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/28148339760535)

 

**

![3 FINAL.png](/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE)

 ****Realize o procedimento de reajuste salarial selecionando os funcionários. Agora, o processo deve ser concluído sem que a mensagem de erro seja exibida.**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28150146288663)

 CAUSA:**

Foi identificado um registro duplicado de aviso prévio para o funcionário com sequência 2, sem que o aviso prévio da sequência anterior tenha sido cancelado.