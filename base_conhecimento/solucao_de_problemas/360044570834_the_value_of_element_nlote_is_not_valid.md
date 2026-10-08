# The value '' of element 'nLote' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044570834-The-value-of-element-nLote-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044570834-The-value-of-element-nLote-is-not-valid)  
> **ID:** `360044570834` | **Última Atualização:** 2026-07-22T15:51:38Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18602756226583)

 MENSAGEM:**

cvc-type.3.1.3: The value '' of element 'nLote' is not valid.
cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18602756232343)

CAUSA:**

Essa mensagem será apresentada quando determinado produto inserido na nota, possui a marcação "Tem Rastro do Lote", as informações de data de validade e fabricação preenchidas, porém a informação de lote está vazia.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18602756234263)

 SOLUÇÃO:**

Essa mensagem será apresentada quando determinado produto inserido na nota, possui a marcação "Tem Rastro do Lote", as informações de data de validade e fabricação preenchidas, porém a informação de lote está vazia.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18602730081943)

 Será necessário alinhar com os responsáveis pelas configurações de controle de lote dos produtos, qual medida cabe ao processo da empresa:

- No cadastro do produto, aba 'Estoque' verifique se existe uma linha com o campo 'Controle' em branco e 'Data de Validade' e 'Data de Fabricação' preenchidos, caso essa seja indevida, proceda com sua exclusão.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18602724746391)

 Após esse ajuste, realize um novo lançamento da nota. Caso a nota anterior tenha gerado 'Número Nota', realize sua inutilização/exclusão.