# The value '0' of element 'MunicipioPrestacao' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043227853-The-value-0-of-element-MunicipioPrestacao-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043227853-The-value-0-of-element-MunicipioPrestacao-is-not-valid)  
> **ID:** `360043227853` | **Última Atualização:** 2026-07-22T16:06:22Z

---

** 

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087027615127)

 MENSAGEM**:

cvc-minInclusive-valid: Value '0' is not facet-valid with respect to minInclusive '1' for type 'tpCodCidade'.
cvc-type.3.1.3: The value '0' of element 'MunicipioPrestacao' is not valid.

 

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086998409495)

 SOLUÇÃO**:

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086998411159)

 Acesse a NFS-e no Portal de Vendas, verifique se o campo **"Cidade de Prestação do Serviço"** está disponível para uso. Caso não esteja, considere liberar  através do [Configurador de Layout de Nota.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)

Preencha este campo com a informação desejada.

 

![The_value__0__of_element__MunicipioPrestacao__is_not_valid.png](https://ajuda.sankhya.com.br/hc/article_attachments/14659269544343)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086998416919)

 Salve o registro na nota e gere o Lote novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086998418711)

 CAUSA**:

Ocorre quando na emissão de uma NFS-e, o campo 'Cidade de Prestação do Serviço' não está devidamente preenchido.


---

### 🔗 Links e Referências Internas:

- [Configurador de Layout de Nota.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)