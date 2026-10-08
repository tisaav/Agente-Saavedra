# cvc-type.3.1.3: The value '' of element 'qrCodCTe' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753054-cvc-type-3-1-3-The-value-of-element-qrCodCTe-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753054-cvc-type-3-1-3-The-value-of-element-qrCodCTe-is-not-valid)  
> **ID:** `360042753054` | **Última Atualização:** 2026-07-22T16:06:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088712355607)

 MENSAGEM:**

cvc-pattern-valid: Value '' is not facet-valid with respect to pattern '((HTTPS?|https?)://.*\?chCTe=[0-9]{44}&tpAmb=[1,2](&sign=[!-y])?)' for type '#AnonType_qrCodCTeinfCTeSuplTCTe'.
cvc-type.3.1.3: The value '' of element '**qrCodCTe**' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088727033495)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088712363543)

 Acesse: Configurações » Avançado » Preferências
Parâmetro **"DATINIULTNTCTE"**: informe a UF e data da última NT
                                                   *  Exemplo: ***MG:31/12/2019***

*Parâmetro ***"*DATINICTEQRCOD": **informe a data início da implementação do QRcode em CT-e
                                                     *Exemplo*: **AN:07/10/2019**
 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088712366487)

 Acesse: Comercial » Preferências » Empresa
Aba:** CT-e**
Opção **"Versão NT CTE": **última (Nota Técnica 3.00a)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088712368663)

 Acesse: Comercial » Arquivo » Cadastros » Modelo de Impressão (Nota/Pedido)
Botão **"Baixar Modelos Padrões", **baixe o modelo DACTE atualizado para impressão do QRCode

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088727045143)

 Após os ajustes, efetue o lançamento do documento novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088712376215)

 CAUSA:**

Ocorre quando a versão da NT não esta em conformidade com a data correta da obrigatoriedade da informação no XML da CT-e