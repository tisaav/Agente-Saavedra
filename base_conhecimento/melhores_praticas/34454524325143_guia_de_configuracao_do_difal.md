# Guia de Configuração do DIFAL

> **Módulo:** Melhores Praticas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34454524325143-Guia-de-Configura%C3%A7%C3%A3o-do-DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/34454524325143-Guia-de-Configura%C3%A7%C3%A3o-do-DIFAL)  
> **ID:** `34454524325143` | **Última Atualização:** 2026-07-22T14:27:05Z

---

O cálculo do **DIFAL (Diferencial de Alíquota do ICMS)** no Sankhya depende de uma série de cadastros e parâmetros.
Este guia apresenta os pontos que devem ser verificados para garantir o funcionamento correto da rotina.

 

### **1. Partilhas DIFAL**

**Caminho:** Configurações » Cadastros » Partilhas DIF**AL**

- 

Verifique se existe partilha cadastrada para o ano vigente.

- 

Configure a **data de início** e o **percentual aplicável** da partilha.

 

### **2. Cadastro da TOP**

**Caminho:** **C**omercial » Arquivo » Cadastros » Tipos de Operação – TOP

Na TOP utilizada para operações sujeitas a DIFAL, verifique os campos:

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Cálculo de ICMS, IPI e ISS:** deve estar configurado para calcular ICMS (ex.: Calcula e Digita/Calcula e Não Digita);

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Calcular DIFAL Partilhado:** deve estar marcado;

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Tem ICMS?:** deve estar marcado;

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Classificação ICMS:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110401175)

 Caso esteja definido como **Consumidor Final Não Contribuinte**, a classificação será levada diretamente da TOP;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110401175)

Caso esteja configurado para buscar do **Parceiro**, será necessário validar também o cadastro do parceiro.

 

### **3. Configuração de Parceiros**

**Caminho:** Configurações » Cadastros » Parceiros

**No cadastro do parceiro:**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Estado (UF):** conferir se está informado corretamente;

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Classificação ICMS:** deve estar definido como **Consumidor Final Não Contribuinte** quando aplicável.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110402711)

 Atenção:** o sistema calcula o **DIFAL apenas para Consumidor Final Não Contribuinte de outra UF**.

 

### **4. Cadastro de Produtos**

**Caminho:** Configurações » Cadastros » Produtos » Produtos

**Verifique se cada produto possui:**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Tributação de ICMS** configurada corretamente;

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 NCM válido** (alguns cenários dependem dele para definição da alíquota interestadual).

 

**Campos obrigatórios:**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

Calcula ICMS:** deve estar marcado;

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Calcula DIFAL Partilhado:** deve estar marcado.

 

### **5. Cadastro de Alíquotas de ICMS**

**Caminho:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

**Na regra de ICMS da nota em questão, valide:**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Alíquota interna do destino** configurada corretamente.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Alíquota interestadual ** deverá estar preenchida.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Tipo de Cálculo de DIFAL** configurado.

Essas **informações são essenciais para que o sistema apure corretamente** a diferença do DIFAL.

 

![Guia de Configuração do DIFAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006267013015)

 

### **6. Regras de Partilha do DIFAL**

No Sankhya é necessário configurar as regras de partilha:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006110396439)

 Percentual destinado à **UF de origem** e à **UF de destino**, conforme legislação vigente.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36062415158039)

 **Observação: **até 2021 havia partilha; a partir de **2022 o valor integral é destinado à UF de destino** (validar se o parâmetro está ajustado).

 

### **Resumindo**

No momento da emissão da NF-e, o sistema considera:

- 

**Alíquota interestadual (origem);**

- 

**Alíquota interna do destino (cadastro da UF);**

- 

Calcula a diferença entre elas → **DIFAL**.

 

Para que o **DIFAL seja calculado corretamente, é indispensável que todos os cadastros listados acima estejam configurados de forma adequada**. Verifique cada item antes da emissão da NF-e.

 

### **Exemplo de rejeição e XML**

Se ao emitir uma NF-e o **Valor do ICMS Interestadual para a UF de Destino (vICMSUFDest)** divergir do cálculo da SEFAZ, é necessário revisar os cadastros acima.
 

EX de XML

 

![Guia de Configuração do DIFAL 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/35006292610711)

####  

#### **Confira também links relacionados à rotina:**

[Alíquota Interna de Destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaalquotainternadedestino)

[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)

[Partilha DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111373)

[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)

[Tipos de Cálculos de Difal / Formulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/24110650363031-Quais-tipos-de-c%C3%A1lculos-de-Difal-est%C3%A3o-dispon%C3%ADveis-no-sistema)


---

### 🔗 Links e Referências Internas:

- [Alíquota Interna de Destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaalquotainternadedestino)
- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)
- [Partilha DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111373)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Tipos de Cálculos de Difal / Formulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/24110650363031-Quais-tipos-de-c%C3%A1lculos-de-Difal-est%C3%A3o-dispon%C3%ADveis-no-sistema)