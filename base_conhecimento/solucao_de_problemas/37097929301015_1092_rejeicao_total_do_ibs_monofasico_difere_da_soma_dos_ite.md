# 1092 Rejeição: Total do IBS monofásico difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097929301015-1092-Rejei%C3%A7%C3%A3o-Total-do-IBS-monof%C3%A1sico-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097929301015-1092-Rejei%C3%A7%C3%A3o-Total-do-IBS-monof%C3%A1sico-difere-da-soma-dos-itens)  
> **ID:** `37097929301015` | **Última Atualização:** 2026-07-22T14:20:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097929275287)

 **MENSAGEM**

1092 Rejeição: Total do IBS monofásico difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097949860887)

 **SITUAÇÃO**

O valor total do IBS monofásico informado na NF-e ou NFC-e difere do somatório dos valores de IBS monofásico apurados para os itens do documento fiscal, em operações sujeitas à tributação monofásica.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097949862039)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097949863959)

 Acesse a tela** ''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se os produtos estão corretamente configurados como sujeitos á tributação monofásica.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097929279895)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se o CST do IBS/CBS estão configurados corretamente para operações monofásicas.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097949868439)

 Confira se o cálculo do IBS monofásico está sendo realizado corretamente para cada item, considerando a fórmula:

```text
vTotIBSMonoItem = vIBSMono + vIBSMonoReten - vIBSMonoDif
```

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38379476934551)

 Verifique se há **diferimento** aplicado aos biocombustíveis conforme o artigo 178 da LC 214/2025 e se este está sendo calculado corretamente.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097949871767)

 Certifique-se de que o **total do IBS monofásico** no documento corresponde exatamente à soma dos valores de IBS monofásico de todos os itens. 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097929289751)

 **CAUSA**

A rejeição ocorre quando o sistema de validação da SEFAZ detecta uma **inconsistência entre o valor total do IBS monofásico declarado no documento fiscal e a soma dos valores de IBS monofásico calculados para cada item individualmente**.

Esta validação está baseada na regra UB104-10, que verifica se o valor total do IBS Monofásico do item (vTotIBSMonoItem) corresponde ao resultado da fórmula:

```text
vTotIBSMonoItem = vIBSMono + vIBSMonoReten - vIBSMonoDif.
```

 

Esta inconsistência pode ocorrer devido a:

- 

Erros de arredondamento nos cálculos dos valores de IBS monofásico;

- 

Configuração incorreta das alíquotas de IBS para produtos sujeitos à tributação monofásica;

- 

Aplicação incorreta de diferimento para biocombustíveis;

- 

Falha na totalização dos valores de IBS monofásico dos itens no documento fiscal.