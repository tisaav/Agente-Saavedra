# ORA-12899: valor muito grande para a coluna "SANKHYA"."TGFEDFDC170"."CST_IPI"

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/27010884310807-ORA-12899-valor-muito-grande-para-a-coluna-SANKHYA-TGFEDFDC170-CST-IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/27010884310807-ORA-12899-valor-muito-grande-para-a-coluna-SANKHYA-TGFEDFDC170-CST-IPI)  
> **ID:** `27010884310807` | **Última Atualização:** 2026-07-22T14:40:18Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27119161292951)

 MENSAGEM:**

ORA-12899: valor muito grande para a coluna "SANKHYA"."TGFEDFDC170"."CST_IPI" (real: 3, máximo: 2)

 

Esse é um erro do Oracle que indica que o valor que está sendo inserido "CST_IPI da tabela ultrapassa o tamanho permitido. A coluna foi modelada para aceitar no máximo 2 caracteres, mas o valor que está sendo fornecido tem 3 caracteres.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27119161298839)

 SOLUÇÃO:**

**Verifique o valor de ****CST_IPI:** o valor que está sendo inserido na coluna CST_IPI tem que ter no máximo 2 caracteres.

É preciso avaliar o valor nos dados de origem para que ele respeite o limite de 2 caracteres.

 

Conforme o Guia prático, **o caractere *(Asterisco) **aposto ao lado do tamanho do campo **indica que o campo deve ser informado com aquela quantidade exata de caracteres.**

 

![Valor muito grande para a coluna 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/27119297112471)

 

Na tabela no banco de dados o campo aceita 2 caracteres.

 

![Valor muito grande para a coluna 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/27119297115031)

 

É necessário pegar um monitor de consultas para identificar o número da nota que está acontecendo o problema e corrigir na raiz.