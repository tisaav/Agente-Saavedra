# Como calcular as férias do trabalhador intermitente?

> **Módulo:** Pessoas+ | **Subseção:** Contrato Intermitente  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39012829384599-Como-calcular-as-f%C3%A9rias-do-trabalhador-intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39012829384599-Como-calcular-as-f%C3%A9rias-do-trabalhador-intermitente)  
> **ID:** `39012829384599` | **Última Atualização:** 2026-09-27T14:42:27Z

---

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Cálculos
**ID da Tela:** br.com.sankhya.rh.CalculoIndFolha

 

## **Descrição e Usabilidade**

No contrato de trabalho intermitente, o trabalhador possui direito ao **gozo de férias a cada 12 meses de vínculo**, conforme previsto na legislação trabalhista. Entretanto, diferentemente do contrato tradicional, o **valor das férias é pago de forma antecipada**, proporcionalmente, **junto ao pagamento da folha intermitente**, sempre que o trabalhador realiza uma prestação de serviço.

Por esse motivo, quando chega o momento do gozo das férias, o sistema realiza apenas o **registro do período de descanso**, sem gerar pagamento adicional ao trabalhador. Ainda assim, é necessário realizar o **cálculo da folha de férias**, pois essa rotina é utilizada pelo sistema como gatilho para atualizar informações relacionadas ao período aquisitivo e à programação de férias.

No cálculo das férias do trabalhador intermitente será apresentado **apenas um evento demonstrativo**, sem incidência no líquido e sem incidência em tributos.

### **1. Descrição da Funcionalidade**

A rotina de férias para trabalhadores intermitentes permite registrar o **período de gozo das férias** no sistema, mantendo o controle dos períodos aquisitivos e garantindo o correto funcionamento das rotinas relacionadas às férias.

Mesmo que o pagamento já tenha sido antecipado na folha intermitente, é necessário realizar o **cálculo da folha de recibo de férias**, pois diversas rotinas do sistema utilizam esse cálculo como **gatilho para geração das informações de férias**, como:

- 

programação de férias;

- 

controle do período aquisitivo;

- 

registro histórico do gozo de férias.

### **2. Pré-requisitos**

Antes de registrar as férias de um trabalhador intermitente, verifique se:

- 

o trabalhador possui **contrato de trabalho intermitente ativo**;

- 

existe **período aquisitivo de férias cadastrados no sistema**;

- 

as **folhas intermitentes foram calculadas corretamente ao longo do período aquisitivo**.

### **3. Jornada de Uso**

Para registrar as férias do trabalhador intermitente no sistema, siga as etapas abaixo.

#### **

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315063870871)

 Parametrização do evento de férias**

Embora o pagamento das férias já tenha sido antecipado na folha intermitente, o sistema exige o cálculo da folha de férias para registrar o período de gozo.

Para isso, deve existir um **evento demonstrativo configurado para esse cálculo na tela Eventos **(Pessoal+ > Cadastros), com:

- 

**Identificação: ****199 – Líquido Mensal Intermitente**.

- 

Esse evento será utilizado apenas como **demonstrativo**, sem incidência na base líquida ou em tributos.

- 

Ele deve possuir **regra de cálculo** para:

  - 

**folha de férias**

  - 

**folha intermitente**

