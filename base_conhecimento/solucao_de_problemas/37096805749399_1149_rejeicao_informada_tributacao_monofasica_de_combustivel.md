# 1149 Rejeição: Informada Tributação Monofásica de Combustível com diferimento indevidamente [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096805749399-1149-Rejei%C3%A7%C3%A3o-Informada-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-com-diferimento-indevidamente-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096805749399-1149-Rejei%C3%A7%C3%A3o-Informada-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-com-diferimento-indevidamente-nItem-999)  
> **ID:** `37096805749399` | **Última Atualização:** 2026-07-22T14:21:09Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096797599511)

 **MENSAGEM**

1149 Rejeição: Informada Tributação Monofásica de Combustível com diferimento indevidamente [nItem: 999] 

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096805730583)

 **SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e, o sistema está informando indevidamente a Tributação Monofásica com diferimento (ID: UB99) aplicado aos biocombustíveis, conforme previsto no art. 178 da LC 214/2025, para um produto que não permite esse tipo de tributação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096797605783)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096797607063)

 Verifique a classificação tributária do produto na tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e certifique-se de que o campo **"Classificação ICMS"** está configurado corretamente para o produto em questão.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096797608087)

 Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se o indicador **"Permite Tributação Monofásica com diferimento"** (ind_gMonoDif) está configurado como **0 (zero)** para a classificação tributária do produto.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096797609111)

 Caso o produto não deva ter tributação monofásica com diferimento, remova esta informação do documento fiscal, ajustando a configuração da operação na tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096797610007)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique se as configurações de tributação estão adequadas para o tipo de operação utilizado, garantindo que não esteja sendo informada indevidamente a tributação monofásica com diferimento.

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096805742359)

 **CAUSA**

Esta rejeição ocorre quando o sistema está informando a Tributação Monofásica com diferimento (ID: UB99) para um produto cuja classificação tributária possui o indicador que **não permite** este tipo de tributação (ind_gMonoDif = 0).

Conforme a regra de validação UB99-20, quando a classificação tributária do produto possui o indicador que não permite Tributação Monofásica de Combustível com diferimento (ind_gMonoDif = 0), não deve ser informada a Tributação Monofásica com diferimento (ID: UB99) aplicado aos biocombustíveis, observado o art. 178 da LC 214/2025.

A tributação monofásica com diferimento é aplicável apenas para casos específicos de biocombustíveis, conforme previsto no artigo 178 da Lei Complementar 214/2025. Quando esta tributação é informada para produtos que não se enquadram nesta categoria, a SEFAZ rejeita o documento fiscal com o código de erro 1149.