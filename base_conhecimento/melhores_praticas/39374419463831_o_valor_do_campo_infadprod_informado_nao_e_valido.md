# O valor do campo infAdProd informado não é válido

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39374419463831-O-valor-do-campo-infAdProd-informado-n%C3%A3o-%C3%A9-v%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/39374419463831-O-valor-do-campo-infAdProd-informado-n%C3%A3o-%C3%A9-v%C3%A1lido)  
> **ID:** `39374419463831` | **Última Atualização:** 2026-08-07T19:55:25Z

---

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39374419461911)

 **Situação**

Ao confirmar uma **Nota Fiscal Eletronica**, o sistema apresenta a mensagem:

**"O valor do campo infAdProd (Informações adicionais do produto - NF referenciada, informações complementares, etc.) informado não é válido."**

Essa mensagem impede a transmissão da NF-e, mesmo quando as configurações e os cadastros gerais aparentam estar corretos.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39374432203159)

 **Solução**

Siga os passos abaixo para realizar a correção:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39374432203415)

 Selecione a nota no respectivo Portal, botão **"NF-e**: **'Gerar XML da NF-e em arquivo para conferência"**'

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39374419462423)

 Abra o XML gerado e localize a tag `**infAdProd**` correspondente ao item da nota.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39374432203799)

Analise o conteúdo enviado nessa tag e verifique se:

- ultrapassa o limite de **500 caracteres**;

- contém caracteres especiais não permitidos, como: `&`, `<`, `>`, `'`, `"`, `#`, `@`, `%`, `*`, `;`, `?` e `§`;

- possui informações inconsistentes ou excesso de conteúdo. 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39374432203927)

Identifique a origem das informações enviadas na tag `**infAdProd**`, que podem ser provenientes de:

- descrição do produto;

- observação do produto;

- informações complementares;

- NF referenciada;

- outras informações adicionadas durante a geração do XML. 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39374432204055)

 Realize os ajustes necessários na origem da informação identificada.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39374419462551)

 Caso a alteração seja realizada em um cadastro utilizado pelo item da nota, remova e inclua novamente o item para atualizar as informações.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/39374419462679)

 Gere um novo lote e transmita novamente a NF-e.
 

##### **

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42549605384471)

IMPORTANTE: **

##### O conteúdo da tag **infAdProd** pode ser composto por diferentes informações, como **descrição do produto**, **observação do produto,**  **informações complementares**, **NF referenciada** ou até mesmo pelo **tamanho total do XML** gerado. Por esse motivo, **a análise deve ser iniciada pelo XML de conferência**, identificando exatamente qual conteúdo está sendo enviado na tag **infAdProd** antes de realizar qualquer ajuste.

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39374419462807)

 **Causa**

A tag **infAdProd** do XML da NF-e possui restrições definidas pela SEFAZ, entre elas:

- limite máximo de **500 caracteres**;

- proibição de determinados caracteres especiais que possam invalidar o XML.

Quando o conteúdo enviado na tag não atende a essas regras, a NF-e é rejeitada, impedindo sua autorização.