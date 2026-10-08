# CFOP não permitido para o CST informado (NT2015/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043070553-CFOP-n%C3%A3o-permitido-para-o-CST-informado-NT2015-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043070553-CFOP-n%C3%A3o-permitido-para-o-CST-informado-NT2015-002)  
> **ID:** `360043070553` | **Última Atualização:** 2026-07-22T16:09:00Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759822615)

 MENSAGEM:**

[382 - Rejeição]: CFOP não permitido para o CST informado (NT2015/002). 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759826327)

 SOLUÇÃO:**

Para correção, siga os passos abaixo.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759828375)

 Na Central de Vendas (ou Compras), na grade Itens, identifique para cada produto, informações apresentadas nos campos "**Tributação"** e "**CFOP"**:

 

![CFOP_n_o_permitido_para_o_CST_informado.png](https://ajuda.sankhya.com.br/hc/article_attachments/14500466853399)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759830167)

 De acordo com as regras abaixo, faça a análise dos produtos com incompatibilidade entre essas duas informações:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759831703)

 CST (Tributação) de ICMS igual (**00, 20, 40, 41 ou 90**) e a CFOP dos itens for diferente de alguma das CFOPs abaixo:

- 5101 - Venda de produção do estabelecimento;

- 5102 - Venda de mercadoria de terceiros;

- 5103 - Venda de produção do estabelecimento, efetuada fora do estabelecimento;

- 5104 - Venda de mercadoria adquirida ou recebida de terceiros, efetuada fora do estabelecimento;

- 5115 - Venda de mercadoria de terceiros, recebida anteriormente em consignação

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759831703)

 CST 60** e CFOP diferente das CFOPs abaixo:

- 5405 - Venda de mercadoria de terceiros, sujeita a ST, como contribuinte substituído;

- 5656 - Venda de combustível ou lubrificante de terceiros, para consumidor final;

- 5667 - Venda de combustível ou lubrificante a consumidor ou usuário final estabelecido em outra unidade da Federação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474713031447)

 Detectada a divergência, sintonize com seu contador os ajustes a serem realizados e os faça conforme cadastros no sistema:

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759831703)

 **Tributação/CST:

- Tela "**[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)" **(*Comercial » Arquivo » Cadastros » Alíquotas*)

- Aba Geral - Campo '**Tributação**'

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759831703)

 **CFOP:

- Tela "**[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso:* Comercial » Arquivo » Cadastros*)

- Aba "**Livro Fiscal"** - Campos "**CFOP'S"**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759841687)

 As combinações de CFOP e CST deverão ser compatíveis com a regra estipulada pela SEFAZ.
Faça os devidos ajustes e caso necessário redigite Empresa/Parceiro e/ou produtos na NFC-e para que a nota assuma as configurações. Posteriormente gere o lote da NFC-e e caso seja possível, exclua o lançamento e fature novamente o pedido e gere o lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759843095)

 CAUSA:**

Quando emitida uma NFC-e com CST de ICMS igual (00, 20, 40, 41 ou 90) e a CFOP dos itens for diferente de alguma das CFOPs abaixo:

- 5101 - Venda de produção do estabelecimento;

- 5102 - Venda de mercadoria de terceiros;

- 5103 - Venda de produção do estabelecimento, efetuada fora do estabelecimento;

- 5104 - Venda de mercadoria adquirida ou recebida de terceiros, efetuada fora do estabelecimento;

- 5115 - Venda de mercadoria de terceiros, recebida anteriormente em consignação

Ou quando emitida uma NFC-e com CST 60 e CFOP diferente das CFOPs abaixo:

- 5405 - Venda de mercadoria de terceiros, sujeita a ST, como contribuinte substituído;

- 5656 - Venda de combustível ou lubrificante de terceiros, para consumidor final;

- 5667 - Venda de combustível ou lubrificante a consumidor ou usuário final estabelecido em outra unidade da Federação.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474759845527)

 OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=v9JbkEY7evI=)) - Nota técnica.


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)