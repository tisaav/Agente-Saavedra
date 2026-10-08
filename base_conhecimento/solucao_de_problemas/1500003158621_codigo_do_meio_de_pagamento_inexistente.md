# Código do meio de pagamento inexistente

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003158621-C%C3%B3digo-do-meio-de-pagamento-inexistente](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003158621-C%C3%B3digo-do-meio-de-pagamento-inexistente)  
> **ID:** `1500003158621` | **Última Atualização:** 2026-07-22T15:25:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334651391511)

 MENSAGEM:**

[436-Rejeição]: Código do meio de pagamento inexistente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334629836567)

SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334651396503)

 Acesse o cadastro de **"Tipos de Titulo"** em: *Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título*;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334629838999)

 Selecione o tipo de título utilizado na nota rejeitada (É possível conferir essa informação na aba **"Financeiro"** da nota, campo **"Tipo de Título"**);

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334651398295)

 Na aba: **"Geral"**, selecione o campo: **"Tipo de pgto para NFC-e / NF-e / CF-e"**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15070615018647)

 

Defina o  tipo de pagamento correto (diferente de 99-Outros), considerando as seguintes opções:

**01-Dinheiro;**
**02-Cheque;**
**03-Cartão de Crédito;**
**04-Cartão de Débito;**
**05-Crédito Loja;**
**10-Vale Alimentação;**
**11-Vale Refeição;**
**12-Vale Presente;**
**13-Vale Combustível;**
**15-Boleto Bancário;
16-Deposito Bancário;
17-Pagamento Instantâneo (PIX);
18-Transferencia Bancaria, Carteira Digital;
19-Programa de Fidelidade, Cashback, Credito Virtual;
****90-Sem pagamento;**

**
**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334629841303)

 O Tipo de Título está vinculado ao cadastro de Tipos de Negociação (*Comercial » Arquivo » Cadastros » Tipos de Negociação*), aba: **"Parcelas";**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15070627475223)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334629842839)

 Feito o ajuste, redigite o cabeçalho da nota e gere um novo lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16334651403543)

CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e no Tipo de Pagamento um valor que não consta na tabela de meios de pagamento disponibilizada pela SEFAZ, haverá a rejeição pelo motivo

**Tabela** [Nota Tecnica: 2020.006 v1.40](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=)

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500008410522)