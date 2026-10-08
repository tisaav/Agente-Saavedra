# Fluxo de Caixa Matricial

> **Módulo:** Financeiro e Patrimônio | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606874-Fluxo-de-Caixa-Matricial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606874-Fluxo-de-Caixa-Matricial)  
> **ID:** `360044606874` | **Última Atualização:** 2026-07-29T14:40:56Z

---

```text
 Módulo: Financeiro > Relatórios > Gerenciais
```

O Sankhya Om conta com um relatório financeiro gerencial de Fluxo de Caixa Matricial, que é localizado por meio desta tela. Esta ferramenta permite a análise de Fluxo de Caixa em formato de Cubos de Decisão, podendo ser detalhado por **"****Natureza"**, **"****Centro de Resultado"**, ou **"****Projeto"**. Neste relatório podem ser listados todos os gastos ou recebimentos, agrupando os lançamentos por período (diário, semanal, mensal, trimestral, ou anual).

Além disso, você pode utilizar das dimensões para cada nível de Natureza, para cada nível de Projeto e para cada nível de Centro de Resultado de acordo com os níveis das máscaras configuradas no sistema. Em outras palavras, se a máscara para Naturezas é **"99.999.999.999"**, por exemplo, então há 4 níveis de Naturezas. Além disso, se para os filtros informados na tela não existe nenhum lançamento para o nível 4 ele será omitido dos **"Campos disponíveis"**.

