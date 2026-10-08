# Títulos de crédito ou débito do parceiro não estão sendo utilizados na compensação? Saiba como resolver.

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35427087506711-T%C3%ADtulos-de-cr%C3%A9dito-ou-d%C3%A9bito-do-parceiro-n%C3%A3o-est%C3%A3o-sendo-utilizados-na-compensa%C3%A7%C3%A3o-Saiba-como-resolver](https://ajuda.sankhya.com.br/hc/pt-br/articles/35427087506711-T%C3%ADtulos-de-cr%C3%A9dito-ou-d%C3%A9bito-do-parceiro-n%C3%A3o-est%C3%A3o-sendo-utilizados-na-compensa%C3%A7%C3%A3o-Saiba-como-resolver)  
> **ID:** `35427087506711` | **Última Atualização:** 2026-07-22T14:25:10Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35427147830679)

** SITUAÇÃO: **

Ao realizar o lançamento da nota de venda ou de compra, o sistema identifica que existem títulos de crédito ou débito vinculados ao parceiro, porém esses valores não estão sendo compensados automaticamente no processo.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35427147831063)

 SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35427087504535)

 **Valide se o crédito ou débito está disponível:

- 

Acesse a tela “**Configurador de Layout da Nota”** (Comercial» Configuração), selecione o layout em uso e adicione o campo **“Valor Crédito”**. Dessa forma, será possível visualizar se o parceiro possui créditos disponíveis no momento do lançamento.

![image (61).png](https://ajuda.sankhya.com.br/hc/article_attachments/36321371782039)

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35427087504919)

 **Confira os títulos na Movimentação Financeira: 

Acesse a tela ''**Movimentação Financeira''** (Financeiro» Rotinas) e aplique os filtros conforme o tipo de operação:

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36321371784343)

 Crédito de cliente:**

- 

Despesas

- 

Real

- 

Pendentes

- 

Informe o **código do parceiro** em questão

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36321371784343)

 Débito de fornecedor:**

- 

Receitas

- 

Real

- 

Pendentes

- 

Informe o **código do parceiro** em questão

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35427087505047)

 **Valide a configuração dos parâmetros e tipos de título: 

- 

Verifique se as configurações estão conforme a documentação ****[Compensação de Crédito ou Débito em Compra ou Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601914-Compensa%C3%A7%C3%A3o-de-Cr%C3%A9dito-ou-D%C3%A9bito-em-Compra-ou-Venda); 

- 

Revise o uso dos tipos de título configurados nos parâmetros:

`**TIPTITCREDCLI**`** **→ Tipo de título utilizado para **crédito de cliente**

`**TIPTITDEBFOR**`** **→ Tipo de título utilizado para **débito de fornecedor**

**

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/36335342582039)

 Observação: **
Se, por exemplo, houver um título de receita utilizando o mesmo tipo de título definido no parâmetro **TIPTITCREDCLI **(que deveria ser destinado a despesas), isso poderá impactar diretamente o processo de compensação. Portanto, é essencial garantir que cada tipo de título esteja corretamente classificado conforme o parâmetro correspondente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35427087505303)

CAUSA:**

Ocorre quando há inconsistências nas configurações do tipo de título financeiro ou na parametrização da compensação de créditos e débitos. Em determinados casos, os títulos podem estar classificados de forma incorreta, por exemplo, como receita em vez de despesa, o que impede que o sistema realize a compensação automática durante o faturamento.


---

### 🔗 Links e Referências Internas:

- [Compensação de Crédito ou Débito em Compra ou Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601914-Compensa%C3%A7%C3%A3o-de-Cr%C3%A9dito-ou-D%C3%A9bito-em-Compra-ou-Venda)