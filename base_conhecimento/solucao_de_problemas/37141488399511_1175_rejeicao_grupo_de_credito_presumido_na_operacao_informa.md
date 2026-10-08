# 1175 Rejeição: Grupo de Crédito Presumido na Operação informado indevidamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141488399511-1175-Rejei%C3%A7%C3%A3o-Grupo-de-Cr%C3%A9dito-Presumido-na-Opera%C3%A7%C3%A3o-informado-indevidamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141488399511-1175-Rejei%C3%A7%C3%A3o-Grupo-de-Cr%C3%A9dito-Presumido-na-Opera%C3%A7%C3%A3o-informado-indevidamente-nItem-999)  
> **ID:** `37141488399511` | **Última Atualização:** 2026-07-22T14:19:11Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141488396183)

 **MENSAGEM**

1175 Rejeição: Grupo de Crédito Presumido na Operação informado indevidamente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141488396439)

 **SITUAÇÃO**

A rejeição é apresentada na validação da **NF-e** em razão de inconsistência relacionada ao grupo **Crédito Presumido na Operação**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141488396695)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141504003991)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se o CST utilizado na operação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141504004119)

 Confirme se o CST utilizado na operação permite o uso de crédito presumido. Para isso, verifique se o indicador **"Permite Crédito Presumido na Operação"** está habilitado para o CST em questão.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141488398103)

 Caso o CST não permita o uso de crédito presumido na operação, você tem duas opções:

- 

Remova o grupo de Crédito Presumido na Operação da nota fiscal, ou

- 

Altere o CST para um que permita o uso de crédito presumido na operação, se aplicável ao seu caso.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141504007575)

 Se for necessário alterar o CST, acesse a tela de **"Tipos de Operação"** (Fiscal » Cadastros » Tipos de Operação) e selecione a operação utilizada na nota fiscal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141504008343)

 Na aba **"IBS/CBS"**, verifique e ajuste o CST configurado para a operação, selecionando um que permita o uso de crédito presumido.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141504008599)

 Após realizar as alterações necessárias, tente emitir a nota fiscal novamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141504009623)

 **CAUSA**

A causa desta rejeição está relacionada à incompatibilidade entre o CST utilizado na operação e a tentativa de informar o grupo de Crédito Presumido na Operação. Conforme a regra de validação UB120-20, quando o CST possui indicador que não permite o uso de crédito presumido na operação (ind_gCredPresOper = 0), o grupo de Crédito Presumido na Operação (IBSCBS/gCredPresOper) não deve ser informado.

Esta validação faz parte das regras estabelecidas pela Lei Complementar nº 214/2025, que implementa a Reforma Tributária, onde cada CST possui características específicas quanto à permissão ou não do uso de créditos presumidos. Quando um contribuinte tenta utilizar um crédito presumido em uma operação cujo CST não permite tal benefício, a SEFAZ rejeita a nota fiscal para garantir a correta aplicação das regras tributárias.