# 1040 Rejeição: Valor do Tributo Regular da UF difere do calculado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096605917719-1040-Rejei%C3%A7%C3%A3o-Valor-do-Tributo-Regular-da-UF-difere-do-calculado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096605917719-1040-Rejei%C3%A7%C3%A3o-Valor-do-Tributo-Regular-da-UF-difere-do-calculado-nItem-999)  
> **ID:** `37096605917719` | **Última Atualização:** 2026-07-22T14:21:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096605904023)

 **MENSAGEM**

1040 Rejeição: Valor do Tributo Regular da UF difere do calculado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096605908375)

 **SITUAÇÃO**

Rejeição apresentada na emissão de uma NF-e ou NFC-e quando o valor do **Tributo Regular do IBS Estadual (vTribRegIBSUF)** informado no documento fiscal está diferente do valor considerado pela Sefaz no grupo de **Tributação Regular**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096597605271)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096605910295)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se a configuração da alíquota efetiva regula do IBS Estadual está correta para a classificação tributária utilizada no item rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096597606167)

 Confira se o **"Código de Classificação Tributária"** (cClassTrib) está corretamente configurado para o produto em questão e se está de acordo com a legislação vigente.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096605913751)

 Verifique se o campo **"Alíquota Regular do IBS da UF"** (pAliqEfetRegIBSUF) está configurado corretamente no cadastro da alíquota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096605914135)

 Certifique-se de que a **Base de Cálculo **(vBC) utilizada para o cálculo do IBS está correta no documento fiscal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096597607831)

 Recalcule o valor do tributo regular do IBS Estadual utilizando a fórmula:

```text
vTribRegIBSUF = gIBSCBS/vBC x (gTribRegular/pAliqEfetRegIBSUF / 100).
```

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096597608343)

 Após realizar as correções, tente emitir o documento fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096605915799)

 **CAUSA**

A rejeição 1040 ocorre devido a uma **inconsistência no cálculo do Tributo Regular do IBS Estadual**. Conforme a regra de validação UB72-10 da Sefaz, quando informado o grupo da Tributação Regular (gIBSCBS/gTribRegular), o valor do Tributo Regular do IBS Estadual (vTribRegIBSUF) deve ser resultante da multiplicação da Base de Cálculo pela Alíquota Efetiva Regular do IBS do Estado, dividida por 100.

Esta validação é aplicada para documentos fiscais modelo 55 (NF-e) e 65 (NFC-e) e está relacionada às novas regras tributárias estabelecidas pela Lei Complementar 214/2025, que implementa o Imposto sobre Bens e Serviços (IBS) como parte da Reforma Tributária.

O erro pode ser causado por: Configuração incorreta das alíquotas efetivas do IBS Estadual Erro no cálculo da base de cálculo do IBS Divergência entre o valor informado e o valor calculado segundo a fórmula estabelecida pela Sefaz Classificação tributária incompatível com a operação realizada