# 1060 Rejeição: Valor do Crédito Presumido da CBS informado indevidamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141554852119-1060-Rejei%C3%A7%C3%A3o-Valor-do-Cr%C3%A9dito-Presumido-da-CBS-informado-indevidamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141554852119-1060-Rejei%C3%A7%C3%A3o-Valor-do-Cr%C3%A9dito-Presumido-da-CBS-informado-indevidamente-nItem-999)  
> **ID:** `37141554852119` | **Última Atualização:** 2026-07-22T14:19:06Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141554837783)

 **MENSAGEM**

1060 Rejeição: Valor do Crédito Presumido da CBS informado indevidamente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141554838679)

 **SITUAÇÃO**

Ao emitir um documento fiscal (NF-e modelo 55), o sistema está informando um **Valor do Crédito Presumido em condição suspensiva** para a CBS (Contribuição sobre Bens e Serviços) em uma situação não permitida pela legislação, resultando na rejeição do documento pela SEFAZ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141538416407)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141554839191)

 Acesse as telas** ''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141538416791)

 Na aba** ''Tributação''**, verifique o campo** ''Código de Class. do Crédito Presumido'' **utilizado na operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38157609864855)

 Caso o código utilizado seja **"4-Aquisição de bens móveis de PF não contrib. para revenda (veículos / brechó)"**, verifique se o ano de emissão do documento é **2027 ou posterior**. Este código só é permitido a partir de 2027.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141538418327)

 Se estiver utilizando outro código de crédito presumido, verifique se o ano de emissão do documento é **anterior a 2027**. Neste caso, não é permitido informar o Valor do Crédito Presumido em condição suspensiva.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141554844183)

 Retorne ao passo 1 e ajuste o ''**Código de Situação Tributária'' (CST) **para um código que seja compatível com a operação e que não exija a informação de crédito presumido em condição suspensiva.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38157609866135)

 Caso seja necessário manter o crédito presumido, aguarde até 2027 para utilizar o código **"4-Aquisição de bens móveis de PF não contrib. para revenda"**. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141538419351)

 **CAUSA**

Esta rejeição ocorre devido à regra de validação UB130-10 da SEFAZ, que estabelece que o **Valor do Crédito Presumido em condição suspensiva** (tag: gCBSCredPres/vCredPresCondSus) só pode ser informado em duas situações específicas:

- 

Quando o ano de emissão do documento for **igual ou superior a 2027**; ou

- 

Quando o **Código de classificação do crédito presumido** (tag: gCBSCredPres/cCredPres) for igual a **"4-Aquisição de bens móveis de PF não contrib. para revenda (veículos / brechó)"**.

Se nenhuma dessas condições for atendida e o valor for informado, o documento será rejeitado com o código 1060.