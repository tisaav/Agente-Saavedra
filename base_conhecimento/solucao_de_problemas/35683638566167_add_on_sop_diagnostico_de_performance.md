# Add-on SOP Diagnóstico de Performance

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35683638566167-Add-on-SOP-Diagn%C3%B3stico-de-Performance](https://ajuda.sankhya.com.br/hc/pt-br/articles/35683638566167-Add-on-SOP-Diagn%C3%B3stico-de-Performance)  
> **ID:** `35683638566167` | **Última Atualização:** 2026-07-22T14:24:53Z

---

### **Visão Geral**

O Add-n "**SOP Diagnóstico de Performance**" está disponível no [Marketplace](https://marketplace.sankhya.com.br/vitrine). Essa tela foi desenvolvida para facilitar a análise de performance e identificação de possíveis configurações que podem impactar o desempenho do sistema Sankhya. É composto por quatro abas principais (Performance, Parâmetros, Diagnóstico e Suspeitos) que apresentam informações consolidadas sobre a infraestrutura necessária, configurações do sistema e personalizações implementadas.

 

### **Objetivo**

O Add-on **tem como objetivo ser um facilitador de análise que: **

- 

Consolida informações relevantes sobre volume de transações e movimentações;

- 

Apresenta cálculo estimado de requisitos de infraestrutura baseado no volume atual;

- 

Exibe parâmetros do sistema que podem impactar a performance quando mal configurados;

- 

Mostra estatísticas sobre personalizações e logins de usuários;

- 

**Apoia** consultores e técnicos na análise de demandas relacionadas a lentidão e performance;

- 

**Orienta** sobre configurações que merecem atenção durante investigações de performance.

⚠️ **Importante**: O Add-on é uma ferramenta de **apoio à análise**, não substitui a expertise técnica do consultor responsável pela investigação de problemas de performance. Também ele **não **tem como objetivo apontar problemas ou realizar diagnósticos automáticos definitivos. 

 

### **Público-Alvo**

#### **Responsáveis pela Instalação**

- 

**Consultores do Service Desk**: responsáveis por atender tickets relacionados à lentidão e performance;

- 

**Consultores de Implantação**: que desejam apoiar o cliente na análise preventiva de performance;

- 

**Clientes**: podem solicitar a liberação do Add-on no Marketplace, visualizar e analisar as informações após o Add-on estar instalado.

###  

### **Instalação**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35683638548247)

 **Para instalar acesse o [Marketplace](https://marketplace.sankhya.com.br/vitrine) Sankhya e pesquise por "**SOP Diagnóstico de Performance"**. Clique em adquirir e aguarde a liberação por parte do time responsável. Logo após liberação o botão será liberado para instalação. 

 

### **Funcionalidades**

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428197527)

 Aba Performance**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Objetivo**

Calcular e apresentar os requisitos de infraestrutura necessários baseados no volume de transações dos últimos 3 meses.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Métricas Analisadas**

1. 

**Pedidos de Venda**

  - 

Média mensal de pedidos de venda (últimos 3 meses)

  - 

Score calculado baseado na tabela:

    - 

>40.000: Score 400

    - 

>6.000: Score 300

    - 

>1.300: Score 200

    - 

≤1.300: Score 100

1. 

**Notas Fiscais de Venda**

  - 

Média mensal de NF de venda emitidas

  - 

Score calculado:

    - 

≥38.001: Score 570

    - 

>5.000: Score 320

    - 

>800: Score 220

    - 

≤800: Score 120

1. 

**Itens por Nota**

  - 

Média de itens por nota fiscal

  - 

Score calculado:

    - 

>60: Score 581

    - 

>40: Score 330

    - 

>15: Score 230

    - 

≤15: Score 130

1. 

**Movimentações Contábeis**

  - 

Média mensal de lançamentos contábeis

  - 

Score calculado:

    - 

≥550.001: Score 440

    - 

>20.000: Score 340

    - 

≥2.001: Score 240

    - 

≤2.000: Score 140

1. 

**Movimentações Financeiras**

  - 

Média de títulos financeiros (origem 'F', não provisórios)

  - 

Score calculado:

    - 

≥15.001: Score 450

    - 

>6.000: Score 350

    - 

>1.000: Score 250

    - 

≤1.000: Score 150

1. 

**Livros Fiscais**

  - 

Média de registros em livros fiscais

  - 

Score calculado:

    - 

≥300.001: Score 460

    - 

>30.000: Score 360

    - 

>2.000: Score 260

    - 

≤2.000: Score 160

1. 

**Usuários Ativos**

  - 

Média de usuários únicos com login

  - 

Score calculado:

    - 

>300: Score 470

    - 

>100: Score 370

    - 

≥16: Score 270

    - 

<16: Score 170

1. 

**Integrações** (necessário clicar sobre o card e informar manualmente)

  - 

Quantidade de integrações habilitadas

  - 

Score calculado:

    - 

≥7: Score 480

    - 

≥5: Score 380

    - 

≥3: Score 280

    - 

≤2: Score 180

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Classificação Final**

O sistema soma todos os scores e classifica em uma das categorias abaixo. Ao clicar no botão **"Visualizar Requisitos Técnicos Completos"**, o sistema abre um PDF com especificações detalhadas da classificação correspondente. Abaixo segue o fluxo e a documentação clicando em cima de cada uma. 

- 

****[Classificação A](https://sankhya.com.br/wp-content/uploads/2025/10/recursoshardware-a.pdf): Score ≤ 1.150

- 

****[Classificação B](https://sankhya.com.br/wp-content/uploads/2025/10/recursoshardware-b.pdf): Score > 1.150 e ≤ 1.950

- 

****[Classificação C](https://sankhya.com.br/wp-content/uploads/2025/10/recursoshardware-c.pdf): Score ≥ 1.951 e < 2.751

- 

****[Classificação D](https://sankhya.com.br/wp-content/uploads/2025/10/recursoshardware-d.pdf): Score ≥ 2.751

###  

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428197527)

 Aba Parâmetros**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Objetivo**

Apresentar parâmetros do sistema que **podem** impactar a performance quando configurados inadequadamente, facilitando a identificação de configurações que merecem atenção durante análises.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Parâmetros Monitorados**

A aba exibe **18 parâmetros críticos** do sistema, cada um com:

- 

Valor **Esperado: **recomendado para melhor performance

- 

Valor **Atual: **configurado no sistema

- 

Indicador visual: verde = OK e vermelho = requer atenção

#####  

##### 
**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 ****Lista de Parâmetros Analisados:**

1. 

**QTDWARNPARLOAD** (100)

  - 

Quantidade de registros antes de exibir aviso

  - 

Alerta educativo para usuários

1. 

**DEBUGXMLSANNFE** (Desligado)

  - 

Debug de XML de NFe

  - 

Deve estar desligado em produção

1. 

**DEBUG_ENVMSGJOB** (Desligado)

  - 

Debug de jobs de mensagens

  - 

Manter desligado em produção

1. 

**INATSESSTIMEOUT** (2 a 30 minutos)

  - 

Timeout de sessões inativas

  - 

Crítico para liberação de recursos

1. 

**REFRESHCARDS** (≥60 segundos)

  - 

Intervalo de atualização de cards

  - 

Valores baixos geram overhead

1. 

**MAXRSLTSIZE** (≤2000)

  - 

Máximo de registros em consultas

  - 

Protege contra consultas excessivas

1. 

**USAPAGINACAOREG** (Ligado)

  - 

Paginação de registros

  - 

Fundamental para performance

1. 

**LIMITLINHASDASH** (≤10000)

  - 

Limite de linhas em dashboards

  - 

Impacta tempo de carregamento

1. 

**HABCOLTELPRO** (Desligado)

  - 

Coletor de telefones em processos

  - 

Ativar apenas se necessário

1. 

**HABILITATEAPP** (Desligado)

  - 

Tela de Estatística de Aplicação (Telemetria)

  - 

Ativar apenas para análises pontuais

1. 

**ENBLMONBD** (Desligado)

  - 

Monitoramento avançado de BD

  - 

Usar apenas para troubleshooting

1. 

**DIASVENCTFILE** (≤5 dias)

  - 

Dias para exclusão de arquivos temporários

  - 

Valores baixos mantêm sistema limpo

1. 

**DIASTOPSREC** (≤5 dias)

  - 

Dias no TOP de consultas

  - 

Reduz espaço e melhora performance

1. 

**DEBUGREINFSKW** (Desligado)

  - 

Debug de integração REINF

  - 

Desligar em produção

1. 

**GEREMAILMDDEBUG** (Desligado)

  - 

Debug de e-mails em massa

  - 

Alto impacto quando ligado

1. 

**MAXPAGRELATORIO** (≤1000)

  - 

Máximo de páginas em relatórios

  - 

Previne timeouts

1. 

**USESTPQUERY** (Desligado)

  - 

Uso de stored procedures

  - 

Alterar apenas com orientação técnica

1. 

**HABBATCHPROVFIN** (Ligado)

  - 

Processamento em lote de provisões

  - 

DEVE estar ligado para melhor performance

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Detalhes por Parâmetro**

Ao clicar em qualquer card de parâmetro, abre-se um modal detalhado contendo:

- 

**O que é**: explicação técnica do parâmetro

- 

**Impacto na Performance**: como afeta o sistema quando mal configurado

- 

**Avisos Importantes**: alertas específicos

- 

**Como Alterar**: passo a passo para ajustar o parâmetro

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336603010583)

 Aviso Crítico**: a aba de parâmetros **não aponta problemas definitivos**, apenas indica configurações que **podem** estar impactando a performance. Cada situação deve ser analisada individualmente pelo consultor responsável, considerando as especificidades do cliente.

 

#### **Aba Diagnóstico**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Objetivo**

Apresentar informações sobre utilização do sistema, personalizações implementadas e estatísticas do banco de dados para apoiar análises de performance.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Logins por Usuário Hoje**

Exibe uma tabela com:

- 

Código do usuário

- 

Nome do usuário

- 

Data (dia atual)

- 

Quantidade de logins realizados

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Utilidade**: 

Identifica usuários com múltiplos logins que podem indicar:

- 

Problemas de sessão

- 

Possíveis automações mal configuradas

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Estatísticas do Banco de Dados - Top 20 Tabelas**

Apresenta as 20 maiores tabelas do banco de dados com:

- 

Nome da tabela

- 

Data da última análise de estatísticas

- 

Quantidade de registros

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Indicadores**:

- 

🔴 **"NUNCA ANALISADA"**: Tabela sem estatísticas (crítico)

- 

Data antiga: Pode necessitar atualização de estatísticas

**Importância**: Tabelas sem estatísticas atualizadas podem causar:

- 

Planos de execução ineficientes

- 

Consultas lentas

- 

Uso inadequado de índices

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336603010583)

Alerta**: a falta de estatísticas é apenas **um dos fatores** que pode impactar performance. A atualização deve ser avaliada pelo DBA ou consultor responsável.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Personalizações do Cliente**

Exibe 6 tipos de personalizações implementadas:

1. 

**Cards e Dashboards** (TSIGDG)

  - 

Quantidade de cards e dashboards cadastrados

  - 

Impacto: Quanto mais complexos, maior o overhead

1. 

**Eventos Programáveis** (TSIEVP)

  - 

Scripts automatizados ativos

  - 

Impacto: Dependem da qualidade do código

1. 

**Ações Agendadas** (TSIAAG)

  - 

Tarefas programadas ativas

  - 

Impacto: Podem competir por recursos

1. 

**Consolidador de Dados** (TSICND)

  - 

Processos de consolidação ativos

  - 

Impacto: Processamento intensivo

1. 

**Regras de Negócios** (TGFRNG)

  - 

Customizações de processos ativos

  - 

Impacto: Variam conforme complexidade

1. 

**Campos Calculados** (TDDCAM)

  - 

Campos customizados com fórmulas

  - 

Impacto: Cálculos em tempo real

**Utilidade**: Identifica o **volume de personalizações** que podem estar impactando a performance, especialmente se:

- 

Não estão otimizadas

- 

Estão executando em horários inadequados

- 

Competem por recursos com processos críticos

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336448973079)

 Nota**: A quantidade de personalizações **por si só** não indica problema. A análise deve considerar a qualidade do código e a necessidade de cada customização.

 

#### **Aba Suspeitos**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Objetivo**

Apresentar informações sobre personalizações mais executadas no dia atual, facilitando identificar alguma job, ação agendada ou até mesmo campo calculado que esteja impactando. 

Nela temos o TOP 30 das mais executadas, nos trazendo a Descrição, Tipo, Entidade, Processo, Execuções, Erros, Tempo Médio (ms), Tempo Total (ms), Última Execução e Servidor.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336428198423)

 Tipos de Customização**

- EVENTO: Scripts acionados por eventos do sistema

- AÇÃO: Ações programadas para execução automática 

- CONSOLIDADOR: Processos de agregação de dados

- REGRA: Regras de negócio customizadas

- CAMPO: Campos calculados com fórmulas

- DASHBOARD: Painéis e visualizações personalizadas

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36336448973079)

 Nota**: Esta telemetria mostra as customizações mais executadas no dia atual. Customizações com alto número de execuções ou erros podem estar impactando a performance do sistema e devem ser investigadas.


---

### 🔗 Links e Referências Internas:

- [Marketplace](https://marketplace.sankhya.com.br/vitrine)
- [Classificação A](https://sankhya.com.br/wp-content/uploads/2025/10/recursoshardware-a.pdf)
- [Classificação B](https://sankhya.com.br/wp-content/uploads/2025/10/recursoshardware-b.pdf)
- [Classificação C](https://sankhya.com.br/wp-content/uploads/2025/10/recursoshardware-c.pdf)
- [Classificação D](https://sankhya.com.br/wp-content/uploads/2025/10/recursoshardware-d.pdf)