# 1128 Rejeição: Informada indevidamente a Tributação Monofásica de Combustível com Retenção [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098858134935-1128-Rejei%C3%A7%C3%A3o-Informada-indevidamente-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-com-Reten%C3%A7%C3%A3o-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098858134935-1128-Rejei%C3%A7%C3%A3o-Informada-indevidamente-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-com-Reten%C3%A7%C3%A3o-nItem-999)  
> **ID:** `37098858134935` | **Última Atualização:** 2026-07-22T14:20:06Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098858124439)

 **MENSAGEM**

1128 Rejeição: Informada indevidamente a Tributação Monofásica de Combustível com Retenção [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098858125847)

 **SITUAÇÃO**

A NF-e ou NFC-e foi emitida com **indicação de Tributação Monofásica com Retenção** sobre biocombustível a ser misturado para produto cuja classificação tributária não permite esse enquadramento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098850165911)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098850167703)

 Verifique se o produto possui tributação monofásica com retenção. Se não for o caso, acesse a tela** ''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP utilizado na operação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098858128663)

 Na aba ''**Impostos''**, verifique se os campos **“Tem CBS”** e **“Tem IBS”** estão marcados indevidamente. Caso estejam selecionados, desmarque as opções correspondentes.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098858128919)

 Caso o produto realmente deva ter tributação monofásica com retenção, acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique a **Classificação ICMS **do produto.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098850169239)

 Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se a classificação tributária do produto está configurada corretamente com o indicador **"ind_gMonoReten"** definido como 1 (permitido).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098850170647)

 Ajuste a classificação tributária do produto para que seja compatível com a tributação monofásica com retenção, conforme estabelecido no Art. 178 da LC 214/2025.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098858130583)

 **CAUSA**

A rejeição 1128 ocorre quando o sistema detecta que foi informada indevidamente a Tributação Monofásica com Retenção do imposto (id: UB90) sobre o biocombustível a ser misturado, enquanto a classificação tributária do produto possui o indicador **ind_gMonoReten = 0**, o que significa que este tipo de produto não permite a tributação monofásica com retenção.

Esta validação está baseada no Art. 178 da Lei Complementar 214/2025, que estabelece regras específicas para a tributação monofásica de combustíveis. Quando o indicador **ind_gMonoReten** está configurado como 0 na classificação tributária do produto, o sistema entende que este produto não deve ter a tributação monofásica com retenção aplicada, e qualquer tentativa de informar este tipo de tributação resultará na rejeição 1128.