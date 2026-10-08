# 1070 Rejeição: Valor do IBS monofásico difere do calculado [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096859411095-1070-Rejei%C3%A7%C3%A3o-Valor-do-IBS-monof%C3%A1sico-difere-do-calculado-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096859411095-1070-Rejei%C3%A7%C3%A3o-Valor-do-IBS-monof%C3%A1sico-difere-do-calculado-nItem-999)  
> **ID:** `37096859411095` | **Última Atualização:** 2026-07-22T14:21:08Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096834441367)

 **MENSAGEM**

1070 Rejeição: Valor do IBS monofásico difere do calculado [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096834444951)

 **SITUAÇÃO**

Rejeição apresentada quando o valor total do **IBS Monofásico do item (vTotIBSMonoItem)** informado na nota fiscal eletrônica está divergente do valor esperado para esse item.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096859394071)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096834446359)

 Acesse a tela **''Produtos'' **(Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está configutado corretamente para a tributação monofásica do IBS.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096834447895)

 Confira se o campo **"Classificação ICMS"** está com o valor adequado para produtos sujeitos à tributação monofásica.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096859399575)

 Acesse as telas **''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquota de CBS'' **(Livros Fiscais » Cadastros » Aliquotas de CBS).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096834449047)

 Verifique se o **"Código de situação tributária"** **(CST)** selecionado permite a utilização do IBS Monofásico.

- 

O indicador **"ind_gIBSCBSMono"** deve estar configurado como 1 para permitir a tributação monofásica.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096834450071)

 Verifique os valores informados nos campos do grupo **"gIBSCBSMono"** e certifique-se de que estão corretos:

- 

Valor do IBS Monofásico (**"vIBSMono"**)

- 

Valor do IBS Monofásico Retido (**"vIBSMonoReten"**)

- 

Valor do IBS Monofásico Diferido (**"vIBSMonoDif"**)

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096834452631)

 Recalcule o valor total do IBS Monofásico do item utilizando a fórmula:

```text
vTotIBSMonoItem = vIBSMono + vIBSMonoReten - vIBSMonoDif
```

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38277439836823)

 Caso esteja utilizando o **"****Assistente de Configuração Integral da Reforma Tributária****"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária), verifique se todas as configurações estão corretas para o cálculo do IBS monofásico.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38277439838743)

 Após realizar as correções necessárias, tente emitir a nota fiscal novamente para verificar se a rejeição foi solucionada.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096834454039)

 **CAUSA**

A rejeição ocorre devido à **inconsistência no cálculo do valor total do IBS Monofásico** do item (vTotIBSMonoItem). Conforme a regra de validação UB104-10, aplicável aos modelos de documentos 55 e 65, quando informado o **grupo do IBS e CBS monofásico** (grupo: gIBSCBSMono), **o valor total do IBS Monofásico do item deve ser resultante da fórmula**:

```text
vTotIBSMonoItem = vIBSMono + vIBSMonoReten - vIBSMonoDif.
```

 

Esta validação está fundamentada no artigo 178 da Lei Complementar 214/2025, que estabelece as regras para a tributação monofásica no contexto da Reforma Tributária. Quando o sistema detecta que o valor informado não corresponde ao resultado da fórmula, a nota fiscal é rejeitada com o código 1070.