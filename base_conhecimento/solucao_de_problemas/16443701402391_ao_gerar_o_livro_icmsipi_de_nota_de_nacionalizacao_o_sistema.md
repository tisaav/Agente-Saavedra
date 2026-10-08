# Ao gerar o Livro ICMS/IPI de nota de nacionalização, o sistema não está somando o valor do ICMS ao valor contábil

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16443701402391-Ao-gerar-o-Livro-ICMS-IPI-de-nota-de-nacionaliza%C3%A7%C3%A3o-o-sistema-n%C3%A3o-est%C3%A1-somando-o-valor-do-ICMS-ao-valor-cont%C3%A1bil](https://ajuda.sankhya.com.br/hc/pt-br/articles/16443701402391-Ao-gerar-o-Livro-ICMS-IPI-de-nota-de-nacionaliza%C3%A7%C3%A3o-o-sistema-n%C3%A3o-est%C3%A1-somando-o-valor-do-ICMS-ao-valor-cont%C3%A1bil)  
> **ID:** `16443701402391` | **Última Atualização:** 2026-07-22T14:55:13Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912686588311)

 SITUAÇÃO:**

Após cadastrar uma nota de compra de nacionalização e gerar o Livro ICMS/IPI, o valor contábil não condiz com o valor total da nota. A diferença em questão se refere ao valor do imposto ICMS.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16912674024855)

 SOLUÇÃO:**

Para que o valor do ICMS seja considerado no valor contábil nas notas cujo CST é diferente de 00, é necessário que a empresa seja optante do Simples Nacional.
 Do contrário, caso a empresa não seja optante do regime, o sistema só irá somar os valores do imposto nas notas que possuem o CST 00.