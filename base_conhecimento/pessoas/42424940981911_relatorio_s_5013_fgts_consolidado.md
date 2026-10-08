# Relatório S-5013 (FGTS consolidado)

> **Módulo:** Pessoas+ | **Subseção:** Totalizadores e Conferência do eSocial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/42424940981911-Relat%C3%B3rio-S-5013-FGTS-consolidado](https://ajuda.sankhya.com.br/hc/pt-br/articles/42424940981911-Relat%C3%B3rio-S-5013-FGTS-consolidado)  
> **ID:** `42424940981911` | **Última Atualização:** 2026-09-27T19:12:45Z

---

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Central do eSocial > Conferência Consolidada de Tributos
**ID da Tela: **br.com.sankhya.CentraleSocial

 

## **Descrição e Usabilidade**

O **Relatório S‑5013 – Conferência Consolidada de FGTS** apresenta, por empregador (matriz) e por estabelecimento, os valores de **base de cálculo** e de **depósito de FGTS** retornados pelo eSocial no evento de totalização **S‑5013**, agrupados por competência e por tipo de valor (`tpValor`).

Diferentemente do ****[Relatório S-5003](https://ajuda.sankhya.com.br/hc/pt-br/articles/36626761293591), que demonstra os valores individualizados por trabalhador, o **S-5013 apresenta exclusivamente os valores oficiais consolidados pelo eSocial**, após o processamento do fechamento da folha (evento **S-1299**).

Esse relatório é indicado para conferências fiscais da empresa como um todo e para validação dos valores consolidados enviados ao FGTS Digital.

 

### **1. Descrição da Funcionalidade**

Após o fechamento dos eventos periódicos no eSocial (S-1299), o governo gera o evento **S-5013**, consolidando os valores de FGTS calculados para todos os trabalhadores do empregador.

O relatório disponibiliza essas informações organizadas por:

- 
**Empresa (matriz)** — CNPJ e razão social do empregador (`CODEMPMATRIZ`);

- 
**Referência** — competência (mês/ano) apurada;

- 
**Estabelecimento** — CNPJ e razão social de cada estabelecimento vinculado à matriz;

- 
**Tipo de Valor (**`**tpValor**`**)** — cada linha detalha um tipo de valor retornado (base mensal, 13º, rescisória, indenizatória, valores suspensos por decisão judicial).

Para cada tipo de valor são apresentados:

- 
**Base de Cálculo do FGTS** (`REMFGTS`);

- 
**Valor de FGTS a ser Depositado** (`DPSFGTS`).

Ao final da consulta, o sistema apresenta o **Total Consolidado do Empregador**, reunindo todos os estabelecimentos selecionados.

****

| ℹ️ Nota O S-5013 não realiza comparação entre valores calculados pelo sistema e valores retornados pelo eSocial. Ele apresenta somente os valores oficialmente consolidados pelo governo. |
| --- |

 

### **2. Pré-requisitos**

Antes de gerar o relatório, verifique se:

- possui permissão de acesso à **Central do eSocial** (Pessoal+ > Rotinas Folha);

- o fechamento da folha (evento **S-1299**) já foi processado no eSocial;

- todas as empresas do grupo estão com o campo **Empresa Matriz** configurado no cadastro da empresa:

  - a própria matriz deve apontar para o seu próprio código; 

  - 

as filiais devem apontar para o código da matriz.

Exemplo:

| Empresa | Empresa Matriz |
| --- | --- |
| Empresa 1 (Matriz) | 1 |
| Empresa 2 (Filial) | 1 |
| Empresa 3 (Filial) | 1 |

Caso esse cadastro esteja incompleto, o relatório poderá não ser gerado.

 

### **3. Jornada de Uso**

![relatorio-S-5013.gif](https://ajuda.sankhya.com.br/hc/article_attachments/42429904267287)

1. 

Acesse pela **Central do eSocial** (Pessoal+ > Rotinas Folha);

1. 

Clique no botão **Conferência Consolidada de Tributos**;

1. 

No popup, selecione:

  - 

Relatório Consolidado de Conferência do: **FGTS (5013)**;

  - 

**Empresa** (matriz);

  - 

**Tipo folha:**

    - 

**Mensal (**`**N**`**)** → traz todos os `tpValor` apurados na competência, com indicador de apuração = 1 (encerramento);

    - 

**13º Salário (**`**D**`**)** → restringe aos `tpValor` do 13º (12, 16 e 18), também apenas apuração encerrada.

  - 

**Referência** (início/fim);

  - 

**Filtros disponíveis por tributo** (consolidado):

****************

| Tributo | Lotações Tributárias | Estabelecimentos | Funcionários |
| --- | --- | --- | --- |
| INSS (S-5011) | ✅ | ✅ | ❌ |
| IRRF (S-5012) | ❌ | ❌ | ❌ (retorno é só por CNPJ Matriz e Código de Receita) |
| FGTS (S-5013) | ✅ | ✅ | ❌ (aba sempre desabilitada no consolidado) |

A aba **Funcionários** existe na tela, mas fica **desabilitada para qualquer tributo consolidado** — o filtro por trabalhador só está disponível no relatório **analítico** (S‑5001/S‑5002/S‑5003).

1. 

Após definir os filtros, clique em **Gerar Relatório**.

O relatório será apresentado com os valores consolidados retornados pelo eSocial.

![ChatGPT Image 3 de ago. de 2026, 11_06_12.png](https://ajuda.sankhya.com.br/hc/article_attachments/42429904269079)

********

| S-5003 | S-5013 |
| --- | --- |
| Analítico | Consolidado |
| Por trabalhador | Por empregador |
| Permite comparar Sistema × eSocial | Exibe apenas valores consolidados do eSocial |
| Auxilia na identificação de divergências individuais | Auxilia na conferência dos valores oficiais consolidados |

Sempre que houver necessidade de investigar diferenças entre os valores calculados na folha e os valores retornados pelo eSocial, utilize o relatório **S-5003**.

 

### 
**4. Pontos de Atenção**

- O relatório utiliza exclusivamente os dados retornados pelo evento S-5013 do eSocial.

- Não existe coluna de diferença entre Sistema e eSocial.

- O relatório considera apenas competências encerradas pelo eSocial.

- Empresas sem configuração correta de Empresa Matriz podem não aparecer na consolidação.

- A ausência dessa configuração também pode afetar outras rotinas do módulo Pessoal.

## 
**Perguntas Frequentes (FAQ)**

**1. O relatório S-5013 compara valores do Sistema com o eSocial?**

Não. O relatório apresenta apenas os valores oficiais consolidados retornados pelo eSocial.

**2. Quando devo utilizar o S-5013?**

Quando for necessário conferir os valores consolidados de FGTS do empregador após o fechamento da folha.

**3. Quando devo utilizar o S-5003?**

Quando precisar identificar divergências entre os valores calculados na folha e os valores retornados pelo eSocial para cada trabalhador.

**4. Por que não consigo emitir a Conferência Consolidada de Tributos?**

Verifique se:

- todas as empresas do grupo possuem o campo **Empresa Matriz** corretamente preenchido:

  - confirme que a própria matriz aponta para ela mesma;

  - confira se as filiais apontam para a matriz;

- o fechamento da folha foi transmitido ao eSocial;

- 

existe retorno do evento S-5013.

Caso a configuração esteja incorreta, o relatório poderá apresentar a mensagem **"Falha - Nenhuma página a apresentar"**.

**5. O relatório permite consultar apenas um colaborador?**

Não. O S-5013 é um relatório consolidado por empregador e não possui filtro por trabalhador.

**6. É possível filtrar por estabelecimento (filial)?**

Sim. É possível selecionar um ou mais estabelecimentos para compor a consolidação.

**7. O que fazer quando houver divergência entre o valor calculado pelo Sistema e o valor retornado pelo eSocial?**

Recomenda-se utilizar o **Relatório S-5003**, que permite a conferência analítica por trabalhador.

Uma das causas mais comuns é a configuração incorreta do **Registro Fiscal** utilizado pelo evento **995 – FGTS Normal**.

Verifique os seguintes itens:

- o parâmetro **FPREGFISCAL**, que define se o Registro Fiscal será obtido pela Empresa ou pelo Departamento;

- o **Registro Fiscal** correspondente à configuração definida pelo parâmetro;

- o **Percentual de FGTS** informado nesse cadastro.

Após realizar os ajustes, recalcule a folha da competência para que os valores sejam atualizados.


---

### 🔗 Links e Referências Internas:

- [Relatório S-5003](https://ajuda.sankhya.com.br/hc/pt-br/articles/36626761293591)