# SPED FISCAL - REGISTRO C170 - CAMPO 10 CST_ICMS valores diferentes

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16034061746071-SPED-FISCAL-REGISTRO-C170-CAMPO-10-CST-ICMS-valores-diferentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/16034061746071-SPED-FISCAL-REGISTRO-C170-CAMPO-10-CST-ICMS-valores-diferentes)  
> **ID:** `16034061746071` | **Última Atualização:** 2026-07-22T14:55:37Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108305665687)

  SITUAÇÃO:**

Como o sistema gera a informação do CST e/ou CSOSN em notas de compra, para o C170 no EFD Fiscal.

 

**

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16034077956631)

 CAUSA:**

Ocorre quando o parceiro (emissor da nota) é simples nacional e não informou o Cód CSOSN.

 

**

![3.png](https://ajuda.sankhya.com.br/hc/article_attachments/16034059131799)

 SOLUÇÃO:**

 O sistema segue uma hierarquia para levar as informações para o arquivo TXT do SPED no  registro C170 no campo 10 CST_ICMS. 
Ao fazer a importação do XML pelo portal de uma nota onde o parceiro é simples nacional automaticamente leva o campo Cód. situação op. Simples nacional (CSON) preenchido, como exemplo levou para o campo o cód 102. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16108195314327)

 

Ao editar o campo deixando ele em branco a informação levada para o TXT do SPED no  registro C170 no campo 10 CST_ICMS é a segunda hierarquia que é o campo tributação, no exemplo para o campo o cód 51.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16108198903063)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108273168151)

 OBSERVAÇÃO:  **

Esse comportamento ocorre quando parceiro (emissor da nota) é simples nacional, que tem por obrigação levar no XML da nota o Cód CSOSN. 
Em parceiros LUCRO REAL ou LUCRO PRESUMIDO não é informado esse código.