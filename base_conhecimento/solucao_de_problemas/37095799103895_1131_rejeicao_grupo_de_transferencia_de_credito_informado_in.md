# 1131 Rejeição: Grupo de transferência de crédito informado indevidamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095799103895-1131-Rejei%C3%A7%C3%A3o-Grupo-de-transfer%C3%AAncia-de-cr%C3%A9dito-informado-indevidamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095799103895-1131-Rejei%C3%A7%C3%A3o-Grupo-de-transfer%C3%AAncia-de-cr%C3%A9dito-informado-indevidamente-nItem-999)  
> **ID:** `37095799103895` | **Última Atualização:** 2026-07-22T14:21:32Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095834942359)

 **MENSAGEM**

1131 Rejeição: Grupo de transferência de crédito informado indevidamente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095799088535)

 **SITUAÇÃO**

Rejeição apresentada na emissão de uma nota fiscal eletrônica (NF-e) quando é informado o grupo de **Transferência de Crédito do IBS/CBS** em conjunto com um CST que não permite a utilização desse grupo no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095799088919)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095799092759)

 Acesse a tela** ''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o CST do IBS/CBS utilizado na operação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095799093271)

 Acesse a aba **"NF-e/NFC-e/CF-e"** e verifique se o campo **"NF-e"** está configurado com a finalidade **"Nota de Débito"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095834946327)

 Caso esteja configurado como Nota de Débito, verifique se o campo **"Tipo de Nota Fiscal de Débito"** está configurado com um valor **diferente** de **"05-Transferência de crédito de sucessão"** ou **"01-Transferência de créditos para Cooperativas"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095799096983)

 Se o problema persistir, acesse a tela **"****Assistente de Configuração Integral da Reforma Tributária****"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se o CST do IBS/CBS utilizado possui indicador que **não permite** a informação de transferência de crédito.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095834948375)

 Altere o CST do IBS/CBS para um código que seja compatível com a operação desejada, ou remova o grupo de transferência de crédito caso não seja necessário para a operação.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095799100951)

 **CAUSA**

A rejeição ocorre devido a uma **incompatibilidade entre o CST do IBS/CBS **informado e o** grupo de transferência de crédito**. Conforme a regra de validação UB13-44 da Sefaz, quando o CST do IBS/CBS possui um indicador que não permite a informação do grupo de transferência de crédito (ind_gTransfCred = 0), o grupo gTransfCred não deve ser informado no documento fiscal.

Além disso, a regra UB106-30 estabelece que o grupo de transferência de crédito só pode ser informado quando a finalidade da NF-e for "Nota de Débito" e o tipo de nota de débito for "05-Transferência de crédito de sucessão" ou "01-Transferência de créditos para Cooperativas".

Esta validação faz parte das novas regras implementadas pela Reforma Tributária, conforme a Lei Complementar 214 de 16 de janeiro de 2025, que estabelece os critérios para transferência de créditos do IBS e da CBS.