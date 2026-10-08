# 1114 Rejeição: Classificação Tributária do IBS e da CBS informada não permite informação da tributação regular [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096547825175-1114-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-da-CBS-informada-n%C3%A3o-permite-informa%C3%A7%C3%A3o-da-tributa%C3%A7%C3%A3o-regular-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096547825175-1114-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-IBS-e-da-CBS-informada-n%C3%A3o-permite-informa%C3%A7%C3%A3o-da-tributa%C3%A7%C3%A3o-regular-nItem-999)  
> **ID:** `37096547825175` | **Última Atualização:** 2026-08-25T00:56:48Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096572764823)

 **MENSAGEM**

1114 Rejeição: Classificação Tributária do IBS e da CBS informada não permite informação da tributação regular [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096572765207)

 **SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e, o documento foi rejeitado porque foi informado o grupo de **Tributação Regular** para uma **Classificação Tributária do IBS e da CBS** que não permite a utilização desse grupo.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096572768279)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096547816471)

 Acesse as telas** ''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique a configuração da alíquota utilizada no item rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096572775703)

 Na aba **''Tributação''**, verifique se o campo **"Código de Classificação Tributária"** está configurado com um código que **não permite** a informação do grupo de Tributação Regular.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096547818391)

 Caso esteja utilizando uma classificação tributária que não permite a informação do grupo de Tributação Regular, você tem duas opções:

Caso esteja sendo utilizada uma classificação tributária que não permita a informação do grupo de **Tributação Regular**, escolha uma das seguintes opções:

- 

**Opção 1:** Remover o grupo de Tributação Regular da alíquota, desmarcando a opção correspondente na aba **"Tributação"**.

- 

**Opção 2:** Alterar a **Classificação Tributária **para uma que permita a informação do grupo de Tributação Regular, conforme a necessidade da operação.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38274790774551)

 Após realizar as alterações necessárias, salve as configurações e tente emitir o documento fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096547821847)

 **CAUSA**

A rejeição ocorre porque cada **Classificação Tributária do IBS e da CBS** possui indicadores específicos que determinam se o grupo de **Tributação Regular** pode ou não ser informado. Quando uma classificação tributária tem o indicador **ind_gTribRegular = 0**, significa que ela **não permite** a informação do grupo de Tributação Regular.

Ao configurar uma alíquota com uma classificação tributária que não permite o grupo de Tributação Regular e, mesmo assim, informar esse grupo, o sistema da SEFAZ rejeita o documento fiscal com o código 1114. Esta validação está prevista na regra UB68-11 da SEFAZ, que verifica a compatibilidade entre a Classificação Tributária informada e a presença do grupo de Tributação Regular no documento fiscal.