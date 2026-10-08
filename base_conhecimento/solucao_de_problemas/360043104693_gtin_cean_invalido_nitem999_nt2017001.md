# GTIN (cEAN) inválido [nItem:999] (NT2017/001)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043104693-GTIN-cEAN-inv%C3%A1lido-nItem-999-NT2017-001](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043104693-GTIN-cEAN-inv%C3%A1lido-nItem-999-NT2017-001)  
> **ID:** `360043104693` | **Última Atualização:** 2026-07-22T16:08:10Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509620174999)

 MENSAGEM:**

[611 - Rejeição]: GTIN (cEAN) inválido [nItem:999]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509613630487)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509613632023)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*

Aba: **"Impostos"**

Campo "**EAN/GTIN Produto p/ NF-e"**. Este campo possui as seguintes opções: 

- **"Referência"**

- **"Código de barras estoque"**

- **"Código do produto"**

- **"Código de Barras Unidade Alternativa"**

- **"Não informar"**

Caso esteja diferente de 'Não informar'**,** acesse o campo no qual está referenciando acima e ajuste o Código EAN.

Unidade Alternativa (Só utilizar essa opção caso a operação seja diferente da Unidade Padrão)

Campo "**EAN/GTIN Produto p/ NF-e"**, este campo possui as seguintes opções: 

- **"Código de barras "**

- **"Código do produto"**

- **"Referência"**

- **"Não informar"**

Vale destacar que a mesma informação do item anterior, caso esteja diferente de 'Não informar', acesse o campo no qual esta referenciando acima e ajuste o Código EAN.

O site '[Codigo de Barras EAN](https://www.gs1.org/services/check-digit-calculator)'  pode ser usado para validar o dígito verificador do código.

 

- 

1. ****
1. 
1. ****

- 

| Para validar o dígito verificador ele deve ser retirado do código, conforme exemplo:   Considere a tag do xml: <cEAN>7897534803631</cEAN> Retire o último número que representa o dígito Consulte no site o número 789753480363:   O retorno do site mostra que o último número, o dígito, deve ser 3, ficando: 7897534803633 |
| --- |

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509620185879)

 Após o ajuste no cadastro do produto, redigite o produto na nota e gere lote novamente.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509613636247)

 IMPORTANTE:**

- "**DESCRREF**" - Descrição para Referência: Modifica-se por meio deste parâmetro, o nome do campo "**Referência**", aba: "**Geral".**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509620190743)

 CAUSA:**

Quando informado números no campo cEAN e houver a rejeição 611, significa que o último número do sequencial não é válido. Esse último número é gerado a partir de um cálculo realizado sobre os números anteriores. Se qualquer número for digitado pelo usuário ou for preenchido incorreto pelo ERP, o dígito verificar do cEAN (último número dó Código de Barras) estará inválido.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16509620193943)

 OBSERVAÇÃO:**

([NT2017/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=xOi0MNXspSM=)) - Nota Técnica: