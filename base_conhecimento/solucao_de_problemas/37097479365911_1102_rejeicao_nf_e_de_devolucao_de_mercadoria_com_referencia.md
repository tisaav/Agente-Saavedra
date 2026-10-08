# 1102 Rejeição: NF-e de devolução de mercadoria com referenciamento a nível de item exige referenciamento do item da NF-e original [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097479365911-1102-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-de-mercadoria-com-referenciamento-a-n%C3%ADvel-de-item-exige-referenciamento-do-item-da-NF-e-original-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097479365911-1102-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-de-mercadoria-com-referenciamento-a-n%C3%ADvel-de-item-exige-referenciamento-do-item-da-NF-e-original-nItem-999)  
> **ID:** `37097479365911` | **Última Atualização:** 2026-07-22T14:20:41Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097487005847)

 **MENSAGEM**

1102 Rejeição: NF-e de devolução de mercadoria com referenciamento a nível de item exige referenciamento do item da NF-e original [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097479351063)

 **SITUAÇÃO**

A NF-e de devolução (finalidade 4) foi emitida sem a correta identificação do item da NF-e original que está sendo devolvido, não sendo informado o número do item correspondente no documento referenciado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097487009559)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097479355159)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione a TOP utilizada para devolução.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097479355799)

 Na aba **"NF-e/NFC-e"**, verifique se a opção **"Buscar NF de Origem p/ Referenciar na NF-e"** está marcada.

- 

Caso não esteja, marque-a e salve a alteração.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097479356951)

 Inutilize a numeração da NF-e de devolução que foi rejeitada.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097487015831)

 Para realizar corretamente a devolução, acesse a tela **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097479358487)

 Localize a NF-e original que deseja devolver.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097479361303)

 Clique no botão **"Devolv./Estor."** e selecione os itens específicos que serão devolvidos.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097487018007)

 Ao realizar a devolução desta forma, o sistema preencherá automaticamente o grupo de documentos referenciados, incluindo a chave da NF-e original e o número do item que está sendo devolvido.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097487019159)

 Confirme a operação e emita a nova NF-e de devolução.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097487020183)

 **CAUSA**

A rejeição 1102 ocorre devido à implementação da **Nota Técnica 2022.005** que estabeleceu novas regras de validação para NF-e de devolução. Conforme esta norma, quando uma NF-e possui finalidade igual a ** ''Devolução"**, é obrigatório não apenas referenciar a NF-e original que está sendo devolvida (através da chave de acesso), mas também informar **qual item específico** da NF-e original está sendo devolvido.

Esta validação faz parte das medidas de controle fiscal implementadas pela SEFAZ para garantir maior rastreabilidade nas operações de devolução, permitindo um controle mais preciso dos itens que estão sendo devolvidos em relação à nota fiscal original.