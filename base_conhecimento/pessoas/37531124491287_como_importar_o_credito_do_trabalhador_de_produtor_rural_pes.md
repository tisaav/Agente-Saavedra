# Como importar o Crédito do Trabalhador de produtor rural pessoa física com CNPJ?

> **Módulo:** Pessoas+ | **Subseção:** Crédito do Trabalhador  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37531124491287-Como-importar-o-Cr%C3%A9dito-do-Trabalhador-de-produtor-rural-pessoa-f%C3%ADsica-com-CNPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/37531124491287-Como-importar-o-Cr%C3%A9dito-do-Trabalhador-de-produtor-rural-pessoa-f%C3%ADsica-com-CNPJ)  
> **ID:** `37531124491287` | **Última Atualização:** 2026-09-27T18:46:32Z

---

**Módulo**: Pessoal+
**Versão Mínima**: 5.70.0
**Caminho de Acesso**: Pessoal+ > Rotinas Folha

## **Descrição e Usabilidade**

Esta funcionalidade garante que a **importação do Crédito do Trabalhador** identifique **onde os trabalhadores estão alocados**, inclusive nos casos em que o **produtor rural é pessoa física**, mas utiliza **CNPJ para emissão de notas fiscais**.

O sistema identifica automaticamente se deve usar **CNPJ **ou** CAEPF**, evitando erro na importação do crédito e possíveis impactos legais.

### **1. Descrição da Funcionalidade**

Durante a importação do arquivo de **Crédito do Trabalhador **retornado pelo Governo, o sistema identifica a empresa para alocação dos trabalhadores com base nas seguintes regras:

- 

**CNPJ**: quando o produtor rural opera apenas com CNPJ;

- 

**CAEPF**: quando o produtor rural é pessoa física;

- 

**CAEPF:** mesmo quando existe **CNPJ no cadastro da empresa**, desde que o **CPF do Produtor Rural esteja informado** na tela **Empresas** (Pessoal+ > Cadastros).

Essa lógica é aplicada tanto para a importação via planilha quanto para a importação via API.

### **2. Pré-requisitos**

#### **Permissões necessárias**

- 

Acesso de usuário DP as telas de **configurações da empresa**, **colaboradores**, **lançamento de movimento** e **cálculos**;

- 

Permissão para **importação do Crédito do Trabalhador**.

#### **Condições obrigatórias**

- 

Empresa e colaboradores cadastrados no sistema;

- 

Arquivo de Crédito do Trabalhador retornado pelo Governo;

- 

Registro Fiscal configurado, quando aplicável.

######  

### **3. Jornada de Uso**

Durante a Importação do arquivo [via API](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Lan%C3%A7amento-do-Cr%C3%A9dito-do-Trabalhador-no-Pessoal#h_01K1X4BQZA1QZQWQ8PYETFW0FH) ou pela [planilha do Governo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Lan%C3%A7amento-do-Cr%C3%A9dito-do-Trabalhador-no-Pessoal#h_01JR8PTPZE0CKK26PRWXEJP737), o sistema identifica automaticamente o estabelecimento correto conforme o cenário cadastral:

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37531737982487)

**Empresa cadastrada apenas com CNPJ**

Quando a empresa possui **apenas CNPJ** informado no cadastro geral da **Empresa**, o sistema utiliza essa informação para a importação do crédito.

- 

O sistema:

- 

compara o **CNPJ do cadastro** com o **CNPJ informado no arquivo**;

- 

importa as informações do crédito usando o **CNPJ** configurado no campo **CNPJ/CPF**, aba **Geral** do cadastro da **Empresa** (Configurações > Cadastros).

![importarprodutorruralcnpj.gif](https://ajuda.sankhya.com.br/hc/article_attachments/37538157154583)

######  

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37531737982487)

 **Empresa cadastrada com CPF + CAEPF**

Quando a empresa é **produtor rural pessoa física** e possui **CAEPF** cadastrado, o sistema utiliza essa identificação para a importação.

- 

Isso ocorre quando:

  - 

existe um **Registro Fiscal **(Pessoal+ > Cadastros) cadastrado com o** Tipo CNPJ/CEI** igual a **CAEPF**; 

