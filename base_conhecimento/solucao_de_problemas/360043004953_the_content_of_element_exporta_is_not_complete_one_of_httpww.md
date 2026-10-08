# The content of element 'exporta' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":xLocExporta}' is expected

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004953-The-content-of-element-exporta-is-not-complete-One-of-http-www-portalfiscal-inf-br-nfe-xLocExporta-is-expected](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004953-The-content-of-element-exporta-is-not-complete-One-of-http-www-portalfiscal-inf-br-nfe-xLocExporta-is-expected)  
> **ID:** `360043004953` | **Última Atualização:** 2026-07-22T16:10:18Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16314968738199)

 MENSAGEM:**

cvc-complex-type.2.4.b: The content of element 'exporta' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":xLocExporta}' is expected.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16314968744343)

 **SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16314968747671)

 Acesse a **Central de Notas** e identifique no rodapé os campos **"Local do Embarque"** e **"UF Local Embarque"**. Preencha os 2 campos corretamente.

 

![Local](https://ajuda.sankhya.com.br/hc/article_attachments/15660356732567)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16314996376855)

 Após os ajustes, transmita a NF-e novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16314996379159)

 **CAUSA:**

Ocorre quando está emitindo uma **Nota de Exportação** com CFOP iniciada em 7 (Ex: CFOP 7949) e não foi preenchida Local de Embarque e UF de Embarque. Caso não seja uma nota de Exportação, considere ajustar a CFOP de acordo com o tipo de movimento da nota.