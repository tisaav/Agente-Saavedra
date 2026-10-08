# ORA-20101: Código Barra REPETIDO na unidade alternativa para o produto XXXX ORA-06512: em "SANKHYA.TRG_INC_UPT_TGFVOA_CODBARRA", line XX ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPT_TGFVOA_CODBARRA'

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20026120604567-ORA-20101-C%C3%B3digo-Barra-REPETIDO-na-unidade-alternativa-para-o-produto-XXXX-ORA-06512-em-SANKHYA-TRG-INC-UPT-TGFVOA-CODBARRA-line-XX-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho-SANKHYA-TRG-INC-UPT-TGFVOA-CODBARRA](https://ajuda.sankhya.com.br/hc/pt-br/articles/20026120604567-ORA-20101-C%C3%B3digo-Barra-REPETIDO-na-unidade-alternativa-para-o-produto-XXXX-ORA-06512-em-SANKHYA-TRG-INC-UPT-TGFVOA-CODBARRA-line-XX-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho-SANKHYA-TRG-INC-UPT-TGFVOA-CODBARRA)  
> **ID:** `20026120604567` | **Última Atualização:** 2026-07-22T14:51:19Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20026115007511)

 **MENSAGEM:**

ORA-20101: Código Barra REPETIDO na unidade alternativa para o produto XXXX
ORA-06512: em "SANKHYA.TRG_INC_UPT_TGFVOA_CODBARRA", line XX
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPT_TGFVOA_CODBARRA'.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20026120603287)

CAUSA:**

Quando o produto que deseja duplicar, trabalha com unidade alternativa, já existe o código de barras da unidade alternativa na tabela TGFVOA (Volume alternativa) e não há como alterá-lo antes de salvar a cópia do novo produto.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20026120602391)

SOLUÇÃO:**

Clique no botão duplicar na rotina Cadastro de **Produtos** *(Configurações » Cadastros » Produtos)* será aberto o pop-up 'Copiar Também' desmarque a opção 'Unidades Alternativas' e salve.

 

![produtos 22-12.png](https://ajuda.sankhya.com.br/hc/article_attachments/20054229290007)