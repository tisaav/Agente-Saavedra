# Botão Roteiro - Processo Produtivo - Nova

> **Módulo:** Produção | **Subseção:** Produção/W - Nova  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360058453293-Bot%C3%A3o-Roteiro-Processo-Produtivo-Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058453293-Bot%C3%A3o-Roteiro-Processo-Produtivo-Nova)  
> **ID:** `360058453293` | **Última Atualização:** 2026-07-29T16:01:05Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42314911749911)

 Módulo: **Produção > Cadastros > Processo Produtivo - Botão Roteiro
```

O objetivo do roteiro em um [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova), é determinar como e quando as atividades devem acontecer no decorrer do processo. A utilização de uma ferramenta de modelagem de processos, possibilita um maior detalhamento destes processos, permitindo um maior controle de suas operações de manufatura.

Através do botão **"Roteiro"**, localizado na barra de navegação, é possível acessar a ferramenta de modelagem **"BPMN 2.0"**. Ao acioná-lo, será aberta a tela para confecção da programação do Processo Produtivo. Nesta tela, você pode configurar o roteiro de produção, editar o desenho do processo, configurar atividades, gateways, eventos e transições.

**Importante:** ao abrir o [Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109793-Bot%C3%A3o-Roteiro) do [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo) que foi criado em flex no Roteiro layout HTML5 pela primeira vez, será apresentada a mensagem abaixo: 

***"O Roteiro do Processo Produtivo foi criado na tela 'Processo Produtivo', ao abri-lo na tela 'Processo Produtivo - Nova' o diagrama BPMN do processo produtivo será convertido, e não poderá ser editado na tela 'Processo Produtivo' somente visualizado, pois existem recursos na tela 'Processo Produtivo - Nova' que não existem na tela 'Processo Produtivo'. Deseja continuar?"***

[Barra Superior](#barrasuperior)                                                                           [Palheta de Elementos](#palhetadeelementos)     

[Folha de Desenho](#folhadedesenho)                                               

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360096091414)

## 
Barra Superior

A barra superior da tela é composta por algumas funções que irão auxiliar consideravelmente durante a construção do roteiro.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360098387633)

Acionando o botão 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/360098387653)

 **"Voltar"**, será retornado o painel principal de exibição do Processo Produtivo.

Utilizando o botão **"Publicar"**, o Sankhya Om realizará o lançamento do fluxo de processo na estrutura interna de Workflow do sistema, além de efetuar algumas validações relacionadas à configuração do procedimento.

[[voltar ao topo]](#top)

## 
Palheta de Elementos

Note no lado esquerdo da tela, uma palheta de elementos, que traz consigo três divisões, onde cada uma delas contém seus elementos e os respectivos tipos. 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/360096092014)

Abaixo, trouxemos detalhadamente sobre cada uma das divisões nos tópicos a seguir:

[Atividades](#atividades)                                          [Eventos](#eventos)                                          [Gateweys](#gateweys)

## 
Atividades

Na configuração de atividades, temos os seguintes elementos:

![Botão Criar Atividade de Usuário FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16620688473495)

 **Atividade de Usuário:** trata-se de uma atividade a ser executada por uma pessoa (usuário do sistema). Será apresentada na lista tarefas (Operações de Produção, ou Apontamento de Produção) dos usuários candidatos executantes.

![Botão Criar Atividade de Serviço FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16620794016919)

 **Atividade de Serviço:** diz respeito à uma tarefa do sistema que realiza um serviço disponível. Temos atributos especiais que determinam o nome do serviço que será solicitado, os parâmetros de entrada e, opcionalmente, a variável da instância onde o resultado será gravado.

**Observação: **o sistema não está preparado para contabilizar na programação das OP's do MRP, o tempo de execução de Atividades de Serviços incluídas no roteiro do Processo Produtivo. Assim, as atividades de serviços são iniciadas e encerradas automaticamente com o mesmo horário, permanecendo com o tempo de execução igual a 0, mesmo que na composição do produto seja configurado tempo de atravessamento na atividade de serviço.

**Nota:** caso queira fazer anotações nas Atividades, para salvar as informações é necessário mover alguma outra atividade dentro do Roteiro ou clicar no botão **"Salvar"** dessa atividade para que essas informações sejam salvas no banco de dados.

[[voltar ao subtítulo]](#palhetadeelementos)

## 
Eventos

Nesta divisão, são disponibilizados os eventos que podem ser utilizados em todo Processo Produtivo. Vejamos sobre cada um deles:

![Botão Criar Evento de Início FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621138790295)

 **Evento de Início:** aqui, você inicia um fluxo de processo sem especificação de nenhum fato particular, para começar o processo.

![Botão Criar Evento de Fim FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621099819415)

 **Evento de Fim:** este evento finaliza o fluxo do processo, independente da existência de fluxos paralelos em execução.

![Botão Criar Apontamento Parcial FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621191192215)

 **Apontamento Parcial:** trata-se de um evento somente de borda. Um fluxo intermediário de processo será iniciado quando se realizar um apontamento parcial na operação. Quando a atividade possuir este evento anexado, o botão **"Transferência Parcial"** será habilitado na aba **"Apontamento"** possibilitando o controle do apontamento/transferência parcial da Ordem de Produção.

**Observação:** quando este evento estiver antes de um Gateway de junção, será necessário que uma mesma quantidade de PA chegue até o Gateway, por meio de todas as demais transições de entrada do mesmo, para que o sistema dê sequência ao fluxo do processo.

![Botão Criar Controle de Qualidade FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621252307607)

 **Controle de Qualidade:** este é um evento apenas de borda, onde se dá partida em um fluxo intermediário de processo referente a um **"Ciclo de Controle de Qualidade"**. Quando a atividade possuir este evento adicionado, o botão **"Iniciar Ciclo"** será disponibilizado na aba **"Controle de Qualidade"**, permitindo assim, que se tenha controle sobre a inicialização do ciclo de controle de qualidade.

![Botão Aguardar PI FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621442638359)

**Aguardar PI:** um fluxo intermediário de processo será introduzido com dependência dos produtos intermediários vinculados ao evento, ou seja, quando as Ordens de Produção do PI's em questão forem finalizadas.

[[voltar ao subtítulo]](#palhetadeelementos)

## 
Gateways

Esta aba está destinada à configuração dos Gateways no Processo. Abaixo, descrevemos as funcionalidades disponíveis:

![Botão Gateway Exclusivo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621703427991)

 **Exclusivo:** trata-se de gateway condicional, onde apenas um fluxo será executado. A junção segue o fluxo normalmente.

![Botão Gateway Paralelo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621829467927)

 **Paralelo:** esse é um gateway incondicional, ou seja, todos os fluxos serão executados. A junção irá esperar todos os fluxos chegarem para então prosseguir.

![Botão Gateway Inclusivo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621862171543)

 **Inclusivo:** assim como os anteriormente citados, temos aqui um gateway condicional onde um ou mais fluxos serão executados. A junção segue juntamente ao primeiro fluxo que chegar, ignorando os outros. 

![Botão Gateway Complexo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621876886679)

 **Complexo:** neste gateway condicional, um ou mais fluxos serão executados, de forma similar ao **"Inclusivo"**. A junção possui uma condição para determinar qual e quando o fluxo irá seguir.

[[voltar ao subtítulo]](#palhetadeelementos) [[voltar ao topo]](#top)

## 
Folha de Desenho

Depois de conhecidas as funcionalidades disponíveis na Palheta de Elementos, temos a Folha de Desenho, que é o espaço destinado à construção do Fluxo de Processo Produtivo. Os elementos aqui são adicionados clicando-se sobre os mesmos e arrastando até a Folha de Desenho.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360098396113)

Através de um clique com o mouse sobre um elemento, é possível executar algumas ações sobre o mesmo. São elas:

![Botão Remover FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621978016279)

 **Remover:** através desta opção, você poderá remover o elemento selecionado do desenho.

![Botão Conectar usando Sequência FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16621986211991)

 **Conectar usando Sequência:** permite a realização da ligação do elemento selecionado com outro elemento do desenho. Uma flecha de ligação é criada no acionamento desse botão, para que este seja ligado a outro elemento (clicando sobre o segundo elemento desejado).

![Botão Alterar tipo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16622041224983)

 **Alterar tipo:** esta opção possibilita que você altere o tipo do elemento em questão no desenho: Configuração de Atividade, Configuração de Transação e Configuração de Evento.

No Roteiro do Processo Produtivo, podemos criar o desenho em diagrama BMPN de forma bastante ágil, observe no gif abaixo como fazemos:

![gif13.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500001148861)

**Observação:** ao clicar na Folha de Desenho, será exibida na lateral superior direita a opção de criação de nova raia:

![gif14.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360102154173)

Através de um duplo clique na lateral esquerda da raia, podemos inserir um nome para ela:

![gif15.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360102154233)

**Observação:** para obter uma melhor performance nas ligações entre as atividades e eventos na geração do Roteiro, deve-se definir no parâmetro **"Validar e limpar dados do Roteiro antes da visualização - LIMPAROTEIROPP"** como ocorrerá o versionamento, dentre as seguintes opções:

- **Não**: não realiza nenhuma alteração;

- **Sim, das tarefas e gateways**: limpa somente as tarefas de usuário e gateway;

- **Sim, das tarefas, gateways e ligações**: limpa tarefas de usuário, gateway e as setas de conexão.

[[voltar ao topo]](#top)

## 
Configuração de Atividades / Configuração de Transições

Depois de ajustado o fluxo do Processo Produtivo, é necessário a realização da Configuração das Atividades, bem como a Configuração das Transições. Acesse os detalhes sobre cada uma destas configurações por meio dos link's [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058460853-Configura%C3%A7%C3%A3o-de-Atividades-Nova) e [Configuração de Transições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova).

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova)
- [Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109793-Bot%C3%A3o-Roteiro)
- [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo)
- [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058460853-Configura%C3%A7%C3%A3o-de-Atividades-Nova)
- [Configuração de Transições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056603434-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es-Nova)