![caepf-registrofiscal.png](https://ajuda.sankhya.com.br/hc/article_attachments/37555122165271)

  1. 

esse Registro Fiscal está vinculado na tela** Empresas** (Pessoal+ > Cadastros), aba **Informações Gerais**, campo **Reg.Fiscal Apro/Guia**;

![registrocaepf-empresa.png](https://ajuda.sankhya.com.br/hc/article_attachments/37555216352023)

  1. 

e, o campo **CPF de produtor rural** preenchido com o CPF do produtor rural na tela **Empresas** (Pessoal+ > Cadastros), aba **Informações Fiscais**.

![cpfprodrural-empresa.png](https://ajuda.sankhya.com.br/hc/article_attachments/37555231879063)

1. 

Nessa situação, o sistema:

  - 

utiliza o **CAEPF do Registro Fiscal**;

  - 

compara com o **CAEPF informado no arquivo**;

  - 

realiza a importação das informações pelo CAEPF.

 

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37531737982487)

**Produtor rural Pessoa Física com CNPJ e CPF informados**

Quando o produtor rural possui **CNPJ, CPF** e **CAEPF **cadastrados, o sistema prioriza o CAEPF para a importação das informações.

- 

Isso ocorre quando:

  - 

existe **CNPJ** na aba **Geral** do cadastro geral da **Empresa **(Configurações > Cadastros);

![cnpjcadastroempresarural.png](https://ajuda.sankhya.com.br/hc/article_attachments/37555418366615)

  1. 

o campo **CPF do Produtor Rural** está preenchido na tela **Empresas** (Pessoal+ > Cadastros), aba **Informações Fiscais;**

![cpfprodrural-empresa.png](https://ajuda.sankhya.com.br/hc/article_attachments/37555231879063)

  1. 

há um** Registro Fiscal **(Pessoal+ > Cadastros) com o** Tipo CNPJ/CEI** igual a **CAEPF**.

![caepf-registrofiscal.png](https://ajuda.sankhya.com.br/hc/article_attachments/37555122165271)

1. 

Nessa situação, o sistema:

  - 

**desconsidera o CNPJ **para fins de importação do crédito;

  - 

**utiliza o ****CAEPF** para identificar o estabelecimento;

  - 

garante a correta alocação dos trabalhadores.

### **4. Pontos de Atenção**

- 

Em alguns estados (ex: **SP, MT e ES**), o produtor rural pessoa física é obrigado a possuir CNPJ para emissão de notas fiscais, enquanto o eSocial utiliza o CPF.

- 

Se o **CPF do Produtor Rural não estiver preenchido**, o sistema **não conseguirá importar por CAEPF**.

- 

O CAEPF deve estar **corretamente cadastrado no Registro Fiscal**.

### **5. Dicas de Usabilidade**

- 

Sempre confira se o **CPF do Produtor Rural** está preenchido no cadastro da empresa.

- 

Para produtores rurais PF com CNPJ, **não altere o CNPJ do cadastro geral** — apenas complemente com o CPF no Pessoal+.

- 

Em caso de erro na importação, valide primeiro:

  - 

cadastro da empresa;

  - 

registro Fiscal (CAEPF);

  - 

estrutura do arquivo retornado pelo Governo.

## **Artigos Relacionados**

- 

[Cadastro de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913)

- 

[Empresa da folha de pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610294)

- 

[Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214)

- 

[Importação do Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Lan%C3%A7amento-do-Cr%C3%A9dito-do-Trabalhador-no-Pessoal#01JX37KE0B6ZM0YFPY0W7A0HH3)


---

### 🔗 Links e Referências Internas:

- [via API](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Lan%C3%A7amento-do-Cr%C3%A9dito-do-Trabalhador-no-Pessoal#h_01K1X4BQZA1QZQWQ8PYETFW0FH)
- [planilha do Governo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Lan%C3%A7amento-do-Cr%C3%A9dito-do-Trabalhador-no-Pessoal#h_01JR8PTPZE0CKK26PRWXEJP737)
- [Cadastro de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913)
- [Empresa da folha de pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610294)
- [Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214)
- [Importação do Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Lan%C3%A7amento-do-Cr%C3%A9dito-do-Trabalhador-no-Pessoal#01JX37KE0B6ZM0YFPY0W7A0HH3)