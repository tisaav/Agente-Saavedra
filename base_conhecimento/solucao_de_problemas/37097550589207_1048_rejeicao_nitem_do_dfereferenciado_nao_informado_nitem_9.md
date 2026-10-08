# 1048 Rejeição: nItem do DFeReferenciado não informado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097550589207-1048-Rejei%C3%A7%C3%A3o-nItem-do-DFeReferenciado-n%C3%A3o-informado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097550589207-1048-Rejei%C3%A7%C3%A3o-nItem-do-DFeReferenciado-n%C3%A3o-informado-nItem-999)  
> **ID:** `37097550589207` | **Última Atualização:** 2026-07-22T14:20:37Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097550577559)

 **MENSAGEM**

1048 Rejeição: nItem do DFeReferenciado não informado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097550579095)

 **SITUAÇÃO**

A NF-e ou NFC-e foi emitida com referência a outro documento fiscal eletrônico (DFe), porém o número do item correspondente no documento referenciado não foi informado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097550579735)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097550580247)

 Acesse a tela **''Central de Vendas'' **(Comercial » Rotinas » Central de Vendas) e localize a nota fiscal que está sendo rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097550581015)

 Clique na aba **"Documentos Referenciados" **(ou Notas Referenciadas) para visualizar os documentos que estão sendo referenciados na nota fiscal atual.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097526068119)

 Para cada documento referenciado, verifique se o campo **"Número do Item"** está preenchido. Este campo deve conter o número do item correspondente no documento fiscal original que está sendo referenciado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097526068631)

 Preencha o **"Número do Item"** para todos os documentos referenciados que estiverem com este campo em branco.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097550583703)

 Caso não saiba qual é o número do item no documento original, consulte o documento referenciado através da tela **"Consulta de Documentos Fiscais"** (Comercial » Consultas » Documentos Fiscais) para identificar o número correto do item.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097526069655)

 Após preencher todos os números de itens referenciados, salve as alterações e tente emitir a nota fiscal novamente. 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097526072855)

 **CAUSA**

A rejeição ocorre devido à **ausência de informação do número do item** no documento fiscal eletrônico que está sendo referenciado. Com a implementação da Reforma Tributária (Lei Complementar nº 214/2025), tornou-se obrigatório informar o número do item do documento referenciado para garantir a rastreabilidade completa das operações fiscais, especialmente para o correto cálculo e transferência de créditos do IBS e da CBS.

Esta validação é particularmente importante em operações que envolvem transferência de créditos tributários, devolução de mercadorias ou complementação de impostos, onde é necessário estabelecer uma relação direta entre os itens dos documentos fiscais para assegurar a correta aplicação das regras tributárias.