![eventodemferiasintermitente.gif](https://ajuda.sankhya.com.br/hc/article_attachments/40493062824983)

1. 

**Fórmula do evento**: *IF((QueFuncionario.CODCATEGESOCIAL = 111) AND (&TIPFOL='F'), 0.01,0)*

Essa fórmula garante que o evento seja exibido apenas para **colaboradores com categoria eSocial 111 (contrato intermitente)** no cálculo da folha de férias.

#### 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315063871639)

 **Consulta de Período Aquisitivo**

1. Acesse a tela **Consulta de Férias** (Pessoal+ > Rotinas Folha).

1. Informe a **Empresa** no painel de filtros, clique em **Aplicar.**

1. 

Pesquise pelo **trabalhador** e verifique o **Período aquisitivo** no canto inferior direito do card.

![CONSFERINTER.png](https://ajuda.sankhya.com.br/hc/article_attachments/39036885774999)

#### **

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315036683927)

 Requisição de férias**

1. 

Acesse a tela **Requisições **(Pessoal+ > Rotinas Folha).

1. 

Clique no botão** Requisições**.

1. 

Informe:

  - 

Data de **Início das férias**;

  - 

a quantidade de **Dias de férias**.

1. 

Confirme a solicitação para salvar a requisição.

![reqisferias-intermitente.gif](https://ajuda.sankhya.com.br/hc/article_attachments/39037036910359)

#### **

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315063874455)

 Aprovação da requisição**

1. Acesse o **Gerenciador de DP** (Pessoal+ > Rotinas Folha).

1. 

Na **Timeline**, localize a requisição de férias do trabalhador e aprove.

![aprovreqferias-intermitente.gif](https://ajuda.sankhya.com.br/hc/article_attachments/39037108171799)

#### **

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315036684951)

 Cálculo da folha de férias**

Após a requisição, é necessário realizar o cálculo da folha de férias por meio da tela **Cálculos** (Pessoal+ > Rotinas Folha).

Esse cálculo é utilizado pelo sistema para atualizar:

- 

a **programação de férias**;

- 

o **período aquisitivo**;

- 

o **histórico do gozo de férias**.

No caso do trabalhador intermitente, o cálculo gera **somente um evento demonstrativo**, sem impacto financeiro.

********

****************[cadastro do funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)

****

| ⚠️ Atenção Se o trabalhador estiver sendo alterado da categoria Intermitente (111) para CLT (101), calcule as férias referentes ao período de direito adquirido enquanto intermitente antes de salvar a alteração da categoria no . O sistema não realiza esse cálculo automaticamente após a alteração da categoria. |
| --- |

![calculoferiasintermitente.gif](https://ajuda.sankhya.com.br/hc/article_attachments/40493641009687)

Após efetuar o cálculo da folha de férias, recomenda-se realizar as seguintes etapas:

- 

**Enviar ou disponibilizar o Aviso de Férias**, informando o período de gozo previamente acordado entre empregador e empregado.

- 

**Disponibilizar o holerite (recibo de férias)** ao trabalhador para consulta ou registro.

![emissaodocferintermitente.png](https://ajuda.sankhya.com.br/hc/article_attachments/40493641010327)

1. 

Verificar se a **programação de férias foi atualizada corretamente** no sistema.

![novoperaquifer-intermitente.png](https://ajuda.sankhya.com.br/hc/article_attachments/39037605312663)

1. 

Verificar se o período de férias foi lançado automaticamente no histórico de ocorrências do trabalhador.

![ferias-ocorrencias-intermitente.png](https://ajuda.sankhya.com.br/hc/article_attachments/39038159186455)

#### 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315036685335)

** Envio ao eSocial**

1. 

Acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha) para gerar e enviar o evento **S-2230 – Afastamento Temporário**.

Nesse evento deve ser informado o **motivo de afastamento correspondente a férias**.

Para o trabalhador intermitente ocorre uma particularidade:

  - 

O **pagamento das férias já foi antecipado** nas folhas intermitentes anteriores.

  - 

O envio ao eSocial ocorre **apenas para registrar o período de gozo das férias**.

Portanto, **não há envio de valores de férias**, apenas o registro do afastamento.

### **4. Pontos de Atenção**

- 

O trabalhador intermitente **possui direito ao gozo de férias a cada 12 meses**, conforme previsto na legislação.

- 

A legislação permite que as férias sejam divididas em até **três períodos**, desde que haja acordo entre empregador e empregado.

- 

Durante o período de férias, **o trabalhador não pode ser convocado para prestar serviços ao mesmo empregador**.

- 

No contrato intermitente, **o valor das férias já é pago antecipadamente na folha intermitente**, proporcionalmente às horas ou dias trabalhados. Por isso o cálculo de férias gera apenas **evento demonstrativo**.

- 

Mesmo sem pagamento adicional, é necessário realizar o **cálculo da folha de férias**, pois outras rotinas do sistema dependem desse processamento.

- 

Após o gozo das férias, o sistema **criará automaticamente um novo período aquisitivo**.

### **5. Dicas de Usabilidade**

- 

Verifique sempre se o trabalhador possui **período aquisitivo criado no sistema** antes de registrar as férias.

- 

Confirme se o **evento demonstrativo está configurado corretamente**, garantindo que o cálculo da folha de férias seja processado sem impacto financeiro.

- 

Utilize a tela de **Consulta de Férias** para acompanhar a programação e o histórico de férias do trabalhador.

- 

Caso o cadastro do funcionário tenha sido importado de outro sistema, pode ser necessário **criar manualmente o período aquisitivo inicial**.

- 

Após registrar as férias, valide se o sistema **criou corretamente o novo período aquisitivo**.

## **Artigos Relacionados**

- 

[Contrato de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38961120003095)

- 

[Cadastro do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38962184136215)

- 

[Convocação de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38968450402455)

- 

[Aceite e Comparecimento da Convocação Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38986155986071)

- 

[Cálculo da Folha do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38988468841623)

- 

[Rescisão do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215)


---

### 🔗 Links e Referências Internas:

- [cadastro do funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Contrato de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38961120003095)
- [Cadastro do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38962184136215)
- [Convocação de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38968450402455)
- [Aceite e Comparecimento da Convocação Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38986155986071)
- [Cálculo da Folha do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38988468841623)
- [Rescisão do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215)