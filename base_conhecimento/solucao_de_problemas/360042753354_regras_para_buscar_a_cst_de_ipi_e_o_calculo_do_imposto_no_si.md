# Regras para Buscar a CST de IPI e o cálculo do imposto no Sistema SankhyaW

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753354-Regras-para-Buscar-a-CST-de-IPI-e-o-c%C3%A1lculo-do-imposto-no-Sistema-SankhyaW](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753354-Regras-para-Buscar-a-CST-de-IPI-e-o-c%C3%A1lculo-do-imposto-no-Sistema-SankhyaW)  
> **ID:** `360042753354` | **Última Atualização:** 2026-09-03T11:56:24Z

---

#### **IPI - IMPOSTO SOBRE PRODUTOS INDUSTRIALIZADOS**

O imposto sobre produtos industrializados (IPI) incide sobre produtos industrializados, nacionais e estrangeiros.

Suas disposições estão regulamentadas pelo **[Decreto 7.212/2010](http://www.normaslegais.com.br/legislacao/decreto7212_2010.htm)** (RIPI/2010).

O campo de incidência do imposto abrange todos os produtos com alíquota, ainda que zero, relacionados na Tabela de Incidência do IPI (TIPI), observadas as disposições contidas nas respectivas notas complementares, excluídos aqueles a que corresponde a notação "NT" (não-tributado).

 

#### **Regras para Buscar a CST de IPI e o cálculo do imposto**

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458157765143)

 Processo de Venda (Saída)**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801273201175)

 TOP

Tem IPI?

Não: pega a CST de Saída informada neste cadastro.

Sim: passa para o próximo cadastro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801273204247)

 Cadastro de Produto

Tem IPI na venda?

Não: pega a CST de Saída informada neste cadastro.

Sim: passa para o próximo cadastro.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801273209111)

 Empresa

Tem IPI?

Não: pega a CST de Saída informada neste cadastro.

Sim: passa para o próximo cadastro.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801260732567)

 PARCEIRO

Tem IPI?

Não: pega a CST de Saída informada neste cadastro.

Sim: passa para o próximo cadastro.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801260734871)

 Alíquota de IPI

Faz o cálculo e pega a CST de saída informada neste cadastro

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458157765143)

 Processo de COMPRA (Entrada):**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801273201175)

 TOP

Tem IPI?

Não: pega a CST de ENTRADA informada neste cadastro.

Sim: passa para o próximo cadastro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801273204247)

 CADASTRO DO PRODUTO

Tem IPI na compra?

Não: pega a CST de ENTRADA informada neste cadastro.

Sim: passa para o próximo cadastro.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801273209111)

 PARCEIRO

TEM IPI?

Não: pega a CST de ENTRADA informada neste cadastro.

Sim: passa para o próximo cadastro.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801260732567)

 ALIQUOTA DE IPI

Faz o cálculo e pega a CST de ENTRADA informada neste cadastro.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17801273226519)

 IMPORTANTE:**

- Existe a exceção da hierarquia quando o Parceiro é Isento de ICMS (Cadastro do Parceiro » Aba Fiscal » Classificação de ICMS) neste caso a C.S.T. IPI utilizada é a do Cadastro do **"Parceiro"**.

- A opção tem ICMS do cadastro da **"Empresa"** (Comercial » Preferências » Empresa) tem que estar marcada para realizar o cálculo.