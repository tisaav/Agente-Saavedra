# 1146 Rejeição: NF-e referenciada de pagamento antecipado informada indevidamente

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098195306135-1146-Rejei%C3%A7%C3%A3o-NF-e-referenciada-de-pagamento-antecipado-informada-indevidamente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098195306135-1146-Rejei%C3%A7%C3%A3o-NF-e-referenciada-de-pagamento-antecipado-informada-indevidamente)  
> **ID:** `37098195306135` | **Última Atualização:** 2026-07-22T14:20:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37988038260119)

 MENSAGEM**

1146 Rejeição: NF-e referenciada de pagamento antecipado informada indevidamente

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098195288215)

 **SITUAÇÃO**

Ao emitir uma **NF-e**, o sistema retorna rejeição quando há **informação de nota fiscal referenciada de pagamento antecipado** vinculada ao documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098195289111)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098225305495)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098195290391)

 Selecione o tipo de operação utilizado na nota fiscal que está sendo rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098195294871)

 Na aba **"NF-e/NFC-e/CF-e''**, verifique o campo **"NF-e"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098225307159)

 Caso a emissão seja de **NF-e de complemento de preço**, verifique se o campo **“NF-e”**, está configurado com a opção **“Complementar”**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098225308183)

 Se **não** se tratar de uma nota fiscal complementar, acesse a tela****[“Central de Vendas”](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas) e **remova a referência à nota fiscal de pagamento antecipado** informada no documento.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098195298199)

 Se a emissão for de **NF-e complementar**, confirme se a **nota fiscal referenciada** está informada corretamente e se corresponde, de fato, a uma **NF-e de pagamento antecipado**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098195299735)

 Após realizar as correções, **gere um novo lote** e tente emitir a **NF-e novamente**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098225313815)

 **CAUSA**

Esta rejeição ocorre quando uma NF-e referenciada de pagamento antecipado é informada em uma nota fiscal que **não possui finalidade de complemento** (finNFe diferente de 2) ou quando a nota fiscal não é do **tipo complemento de preço**. De acordo com a legislação, as notas fiscais de pagamento antecipado só podem ser referenciadas em notas fiscais complementares específicas para complemento de preço.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [“Central de Vendas”](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)