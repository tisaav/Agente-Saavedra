# Cadastro de Tabelas de Faixas

> **Módulo:** Pessoas+ | **Subseção:** Eventos e Regras de Cálculo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36716586861335-Cadastro-de-Tabelas-de-Faixas](https://ajuda.sankhya.com.br/hc/pt-br/articles/36716586861335-Cadastro-de-Tabelas-de-Faixas)  
> **ID:** `36716586861335` | **Última Atualização:** 2026-09-25T18:15:27Z

---

**Módulo: **Pessoal+
**Caminho de acesso: **Pessoal+ > Cadastros
**ID da Tela: **br.com.sankhya.rh.TabelaDeFaixa

## **Sumário**

- 
[Descrição e Usabilidade](#descri%C3%A7%C3%A3o-e-usabilidade)

  - [1. Descrição da Funcionalidade](#1-descri%C3%A7%C3%A3o-da-funcionalidade)

  - [2. Pré-requisitos](#2-pr%C3%A9-requisitos)

  - [3. Diagrama de Fluxo](#3-diagrama-de-fluxo)

  - 
[4. Jornada de Uso](#4-jornada-de-uso)

    - [4.1. Cadastrar uma nova Tabela de Faixa](#h_01KBFW0RJN7MFJTCWEB3YMWD9F)

    - [4.2. Atualizar uma Tabela de Faixa para Nova Referência](#h_01KBFW0RJN88RY076WGKQGXYXS)

    - [4.3. Excluir uma Tabela de Faixa](#h_01KBFW0RJNRKY1DFY6YZYMEQ0B)

    - [4.4. Apontamento manual de Códigos de Tabelas](#h_01KBFW0RJN3BA90BY0XCDQKBF4)

  - [5. Pontos de Atenção](#5-pontos-de-aten%C3%A7%C3%A3o)

  - [6. Dicas de Usabilidade](#6-dicas-de-usabilidade)

  - [7. Casos de Uso](#7-casos-de-uso)

- [FAQ – Dúvidas Frequentes](#faq--d%C3%BAvidas-frequentes)

- [Artigos Relacionados](#artigos-relacionados)

## **Descrição e Usabilidade**

 

### **1. Descrição da Funcionalidade**

As Tabelas de Faixas centralizam informações de valores utilizados em cálculos que variam conforme a remuneração do funcionário, como IRRF, INSS, Salário Família, Salário Mínimo e Planos de Saúde. Esta funcionalidade permite cadastrar, atualizar e identificar automaticamente as tabelas utilizadas nos cálculos da folha de pagamento, garantindo precisão nos descontos e benefícios aplicados aos colaboradores.

Com a implementação de códigos de identificação automática na tabela TFPFAI, o sistema reconhece automaticamente as tabelas mais comuns (INSS, IRRF, Salário Família) por meio de um campo numérico que analisa valores e características específicas, facilitando a gestão e reduzindo erros de configuração.

 

### **2. Pré-requisitos**

 

#### **Permissões necessárias**

- Acesso liberado ao módulo Pessoal+ e a tela **Tabela de Faixas **com permissão de edição em Cadastros. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

#### **Configurações relacionadas**

- Tipos de Tabela configurados;

- Eventos de folha (INSS, IRRF, SALARIOFAMILIA) devidamente parametrizados;

- Funcionários com campo **Tipo de Tabela de INSS/IRRF/SAL.FAM** configurado na aba Contrato da tela Configuração Funcionários.

### **3. Diagrama de Fluxo**

 

![fluxograma-tabela-de-faixa.png](https://ajuda.sankhya.com.br/hc/article_attachments/36716777039639)

### **4. Jornada de Uso**

####  

#### **4.1. Cadastrar uma nova Tabela de Faixa**

1. 

Acesse a tela **Tabelas de Faixas **(Pessoal+ > Cadastros) e clique no botão **Adicionar Tabela** (canto inferior direito).

![cadastrar-tabela-de-faixa.png](https://ajuda.sankhya.com.br/hc/article_attachments/36718157310231)

1. 

No pop-up, preencha:

![cadastrar-tabela-de-faixa.png](https://ajuda.sankhya.com.br/hc/article_attachments/36717961801239)

  - **Descrição da faixa**: identifique claramente (ex: INSS 2025);

  - **Referência**: mês/ano de vigência (ex: 01/2025);

  - **Tipo de Tabela**: código que vincula a tabela ao tipo de cálculo.

1. Clique em **Confirmar.**

1. 

Preencha os dados da tabela:

![cadastrosfaixas-tabeladefaixas.png](https://ajuda.sankhya.com.br/hc/article_attachments/36718015626519)

  - 

**Limite da Faixa**: enquadramentos aplicáveis (valores de referência);

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36750817159063)

 O **Limite da Faixa** da última faixa de desconto deve ser preenchido com **9.999.999 **para as tabelas relacionadas a **INSS** e **IRRF**.

  1. 

**Valor 1**,** Valor 2**,** Valor 3...**: valores ou percentuais utilizados em cada faixa.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36750817159063)

 As colunas de** Valor** devem ser configuradas conforme a necessidade de cada tipo de tabela.

1. Para adicionar mais linhas, clique em 

![botão Novo P+.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36717992984343)

**Adicionar nova faixa**.

1. Marque **Tabela utilizada no cálculo de INSS** se aplicável (garante progressividade).

1. 

Clique em **Finalizar Edição**.

![salvar-cadastro-tabeladefaixas.png](https://ajuda.sankhya.com.br/hc/article_attachments/36718242492823)

####  

#### **4.2. Atualizar uma Tabela de Faixa para Nova Referência**

1. Na tela **Tabelas de Faixas, **clique sobre o card da tabela desejada.

1. 

Clique em **Replicar para outras referências** (canto inferior direito).

![duplicar-valores-tabeladefaixas.gif](https://ajuda.sankhya.com.br/hc/article_attachments/36718793481879)

1. 
Preencha:

  - **De**: referência de origem;

  - **Até**: referência final (se desejar duplicar para múltiplas referências).

1. Clique em **Duplicar valores.**

1. Caso necessário, selecione a referência e ajuste os valores conforme as novas alíquotas/limites publicados pelo governo e clique em **Finalizar Edição**.

####  

#### **4.3. Excluir uma Tabela de Faixa**

**Opção 1 - Exclusão direta:**

![EXCLUIR1-TABELADEFAIXA.gif](https://ajuda.sankhya.com.br/hc/article_attachments/36718962880407)

1. Passe o mouse sobre o card da tabela;

1. Clique em **Excluir tabela**;

1. Confirme a exclusão na mensagem exibida.

**Opção 2 - Exclusão por remoção de linhas:**

![EXCLUSAO2-TABELADEFAIXA.gif](https://ajuda.sankhya.com.br/hc/article_attachments/36720983163799)

1. Abra a tabela;

1. Remova todas as linhas;

1. Clique em **Finalizar Edição** (a tabela será excluída automaticamente).

####  

#### **4.4. Apontamento manual de Códigos de Tabelas**

```text
A partir da versão 5.67.0
```

Se o sistema não conseguir identificar automaticamente um código único após as verificações acima, será solicitado ao usuário que faça a identificação manual.

**Como funciona:**

1. 

Ao realizar o cálculo da folha com ausência de tabela identificada, um pop-up será exibido com a seguinte mensagem:

*"Para continuar com o cálculo e ter a atualização das suas tabelas de faixa padrão de forma automática, é necessário que seja feito o apontamento das seguintes tabelas:"*

![CALCULO-TABELA-SEM-IDENTIFICACAO.png](https://ajuda.sankhya.com.br/hc/article_attachments/36721269630359)

1. 

O pop-up apresentará uma lista com os códigos das tabelas não identificadas, exemplo:

  - Tabela de INSS

  - Salário Mínimo

1. 

Clique no botão **Apontar agora** para abrir a tela **Tabelas de Faixas**.

1. 

Na tabela de faixa, selecione o código correto no campo **Identificação** e salve as alterações.

1. 

Retorne a tela do cálculo e finalize a operação.

**Regras importantes:**

- Cada código de tabela de faixa deve possuir apenas um apontamento (relação 1:1);

- Se uma tabela já estiver identificada (ex: 1 - INSS), ela não aparecerá nas opções de apontamento manual;

- Para apontar um código já utilizado em outra tabela, o vínculo anterior deve ser removido;

- É possível remover a identificação, deixando o campo sem preenchimento.

 

### **5. Pontos de Atenção**

- **Auxílio Creche**: o campo "Limite da Faixa" deve ser preenchido em **meses**, não em anos.

- **Criação completa**: crie os detalhes da tabela para **todas as referências do ano** para evitar inconsistências nos cálculos.

- **Vinculação ao funcionário**: após cadastrar o Tipo de Tabela, vincule-o ao funcionário em **Configuração Funcionários > **Aba** Contrato >** Campo** Tipo de Tabela de INSS/IRRF/SAL.FAM.**

- **Reajuste**: ao utilizar Tabela de Faixas, nenhum percentual deve ser informado no reajuste.

- **Identificação única**: cada código de tabela de faixa deve ter apenas um apontamento (relação 1:1).

- **Campo não obrigatório**: o campo de identificação na TFPFAI pode permanecer vazio.

- **Bloqueio após fechamento**: após o fechamento da primeira folha com o campo preenchido, as tabelas identificadas automaticamente passarão a ser somente de consulta. 

- **Remoção de vínculo**: para apontar um código já utilizado a outra tabela, é necessário remover o vínculo anterior.

 

### **6. Dicas de Usabilidade**

- **Estrutura flexível**: as colunas de Valor são livres para uso em outros tipos de eventos além dos padrões. Planeje sua utilização para facilitar a construção de fórmulas de cálculo.

- **Replicação em lote**: use o recurso "Replicar para outras referências" preenchendo o campo "Até" para duplicar valores para várias referências de uma só vez.

- **Consulta à base modelo**: a base modelo já inclui as tabelas de faixas mais comuns cadastradas, facilitando a configuração inicial.

- **Atualização governamental**: sempre consulte as tabelas oficiais publicadas pelo governo ao atualizar limites e alíquotas.

- **Identificação automática**: o sistema busca características específicas (valores, alíquotas, campos marcados) para identificar automaticamente o tipo de tabela.

- **Verificação de eventos**: se houver dúvida na identificação automática, o sistema verifica se os eventos relacionados (INSS, IRRF, entre outras) são padrões ou personalizados.

- **Consulta de fórmulas**: em casos de personalização, o sistema consulta a fórmula vinculada na FTF para determinar qual código está sendo utilizado.

 

### **7. Casos de Uso**

✅ **Exemplo Real**: 

Cadastro da tabela INSS 2025 com faixas de 1518, 4190,83 e alíquotas progressivas de 7,5%, 9%, 12% e 14%, marcada como "Tabela utilizada no cálculo de INSS" - Sistema identifica automaticamente como código 1.

✅ **Exemplo Real**: 

Replicação da tabela de Salário Família de janeiro para todos os meses do ano, com limite de faixa R1.906, 04evalor R 65,00 - Sistema identifica automaticamente como código 3.

✅ **Exemplo Real**: 

Usuário realiza cálculo da folha e sistema não identifica tabela de Salário Mínimo. Pop-up é exibido solicitando apontamento manual, usuário clica em "Apontar agora" e vincula o código 5 à tabela correta.

❌ **Erro Comum**: 

Usuário cria tabela de Auxílio Creche informando "Limite da Faixa" em anos (ex: 2 anos) ao invés de meses (ex: 24 meses).

❌ **Erro Comum**: 

Usuário atualiza tabela de IRRF para nova referência, mas esquece de criar detalhes para todos os meses do ano, gerando erros de cálculo nos meses seguintes.

 

## **FAQ – Dúvidas Frequentes**

 

1. 

**O que são Tabelas de Faixas e para que servem?**

São tabelas que armazenam valores utilizados em cálculos da folha que variam conforme a remuneração do funcionário, como descontos de INSS, IRRF e benefícios como Salário Família.

1. 

**Por que devo criar detalhes da tabela para todas as referências do ano?**

Para evitar inconsistências e erros nos cálculos da folha nos meses subsequentes. Cada referência (mês/ano) precisa ter seus valores definidos.

1. 

**Como funciona a identificação automática de códigos?**

O sistema possui um campo na tabela TFPFAI que analisa características específicas das tabelas (valores, alíquotas, limites) baseadas em dados de 2025 para identificar automaticamente os tipos mais comuns (INSS, IRRF, Salário Família).

1. 

**O que faço se o sistema não identificar automaticamente minha tabela?**

Um pop-up será exibido na tela de cálculo solicitando o apontamento manual. Clique em "Apontar agora" e selecione o código correto para cada tabela.

1. 

**Posso usar o mesmo código de identificação para duas tabelas diferentes?**

Não. Cada código deve estar vinculado a apenas uma tabela (relação 1:1). Para reutilizar um código, é necessário remover o vínculo anterior.

1. 

**Como vincular a tabela de faixa ao funcionário?**

Acesse **Configuração Funcionários > Aba Contrato** e preencha o campo **"Tipo de Tabela de INSS/IRRF/SAL.FAM"** com o código da tabela correspondente.

1. 

**Posso editar uma tabela já identificada automaticamente após o fechamento da folha?**

Após o fechamento da primeira folha com o campo preenchido, as tabelas identificadas automaticamente ficam em modo consulta.

1. 

**Por que o campo "Limite da Faixa" da tabela de Auxílio Creche deve ser preenchido em meses?**

É uma especificidade deste tipo de tabela. Informe a idade em meses (ex: 24) ao invés de anos (ex: 2).

1. 

**Posso remover a identificação de uma tabela?**

Sim. É possível deixar o campo de identificação vazio, removendo o código atribuído.

1. 

**O que significa marcar a opção "Tabela utilizada no cálculo de INSS"?**

Esta marcação garante que o sistema respeite a progressividade prevista na regra de cálculo do INSS.

1. 

**O campo de identificação na TFPFAI é obrigatório?**

Não. O campo pode permanecer vazio caso não seja necessário utilizar a identificação automática.

1. 

**Quanto tempo o campo de identificação fica liberado para edição?**

Inicialmente, o campo ficará liberado para edição durante o primeiro mês após a implementação. Após o fechamento da primeira folha, as tabelas identificadas passam a modo consulta.

1. 

**Como o sistema decide entre dois códigos candidatos?**

O sistema verifica se os eventos relacionados (INSS, IRRF, SALARIOFAMILIA, etc.) são padrões. Se forem personalizados, verifica a fórmula vinculada na FTF para determinar qual código está sendo utilizado.

## **Artigos Relacionados**

- [Tabelas de Faixas atualizadas 2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/29189984521495)

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)

- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)

- [Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287)


---

### 🔗 Links e Referências Internas:

- [Tabelas de Faixas atualizadas 2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/29189984521495)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287)