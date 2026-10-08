# A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK_TGFCOT_CODNAT_TGFNAT". O conflito ocorreu no banco de dados "SANKHYA_PROD", tabela "SANKHYA.TGFNAT", column 'CODNAT'

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360055287353-A-instru%C3%A7%C3%A3o-INSERT-conflitou-com-a-restri%C3%A7%C3%A3o-do-FOREIGN-KEY-FK-TGFCOT-CODNAT-TGFNAT-O-conflito-ocorreu-no-banco-de-dados-SANKHYA-PROD-tabela-SANKHYA-TGFNAT-column-CODNAT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055287353-A-instru%C3%A7%C3%A3o-INSERT-conflitou-com-a-restri%C3%A7%C3%A3o-do-FOREIGN-KEY-FK-TGFCOT-CODNAT-TGFNAT-O-conflito-ocorreu-no-banco-de-dados-SANKHYA-PROD-tabela-SANKHYA-TGFNAT-column-CODNAT)  
> **ID:** `360055287353` | **Última Atualização:** 2026-07-22T15:28:37Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15916030630039)

 MENSAGEM**:

A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK_TGFCOT_CODNAT_TGFNAT". O conflito ocorreu no banco de dados "SANKHYA_PROD", tabela "SANKHYA.TGFNAT", column 'CODNAT'.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15916077254039)

 CAUSA:**

Ocorre quando não existe ou a natureza informada nas Preferências para gerar a cotação não é analítica e/ou não esta ativa.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15916077257495)

 SOLUÇÃO:**

Para correção seguir os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15916030642583)

 Acesse o botão   

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360089396074)

  em Comercial » Rotinas » Análise de Giro
No campo 'Natureza', escolha uma Natureza do tipo 'Analítica' e 'Ativa'

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360089396414)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15916030650519)

 Após os ajustes, pode-se Gerar a Cotação novamente.