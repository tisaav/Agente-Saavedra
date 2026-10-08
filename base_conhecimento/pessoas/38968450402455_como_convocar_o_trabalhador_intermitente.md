# Como convocar o trabalhador intermitente?

> **Módulo:** Pessoas+ | **Subseção:** Contrato Intermitente  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38968450402455-Como-convocar-o-trabalhador-intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38968450402455-Como-convocar-o-trabalhador-intermitente)  
> **ID:** `38968450402455` | **Última Atualização:** 2026-09-27T14:41:13Z

---

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.ConvocacaoTrabalhoIntermitente

 

## **Descrição e Usabilidade**

A convocação de trabalho intermitente é a rotina utilizada para **registrar e gerenciar o chamado do trabalhador intermitente para prestação de serviço** em um determinado período.

De acordo com a legislação trabalhista, o empregador deve convocar o trabalhador **com antecedência mínima de três dias corridos** antes da data de início do trabalho. Após receber o chamado, o trabalhador possui **até um dia útil para responder**, podendo **aceitar ou recusar a convocação**. Caso não haja resposta nesse prazo, entende-se que a convocação foi **recusada**, sem que isso caracterize insubordinação.

No sistema, essa rotina permite registrar os dados da convocação, informar o período de trabalho e selecionar os trabalhadores que participarão da atividade, além de possibilitar o envio de e-mail de convocação.

 

### **1. Descrição da Funcionalidade**

A convocação permite registrar formalmente o **período de trabalho de um colaborador com contrato intermitente**, informando:

- 

empresa responsável pela convocação;

- 

período da prestação do serviço;

- 

local da prestação do trabalho;

- 

trabalhadores convocados;

- 

previsão de pagamento.

Essas informações são utilizadas posteriormente para **controle do trabalho realizado e cálculo da folha intermitente**.

É importante destacar que, no eSocial, **não existe mais evento específico para convocação**. O evento **S-2260 (Convocação para Trabalho Intermitente)** foi **excluído no eSocial simplificado**, portanto o sistema não gera pendências ou validações relacionadas a esse evento.

As informações de convocação e dias trabalhados agora devem ser enviadas no XML dos eventos de remuneração S-1200 (mensal) ou S-2299 (desligamento).

 

### **2. Pré-requisitos**

Antes de registrar uma convocação, verifique se:

- 

O colaborador está **ativo e com contrato intermitente válido**.

- 

A **admissão do trabalhador foi enviada ao eSocial por meio do evento S-2200**.

- 

Tem o acesso a tela **Convocação de Trabalho Intermitente. **Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

### **3. Jornada de Uso**

Para registrar uma convocação de trabalho intermitente, siga os passos abaixo.

- 

[Convocação de trabalho](#h_01KKH23S2HDXBX88653PCCBDH6)

- 

[Convocação do trabalhador](#h_01KKH25306EYME95WZMQXY5353)

- 

[Envio de e-mail da convocação para o trabalhador](#h_01KKH265NKGM9C7E7ST0YQA6BW)

![convocacao-intermitente.png](https://ajuda.sankhya.com.br/hc/article_attachments/38968792177687)

1. Acesse a tela **Convocação de Trabalho Intermitente **(Pessoal+ > Cadastros).

2. Informe a **Empresa**.

3. Clique em **Aplicar**.

 

#### 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315063154967)

  **Convocação de trabalho**

4. Clique no botão 

![botão Novo P+.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38968792181527)

 **Nova Convocação **e preencha as abas a seguir:

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38969393931543)

Aba Informações da Convocação**

![convocacao-intermitente1aba.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38969393937047)

Na seção **Informações da Convocação de Trabalho Intermitente**, preencha:

- 

**Descrição**: informe um nome ou identificação para a convocação.

- 

**Empresa**: este campo é preenchido automaticamente.

Caso o trabalho seja realizado fora das dependências da empresa, preencha o endereço na seção **Informações do Local de Trabalho Fora da Empresa.**

Após preencher os dados, clique em **Salvar**.

 

#### 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315036028439)

 **Convocação do trabalhador**

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38969393931543)

Aba Funcionários Convocados**

![convocacao-funcintermitente.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38985011454871)

Nesta aba são informados os trabalhadores que participarão da convocação.

1. 

Clique em **Adicionar Funcionário(s)**.

1. 

Preencha as informações da convocação:

  - 

**Data de Início**

  - 

**Data de Fim**

  - 

**Previsão de Pagamento**

1. 

No campo **Local da Prestação do Trabalho**, selecione onde o serviço será realizado.

Também é possível definir como o sistema considerará os dias trabalhados atravéz da opção **Considerar como dias trabalhados a carga horária?**:

- 

**Marcada:** o sistema utiliza a **carga horária cadastrada para o funcionário intermitente**.

- 

**Desmarcada:** o sistema considera **dias corridos** no período informado.

Na grade lateral direita serão exibidos os **funcionários disponíveis para convocação**, ou seja, aqueles que ainda não foram convocados para o mesmo período.

1. 

Clique sobre o **card do trabalhador desejado**.

1. 

Confira as datas da convocação.

1. 

Clique em **Confirmar**.

#### 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315063157527)

 **Envio de e-mail da convocação para o trabalhador**

![email-convocacao-funcintermitente.gif](https://ajuda.sankhya.com.br/hc/article_attachments/38985457226775)

Após adicionar o trabalhador, é possível encaminhar o chamado por e-mail.

1. 

Clique em **Ativa Seleção**.

1. 

Selecione o(s) funcionário(s) desejado(s).

1. 

Clique em **Encaminhar e-mail de convocação** e confirme.

### **4. Pontos de Atenção**

- 

O trabalhador intermitente deve ser convocado **com antecedência mínima de três dias** antes da data do trabalho.

- 

O funcionário possui **até um dia útil para responder** à convocação.

- 

Caso não haja resposta nesse prazo, a convocação será considerada **recusada**.

- 

A recusa do trabalhador **não caracteriza insubordinação**.

- 

Após **confirmar o envio do e-mail de convocação**, **não será possível editar dados ou remover os funcionários da convocação.**

### **5. Dicas de Usabilidade**

- 

Utilize uma **descrição clara na convocação** para facilitar a identificação futura.

- 

Antes de adicionar os funcionários, **revise o período de início e fim da convocação**, evitando ajustes posteriores.

- 

Utilize o envio de e-mail para **formalizar a comunicação da convocação ao trabalhador**.

## **Artigos Relacionados**

- 

[Contrato de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38961120003095)

- 

[Cadastro do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38962184136215)

- 

[Aceite e Comparecimento da Convocação Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38986155986071)

- 

[Cálculo da Folha do trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38988468841623)

- [Férias do Trabalhor Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39012829384599)

- 

[Rescisão do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215)


---

### 🔗 Links e Referências Internas:

- [Contrato de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38961120003095)
- [Cadastro do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38962184136215)
- [Aceite e Comparecimento da Convocação Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38986155986071)
- [Cálculo da Folha do trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38988468841623)
- [Férias do Trabalhor Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39012829384599)
- [Rescisão do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215)