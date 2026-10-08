# 1014 Rejeição: CST do Imposto Seletivo informado inexistente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098961170711-1014-Rejei%C3%A7%C3%A3o-CST-do-Imposto-Seletivo-informado-inexistente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098961170711-1014-Rejei%C3%A7%C3%A3o-CST-do-Imposto-Seletivo-informado-inexistente-nItem-999)  
> **ID:** `37098961170711` | **Última Atualização:** 2026-07-22T14:20:03Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098961159703)

 **MENSAGEM**

1014 Rejeição: CST do Imposto Seletivo informado inexistente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098961160471)

 **SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) com produtos sujeitos ao Imposto Seletivo (IS), o documento foi rejeitado pela SEFAZ porque o Código de Situação Tributária (CST) do Imposto Seletivo informado não existe na tabela de códigos válidos estabelecida pela legislação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098969927319)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098969927959)

 Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098961161623)

 Localize o produto que está gerando a rejeição e verifique a configuração do **"CST do Imposto Seletivo"** atribuído a ele.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098961161879)

 Selecione um **CST válido** para o Imposto Seletivo conforme a tabela de códigos estabelecida pela legislação da Reforma Tributária.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098961162391)

 Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e localize o produto em questão.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098969932951)

 Na aba ''Impostos'' verifique se o **''NCM'' **está configurado corretamente.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38046113493655)

 Após realizar as correções, tente emitir a nota fiscal novamente. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098961168407)

 **CAUSA**

Esta rejeição ocorre quando o sistema envia um código de CST do Imposto Seletivo que não consta na tabela de Códigos de Situação Tributária válidos para o Imposto Seletivo. O Imposto Seletivo, introduzido pela Reforma Tributária (Lei Complementar nº 214/2025), possui uma tabela específica de CSTs que devem ser utilizados corretamente na emissão de documentos fiscais eletrônicos.

A regra de validação UB02-10 da SEFAZ verifica se o CST do Imposto Seletivo informado existe na tabela oficial. Quando um código inexistente é informado, a nota é rejeitada com o código 1014.