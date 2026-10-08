# Processo financeiro das operações

> **Módulo:** Financeiro e Patrimônio | **Subseção:** Venda Mais  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30451505691927-Processo-financeiro-das-opera%C3%A7%C3%B5es](https://ajuda.sankhya.com.br/hc/pt-br/articles/30451505691927-Processo-financeiro-das-opera%C3%A7%C3%B5es)  
> **ID:** `30451505691927` | **Última Atualização:** 2026-07-29T13:12:52Z

---

Quando uma Nota Fiscal Eletrônica (NF-e) tem o crédito aprovado, os títulos financeiros dessa operação são registrados como **A Receber** em nome do **parceiro de crédito**. Dessa forma, ao ser aprovada, a operação passa por um processo de **renegociação**, no qual:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30451491322903)

 Os títulos financeiros originados da NF-e (vinculados ao cliente da venda) tornam-se títulos renegociados:

- o campo **Receita/Despesa** fica vazio;

- o campo **Nro da Renegociação** é preenchido.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30451491322903)

 São gerados novos títulos de destino na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) seguindo as regras abaixo:

- o campo **Parceiro** é preenchido com o parceiro de crédito (ex: Trademaster) habilitado para essa operação;

- o **Valor Desdobramento** é preenchido com o valor líquido do título original;

- 
a **Data de Vencimento** é calculada conforme os seguintes tipos de contratos:

  - **com antecipação** = Data da aprovação da operação + Dias de antecipação (Configurações Venda Mais > aba Dados contratuais);

  - **sem antecipação** = Data do vencimento do título original + Dias para recebimento (Configurações Venda Mais > aba Dados contratuais).

- os campos **Tipo de título**, **Natureza**, **Centro de resultado** e **Lançamento**, recebem as informações configuradas na tela Configurações Venda Mais > aba Processos > Configurar rotinas > Financeiro;

- o campo **Histórico** é preenchido com o número da nota (ex: VM-54);

- 
o campo **Nosso número** é preenchido com um identificador do parceiro de crédito para este título (Ticket Number).

- Os campos da **seção Venda Mais** serão preenchidos da seguinte forma:

  - 
**Dt Aprovação**: data em que a operação foi aprovada junto ao parceiro de crédito;

  - 
**Taxa Venda Mais**: é calculada conforme contrato com parceiro de crédito. (cálculo detalhado nos próximos tópicos);

  - **Código da Operação**: número identificador do parceiro de crédito para esta operação;

  - **Venda Mais**: estará marcada, sempre que se tratar de um título aprovado por operações Venda Mais.

![venda-mais-mov-financeira.png](https://ajuda.sankhya.com.br/hc/article_attachments/30451505687319)

**Importante:** para visualizar os títulos originais (renegociados), é necessário:

- ligar o parâmetro** Visualizar títulos renegociados? - VERTITRENEG** na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834);

- habilitar a opção **Mostrar renegociados** no botão **Preferências** da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

### **Taxa Venda Mais**

A taxa Venda Mais é calculada conforme o tipo de contrato firmado com o parceiro de crédito.

#### 
**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309692202903)

 ****Contrato com antecipação**

**Fórmula:**

```text
*Taxa Venda Mais = [(Dias Operacionais * (Taxa/30)) * Valor do Desdobramento] / 100*
```

Onde:

- **Dias Operacionais** = Data de Vencimento - Data de Aprovação

- **Taxa** = Taxa de antecipação configurada na aba **Dados Contratuais** da tela **Configurações Venda Mais**, produto **Venda Mais com Antecipação**

#### 
**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309692202903)

 ****Contrato sem antecipação**

**Fórmula:**

```text
*Taxa Venda Mais = (Valor do Desdobramento * Taxa Fixa) + [(Dias Operacionais * 
(Taxa Variável/30)) * Valor do Desdobramento]*
```

Onde:

- **Dias Operacionais** = Data de Vencimento - Data da Operação - 30

- **Taxa Fixa** e **Taxa Variável **= Valor configurado na aba **Dados Contratuais** da tela **Configurações Venda Mais**, produto **Venda Mais sem Antecipação**

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)
- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)