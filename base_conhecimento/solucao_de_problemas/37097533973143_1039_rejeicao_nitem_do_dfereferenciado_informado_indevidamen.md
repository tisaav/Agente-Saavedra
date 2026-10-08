# 1039 Rejeição: nItem do DFeReferenciado informado indevidamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097533973143-1039-Rejei%C3%A7%C3%A3o-nItem-do-DFeReferenciado-informado-indevidamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097533973143-1039-Rejei%C3%A7%C3%A3o-nItem-do-DFeReferenciado-informado-indevidamente-nItem-999)  
> **ID:** `37097533973143` | **Última Atualização:** 2026-07-22T14:20:38Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097533954967)

 **MENSAGEM**

1039 Rejeição: nItem do DFeReferenciado informado indevidamente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097536871447)

 **SITUAÇÃO**

A NF-e ou NFC-e foi emitida com referência a documento fiscal eletrônico (DFe) anterior, porém o número do item (**nItem**) informado no documento referenciado está incorreto.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097533960343)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097533961623)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a operação está configurada corretamente para o tipo de documento que está sendo emitido.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097533962519)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e"** está configurado adequadamente para a operação que está realizando (devolução, complemento ou normal).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097533963543)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e verifique se os **itens referenciados **estão sendo informados corretamente:

- 

Certifique-se de que o número do item (nItem) informado existe no documento fiscal referenciado.

- 

Verifique se o documento fiscal referenciado está sendo informado com a chave de acesso correta.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097536885527)

 Para identificar qual item está causando a rejeição, verifique o número indicado na mensagem de erro [nItem: 999] e corrija a referência deste item específico.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097536886935)

 Caso esteja realizando uma devolução, certifique-se de que está referenciando corretamente os itens da nota fiscal original, mantendo a mesma numeração de itens.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097533967127)

 **CAUSA**

Esta rejeição ocorre devido à **informação incorreta do número do item (nItem)** no documento fiscal eletrônico referenciado. Isso pode acontecer por diversos motivos:

- 

O número do item informado não existe no documento fiscal referenciado;

- 

O documento fiscal referenciado foi informado incorretamente;

- 

Em operações de devolução ou complemento, a numeração dos itens não está seguindo a mesma sequência do documento original;

- 

Houve erro na configuração do Tipos de Operação para a finalidade específica do documento (devolução, complemento, etc.).

A validação da SEFAZ verifica se o número do item referenciado existe no documento original, e quando não encontra correspondência, gera esta rejeição para garantir a integridade das informações fiscais.