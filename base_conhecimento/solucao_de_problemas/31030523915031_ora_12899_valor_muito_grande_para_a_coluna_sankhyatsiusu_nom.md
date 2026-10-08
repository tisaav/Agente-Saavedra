# ORA-12899: valor muito grande para a coluna “SANKHYA"TSIUSU" *NOMEUSUALTER"

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31030523915031-ORA-12899-valor-muito-grande-para-a-coluna-SANKHYA-TSIUSU-NOMEUSUALTER](https://ajuda.sankhya.com.br/hc/pt-br/articles/31030523915031-ORA-12899-valor-muito-grande-para-a-coluna-SANKHYA-TSIUSU-NOMEUSUALTER)  
> **ID:** `31030523915031` | **Última Atualização:** 2026-07-29T13:19:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31108825448855)

 ****MENSAGEM:**

ORA-12899: valor muito grande para a coluna “SANKHYA"TSIUSU" *NOMEUSUALTER"

 

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31108793574167)

**** SOLUÇÃO:**

Será necessário que o DBA faça a correção, ajustando o tamanho dos campos para torná-los compatíveis. Caso a empresa não tenha um DBA, a Unidade poderá disponibilizar um profissional para realizar esse ajuste.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/31030523912599)

 

****

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31030523912983)

 CAUSA:****

Esse erro ocorre quando a quantidade de caracteres dos campos NOMEUSU e NOMEUSUALTER da tabela TSIUSU são diferentes.

Para verificar a quantidade de caracteres cadastrada em cada campo, acesse a tela **"DBExplorer"**, busque pela tabela TSIUSU e localize os campos NOMEUSU e NOMEUSUALTER. Se os tamanhos forem diferentes, o erro será apresentado.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/31030498355863)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/31030523913495)