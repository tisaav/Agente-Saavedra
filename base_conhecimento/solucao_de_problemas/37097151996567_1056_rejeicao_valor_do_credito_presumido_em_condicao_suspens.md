# 1056 Rejeição: Valor do Crédito Presumido em condição suspensiva do IBS informado indevidamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097151996567-1056-Rejei%C3%A7%C3%A3o-Valor-do-Cr%C3%A9dito-Presumido-em-condi%C3%A7%C3%A3o-suspensiva-do-IBS-informado-indevidamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097151996567-1056-Rejei%C3%A7%C3%A3o-Valor-do-Cr%C3%A9dito-Presumido-em-condi%C3%A7%C3%A3o-suspensiva-do-IBS-informado-indevidamente-nItem-999)  
> **ID:** `37097151996567` | **Última Atualização:** 2026-07-22T14:20:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097132398231)

 **MENSAGEM**

1056 Rejeição: Valor do Crédito Presumido em condição suspensiva do IBS informado indevidamente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097132402711)

 **SITUAÇÃO**

A NF-e foi emitida com informação de Crédito Presumido em condição suspensiva do IBS em situação não permitida, considerando o período de apuração ou o Código de Classificação do Crédito Presumido informado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097151979287)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097132405527)

 Verifique se o valor de **Crédito Presumido em condição suspensiva do IBS** está sendo informado em situação permitida pela legislação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097151983511)

 O preenchimento é permitido somente a partir do ano de **2033** ou quando o **Código de Classificação do Crédito Presumido** estiver configurado como **“4 - Aquisição de bens móveis de PF não contribuinte para revenda (ex.: veículos / brechó)”**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097132407063)

 Acesse a tela de** "Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o tipo de operação utilizado está configurado corretamente para a operação que deseja realizar.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097151986711)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo "NF-e" está configurado corretamente como **"Nota de Crédito"**. Se a operação não se enquadra nas exceções permitidas, **não informe** valores no campo de crédito presumido em condição suspensiva.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097132412439)

 Se estiver emitindo uma nota fiscal para aquisição de bens móveis de pessoa física não contribuinte para revenda (como veículos usados ou itens de brechó), certifique-se de que o código de classificação do crédito presumido esteja configurado como "4" e que os valores estejam sendo informados corretamente.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38388075111959)

 Para as demais operações, **não informe** valores no campo de crédito presumido em condição suspensiva do IBS até o ano de 2033, conforme determinado pela legislação. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097132412951)

 **CAUSA**

Esta rejeição ocorre devido à regra de validação UB126-10 da Sefaz, que determina que o valor do crédito presumido em condição suspensiva do IBS (campo vCredPresCondSus) só pode ser informado em duas situações específicas:

- 

Quando o ano de emissão da nota fiscal for igual ou posterior a 2033; ou

- 

Quando o código de classificação do crédito presumido (cCredPres) for igual a "4-Aquisição de bens móveis de PF não contribuinte para revenda (exemplo: veículos / brechó)".

Caso o documento fiscal seja emitido antes de 2033 e com um código de classificação diferente de "4", o sistema da Sefaz rejeitará a nota fiscal com a mensagem 1056, indicando que o valor do crédito presumido em condição suspensiva do IBS foi informado indevidamente.