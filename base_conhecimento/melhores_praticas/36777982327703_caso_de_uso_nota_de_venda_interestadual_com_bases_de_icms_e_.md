# Caso de uso: Nota de Venda interestadual, com Bases de ICMS e ST iguais e o valor do ST será o diferencial de alíquotas (DIFAL)

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36777982327703-Caso-de-uso-Nota-de-Venda-interestadual-com-Bases-de-ICMS-e-ST-iguais-e-o-valor-do-ST-ser%C3%A1-o-diferencial-de-al%C3%ADquotas-DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/36777982327703-Caso-de-uso-Nota-de-Venda-interestadual-com-Bases-de-ICMS-e-ST-iguais-e-o-valor-do-ST-ser%C3%A1-o-diferencial-de-al%C3%ADquotas-DIFAL)  
> **ID:** `36777982327703` | **Última Atualização:** 2026-07-22T14:22:23Z

---

Este caso de uso trata de situações em que, ao emitir uma **Nota de Venda interestadual**, as **bases de cálculo do ICMS e da Substituição Tributária (ST)** são iguais. No entanto, o valor destacado como ST na nota representa, na prática, o **Diferencial de Alíquotas (DIFAL)**.

O objetivo é explicar como o sistema reconhece essa configuração e como o **DIFAL **é representado utilizando a estrutura de ST na nota fiscal.

 

#### **Configuração da Alíquota de ICMS**

Ao tratar de **Nota de Venda Interestadual** com bases na** ICMS** e **ST iguais** a **DIFAL destacado como ST**, é importante analisar duas situações:

1. 

**Alíquota de ICMS usada na nova de venda interestadual.**

1. 

**Alíquota de ICMS interna do estado de destino**, configurada como ''sem exceção/sem exceção''.

 

#### **Alíquota de ICMS usada na nota de venda interestadual**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36854950699159)

 Acesse a tela ****[''Alíquota de ICMS''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS) (Comercial > Arquivo > Cadastros > Alíquotas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36854972589207)

 Na aba **''Geral''** configure:

- 

**Tributação:** `10 - Tributada e c/cobrança por substituição`

- 

**Alíquotas:** preencher com a alíquota correta

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36855158333591)

 Na aba **''Substituição Tributária''**:

- 

**Modalidade BC ICMS ST:** `Valor da Operação`

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36854972590231)

 OBSERVAÇÃO:** não é necessário preencher **MVA** nem **Alíquota de Substituição Tributária**

 

#### **Alíquota interna do estado de destino (sem exceção/sem exceção)**

O sistema utilizará a alíquota configurada neste registro como **parâmetro para calcular o DIFAL**.

##### **Cálculo do DIFAL utilizando a alíquota de ST**

Na alíquota interna de destino (sem exceção/sem exceção), o sistema utiliza a alíquota configurada como parâmetro para calcular o DIFAL.

**Exemplo prático:**

- 

**Origem:** DF

- 

**Destino:** MG

- 

**Valor do item:** R$ 1.000,00

- 

**Alíquota ICMS interestadual:** 18%

- 

**Alíquota interna do destino:** 12%

- 

**Base de substituição:** R$ 1.000,00 (definida como “Valor da Operação”)

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36854972590231)

 OBSERVAÇÃO:** Podemos notar, que o valor destacado como **ST** corresponde ao **diferencial de alíquotas (DIFAL)**, aplicando a mesma lógica utilizada no cálculo no DIFAL.

 

![image (87).png](https://ajuda.sankhya.com.br/hc/article_attachments/36854972591895)

 

![image (88).png](https://ajuda.sankhya.com.br/hc/article_attachments/36854950705175)

 

![image (89).png](https://ajuda.sankhya.com.br/hc/article_attachments/36854972595479)

 

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/36855100414359)

** ESSENCIAL:**

- 

Se o parceiro estiver marcado com o campo **"Possui Suframa para PIS/COFINS"** a **base de substituição** sofrerá dedução do ICMS da operação.

- 

Se, no cadastro do produto, o campo **"Tabela c/ base p/ substituição na venda"** estiver preenchido com alguma tabela, **será o valor da tabela que o sistema usará na base de ST**.

- 

Confirme com sua contabilidade se esta operação deve, de fato, ser utilizada no seu processo.


---

### 🔗 Links e Referências Internas:

- [''Alíquota de ICMS''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)