# 1174 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no estorno de crédito [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141512396311-1174-Rejei%C3%A7%C3%A3o-Valor-do-IBS-ou-da-CBS-deve-ser-maior-que-zero-no-estorno-de-cr%C3%A9dito-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141512396311-1174-Rejei%C3%A7%C3%A3o-Valor-do-IBS-ou-da-CBS-deve-ser-maior-que-zero-no-estorno-de-cr%C3%A9dito-nItem-999)  
> **ID:** `37141512396311` | **Última Atualização:** 2026-07-22T14:19:12Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141495912599)

 **MENSAGEM**

1174 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no estorno de crédito [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141512384919)

 **SITUAÇÃO**

Ao emitir uma nota fiscal com estorno de crédito do IBS e da CBS, o documento foi rejeitado pela SEFAZ porque os valores do IBS e da CBS no grupo de estorno de crédito foram informados como zero ou não foram preenchidos.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141495914135)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141512386455)

 Acesse a tela** ''Central de Vendas'' **(Comercial » Rotinas » Central de Vendas) e localize a nota fiscal que foi rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141512387991)

 Gere o arquivo da XML e verifique se a nota fiscal é do tipo **''Nota de Débito''** (finNFe=6) e se possui o grupo de estorno de crédito.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141495916439)

 Na grade **"Itens"** da nota fiscal e verifique o item que está apresentando a rejeição.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141495917335)

 Clique em **''Outras opções'' (ícone com três pontos)** e selecione a opção** ''Consultar/Alterar Dados do Imposto do Item''**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141512390295)

 Verifique o grupo de **Estorno de Crédito**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141512391063)

 Certifique-se de que pelo menos um dos campos abaixo esteja preenchido com valor **maior que zero**:

- 

Campo** "Valor"** (vIBS);

- 

Campo** "Valor" **(vCBS).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38197675838487)

 Após corrigir os valores, salve as alterações e tente emitir a nota fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141512391703)

 **CAUSA**

Esta rejeição ocorre quando o grupo de estorno de crédito (**gEstornoCred**) é informado na nota fiscal, mas os valores do IBS e da CBS estão zerados ou não foram preenchidos. De acordo com a regra de validação UB116-30, quando o grupo de estorno de crédito é informado, pelo menos um dos valores (IBS ou CBS) deve ser maior que zero.

A única exceção para esta regra é quando a nota fiscal de débito é do tipo "07-Perda em estoque" (campo **tpNFDebito**), situação em que a regra não se aplica.