# 1132 Rejeição: Grupo de transferência de crédito não informado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095838597783-1132-Rejei%C3%A7%C3%A3o-Grupo-de-transfer%C3%AAncia-de-cr%C3%A9dito-n%C3%A3o-informado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095838597783-1132-Rejei%C3%A7%C3%A3o-Grupo-de-transfer%C3%AAncia-de-cr%C3%A9dito-n%C3%A3o-informado-nItem-999)  
> **ID:** `37095838597783` | **Última Atualização:** 2026-07-22T14:21:31Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095852972439)

 **MENSAGEM**

1132 Rejeição: Grupo de transferência de crédito não informado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095838564503)

 **SITUAÇÃO**

Rejeição apresentada na emissão de uma nota fiscal quando é utilizado um **CST do IBS/CBS** que requer a informação do grupo de **Transferência de Crédito**, porém esse grupo não foi informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095838566935)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095838567447)

 Acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique o **Código de Situação Tributária do IBS/CBS **utilizado na operação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095852981015)

 Acesse a aba **"NF-e/NFC-e/CF-e"** e verifique se a finalidade da nota fiscal no campo **"NF-e"** está configurada como **"Nota de Débito"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095852982039)

 Caso esteja utilizando uma nota fiscal de débito, certifique-se de que o campo **"Tipo de Nota Fiscal de Débito"** esteja configurado como **"01 - Transferência de créditos para Cooperativas"** ou **"05 - Transferência de crédito de sucessão"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095838577687)

 Acesse a tela **"****Assistente de Configuração Integral da Reforma Tributária****" **(Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se o CST utilizado possui o indicador que exige a informação do grupo de transferência de crédito.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095852984471)

 Ao emitir a nota fiscal, certifique-se de informar corretamente o grupo de transferência de crédito, incluindo os valores do IBS e da CBS que devem ser maiores que zero.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095852987287)

 Verifique se a finalidade da nota fiscal e o tipo de nota de débito estão compatíveis com o CST utilizado, conforme as regras UB106-30 e UB106-31.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095838582295)

 **CAUSA**

A rejeição ocorre devido à **ausência do grupo de transferência de crédito** quando este é obrigatório para o **CST do IBS/CBS **informado. Conforme a regra de validação UB13-45, quando o CST possui indicador que exige informação do grupo de Transferência de Crédito (ind_gTransfCred = 1), o grupo gTransfCred deve ser obrigatoriamente informado no documento fiscal.

Esta validação é parte das novas regras implementadas pela Reforma Tributária (Lei Complementar nº 214 de 16 de janeiro de 2025), que introduziu os **novos tributos IBS** **(Imposto sobre Bens e Serviços)** e **CBS** **(Contribuição sobre Bens e Serviços)**, substituindo gradualmente os impostos anteriores.

Quando se utiliza um CST específico para transferência de crédito, é necessário informar os valores correspondentes do IBS e da CBS, sendo que pelo menos um deles deve ser maior que zero, conforme a regra UB106-40.