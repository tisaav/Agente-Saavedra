# Informado incorretamente o campo meio de pagamento

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000482862-Informado-incorretamente-o-campo-meio-de-pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000482862-Informado-incorretamente-o-campo-meio-de-pagamento)  
> **ID:** `1500000482862` | **Última Atualização:** 2026-07-22T15:26:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275679327255)

 MENSAGEM**:

[899-Rejeição] Informado incorretamente o campo meio de pagamento.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275633371927)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275633373847)

 Acesse o Tipos de Título em: *Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título*
Aba: **"Geral"**
Campo **"Tipo de pgto para NFC-e / NF-e / CF-e": **configurar, observando as opções abaixo

Para NFC-e considere as seguintes formas de pagamento:

- 01-Dinheiro;

- 02-Cheque;

- 03-Cartão de Crédito;

- 04-Cartão de Débito;

- 05-Crédito Loja;

- 10-Vale Alimentação;

- 11-Vale Refeição;

- 12-Vale Presente;

- 13-Vale Combustível;

- 15 - Boleto Bancário;

- 99 - Outros

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275633375127)

 Após os ajustes, acesse novamente a nota, redigite o tipo de negociação ou fature novamente e gere lote.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275633376407)

 OBSERVAÇÃO:**

Pode causar rejeição também quando a empresa informada no cabeçalho for diferente da empresa informada no financeiro. Pois, o sistema busca os dados dos títulos e liga a empresa do financeiro com a empresa do cabeçalho.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16275679337623)

 CAUSA:**

Ocorre quando quando for emitida uma NFC-e (modelo 65) e no Tipo de Pagamento for informado sem pagamento, acontece a rejeição.

Trecho de XML: [tPag 90-Sem pagamento - Incorreto.]

 

![Imagem](https://lh3.googleusercontent.com/-ypVypwAMoX0/X9tzoVBMqcI/AAAAAAAAIGw/Q89BGEZOhQAr0R6eeSkjJLKmkXxOScarQCK8BGAsYHg/s0/2020-12-17.png)

 

**Nota técnica:** [Nota Técnica 2016.002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=XPcFD/sRNlQ=)