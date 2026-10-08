# Gerência de Processos

> **Módulo:** Plataforma e Integrações | **Subseção:** Flow  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4403486477719-Ger%C3%AAncia-de-Processos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403486477719-Ger%C3%AAncia-de-Processos)  
> **ID:** `4403486477719` | **Última Atualização:** 2026-07-29T15:08:35Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313245949463)

 **Módulo:** Flow                     

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279105559)

 **Versão disponível:** a partir da 4.7
```

A Gerência de Processos é um painel gerencial do SankhyaFlow, que permite aos gestores de um processo monitorar em tempo real as informações dos processos, como o volume de solicitações pendentes, a distribuição das tarefas com cada membro da equipe e diversas estatísticas de desempenho do processo. 

O gestor utiliza a Gerência de Processos para monitorar a execução de atividades de um processo e suas estatísticas de desempenho. Dessa maneira, esse gestor terá condições de tomar decisões estratégicas apropriadas, visando corrigir ou aperfeiçoar o desempenho do processo.

Vamos utilizar um caso de uso para que a funcionalidade dessa rotina se torne mais clara para você, veja só:

O usuário Marcos é gestor do Processo de **"****Liberação de Acessos"** da empresa Alpha Ltda, que é representado na [imagem 1](#imagem1). Esse processo tem o objetivo de atender solicitações internas para liberações de acessos aos sistemas da empresa.

Como gestor, ele deseja acessar informações gerenciais desse processo para verificar como está a distribuição das atividades para cada um de seus colaboradores, as solicitações que estão pendentes e também as estatísticas gerais de desempenho do processo, como tempo médio de atendimento, tempo médio de fila, dentre outros. Com essas informações, o gestor poderá tomar decisões para o melhor desempenho do processo, bem como, verificar se os prazos de atendimento às solicitações definidos previamente estão sendo cumpridos.

![flow.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403501353239)

****

| Processo de Liberação de Acessos |
| --- |

Para que o gestor Marcos possa acessar a Gerência de Processos, é necessário que o modelador do processo libere seu acesso no cadastro do [Processo de Negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107733-Processos-de-Neg%C3%B3cio) **"Liberação de Acessos"**, na aba [Gestores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107733-Processos-de-Neg%C3%B3cio#abagestores):

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403548804759)

****

| Cadastro de Gestores de um Processo |
| --- |

É possível realizar 3 tipos de análises acessando as informações da Gerência de Processos através do ícone 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403549065751)

 (localizado ao lado superior esquerdo da tela), que estão agrupadas em **"Monitor de Processos"**, **"Estatísticas de Processos"** e **"Gestão de Tarefas"**. Conforme os processos são executados, automaticamente os dados da Gerência de Processos são atualizados para permitir as análises. Para saber mais sobre essas análises, clique nas imagens abaixo:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279106839)

[#monitordeprocessos](#monitordeprocessos)

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313245951511)

[#estat%C3%ADsticasdeprocessos](#estat%C3%ADsticasdeprocessos)

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279109911)

[#gest%C3%A3odetarefas](#gest%C3%A3odetarefas)

|  |  |  |
| --- | --- | --- |

#### **Monitor de processos**

O Monitor de processos possibilita que o gestor visualize todas as solicitações pendentes por processo, os usuários que mais realizaram solicitações em cada processo (gráfico TOP 5 solicitantes) e o gráfico de solicitações pendentes de conclusão.

Sempre que a Gerência de Processos é aberta, por padrão são apresentadas as informações gerenciais do Monitor de processos. O acesso também pode ser realizado pelo botão 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403549065751)

:

### 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279110295)

****

| Acesso ao Monitor de processos na Gerência |
| --- |

No Monitor de processos é possível aplicar filtros de solicitações utilizando o **"Número da solicitação"**, o **"Solicitante"**, o **"Período de abertura"** e o **"Processo de Negócio"**.

No nosso caso de uso, o gestor Marcos possui acesso a 2 processos (solicitação de manutenção e liberação de acessos). Em nosso exemplo, iremos filtrar pela data de abertura e pelo processo Liberação de Acessos, conforme exibimos na imagem abaixo:

### 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279111063)

****

| Aplicação de filtros no Monitor de processos |
| --- |

Na próxima imagem, temos o resultado dos filtros aplicados no Monitor de processos:

### 

![image__4_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313245957399)

****

| Monitor de processos |
| --- |

Na grade **"Lista de solicitações pendentes"** podemos clicar sobre uma determinada solicitação para visualizar mais detalhes sobre ela:

### 

![detalhes_solicitacao.gif](https://ajuda.sankhya.com.br/hc/article_attachments/42313279113367)

****

| Detalhes de uma solicitação no Monitor de processos |
| --- |

Na imagem acima temos os detalhes da solicitação, como o número do processo e versão, o solicitante (pessoa que abriu o processo) e a data da solicitação. 

Abaixo dos **"Detalhes da solicitação"**, temos o **"****Histórico da Solicitação"**, que apresenta de forma cronológica, a execução de cada elemento (eventos de início/fim/intermediário, gateways e tarefas) contido no fluxo do processo, com a data de criação, conclusão, duração e o dono de atividades.

Quando configurado na modelagem pelo modelador e preenchidos pelos usuários, os apontamentos de horas realizados na solicitação também serão exibidos na grade **"Apontamentos"**.

Para voltar para a tela inicial do Monitor de processos basta clicar sobre o botão voltar localizado na parte superior da tela:

### 

![botao_voltar.gif](https://ajuda.sankhya.com.br/hc/article_attachments/42313279114519)

****

| Voltar para a tela inicial do Monitor de processos |
| --- |

[[voltar ao topo]](#top)

#### **Estatísticas de processos**

Através da Estatística de processos podemos realizar análises históricas para visualizar diversos indicadores de um processo para melhor gerenciar seu desempenho.

Acessando a tela de Estatísticas de processos pelo menu, iremos filtrar as solicitações abertas de 01/04/2021 à 27/04/2021 para o processo Liberação de Acessos:

### 

![estatistica_processos.gif](https://ajuda.sankhya.com.br/hc/article_attachments/42313245959447)

****

| Aplicação de filtros na tela de Estatísticas de processos |
| --- |

A seguir, temos a imagem das estatísticas do processo Liberação de Acessos para o período de 01/04/2021 à 27/04/2021:

### 

![image__7_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279116951)

****

| Estatísticas de processos |
| --- |

Na grade **"Lista de Processos"**, temos a relação de todos os processos que o gestor Marcos possui acesso, respeitando os filtros aplicador anteriormente.

Já na grade **"Versões do processo 'Liberação de acessos'"**, são apresentadas todas as versões de um processo com suas respectivas estatísticas, considerando o filtro aplicado inicialmente.

Lembrando que aplicamos um filtro para solicitações abertas de 01/04/2021 à 27/04/2021, nesse período foram executados processos somente na versão 28. Sendo assim, é possível avaliar o desempenho do processo em cada uma de suas versões.

Abaixo trataremos sobre cada um dos indicadores disponibilizados pelas Estatísticas de processos:

- 
**Tempo de atendimento (TA):** O tempo de atendimento é o intervalo entre a abertura de uma solicitação até a sua conclusão. Também são apresentados os tempos de atendimento mínimo (TA min.) e máximo (TA máx.) de uma solicitação no período analisado.

- 
**Tempo médio de atendimento (TMA):** É a média dos tempos de atendimento das solicitações do período.

- 
**Tempo de execução (TE)**: Esse trata-se do tempo total de execução das tarefas de um processo, o intervalo entre atribuição das tarefas até a finalização das mesmas.

- 
**Tempo médio de execução (TME):** É a média dos tempos de execução.

- 
**Eficiência:** A eficiência é calculada dividindo o tempo médio de execução (TME) pelo tempo médio de atendimento (TMA), sendo que, quanto maior o resultado melhor o desempenho.

1. 
**Tempo de fila (TF):** É o tempo que a solicitação ficou na fila aguardando a execução de tarefas, o tempo entre a criação da tarefa até a atribuição pelo dono.

1. 
**Tempo médio de fila (TMF):** É a média dos tempos de fila.

Agora, iremos consultar os detalhes dos indicadores do processo Liberação de Acessos em sua versão 28. Para isso, basta clicar sobre o registro contido na tabela versão do processo, conforme demonstramos abaixo:

### 

![detalhes_vers_oprocesso.gif](https://ajuda.sankhya.com.br/hc/article_attachments/42313279117463)

****

| Estatísticas de processos |
| --- |

Em seguida será aberta a tela com o detalhamento dos indicadores dessa versão do processo:

### 

![image__8_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279117847)

****

| Detalhamento Estatísticas de processos |
| --- |

A visão acima permite ao gestor realizar 4 tipos de análises diferentes, sendo elas:

1. O volume de entradas (solicitações abertas) e saídas (fechadas) no período avaliado.

1. Os usuários que mais abriram solicitações no período.

1. Na grade **"Solicitações"** avaliar os indicadores de desempenho em cada solicitação trabalhada pela equipe.

1. Verificar na grade **"Tarefas"** o desempenho das equipes em cada tarefa do processo. É possível constatar, por exemplo, que a tarefa **"Finalizar solicitação"** está com uma eficiência de 0,28, enquanto a tarefa **"Atender solicitação"** teve uma eficiência 0,19 no período avaliado.

[[voltar ao topo]](#top)

#### **Gestão de tarefas**

A visão disponibilizada ao gestor pela tela Gestão de tarefas permite que ele visualize como está a distribuição de tarefas pendentes de um processo entre os membros da equipe, possibilitando uma tomada de decisão tempestiva em caso de desvios. 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403797206935)

****

| Aplicação de filtros na Gestão de tarefas |
| --- |

É possível implementar personalizações relacionadas à Gerência de Processos. Para isso, a ação deve ser cadastrada na tabela TWFITAR. Um exemplo de personalização seria a partir de um botão de ação, para permitir que o gestor do processo possa atribuir ou desatribuir tarefas de um determinado usuário.

Na sequência, filtramos as solicitações abertas de 01/04/2021 à 27/04/2021 do processo de Liberação de Acessos, conforme a imagem abaixo:

### 

![image__11_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279118231)

****

| Gestão de tarefas |
| --- |

Na próxima imagem, trouxemos a visão completa das tarefas pendentes, atribuídas e não atribuídas, e a carga de tarefas dos membros da equipe. Dessa forma, é possível realizar 2 tipos de análises:

1. O volume de tarefas que estão na fila (não atribuídas) e atribuídas (que possuem dono).

1. Verificar o dimensionamento das atividades entre os membros da equipe.

### 

![image__14_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313279119383)

****

| Gestão de tarefas |
| --- |

Portanto, conseguimos visualizar que temos 96,7% de tarefas não atribuídas (sem donos), que representam 88 tarefas de um total de 91 tarefas.

[[voltar ao topo]](#top)

Conforme tratamos acima, as informações gerenciais do processo de Liberação de Acessos contidas no [Monitor de processos](#monitordeprocessos), [Estatísticas de processos](#estat%C3%ADsticasdeprocessos) e [Gestão de tarefas](#gest%C3%A3odetarefas) possibilitaram ao gestor realizar diversas análises para melhor gerir o desempenho de Liberação de Acessos. Dentre elas, podemos destacar as seguintes:

1. 
A identificação de tarefas pendentes em um determinado período que, em sua maioria, estavam pendentes na tarefa "**Finalizar solicitação" **(sem atribuição), com 96,7% de tarefas não atribuídas (sem donos), que representam 88 tarefas de um total de 91 tarefas. Essas informações podem embasar o gestor para tomar uma decisão específica para melhoria na execução dessa atividade e/ou distribuir melhor as atividades para os membros da equipe. 

1. 
Constatar que a tarefa Finalizar solicitação apresentou uma eficiência menor em relação à outra tarefa de usuário executada pelos colaboradores e um tempo médio de fila, consideravelmente maior em relação às outras tarefas do processo, de acordo com a imagem abaixo:
 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403797573399)

****

| Gestão de tarefas |
| --- |

 

1. 

Também conseguimos visualizar no gráfico de entradas x saídas que as entradas em grande parte do período analisado foram maiores do que as saídas, o que pode sinalizar um desvio ou alteração na demanda ou capacidade de concluir tarefas do processo nesse período:

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403790637463)

****

| Volume de entradas x saídas de solicitações |
| --- |

Assim, concluímos que as informações desse painel gerencial do SankhyaFlow permite ao gestor realizar diversas análises e avaliar constantemente se os acordos previamente definidos e baseados nos indicadores apresentados estão sendo alcançados pelas equipes e, a partir dessas análises, tomar as decisões apropriadas quando necessárias.

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Processo de Negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107733-Processos-de-Neg%C3%B3cio)
- [Gestores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107733-Processos-de-Neg%C3%B3cio#abagestores)