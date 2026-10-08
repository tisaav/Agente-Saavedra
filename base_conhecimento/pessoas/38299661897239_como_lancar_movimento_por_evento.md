# Como lançar movimento por evento?

> **Módulo:** Pessoas+ | **Subseção:** Lançamentos da Folha  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38299661897239-Como-lan%C3%A7ar-movimento-por-evento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38299661897239-Como-lan%C3%A7ar-movimento-por-evento)  
> **ID:** `38299661897239` | **Última Atualização:** 2026-09-27T17:35:10Z

---

**Módulo: **Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha
**ID da Tela: ** br.com.sankhya.rh.MovimentacoesFolha

## **Descrição e Usabilidade**

### **1. Descrição da Funcionalidade**

A opção **Lançamento de movimento por evento** permite lançar um mesmo evento para vários funcionários de forma rápida e centralizada.

Essa forma de lançamento é indicada quando o objetivo é aplicar um evento específico para diversos colaboradores simultaneamente, informando os valores ou índices diretamente na lista de funcionários.

Os lançamentos podem ser feitos:

- 

****[Por Funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319)

- 

**Por Evento**

Este artigo explica o **lançamento por evento**.

********

****[Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)

| ⚠️ Atenção Se já existir folha calculada para a competência, não é possível lançar novos movimentos para os colaboradores dessa referência. Antes de lançar, acesse o  e exclua o cálculo da folha desses funcionários; depois de lançar o movimento, calcule a folha novamente. |
| --- |

### **2. Pré-requisitos**

Para utilizar a rotina, é necessário:

- 

Ter acesso ao módulo **Pessoal+ **e às rotinas de folha.

- 

Ter eventos previamente cadastrados.

- 

A folha da referência não pode estar calculada para os funcionários que receberão o lançamento. Caso já exista cálculo, acesse o ****[Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247) e exclua-o antes de lançar o movimento.

### **3. Jornada de Uso**

![lançarmovimentoevento.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38326343691543)

#### **Lançar evento**

1. 

Acesse a tela **Lançamento de Movimento** (Pessoal+ > Rotinas Folha) e selecione **Por evento**.

1. 

No painel de filtros, informe:

  - 

**Empresa**;

  - 

**Referência**;

  - 

**Tipo de Movimento**.

O movimento determina:

    - 

Em qual folha o lançamento será feito;

    - 

Se o lançamento será mensal ou fixo.

1. 

Clique em **Pesquisar** para carregar os eventos.

1. 

Clique no **card do evento** desejado.

O sistema exibirá as informações do evento e a lista de colaboradores da empresa.

Se algum colaborador já possuir a folha da referência calculada, será exibido o aviso **Com folha calculada**, impedindo o lançamento.

1. 

Para selecionar os colaboradores, você pode:

  - 

utilizar o botão **Filtrar** para localizar colaboradores;

  - 

selecionar, clicando na linha de cada colaborador.

1. 

Após a seleção, o botão **Informar Valores** será habilitado.

1. 

Clique em **Informar Valores**

1. 

Informe:

  - 

Valor (eventos em unidade Valor);

  - 

Índice (eventos em Hora/Dia).

1. 

Se desejar incluir mais colaboradores para o mesmo evento, utilize o botão **Selecionar Outros Funcionários**.

1. 

Caso queira lançar um único valor para todos os colaboradores selecionados, acione o botão **Lançar valor único**, informe o valor e confirme.

1. 

Após revisar os dados, clique em **Lançar Movimentos**.

1. 

O sistema exibirá a mensagem: **"Movimentos lançados com sucesso!"**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38327937977495)

 Após o lançamento dos movimentos, já é possível **realizar o cálculo da folha dos funcionários** normalmente.

#### **Visualizar, editar ou excluir lançamentos**

- 
**Visualizar** **e conferir os eventos lançados**

  1. Selecione o tipo de movimento **Por funcionário**.

  1. Preencha os** filtros** e clique em** Pesquisar**.

  1. 

Selecione o(s) funcionário(s) e clique na aba **Visualização**.

![visualizarmovimentoevento.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38326315340055)

1. 
**Editar valor ou índice do evento lançado**

  1. 

Estenda o card do evento e passe o mouse sobre a linha do mesmo, clique em **Editar evento** (lápis) e salve a alteração.

![editarlançamentomovimentoporfuncionario.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38326315343255)

