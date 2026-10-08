# Erro 1867 - Quando o valor relativo à dedução do rendimento tributável correspondente a pagamento a plano de saúde do titular (vlrSaudeTit) for igual a zero, deve existir pelo menos um registro filho relativo a dependentes (infoDepSau).

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31066620022551-Erro-1867-Quando-o-valor-relativo-%C3%A0-dedu%C3%A7%C3%A3o-do-rendimento-tribut%C3%A1vel-correspondente-a-pagamento-a-plano-de-sa%C3%BAde-do-titular-vlrSaudeTit-for-igual-a-zero-deve-existir-pelo-menos-um-registro-filho-relativo-a-dependentes-infoDepSau](https://ajuda.sankhya.com.br/hc/pt-br/articles/31066620022551-Erro-1867-Quando-o-valor-relativo-%C3%A0-dedu%C3%A7%C3%A3o-do-rendimento-tribut%C3%A1vel-correspondente-a-pagamento-a-plano-de-sa%C3%BAde-do-titular-vlrSaudeTit-for-igual-a-zero-deve-existir-pelo-menos-um-registro-filho-relativo-a-dependentes-infoDepSau)  
> **ID:** `31066620022551` | **Última Atualização:** 2026-07-29T13:19:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31284772345495)

 MENSAGEM:**

Erro 1867 - Quando o valor relativo à dedução do rendimento tributável correspondente a pagamento a plano de saúde do titular (vlrSaudeTit) for igual a zero, deve existir pelo menos um registro filho relativo a dependentes (infoDepSau).

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31284772355991)

 SITUAÇÃO:**

Ao tentar enviar os eventos do **S1210.**

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31284772358295)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31284772359959)

  Verifique qual evento de plano de saúde está sendo descontado em folha do colaborador referente ao plano de saúde do dependente;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31284772362007)

 Verifique se no cadastro do dependente está com o devido cadastro deste plano de saúde identificado;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31284772366231)

 Após ajustar o cadastro, bloqueie as folhas, libere-as novamente e, em seguida, gere os eventos **S1210** e tente enviá-los.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31284831799959)

 CAUSA:**

Esse erro ocorre quando o campo **vlrSaudeTit** (valor de dedução de plano de saúde do titular) está zerado e não há nenhum dependente vinculado com valor declarado no campo **infoDepSau**. 

Isso acontece quando o titular possui um plano de saúde 100% custeado pela empresa e possui plano de saúde para seus dependentes, mas devido a falta do cadastro correto para dependente não montou a informação **infoDepSau**.