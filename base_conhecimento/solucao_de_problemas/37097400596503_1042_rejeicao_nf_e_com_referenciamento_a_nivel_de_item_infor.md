# 1042 Rejeição: NF-e com referenciamento a nível de item informado indevidamente

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097400596503-1042-Rejei%C3%A7%C3%A3o-NF-e-com-referenciamento-a-n%C3%ADvel-de-item-informado-indevidamente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097400596503-1042-Rejei%C3%A7%C3%A3o-NF-e-com-referenciamento-a-n%C3%ADvel-de-item-informado-indevidamente)  
> **ID:** `37097400596503` | **Última Atualização:** 2026-07-22T14:20:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097431582487)

 **MENSAGEM**

1042 Rejeição: NF-e com referenciamento a nível de item informado indevidamente

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097400581911)

 **SITUAÇÃO**

Ao emitir uma NF-e que não é de devolução (finalidade diferente de 4), mas que contém referenciamento a nível de item de outra NF-e, o documento é rejeitado pela SEFAZ com a mensagem 1042.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097400583959)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097431585047)

 Verifique a finalidade da NF-e no cadastro do **"Tipo de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097431589911)

 Na tela de **"Tipos de Operação - TOP"**, acesse a aba **"NF-e/NFC-e/CF-e"** e verifique o campo **"NF-e"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097431590935)

 Se a operação não for de devolução, altere o campo **"NF-e"** para uma finalidade diferente de **"Devolução"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097431591447)

 Caso a operação seja realmente de devolução, mantenha a finalidade "Devolução" e certifique-se de que o referenciamento a nível de item esteja correto.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097431592727)

 Se a operação **não for** de devolução, acesse a tela de **"Central de Vendas" **(Comercial » Rotinas » Central de Vendas) e remova o referenciamento a nível de item que foi informado indevidamente.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097400589591)

 Para remover o referenciamento, acesse a aba **"Documentos Referenciados"** na tela da nota fiscal e exclua as referências a nível de item que foram informadas.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097400590615)

 Após realizar as alterações necessárias, gere novamente a NF-e para transmissão à SEFAZ.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097400591511)

 **CAUSA**

Esta rejeição ocorre porque o referenciamento a nível de item (tag DFeReferenciado/nItem) só é permitido quando a NF-e possui finalidade de devolução (finNFe = 4). Quando a finalidade da NF-e é diferente de devolução, o sistema não deve informar o referenciamento a nível de item, apenas a chave de acesso do documento referenciado.

De acordo com as regras de validação da SEFAZ, o referenciamento detalhado de itens só é necessário e permitido em operações de devolução, para que seja possível rastrear exatamente quais itens estão sendo devolvidos em relação à nota fiscal original.