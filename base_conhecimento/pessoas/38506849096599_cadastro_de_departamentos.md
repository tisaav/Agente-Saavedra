# Cadastro de Departamentos

> **Módulo:** Pessoas+ | **Subseção:** Estrutura da Empresa  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos)  
> **ID:** `38506849096599` | **Última Atualização:** 2026-07-29T16:04:32Z

---

**Módulo: **Pessoal+
**Caminho de acesso: **Pessoal+ > Cadastros
**ID da Tela: **br.com.sankhya.pes.cad.departamentos

 

## **Descrição e Usabilidade**

### **1. Descrição da Funcionalidade**

Os **Departamentos** representam as divisões internas da empresa conforme as atividades executadas.

Eles são utilizados no cadastro de colaboradores, controle de centros de resultado, relatórios e geração de guias.

Uma estrutura de departamentos bem definida ajuda a organizar a empresa e garantir análises e obrigações legais corretas.

![cadastro-departamentop+.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522780929943)

 

### **2. Pré-requisitos**

Antes de cadastrar os departamentos, é necessário configurar a máscara hierárquica:

- 

**Máscara para Departamentos – FPMASCDEP** (tela **Preferências**)

A máscara define a estrutura hierárquica dos departamentos entre níveis sintéticos e analíticos, podendo ter até **4 níveis**.

![mascara-departamento.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522780930711)

⚠️ Não é recomendado alterar a máscara após já existirem departamentos cadastrados, pois isso pode comprometer a hierarquia existente.

 

### **3. Jornada de Uso**

1. 

Acesse a tela **Departamentos** (Pessoal+ > Cadastros).

1. 

Clique no botão 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522780931223)

 **Cadastrar Departamentos**.

1. 

Preencha:

  - 

Código do **Departamento**;

  - 

**Descrição**.

1. 

Na aba **Geral**, configure:

  - 

**Status do departamento**

    - 

**Ativo:** habilita o uso do departamento.

    - 

**Analítico: **quando marcada, indica que o departamento não terá filhos (usado em cadastros e movimentações).

Desmarcada → departamento **Sintético** (apenas estrutura hierárquica).

  - 

**Endereço**

    - 

Endereço, Número e Complemento: localização física do departamento.

  - 

**Centro de Resultado**

    - 

Alocação de custos/resultados. O sistema segue a prioridade:

      1. 

Movimento

      1. 

Funcionário

      1. 

Evento

      1. 

Departamento

      1. 

Empresa

Se o controle for por departamento, preencha o campo.

  - 

**Registro Fiscal**

    - 

Regime fiscal do departamento. É controlado pelo parâmetro **Onde Utiliza o Registro Fiscal - ****FPREGFISCAL**:

      - 

preenchido com Departamentos → permite gerar o resumo da folha (Guias de Previdência Social) por departamento;

      - 

preenchido com Empresas → geração apenas por empresa.

  - 

**Departamentos externos (cessão de mão de obra)**

Esse conceito é utilizado por empresas que trabalham com **cessão de mão de obra**, permitindo identificar a **lotação de cada funcionário**.

O **Tomador de Serviços** é o parceiro que contrata os serviços terceirizados e assume a **corresponsabilidade pelo contrato de trabalho** do empregado vinculado à prestação de serviço.

    - 

Preencher o **Cód. Parceiro** e o **Tipo de Lotação**.

As abas **Inscrição do proprietário do CNO** e **Inscrição do contratante** devem ser **preenchidas **com as devidas identificações **apenas** quando o **Tipo de Lotação** for **2 – Obra de Construção Civil (Empreitada/Subempreitada)**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522749285911)

**Exemplo prático** – Configuração da máscara e estrutura de Departamentos

Suponha que a empresa possua a seguinte estrutura:

- 

1.0.00 – Administrativo

  - 

1.3.00 – Financeiro

    - 

1.3.01 – Contas a Pagar

    - 

1.3.02 – Contas a Receber

A máscara deve estar configurada no parâmetro **FPMASCDEP **como: 9.9.99;0

Agora, se desejar criar os departamentos nessa estrutura abaixo:

- 

1.0.000 – Administrativo

  - 

1.3.000 – Financeiro

    - 

1.3.001 – Contas a Pagar

    - 

1.3.002 – Contas a Receber

A máscara deve estar configurada no parâmetro **FPMASCDEP **como: 9.9.999;0

 

### **4. Pontos de Atenção**

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522749286423)

 **Não altere a máscara com estrutura ativa**

Se já existirem:

- 

funcionários vinculados;

- 

centros de resultado associados;

- 

relatórios configurados;

- 

histórico de movimentações.

Alterar a máscara (**FPMASCDEP**) pode exigir reestruturação completa da hierarquia e revisão de integrações contábeis.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522749286423)

**Departamento Sintético não pode ser usado em movimentações**

Departamentos marcados como **Sintéticos**:

- 

não devem ser vinculados a funcionários;

- 

não devem receber movimentações;

- 

servem apenas para organização hierárquica e consolidação.

Somente departamentos **Analíticos** podem ser utilizados operacionalmente.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522749286423)

**Impacto na geração de guias**

Se o parâmetro **FPREGFISCAL** estiver configurado para utilizar Registro Fiscal por Departamento:

- 

todos os departamentos utilizados na folha devem ter o campo **Registro Fiscal** preenchido.

- 

a ausência dessa informação pode impedir ou distorcer a geração da GPS.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522749286423)

**Centros de Resultado – prioridade de aplicação**

Mesmo que o Centro de Resultado esteja preenchido no departamento, ele pode ser sobrescrito por:

1. 

Movimento

1. 

Funcionário

1. 

Evento

Isso pode gerar divergências se a empresa não padronizar o nível de controle adotado.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522749286423)

**Exclusão de departamento com vínculo ativo**

Não é recomendável excluir departamentos que:

- 

possuam funcionários vinculados;

- 

tenham histórico em folhas já calculadas;

- 

estejam associados a lançamentos contábeis.

O ideal é **desativar (inativar)** o departamento.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38522749286423)

**Departamentos externos (Tomador de Serviços)**

Ao utilizar **Tipo de Lotação**:

- 

Verifique se o Cód. Parceiro está corretamente vinculado.

- 

Dados incorretos podem gerar inconsistência na lotação enviada ao eSocial.

 

### **5. Dicas de Usabilidade**

- 

Planeje a máscara considerando o crescimento da empresa.

- 

Defina previamente se o Registro Fiscal será por empresa ou departamento.

- 

Utilize departamentos sintéticos para organização e analíticos para uso operacional.

 

## **Artigos Relacionados**

- 

[Cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)

- 

[Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214)

- 

[Resumo da Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/17268960280727)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214)
- [Resumo da Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/17268960280727)