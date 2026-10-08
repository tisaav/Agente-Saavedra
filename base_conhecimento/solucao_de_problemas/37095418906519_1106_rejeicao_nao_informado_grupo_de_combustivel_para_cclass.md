# 1106 Rejeição: Não informado grupo de combustível para cClassTrib de Combustível [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095418906519-1106-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-grupo-de-combust%C3%ADvel-para-cClassTrib-de-Combust%C3%ADvel-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095418906519-1106-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-grupo-de-combust%C3%ADvel-para-cClassTrib-de-Combust%C3%ADvel-nItem-999)  
> **ID:** `37095418906519` | **Última Atualização:** 2026-07-22T14:21:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095418898199)

 **MENSAGEM**

1106 Rejeição: Não informado grupo de combustível para cClassTrib de Combustível [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095418899863)

 **SITUAÇÃO**

Esta rejeição ocorre quando o contribuinte tenta emitir uma NF-e ou NFC-e contendo produtos classificados como combustíveis, mas não informa o grupo específico de tributação monofásica de combustíveis exigido pela legislação da Reforma Tributária (LC 214/2025).

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095418900759)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095450599191)

 Acesse a tela** ''Produtos'' **(Configurações » Cadastros » Produtos » Produtos).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095418901527)

 Na aba** ''Impostos''**, verifique se o campo **''Classificação Substituição Tributária''**, está classificado como **''Derivados de petróleo, lubrificantes e outros''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38016933835671)

 Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095418902423)

 Configure corretamente as alíquotas para produtos combustíveis.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095418903063)

 Verifique se o **"Código de situação tributária" (CST)** está configurado adequadamente para operações com combustíveis, considerando a tributação monofásica conforme a LC 214/2025.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38016964901143)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38016964902807)

 Na aba **''Impostos''**, verifique se o campo **''Tem IBS/CBS Monofásico''** está configurado para operações com combustíveis.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38016933841175)

 Ao emitir a nota fiscal, certifique-se de que o **grupo de tributação monofásica de combustíveis** esteja sendo corretamente informado no documento fiscal eletrônico.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095418903575)

 **CAUSA**

A rejeição ocorre devido à obrigatoriedade de informar o grupo específico de tributação monofásica para produtos classificados como combustíveis, conforme estabelecido na Lei Complementar 214/2025. Quando o produto possui uma classificação tributária (cClassTrib) que exige a informação do grupo de combustível, mas este grupo não é informado na nota fiscal, a SEFAZ rejeita o documento eletrônico.

Esta validação está relacionada às regras específicas para tributação monofásica de combustíveis, onde o imposto é cobrado em uma única fase da cadeia de comercialização, geralmente na produção ou importação, conforme previsto nos artigos 172 e 178 da LC 214/2025, que tratam da tributação do IBS e da CBS sobre combustíveis.