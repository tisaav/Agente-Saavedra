# 1010 Rejeição: NF-e com referenciamento a nível de nota e item [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37099289989015-1010-Rejei%C3%A7%C3%A3o-NF-e-com-referenciamento-a-n%C3%ADvel-de-nota-e-item-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37099289989015-1010-Rejei%C3%A7%C3%A3o-NF-e-com-referenciamento-a-n%C3%ADvel-de-nota-e-item-nItem-999)  
> **ID:** `37099289989015` | **Última Atualização:** 2026-07-22T14:19:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099260649623)

 **MENSAGEM**

1010 Rejeição: NF-e com referenciamento a nível de nota e item [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099289983639)

 **SITUAÇÃO**

Ao emitir uma NF-e, o sistema retorna uma rejeição ao identificar a presença de documentos fiscais referenciados no cabeçalho da nota e também nos itens do documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099260650391)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37936080980887)

 Acesse a tela **''Tipos de Operação - TOP''** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37936080983063)

 Verifique a configuração da TOP utilizada na nota fiscal rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37936080985239)

 Na aba **“NF-e/NFC-e/CF-e”**, verifique se existe alguma configuração de **referenciamento de documentos fiscais** definida no nível da nota fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099260652951)

 Acesse a nota fiscal que apresentou a rejeição e confirme se há **documentos fiscais referenciados**, tanto no **cabeçalho** da nota quanto nos **itens**, removendo qualquer referência indevida, se necessário.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099289985303)

 Escolha **apenas um nível** para referenciar os documentos fiscais: Se optar pelo referenciamento no nível da nota (cabeçalho), remova todos os referenciamentos nos itens. Se optar pelo referenciamento no nível dos itens, remova todos os referenciamentos no cabeçalho da nota.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38194755844247)

 Após realizar as alterações necessárias, gere novamente a NF-e para transmissão à Sefaz.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099260653463)

 **CAUSA**

Esta rejeição ocorre devido a uma regra de validação da Sefaz que impede o referenciamento simultâneo de documentos fiscais em dois níveis diferentes na mesma NF-e. De acordo com as especificações técnicas, o referenciamento de documentos fiscais deve ser feito **exclusivamente** em um dos níveis:

- 

**Nível de nota (cabeçalho)**: quando o referenciamento se aplica a toda a nota fiscal.

- 

**Nível de item**: quando o referenciamento é específico para determinados itens da nota fiscal.

Quando o sistema detecta referenciamentos nos dois níveis simultaneamente, a validação falha e a nota é rejeitada com o código 1010.