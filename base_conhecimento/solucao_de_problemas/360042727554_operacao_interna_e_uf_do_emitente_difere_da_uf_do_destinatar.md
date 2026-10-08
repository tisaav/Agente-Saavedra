# Operação Interna e UF do emitente difere da UF do destinatário/remetente contribuinte do ICMS(NT2015/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042727554-Opera%C3%A7%C3%A3o-Interna-e-UF-do-emitente-difere-da-UF-do-destinat%C3%A1rio-remetente-contribuinte-do-ICMS-NT2015-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042727554-Opera%C3%A7%C3%A3o-Interna-e-UF-do-emitente-difere-da-UF-do-destinat%C3%A1rio-remetente-contribuinte-do-ICMS-NT2015-002)  
> **ID:** `360042727554` | **Última Atualização:** 2026-07-22T16:06:36Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513055583639)

 MENSAGEM:**

[521 - Rejeição]: Operação Interna e UF do emitente difere da UF do destinatário/remetente contribuinte do ICMS.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513071302935)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513055593111)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*

Aba: **"Livro Fiscal"**

Campo **"****Atualização de Livro ICMS":** Livro de Saída - Se Movimento de Venda, a atualização do Livro será Saída.

- CFOP's para FORA do Estado: Se Movimento de Venda, CFOP inicia com 6

- CFOP's para DENTRO do Estado: Se Movimento de Venda, CFOP inicia com 5

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513055599255)

 Caso as configurações acima estejam incorretas, realize os devidos ajustes, considere inutilizar numeração da nota e realizar um novo lançamento/faturamento.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513055605911)

 IMPORTANTE:**

Para os casos onde a UF do Emitente for diferente da UF do Destinatário, e definido um endereço de entrega dentro do Estado, atente-se as configurações abaixo:

*A regra de validação 521 não se aplica se a operação é presencial (campo <indPres> igual a 1 - "Operação presencial") e não possui frete (o campo <modFrete> igual a 9 - "Sem frete"). (NT 2011/00*4).

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513055593111)

 Tela **"[Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)** (*Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*)

- Aba** "NF-e/NFC-e"**

- Campo **"Indicador de Presença para NF-e/NFC-e"**= 1 - Operação Presencial

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513055599255)

 Lançamento da nota, aba **"Transporte"**, campo **"CIF/FOB": **sem frete**.**

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513071323159)

 Se ajustada a informação do item 1, inutilize o lançamento e emita uma nova nota.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513071325591)

 **CAUSA:**

Quando for emitida uma NF-e com Indicador de Destino da Operação (idDest) igual a 1 - "Estadual" (Operação Interna) e a UF do Emitente da NF-e for diferente da UF do Destinatário, será retornado a rejeição.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458184305047)

 Exceções a regra:**

1. A regra de validação 521 não se aplica se o campo <UFCons> (UF de Consumo) foi informada com a mesma UF do emitente. (NT 2010/007);

1. A regra de validação 521 não se aplica se a operação é presencial (campo <indPres> igual a 1 - "Operação presencial") e não possui frete (o campo <modFrete> igual a 9 - "Sem frete"). (NT 2011/004).

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16513071336343)

 OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=)) - Nota técnica


---

### 🔗 Links e Referências Internas:

- [Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)