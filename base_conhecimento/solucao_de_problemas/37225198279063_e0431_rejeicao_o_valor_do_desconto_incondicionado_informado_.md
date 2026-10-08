# E0431 Rejeição: O valor do desconto incondicionado informado na DPS deve ser menor que o valor do serviço e maior que zero.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225198279063-E0431-Rejei%C3%A7%C3%A3o-O-valor-do-desconto-incondicionado-informado-na-DPS-deve-ser-menor-que-o-valor-do-servi%C3%A7o-e-maior-que-zero](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225198279063-E0431-Rejei%C3%A7%C3%A3o-O-valor-do-desconto-incondicionado-informado-na-DPS-deve-ser-menor-que-o-valor-do-servi%C3%A7o-e-maior-que-zero)  
> **ID:** `37225198279063` | **Última Atualização:** 2026-07-22T14:16:09Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225166912663)

 **MENSAGEM**

E0431 Rejeição: O valor do desconto incondicionado informado na DPS deve ser menor que o valor do serviço e maior que zero.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225150397335)

 **SITUAÇÃO**

O Documento de Prestação de Serviços (DPS) foi transmitido com a informação de um valor de desconto incondicionado inconsistente em relação ao valor total do serviço informado no documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225150397847)

 **SOLUÇÃO**

Para resolver esta rejeição, ajuste o **valor do desconto incondicionado** no documento fiscal, seguindo os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225166916759)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento que foi rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225150398743)

 Na grade **''Itens''**, localize o campo **''Vlr. desconto'' **do documento.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225150399767)

 Verifique o **valor total do serviço** informado no documento.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225150402583)

 Ajuste o valor do desconto incondicionado considerando as seguintes regras:

- 

O valor do desconto deve ser **maior que zero**;

- 

O valor do desconto deve ser **menor que o valor total do serviço**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225166921367)

 Salve as alterações.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225150405911)

 Transmita novamente o **Documento de Prestação de Serviços (DPS)** para a Sefaz.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225166929431)

 **CAUSA**

A rejeição ocorre quando o **valor do desconto incondicionado** informado no Documento de Prestação de Serviços não atende às regras de validação da Sefaz. Especificamente, o sistema rejeita o documento quando:

- 

O valor do desconto é **igual ou menor que zero**;

- 

O valor do desconto é **igual ou maior que o valor total do serviço**, o que resultaria em um valor líquido negativo ou zero para o serviço prestado.

Essa validação garante a **consistência fiscal** do documento e impede que sejam transmitidos valores incompatíveis com a prestação de serviços.