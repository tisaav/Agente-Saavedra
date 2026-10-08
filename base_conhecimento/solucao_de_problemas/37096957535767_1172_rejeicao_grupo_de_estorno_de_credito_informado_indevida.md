# 1172 Rejeição: Grupo de Estorno de Crédito informado indevidamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096957535767-1172-Rejei%C3%A7%C3%A3o-Grupo-de-Estorno-de-Cr%C3%A9dito-informado-indevidamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096957535767-1172-Rejei%C3%A7%C3%A3o-Grupo-de-Estorno-de-Cr%C3%A9dito-informado-indevidamente-nItem-999)  
> **ID:** `37096957535767` | **Última Atualização:** 2026-07-22T14:21:00Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096971528599)

 **MENSAGEM**

1172 Rejeição: Grupo de Estorno de Crédito informado indevidamente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096971529879)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e modelo 55), o documento foi rejeitado pela SEFAZ porque o **sistema incluiu indevidamente o grupo de Estorno de Crédito na nota fiscal**, quando a Classificação Tributária (cClassTrib) utilizada não permite o preenchimento deste grupo.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096957522583)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096971530775)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a TOP utilizada na nota fiscal rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096957525015)

 Na aba **''N****F-e/NFC-e/CF-e''**, verifique se TOP está configurada com campo **"Tipo de Nota Fiscal de Débito" **diferente de **"07-Perda em estoque"**.

- 

Se estiver configurada com outro valor, mantenha esta configuração.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096971532823)

 Acesse as telas** ''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096971534487)

 Na aba '**'Tributação''** verifique qual código foi selecionado no campo ''**Código de Classificação Tributária''**.

- 

Se a operação exige Estorno de Crédito (ex: Nota de Débito de Perda), este código **deve ser substituído** por uma Classificação Tributária que permita essa operação conforme a Tabela Oficial.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38277923844631)

 Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique o produto que está sendo utilizado na nota fiscal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096971536791)

 Na aba **"Tributação"** do produto, verifique se há alguma configuração que esteja forçando o preenchimento do grupo de Estorno de Crédito e ajuste conforme necessário.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096957530775)

 Ao emitir a nota fiscal novamente, certifique-se de que o sistema não está incluindo o grupo de Estorno de Crédito indevidamente para a Classificação Tributária utilizada.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096957531543)

 **CAUSA**

A rejeição ocorre porque o sistema está incluindo o **grupo de Estorno de Crédito (gEstornoCred) **na nota fiscal, quando a Classificação Tributária (cClassTrib) utilizada possui um indicador que **veda o preenchimento** deste grupo (ind_gEstornoCred = 0).

De acordo com a regra de validação UB116-10, quando o indicador de Estorno de Crédito está configurado como 0 (não permitido) na Classificação Tributária, o grupo "gEstornoCred" não deve ser informado na nota fiscal, exceto quando o tipo de nota fiscal de débito for "07-Perda em estoque".

Esta validação faz parte das novas regras implementadas para a Reforma Tributária, conforme a Lei Complementar nº 214 de 16 de janeiro de 2025, que estabelece os critérios para o preenchimento dos grupos relacionados ao IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços).