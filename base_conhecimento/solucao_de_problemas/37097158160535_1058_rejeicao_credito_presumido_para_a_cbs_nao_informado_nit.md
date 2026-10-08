# 1058 Rejeição: Crédito Presumido para a CBS não informado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097158160535-1058-Rejei%C3%A7%C3%A3o-Cr%C3%A9dito-Presumido-para-a-CBS-n%C3%A3o-informado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097158160535-1058-Rejei%C3%A7%C3%A3o-Cr%C3%A9dito-Presumido-para-a-CBS-n%C3%A3o-informado-nItem-999)  
> **ID:** `37097158160535` | **Última Atualização:** 2026-07-22T14:20:51Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097172123671)

 **MENSAGEM**

1058 Rejeição: Crédito Presumido para a CBS não informado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097172124183)

 **SITUAÇÃO**

A NF-e foi emitida com um CST que exige a informação de Crédito Presumido da CBS, porém o grupo correspondente ao crédito presumido não foi informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097158143895)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097158145303)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o TOP utilizado na operação está configurado corretamente para a Reforma Tributária.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097158146071)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e"** está configurado adequadamente para a operação que está sendo realizada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097158148759)

 Acesse a tela **"****Assistente de Configuração Integral da Reforma Tributária****" **(Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique as configurações de crédito presumido para a CBS.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097158151063)

 Certifique-se de que o **CST do IBS/CBS** utilizado na operação está corretamente configurado. Se o CST exige a informação de crédito presumido (indicador **ind_gCBSCredPres = 1**), é necessário informar o grupo de crédito presumido para a CBS.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097172134167)

 Ao emitir a nota fiscal, verifique se o item está com o **grupo de crédito presumido da CBS** devidamente preenchido, conforme exigido pelo CST utilizado.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097172134423)

 **CAUSA**

A rejeição 1058 ocorre devido à **ausência de informação do crédito presumido para a CBS** quando o CST utilizado exige essa informação. De acordo com a regra de validação UB127-20, quando o código de classificação do crédito presumido (cCredPres) possui indicador que exige o uso de crédito presumido para a CBS (ind_gCBSCredPres = 1), é obrigatório informar o grupo de crédito presumido para a CBS (grupo: IBSCBS/gCredPresOper/gCBSCredPres).

Esta validação faz parte das regras implementadas pela Reforma Tributária (Lei Complementar nº 214/2025), que estabelece novos requisitos para a emissão de documentos fiscais eletrônicos com a inclusão dos novos tributos IBS e CBS.