[Painel Geral](#painelgeral)                                                          [Painel Avançado](#painelavan%C3%A7ado)

[Seleção de Contas](#sele%C3%A7%C3%A3odecontas)                                             [Dicas de análise do Fluxo de Caixa Matricial](#Dicasdean%C3%A1lisedoFluxodeCaixaMatricial)

![fluxo_de_caixa_1.png](https://ajuda.sankhya.com.br/hc/article_attachments/8743746245015)

Para geração do Cubo de Decisões, informe no filtro os critérios para a busca de dados. O filtro é dividido nos painéis **"Geral"** e **"Avançado"**, os quais serão detalhados mais adiante nesta documentação. Estes painéis estão contidos na aba **"Configuração"**, onde são definidos os critérios de busca. Assim, para visualizar os resultados dos filtros e suas respectivas configurações, acione o botão **"Aplicar filtros e visualizar o cubo"** localizado no canto superior direito desta tela.

### 
Painel Geral

![fluxo_de_caixa_2.png](https://ajuda.sankhya.com.br/hc/article_attachments/8743857284503)

Informe no campo** "Data de Negociação no Período"**, o período de negociação que os títulos foram negociados no período (são considerados também os títulos pendentes).

Preencha o campo** "Data de Movimentos no Período"** com o período de movimentação financeira, ou seja, os títulos movimentados no período.

Efetuando a marcação** "Pendentes no Período"**, serão habilitados os campos que definem o período dos títulos pendentes.

O Float é definido no cadastro de [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo). É necessário configurar os Tipos de Título recebíveis da empresa e efetuar a marcação **"Considerar Float"** na visualização do relatório de Fluxo de Caixa para que não seja considerado como um dinheiro na conta antes desse realmente estar disponível. Considere o seguinte exemplo de Float:

Um recebível com vencimento em 25/11, cujo Tipo de Título contiver o Float igual a 2 dias, constará nos relatórios de fluxo de caixa na data do dia 27/11.

**Observação:** quando a marcação **"Considerar dias úteis"** da tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) estiver habilitada, o sistema irá ponderar a data de vencimento + marcação Considerar float para exibir os títulos para análises. **{disponível na versão ≥ 4.12}**

Efetuando a marcação** "Baixados no Período"**, serão habilitados os campos que definem o período dos títulos baixados. Se realizada esta marcação, os campos abaixo dela deverão ser obrigatoriamente preenchidos.

**Nota:** poderão ser selecionados títulos Pendentes, Baixados ou Ambos. O Período de análise para o que for escolhido deverá ser informado.

Você pode utilizar como critério de filtro, as opções **"****Receitas****"** e/ou **"****Despesas****"** e **"****Real****"** e/ou **"****Provisão****"**.

Por meio do botão **"Aplicar filtros e visualizar o cubo" **localizado na parte superior desta tela, aplica-se as configurações efetuadas nos painéis **"Geral"** e **"Avançado"**, de acordo com seus respectivos filtros, permitindo desse modo, visualizar os resultados que compõem os cubos de decisões.

Nesse momento, o cubo é gerado contendo as opções para campos disponíveis, tais como: Centro de Resultado, Natureza e Projeto, além das dimensões para cada nível de Natureza, Projeto e Centro de Resultado de acordo com os níveis das máscaras configuradas no sistema.

Dessa forma, selecione os campos para o filtro desejado, arrastando-os com o mouse para o cubo.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360083684433)

Assim, os valores serão apresentados de forma detalhada por Centro de Resultado, Natureza e/ou Projeto, e suas respectivas dimensões.

Considerando isso, temos à esquerda os seguintes botões:

**

![Botão Resultado da Consulta (Grade de Dados) FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16281648166167)

**** Resultado da Consulta (Grade de Dados): **Este botão apresenta o resultado do cubo de decisão através da visualização de uma tabela, ou seja, uma grade contendo os dados.

**

![Botão Apresentar Lista de Campos FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16281632048791)

 ****Apresentar Lista de Campos:** Botão utilizado para ocultar ou apresentar a lista de campos.

**

![Botão Exportar para o Excel FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16281648180631)

 Exportar para o Excel: **Este botão tem a função de exportar o cubo de decisão para uma planilha do Excel.

É relevante mencionarmos que o sistema possui configurações personalizadas que permitem uma melhor utilização e aplicabilidade de seus respectivos cubos de decisões. Sendo assim, considera-se para esse caso, cubos do tipo relatório que contenham as opções de múltiplas perspectivas.

**Nota:** inicialmente, as informações mencionadas aplicam-se ao cubo Fluxo de Caixa Matricial.

Considerando a otimização na execução do cubo em questão, obtém-se uma execução alternativa ao realizar a consolidação de dados. Desse modo, para que seja possível utilizar essa funcionalidade, configure o parâmetro **"FCMTABCONSOL - Tabela de consolidação p/ Fluxo de Caixa Matricial"** registrando no campo **"Texto" **da tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), a nomenclatura da tabela que será utilizada para a consolidação do Fluxo de Caixa Matricial. Assim, ao configurá-lo, será disponibilizado no canto superior direito da tela Fluxo de Caixa Matricial, o botão **"Gerar Query de Consolidação"**.

Acionando o botão Gerar Query de Consolidação, será gerada uma query, anteriormente embasada na query original, considerando que sua aplicação está diretamente relacionada à tela [Consolidador de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994). Uma vez configurado o parâmetro e criado o registro pertinente ao consolidador de dados, o cubo de decisão correspondente passará a buscar os dados diretamente na tabela em que os dados já se encontram consolidados.

**Observação:** ainda considerando as funcionalidades dessa tela, o sistema disponibiliza a opção **"Ativar consolidação de dados"** localizada no botão **"Outras Opções..."** na parte superior da tela em referência.

[[voltar ao topo]](#top)

### 
Painel Avançado

**Nota**: as definições de moeda e conversão nesta tela são influenciadas pelo parâmetro `PROCMOEINEX`. A opção escolhida neste parâmetro afetará não apenas o Fluxo de Caixa Matricial, mas também os relatórios *Gerencial Financeiro e Fluxo de Caixa, além das telas de Consulta de Produtos, Consulta Saldo Bancário, Baixa Agrupada e Movimentação Financeira*.

![fluxo_de_caixa_3.png](https://ajuda.sankhya.com.br/hc/article_attachments/8744159213975)

Informe no campo** "Moeda"** a moeda a ser considerada, quando existirem transações financeiras em moedas estrangeiras.

Na seção** "Data para converter a moeda" **temos a data a ser admitida para conversão da moeda estrangeira, dentre as seguintes opções:

- 

**Negociação:** Converte através data de negociação do Título. Utilizada quando o valor de conversão for fixado na data de negociação.

- 

**Vencimento:** Converte por meio da data de vencimento do Título. Empregada quando a conversão ocorrer na data de vencimento.

- 

**Baixa:** Converte pela data da baixa. Seu uso ocorre quando o valor for convertido na data da baixa do Título.

- 

**Fixa:** A conversão é feita através de um valor fixo informado no cadastro de moedas. Normalmente utilizado em negociações contratuais que estipulam um valor fixo de conversão durante a vigência do contrato. Quando selecionada essa opção, será apresentado o campo logo ao lado onde informa-se a data.

 

A conversão da moeda será da seguinte forma:

Os títulos que possuem moeda diferente da 'moeda corrente', serão convertidos para moeda corrente considerando a data estipulada para conversão. Para valores que vêm da tabela `TGFSBC`, a conversão será pela data de referência; na tabela `TGFMBC`, a conversão será pela data de lançamento. Se a data para converter a moeda for 'Fixa', será disponibilizado um campo de data para a digitação da mesma. Uma linha no cabeçalho do relatório trará qual moeda foi escolhida e qual a data para conversão da mesma. **Ressalta-se que o comportamento desta conversão é definido pelo parâmetro **`**PROCMOEINEX**`**, que também rege o processamento de moedas nas telas de Consulta de Produtos, Consulta Saldo Bancário, Baixa Agrupada e Movimentação Financeira.**

A seção** "Saldos"** permite o agrupamento dos saldos das contas, de acordo as seguintes opções:

- Apenas no início;

- Diário;

- Semanal;

- Mensal;

- Trimestral;

- Anual.

A marcação** "Considerar Renegociações" **fará com que o sistema busque os títulos renegociados no período; por padrão, esta marcação é apresentada realizada e desabilitada.

A marcação** "Considerar Naturezas especiais" **busca os dados cadastrados em Naturezas especiais, localizados na tela [Naturezas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606154-Naturezas-Especiais).

A marcação** "Imprime o valor Líquido"** fará com que o sistema analise os valores marcados na tela [Componentes do Valor Líquido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607174-Componentes-do-Valor-L%C3%ADquido).

Quando a marcação** "Considerar baixa futura como títulos a pagar/a receber"** estiver efetuada, fará com que o sistema considere os títulos baixados, com data da baixa maior que a data atual, como títulos a receber/a pagar. Se desmarcada, serão considerados os títulos com baixa futura como recebidos ou pagos.

A marcação** "Usar Antecipação/Atraso habitual de pgto do Cad. Parceiro?"**, quando efetuada,** **fará com que o sistema considere os dias informados de atraso ou antecipação que habitualmente o parceiro tenha, na formação do fluxo de caixa. Assim, o gestor não contará com o valor antes do dia que o parceiro costuma pagar. A Antecipação/Atraso é configurada na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito).

A marcação** "Gerar uma linha p/Movimento Bancário para o período de Baixa"** lança no cubo um somatório das movimentações bancárias relacionadas às contas que foram selecionadas na grade. Estas movimentações bancárias são filtradas e somadas, conforme o período especificado no filtro, campo **"Baixados no Período"**.

**Observação:** quando já existir no cubo uma linha com o saldo (o valor proveniente de receitas), essa marcação totalizará a somatória das baixas daquele período, ao valor desse saldo. Nos casos em que o cubo ainda não tenha uma linha com o saldo das receitas, essa marcação gerará essa linha.

Quando a marcação **"Filtrar baixados pela conta da baixa"** estiver realizada, fará com que o sistema filtre as baixas no período, considerando a seleção de contas bancárias presentes na tela, verificando se cada uma das baixas no período foi realizada em alguma das contas marcadas e incluirá no relatório apenas as que pertencem às contas selecionadas, evitando assim, que outras baixas de outras contas incidam no saldo visualizado no cubo.

[[voltar ao topo]](#top)

### 
Seleção de Contas

![fluxo_de_caixa_4.png](https://ajuda.sankhya.com.br/hc/article_attachments/8744154326295)

Se a marcação** "Apenas Contas Ativas" **estiver efetuada, o sistema avaliará apenas as operações realizadas com as contas ativas.

A marcação** "Marcar/Desmarcar Todas"** marca ou desmarca todos os registros da grade de seleção das contas.

**Importante:** a **"Seleção de Contas"** serve para selecionar contas das quais o saldo será somado para apresentação no cubo, não um filtro para os financeiros que serão filtrados. Assim, para filtrar os financeiros, é necessário que você crie um filtro personalizado.

[[voltar ao topo]](#top)

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16281442609303)

 **Dicas que facilitarão a análise do Fluxo de Caixa Matricial:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458051054615)

 Diferenças Entre Fluxo de Caixa Matricial e Sintético

Podemos analisar o **"Fluxo de Caixa"** em forma **"Matricial"** utilizando os mesmos conceitos do **"Fluxo de Caixa Sintético"**, observadas algumas diferenças:

- 

O **"Fluxo de Caixa Matricial"** sempre considera **"Saldo Inicial"** no primeiro dia do período analisado e a data para mostrar o saldo, não precisa ser informada.

- 

Não considera **"Percentuais de Inadimplência"**.

- 

Não possui a opção de considerar baixa futura como título a pagar ou a receber.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458051054615)

 Gerar apenas um saldo inicial analisando passado com periodicidade Mensal

Para analisar o desempenho da empresa considerando o saldo inicial e o resultado mês a mês compondo o saldo atual, é necessário efetuar as marcações **"Saldo/Apenas no início"** e **"Saldo/ Mensal"**.

Escolha um período passado e faça a análise, considerando apenas títulos baixados (recebidos e pagos).

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458051054615)

 Considerar Naturezas Especiais

Para visualizar no Fluxo de Caixa os valores separadamente de Juros, Multa, Despesas com cartório etc, utilize esta marcação. Para isso, é necessário cadastrar na tela [Naturezas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606154) as naturezas para as quais o sistema irá ratear os valores na visualização do relatório.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)
- [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)
- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)
- [Consolidador de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601994)
- [Naturezas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606154-Naturezas-Especiais)
- [Componentes do Valor Líquido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607174-Componentes-do-Valor-L%C3%ADquido)
- [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)
- [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito)
- [Naturezas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606154)