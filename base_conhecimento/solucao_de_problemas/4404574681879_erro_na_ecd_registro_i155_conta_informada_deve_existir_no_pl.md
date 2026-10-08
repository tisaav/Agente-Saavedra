# Erro na ECD Registro I155: Conta informada deve existir no plano de contas e ser analítica

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4404574681879-Erro-na-ECD-Registro-I155-Conta-informada-deve-existir-no-plano-de-contas-e-ser-anal%C3%ADtica](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404574681879-Erro-na-ECD-Registro-I155-Conta-informada-deve-existir-no-plano-de-contas-e-ser-anal%C3%ADtica)  
> **ID:** `4404574681879` | **Última Atualização:** 2026-07-22T15:23:12Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347520871959)

 MENSAGEM: **

Erro na ECD Registro I155: Conta informada deve existir no plano de contas e ser analítica

​

****

| Trecho do Guia Prático > Registro I155: Detalhe dos Saldos Periódicos O registro I155, que é filho do registro I150, informa os saldos das contas contábeis, trazendo o total dos débitos e créditos mensais para as contas patrimoniais e de resultado. Os saldos devem ser informados por mês, ou seja, deve haver um registro I150 por mês. |
| --- |

 

Pegando de exemplo a conta acima 3.1.01.02.04.001, existe saldo nessa conta, mas a mesma não foi gerada no registro específico I050.

No exemplo abaixo, ao consultar a conta no arquivo pelo aplicativo notepad++ a conta existe no registro I155 (saldos periódicos), I250 (partidas dos lançamentos).

Mas a conta não existe no plano de contas.

 

![Imagem](/attachments/token/k4yKSm65pWVW0eSbRXWDXxC79/?name=inline-1197142629.png)

​

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16347520874647)

 SOLUÇÃO:**

 Verifique a conta criticada pelo validador da Receita para ver se a mesma existe no plano de contas.

- 

Conta deve estar ativa.

- 

Deve ser analítica.

- 

A data informada no campo **"Referência de Ativação"** deverá estar preenchida e a data ser do período do arquivo gerado ou anterior.

- 

Caso a data não esteja preenchida ou for superior ao período do arquivo, o sistema não irá gerar a conta no referido registro.

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15689380479895)

​