# 1142 Rejeição: Soma dos valores de IBS e CBS em compras governamentais divergente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096675910807-1142-Rejei%C3%A7%C3%A3o-Soma-dos-valores-de-IBS-e-CBS-em-compras-governamentais-divergente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096675910807-1142-Rejei%C3%A7%C3%A3o-Soma-dos-valores-de-IBS-e-CBS-em-compras-governamentais-divergente-nItem-999)  
> **ID:** `37096675910807` | **Última Atualização:** 2026-09-18T11:51:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096650781335)

 **MENSAGEM**

1142 Rejeição: Soma dos valores de IBS e CBS em compras governamentais divergente [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096675902359)

 **SITUAÇÃO**

Rejeição apresentada na emissão de uma NF-e quando, com o grupo de **compras governamentais** informado, a soma dos valores de **IBS e CBS** declarados no grupo de **composição do valor do IBS e da CBS em compras governamentais (gTribCompraGov)** está divergente dos valores informados nos grupos **gIBSUF**, **gIBSMun** e **gCBS**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096650782359)

 **SOLUÇÃO**

Para solucionar esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096650785047)

 Verifique se o documento fiscal possui o grupo de compras governamentais informado corretamente na tela de emissão de notas fiscais.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096650786199)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o tipo de operação utilizado está configurado corretamente para operações de compras governamentais.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096650786839)

 Certifique-se de que os valores informados no grupo de informações da composição do valor do IBS e da CBS em compras governamentais (grupo gTribCompraGov) estejam consistentes com os valores declarados nos grupos gIBSUF, gIBSMun e gCBS.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096650787479)

 Verifique se a seguinte equação está sendo respeitada:

```text
A soma dos valores de vTribIBSUF + vTribIBSMun + vTribCBS do grupo gTribCompraGov deve ser igual ao resultado de gIBSUF/vIBSUF + gIBSMun/vIBSMun + gCBS/vCBS.
```

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096675906199)

 Caso necessário, ajuste os valores para que a soma esteja correta e reenvie o documento fiscal. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096675906967)

 **CAUSA**

Esta rejeição ocorre devido à inconsistência entre os valores declarados no grupo de informações da composição do valor do IBS e da CBS em compras governamentais (grupo gTribCompraGov) e os valores informados nos grupos gIBSUF, gIBSMun e gCBS.

De acordo com a regra de validação UB82a-20, quando o grupo gTribCompraGov é informado, a soma dos valores de IBS e CBS deste grupo (vTribIBSUF + vTribIBSMun + vTribCBS) deve ser igual ao resultado da soma dos valores informados em tag:gIBSUF/vIBSUF + tag:gIBSMun/vIBSMun + tag:gCBS/vCBS. Caso contrário, a nota fiscal será rejeitada com o código 1142.

Esta validação é necessária para garantir a consistência dos valores tributários declarados em operações de compras governamentais, conforme estabelecido pela Lei Complementar 214/2025 que implementa a Reforma Tributária.