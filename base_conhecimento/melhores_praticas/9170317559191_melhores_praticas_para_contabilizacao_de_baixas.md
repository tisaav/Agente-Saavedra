# Melhores práticas para contabilização de Baixas

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9170317559191-Melhores-pr%C3%A1ticas-para-contabiliza%C3%A7%C3%A3o-de-Baixas](https://ajuda.sankhya.com.br/hc/pt-br/articles/9170317559191-Melhores-pr%C3%A1ticas-para-contabiliza%C3%A7%C3%A3o-de-Baixas)  
> **ID:** `9170317559191` | **Última Atualização:** 2026-07-22T15:09:58Z

---

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450818983063)

 Na contabilização dos recebimentos e pagamentos quando se utilizada a mesma top de baixa, a diferenciação entre os títulos que foram recebidos/pagos dos títulos quer foram compensados se dá pelo número da compensação registrada no movimento financeiro.

Acontece que as vezes esta informação nos títulos não compensados fica com valor igual a zero ou nulo, o que dificulta sua validação na fórmula de contabilização.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450818983063)

 Então, considerando as fórmulas de contabilização abaixo exemplificadas:**

Títulos recebidos/pagos:
Debito : IF(Formula.NUCOMPENS = 0, Formula.VLRBAIXA, 0)
Crédito: IF(Formula.NUCOMPENS = 0, Formula.VLRBAIXA, 0)

Títulos compensados:
Debito : IF(Formula.NUCOMPENS <> 0, Formula.VLRBAIXA, 0)
Crédito: IF(Formula.NUCOMPENS <> 0, Formula.VLRBAIXA, 0)

Para que o sistema faça a correta validação do conteúdo retornado pela expressão Formula.NUCOMPENS, independente se o número da compensação está com valor nulo e ou preenchido com valor igual ou diferente de zero, é preciso converter o valor retornado pela expressão Formula.NUCOMPENS utilizando a função Val().

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450818983063)

 Ficando então as fórmulas exemplificadas anteriormente no seguinte formato:**

Títulos recebidos/pagos:
Debito : IF(Val(Formula.NUCOMPENS) = 0, Formula.VLRBAIXA, 0)
Crédito: IF(Val(Formula.NUCOMPENS) = 0, Formula.VLRBAIXA, 0)

Títulos compensados:
Debito : IF(Val(Formula.NUCOMPENS) <> 0, Formula.VLRBAIXA, 0)
Crédito: IF(Val(Formula.NUCOMPENS) <> 0, Formula.VLRBAIXA, 0)