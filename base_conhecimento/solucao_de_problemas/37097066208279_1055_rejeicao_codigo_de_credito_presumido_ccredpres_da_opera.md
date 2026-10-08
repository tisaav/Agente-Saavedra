# 1055 Rejeição: Código de Crédito Presumido (cCredPres) da Operação inexistente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097066208279-1055-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Cr%C3%A9dito-Presumido-cCredPres-da-Opera%C3%A7%C3%A3o-inexistente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097066208279-1055-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Cr%C3%A9dito-Presumido-cCredPres-da-Opera%C3%A7%C3%A3o-inexistente-nItem-999)  
> **ID:** `37097066208279` | **Última Atualização:** 2026-07-22T14:20:57Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097066187543)

 **MENSAGEM**

1055 Rejeição: Código de Crédito Presumido (cCredPres) da Operação inexistente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097041212311)

 **SITUAÇÃO**

Ao tentar emitir uma nota fiscal eletrônica (NF-e) com informações de crédito presumido para IBS/CBS, o documento foi rejeitado pela SEFAZ porque o código de crédito presumido informado na operação não existe na tabela de códigos válidos estabelecidos pela legislação da Reforma Tributária.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097066190743)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097041215895)

 Acesse a tela de **"Tipos de Operação - TOP" **(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize o TOP utilizado na operação que gerou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097041216535)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"Permite Crédito Presumido"** está marcado como **Sim**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097066194071)

 Acesse a tela **"****Assistente de Configuração Integral da Reforma Tributária****"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097066196759)

 Na aba **"Crédito Presumido"**, verifique se o código de crédito presumido informado na operação está cadastrado e ativo.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097066197399)

 Ao emitir a nota fiscal, certifique-se de utilizar apenas os seguintes códigos de crédito presumido válidos:

- 

1 - Aquisição de bens e serviços de pessoa física não contribuinte

- 

2 - Aquisição de bens e serviços de pessoa jurídica não contribuinte

- 

3 - Aquisição de bens e serviços de pessoa jurídica optante pelo Simples Nacional

- 

4 - Aquisição de bens móveis de PF não contribuinte para revenda (exemplo: veículos/brechó).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097066198295)

 Corrija o código de crédito presumido no documento fiscal, utilizando um dos códigos válidos listados acima, de acordo com a operação realizada. 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097041219223)

 **CAUSA**

Esta rejeição ocorre quando o sistema tenta utilizar um código de crédito presumido (cCredPres) que não está previsto na legislação da Reforma Tributária. De acordo com a regra de validação UB122-10, quando informado o código de crédito presumido da operação, este deve existir na tabela de códigos válidos estabelecidos pela SEFAZ. Caso contrário, a nota fiscal será rejeitada com o código 1055.

O crédito presumido é um benefício fiscal concedido em determinadas operações, conforme previsto na Lei Complementar 214/2025, e só pode ser aplicado utilizando os códigos oficialmente estabelecidos pela legislação tributária.