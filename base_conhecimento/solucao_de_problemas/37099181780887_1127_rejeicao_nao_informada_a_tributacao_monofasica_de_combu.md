# 1127 Rejeição: Não informada a Tributação Monofásica de Combustível com Retenção [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37099181780887-1127-Rejei%C3%A7%C3%A3o-N%C3%A3o-informada-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-com-Reten%C3%A7%C3%A3o-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37099181780887-1127-Rejei%C3%A7%C3%A3o-N%C3%A3o-informada-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-com-Reten%C3%A7%C3%A3o-nItem-999)  
> **ID:** `37099181780887` | **Última Atualização:** 2026-07-22T14:19:59Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099181769879)

 **MENSAGEM**

1127 Rejeição: Não informada a Tributação Monofásica de Combustível com Retenção [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099181771287)

 **SITUAÇÃO**

A NF-e ou NFC-e foi emitida para operação com combustível sujeita à Tributação Monofásica com Retenção, porém o grupo de tributação correspondente não foi informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099172916887)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099172918551)

 Acesse a tela **''Produtos'' **(Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está corretamente configurado como combustível que exigem tributação monofásica com retenção.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099181774103)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a operação está configurada corretamente para operações com combustíveis.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099172919703)

 Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e configure corretamente as alíquotas para tributação monofásica com retenção de combustíveis.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099172923543)

 Verifique se o indicador **"ind_gMonoReten"** está configurado como **"1"** na classificação tributária do produto, indicando que é exigida a Tributação Monofásica de Combustível com Retenção.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099172924823)

 Ao emitir a nota fiscal, certifique-se de que o grupo de Tributação Monofásica com Retenção (ID: UB90) esteja devidamente preenchido para os itens de combustíveis que exigem essa tributação, conforme o Art. 178 da LC 214/2025.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37099181776407)

 **CAUSA**

A rejeição 1127 ocorre quando a classificação tributária do produto (**cClassTrib**) possui o indicador que exige Tributação Monofásica de Combustível com Retenção (**ind_gMonoReten = 1**), mas o grupo de Tributação Monofásica com Retenção do imposto (ID: UB90) não foi informado na nota fiscal para o biocombustível a ser misturado, conforme exigido pelo Art. 178 da Lei Complementar 214/2025.