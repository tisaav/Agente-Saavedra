# 1081 Rejeição: Total de Diferimento do IBS Municipal difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098933996055-1081-Rejei%C3%A7%C3%A3o-Total-de-Diferimento-do-IBS-Municipal-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098933996055-1081-Rejei%C3%A7%C3%A3o-Total-de-Diferimento-do-IBS-Municipal-difere-da-soma-dos-itens)  
> **ID:** `37098933996055` | **Última Atualização:** 2026-07-22T14:20:05Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098933971479)

 **MENSAGEM**

1081 Rejeição: Total de Diferimento do IBS Municipal difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098933973783)

 **SITUAÇÃO**

Ao tentar emitir um documento fiscal eletrônico (NF-e ou NFC-e) que contém itens com diferimento do IBS Municipal, o sistema da Sefaz rejeita o documento porque o valor total do diferimento informado no documento não corresponde à soma dos valores de diferimento calculados para cada item.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098933975447)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098946790935)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098933981207)

 Verifique se o campo **''Código de Situação Tributária'' (CST)** utilizado nos itens do documento permite o uso de diferimento (ind_gDif = 1) podem ter valores de diferimento aplicados.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098933984023)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a configuração do TOP utilizado está correta para operações com diferimento do IBS Municipal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098933986455)

 Verifique os valores de diferimento calculados para cada item do documento.

- 

O valor do diferimento (vDif) deve ser calculado conforme a fórmula:

```text
vDif = vBC x (pIBSMun / 100) x (pDif / 100)
```

 

**vBC** = Base de cálculo

**pIBSMun **= Percentual do IBS Municipa

**pDif **= Percentual do diferimento 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098946799767)

 Recalcule o documento fiscal para garantir que o sistema atualize corretamente os valores de diferimento de cada item e o total do documento.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38478766395543)

 Verifique se o valor total do diferimento do IBS Municipal no documento corresponde exatamente à soma dos valores de diferimento de todos os itens.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098946801687)

 **CAUSA**

Esta rejeição ocorre devido a uma inconsistência no cálculo do diferimento do IBS Municipal. Conforme a regra de validação UB42-10 da Sefaz, quando informado o grupo de Diferimento (gIBSMun/gDif), o valor do diferimento (vDif) deve ser calculado pela fórmula: vDif = vBC x (pIBSMun / 100) x (pDif / 100).

A rejeição 1081 é acionada quando o valor total do diferimento do IBS Municipal informado no documento não corresponde à soma dos valores de diferimento calculados para cada item, conforme a fórmula estabelecida pela legislação da Reforma Tributária (Lei Complementar 214/2025).

Possíveis causas incluem:

- 

Cálculo incorreto do diferimento em um ou mais itens

- 

Inconsistência na totalização dos valores de diferimento

- 

Utilização de CST que não permite diferimento

- 

Configuração incorreta das alíquotas do IBS Municipal ou dos percentuais de diferimento