1. 
**Excluir eventos**

  1. 

Para excluir, estenda o card do evento e passe o mouse sobre a linha do mesmo, clique em **Excluir evento** (lixeira) e confirme a exclusão.

![excluirlançamentomovimentoporfuncionario.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38326315344919)

  1. 

Caso queira excluir o lançamento em lote, clique em **Ver movimentações**, selecione os colaboradores, clicando em seus respectivos cards, e, depois, em **Excluir movimentos** (lixeira).

![excluirmovimentolote.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38326315349015)

### **4. Pontos de Atenção**

- 

**Eventos com parametrização personalizada**

Eventos com parametrização personalizada (por exemplo, um evento de insalubridade configurado de forma específica para a empresa) podem não ser gerados automaticamente durante o cálculo da folha. Nesses casos, lance o evento manualmente pelo **Lançamento de Movimento**, como **Movimento Fixo**, para que ele passe a ser considerado também nas competências seguintes.

A replicação de um lançamento fixo para a competência seguinte só ocorre depois que a referência atual é fechada. Se a referência ainda não tiver sido fechada, o lançamento fixo não aparece automaticamente na próxima competência, isso não indica um erro, apenas que o fechamento ainda está pendente.

- 

**Rescisão Complementar**

Ao selecionar o tipo de movimento **Rescisão Complementar**, o sistema exibirá o aviso:

***"Só é possível lançar movimentos de Rescisão Complementar dentro da referência de desligamento do funcionário. Para pagamentos em referências posteriores, utilize o tipo Verba de Meses Anteriores."***

- 

**Folha já calculada**

Se a folha estiver calculada para o colaborador:

  - 

Não será possível realizar novos lançamentos.

  - 

Será exibido o aviso **Com folha calculada**.

Para liberar o lançamento, acesse o ****[Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247), exclua o cálculo da folha do(s) funcionário(s) e, em seguida, lance o movimento normalmente. Depois de lançado, calcule a folha novamente.

- 

**Lançamento via API**

Quando o lançamento for realizado via API:

  - 

As mesmas validações do lançamento manual serão aplicadas.

  - 

É necessário preencher corretamente todos os campos.

- 

**Bloqueio para eventos de Plano de Saúde**

O sistema impede o lançamento quando o evento possuir simultaneamente:

  - 

**Natureza da rubrica:** 9219

  - 

**Código de incidência de IRRF:** 09, 67 ou 9067

  - 

**Tipo de rubrica:** 2

Ao tentar lançar o movimento nessas condições, o sistema exibirá uma mensagem de bloqueio do lançamento.

- 

**Bloqueio de lançamento de evento de Plano de Saúde fora da vigência**

O sistema também impede o lançamento de eventos de plano de saúde quando a referência do lançamento está fora do período de vigência cadastrado, tanto para o titular quanto para o dependente.

  - 

Se a referência do lançamento **for anterior à Referência Inicial** cadastrada, o sistema exibe:

***"Não foi possível lançar o evento de plano de saúde para o funcionário (ou para o dependente). A referência de início de validade do plano de saúde é: [Referência Inicial]. Para mais detalhes, acesse (Configuração de Funcionários > Plano de Saúde, ou > Dependentes)."***

  - Se a referência do lançamento **for posterior à Referência Final** cadastrada, o sistema exibe a mesma mensagem, trocando "referência de início" por "referência final".

Em ambos os casos, a mensagem vem acompanhada de um atalho direto para a tela onde a vigência do plano pode ser corrigida.

**Importante:** esse bloqueio vale para o lançamento manual, feito pela tela de **Lançamento de Movimento**. Ele não se aplica ao lançamento automático gerado pela rotina de fechamento da folha (lançamento fixo); para esse caso, continue seguindo a orientação de excluir o lançamento fixo manualmente, descrita no artigo [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959).

### **5. Dicas de Usabilidade**

- 

Utilize este modo quando precisar lançar o mesmo evento para muitos colaboradores.

- 

Use filtros para agilizar a seleção.

- 

Sempre confirme se a folha não está calculada antes de iniciar o processo.

## **Artigos Relacionados**

- 

[Lançamento de movimento por funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319)

- 

[Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)

- [Cadastro e Vínculo de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)

- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)


---

### 🔗 Links e Referências Internas:

- [Por Funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Cadastro e Vínculo de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)