# Não existem produtos nos itens desta nota. Informe o valor de desconto no campo desconto de serviços

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656493-N%C3%A3o-existem-produtos-nos-itens-desta-nota-Informe-o-valor-de-desconto-no-campo-desconto-de-servi%C3%A7os](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656493-N%C3%A3o-existem-produtos-nos-itens-desta-nota-Informe-o-valor-de-desconto-no-campo-desconto-de-servi%C3%A7os)  
> **ID:** `360043656493` | **Última Atualização:** 2026-07-22T16:04:33Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135440524951)

 MENSAGEM:**

[CORE_E02699] Não existem produtos nos itens desta nota. Informe o valor de desconto no campo desconto de serviços.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135417891607)

 SITUAÇÃO:**

Ao tentar inserir um desconto no total da nota(rodapé), para uma NFS-e, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135440528279)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135440530583)

 Acesse (*Comercial » Configuração » Configurador de Layout da Nota)*:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135417895063)

 Acesse o Layout que geralmente é usado para Notas de Serviço e na grade de **"Campos disponíveis"**, pesquise pelo campo **"Total desc. serviços"**. Disponibilize o campo no rodapé do Layout da Nota e salve a alteração.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135417896343)

 Acesse (*Comercial » Rotinas » Central de Vendas)*:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135417895063)

 Acesse novamente a Nota e no rodapé apresentará o campo Total desc. serviços** **que será usado para destacar desconto em NFS-e's. Este campo será considerado para trabalhar com desconto em notas de serviço. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16135440536215)

 CAUSA:**

Ocorre quando o desconto em uma NFS-e não está declarado no campo próprio que é Total desc. serviços, geralmente no rodapé da Nota.