# 1025 Rejeição: cClassTrib do IBS/CBS não permitido neste modelo de DFe [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37099044727575-1025-Rejei%C3%A7%C3%A3o-cClassTrib-do-IBS-CBS-n%C3%A3o-permitido-neste-modelo-de-DFe-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37099044727575-1025-Rejei%C3%A7%C3%A3o-cClassTrib-do-IBS-CBS-n%C3%A3o-permitido-neste-modelo-de-DFe-nItem-999)  
> **ID:** `37099044727575` | **Última Atualização:** 2026-08-03T12:54:37Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099044717335)

 **MENSAGEM**

1025 Rejeição: cClassTrib do IBS/CBS não permitido neste modelo de DFe [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099064592279)

 **SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e com a Classificação Tributária do IBS/CBS (cClassTrib) que não é permitida para o modelo de documento fiscal eletrônico utilizado, a SEFAZ rejeita o documento e apresenta esta mensagem de erro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099064594327)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099064595863)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099064596759)

 Verifique a classificação tributária configurada para o produto que esteja gerando a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099044724119)

 Verifique se a **Classificação Tributária** selecionada possui o indicador correto para o modelo de documento que está tentando emitir:

- 

**Para NF-e (modelo 55)**: a Classificação Tributária deve ter o indicador **"indNFe = 1"**

- 

**Para NFC-e (modelo 65)**: a Classificação Tributária deve ter o indicador **"indNFCe = 1"** 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099064599575)

 Caso a Classificação Tributária esteja incorreta, selecione uma classificação compatível com o modelo de documento fiscal que está emitindo.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099044725271)

 Alternativamente, acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está com a **Classificação Tributária do IBS/CBS** correta para o modelo de documento que está sendo emitido.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37942218095255)

 Após realizar as correções, tente emitir o documento fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099044726039)

 **CAUSA**

Esta rejeição ocorre porque a **Classificação Tributária do IBS/CBS** (cClassTrib) informada no documento fiscal possui um indicador que **não permite sua utilização** no modelo de documento que está sendo emitido.

Conforme a regra de validação UB14-25, cada Classificação Tributária possui indicadores específicos que determinam em quais modelos de documentos fiscais ela pode ser utilizada:

- 

Para NF-e (modelo 55): o indicador **indNFe** deve ser igual a 1

- 

Para NFC-e (modelo 65): o indicador **indNFCe** deve ser igual a 1

Se o indicador correspondente ao modelo do documento for igual a 0, a Classificação Tributária não pode ser utilizada naquele modelo específico, resultando nesta rejeição.