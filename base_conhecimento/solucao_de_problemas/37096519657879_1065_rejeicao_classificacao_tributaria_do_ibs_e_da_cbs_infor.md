# 1065 Rejeição: Classificação Tributária do IBS e da CBS informada obriga informação da tributação regular [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096519657879-1065-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-da-CBS-informada-obriga-informa%C3%A7%C3%A3o-da-tributa%C3%A7%C3%A3o-regular-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096519657879-1065-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-da-CBS-informada-obriga-informa%C3%A7%C3%A3o-da-tributa%C3%A7%C3%A3o-regular-nItem-999)  
> **ID:** `37096519657879` | **Última Atualização:** 2026-07-28T13:38:15Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096519642903)

 **MENSAGEM**

1065 Rejeição: Classificação Tributária do IBS e da CBS informada obriga informação da tributação regular [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096511415703)

 **SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e com a nova tributação do IBS e CBS, o documento foi rejeitado pela SEFAZ porque a **Classificação Tributária** selecionada exige que seja informado o grupo de **Tributação Regular**, porém este grupo não foi informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096511415959)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096511416855)

 Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096519645335)

 Verifique a **Classificação Tributária** que está sendo utilizada na operação e confirme se ela exige a informação do grupo de Tributação Regular.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096519646231)

 Acesse as telas** ''Alíquotas de IBS'**' (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e selecione a alíquota utilizada na operação.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096519651735)

 Na aba **"Tributação"**, preencha os campos obrigatórios:

- 

Selecione o **"Código de Situação Tributária Regular"** adequado para a operação;

- 

Informe a **"Código de Classificação Tributária Regular" **compatível com o CST Regular.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096519651991)

 Salve as alterações e tente emitir o documento fiscal novamente.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096511423255)

 **CAUSA**

Esta rejeição ocorre porque a **Classificação Tributária do IBS e da CBS** informada no documento fiscal possui um indicador que **exige** a informação do grupo de Tributação Regular (ind_gTribRegular = 1), conforme estabelecido nas regras de validação da SEFAZ.

De acordo com a regra de validação UB68-10, quando a Classificação Tributária (cClassTrib) informada possui indicador que exige a informação do grupo de Tributação Regular, este grupo deve ser obrigatoriamente preenchido no documento fiscal.

A Tributação Regular é um componente essencial para determinadas classificações tributárias no contexto da Reforma Tributária, pois complementa as informações necessárias para o correto cálculo e aplicação do IBS e da CBS.