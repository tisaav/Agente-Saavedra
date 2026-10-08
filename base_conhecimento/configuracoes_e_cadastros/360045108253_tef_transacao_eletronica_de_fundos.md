# TEF - Transação Eletrônica de Fundos

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108253-TEF-Transa%C3%A7%C3%A3o-Eletr%C3%B4nica-de-Fundos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108253-TEF-Transa%C3%A7%C3%A3o-Eletr%C3%B4nica-de-Fundos)  
> **ID:** `360045108253` | **Última Atualização:** 2026-07-29T13:54:47Z

---

Esta documentação visa atender os usuários do sistema de modo que estes possam realizar suas operações de prestação de serviço ou venda de mercadorias, com base em transações com cartão de crédito e/ou débito.

Por meio das configurações descritas abaixo, será possível efetuar o recebimento e o cancelamento de recebimentos de títulos correspondentes às notas de produtos e serviços via cartão de crédito e débito, tanto na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela), quanto na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), utilizando a integração via Pay&Go, SiTef ou Auttar.

Premissas:

- 

[Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394) (última versão disponível);

- 

Versão mínima do sistema 3.27 devidamente configurada;

- 

É necessário possuir a licença do Sankhya Om para o produto **"30601 - FINANCEIRO /W"**;

- 

Aquisição do produto junto à Administradora;

- 

Caso utilize Pay&Go: Integração (troca de arquivos) da NTK - Instalação/Configuração do Servidor Pay&Go e Pay&Go Client (responsabilidade NTK);

- 

Caso utilize SiTef: Integração (troca de arquivos) da SkyTef - Instalação/Configuração do Servidor da solução SiTef (responsabilidade SkyTef);

- 

Caso utilize Auttar:  Integração (WebSocket) da Auttar (Getnet/Santander) - Instalação/Configuração do CTFClient (responsabilidade Auttar).

Vejamos os detalhes acerca das configurações a serem realizadas no sistema, bem como seu consequente comportamento:

[Tipos de Transações Atendidas](#tiposdetransaesatendidas)[Funcionalidades](#funcionalidades)

[Restrições](#restries)[Preferências](#preferncias)

[Tipos de Título](#tiposdettulo)[Tipos de Negociação](#tiposdenegociao)

[Modelo de Impressão do Comprovante](#modelodeimpressodocomprovante)[Recebimento](#recebimento)

[Layout de Processamento de Arquivo](#layoutdeprocessamentodearquivo)[Conciliação de Cartões](#conciliaodecartes)

[Suporte Técnico](#suportetcnico)

|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

 

## Tipos de Transações Atendidas

Vejamos os tipos de transações atendidas (Operações TEF):

#### Crédito:

112 - À Vista;

113 - Crédito Parcelado Lojista (sem juros);

114 - Crédito Parcelado Administradora (com juros).

#### Débito:

101 - Débito;

103 - Débito Pré-datado;

104 - Débito Parcelado;

105 - Débito Parcelado com parcela à vista.

106 - Voucher

#### Cancelamento:

128 - Cancelamento;

128.1 - Cancelamento automático junto à Administradora de Crédito;

128.2 - Cancelamento (Administrativo) - Cancelamento apenas no ERP, ficando a responsabilidade do backoffice comunicar a Administradora de Crédito.

[[voltar ao topo]](#top)

## Funcionalidades

Nos pontos descritos abaixo, temos as principais funcionalidades comportadas por este processo:

#### Portal de Vendas / Central de Vendas

Realizar o recebimento da nota diretamente pela Central de Vendas, com a possibilidade de utilizar mais de um tipo de título, parte em débito, parte em crédito, por exemplo;

Efetuar a baixa automática do título após o recebimento.

#### Movimentação Financeira

Executar o recebimento de vários financeiros contendo diversos tipos de títulos (dinheiro/cheque/cartão de crédito/cartão de débito) ao mesmo tempo;

Realizar a baixa automática do(s) título(s) após o recebimento via TEF;

Efetuar o cancelamento das transações TEF efetivadas/autorizadas.

#### Conciliação de Cartão

Realizar a conferência das transações realizadas;

Executar a baixa automática de acordo com as transações recebidas pela Administradora de Crédito.

[[voltar ao topo]](#top)

## Restrições

A instalação/configuração do integrador (Auttar, Pay&Go ou Sitef) é de total responsabilidade do suporte técnico da respectiva administradora;

A integração permite o recebimento das bandeiras mapeadas pela administradora:

- 

Auttar - [Mapa de Cartões AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602474);

- 

Pay&GO - [www.ntk.com.br/tef](https://www.ntk.com.br/tef);

- 

Sitef - Atende mais de 270 bandeiras/serviços, para maiores informações é necessário entrar em contato com o suporte.

O produto poderá ter limitações de recebimento por bandeira (por exemplo, American Express) de acordo com o contrato realizado junto à administradora;

Demais tipos de operação não contempladas neste documento deverão ser previstas em implementações futuras;

A administradora responsável pelo recebimento deverá ser negociada junto à Administradora de Crédito (Santander, Cielo, Rede etc);

O Sankhya Om não se responsabiliza por indisponibilidade de comunicação entre o ERP e a administradora de crédito contratada.

[[voltar ao topo]](#top)

## Preferências

É essencial que o parâmetro **"URL do gateway (TEF) - TEFGATEWAYURL"** contenha o endereço que o Gateway do TEF responde as requisições:

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408402822039)

**Nota:** por padrão, o parâmetro já possui o endereço correto configurado.

Além disso, no parâmetro **"Gateway de recebimento com cartão (TEF) - TEFGATEWAY"** aponta qual administradora será utilizada:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408402887703)

[[voltar ao topo]](#top)

## Tipos de Título

No [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), determine na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) a **"Forma de pagamento**** TEF****"**; esta informação posteriormente irá auxiliar nas análises gerenciais. Configure também o campo **"Tipo de pgto para NFC-e / NF-e / CF-e"** com as opções 03-Cartão de Crédito ou 04-Cartão de Débito.

No [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#painelprincipal), campo **"****Subtipo"**, a categoria do tipo de título em questão, deve ser definido dentre as seguintes opções:

- Cartão de crédito;

- Cartão de débito.

Além disso, as marcações **"Utiliza no Fast Service?"** e **"Baixa Automática?"** da aba [Fast Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abafastservice), devem estar acionadas para os casos em que a baixa do título necessite acontecer automaticamente ao confirmar o recebimento.

Ainda no Cadastro de Tipos de Título, é necessário atentar-se para a aba [Preferências de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto):

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408402955799)

**Importante:** os campos desta aba serão habilitados para uso, caso os campos **"Tipo de pagto para NFC-e / NF-e / CF-e"** e **"Subtipo"** presentes na aba Geral e Painel Principal, respectivamente, do Cadastro de Tipos de Título, estejam definidos como **"Cartão de Crédito" **ou **"Cartão de Débito"**.

Você deve configurar todos os campos presentes na aba. A saber:

Determine no campo **"Operação CTF"** a operação primordial a ser realizada pelo TEF, de acordo com as seguintes opções:

- Voucher;

- Créd. à vista;

- Créd. Parcelado Administradora (com juros);

- Débito;

- Débito Parcelado com parcela à Vista;

- Débito Parcelado;

- Débito Pré-datado;

- Créd. Parcelado Lojista (sem juros).

Selecione no campo** "Tipo vencimento"** a data de vencimento do título, conforme as seguintes alternativas:

- Dia fixo;

- Hoje + Vencimento (data atual somando-a ao vencimento).

O campo **"Vencimento"** funciona em conjunto com a configuração realizada no campo Tipo vencimento. Se for selecionado Dia fixo informe aqui o dia do recebimento, caso você escolha Hoje + Vencimento informe a quantidade de dias que o sistema deve somar na data do recebimento/transação.

Informe a "**Qtd. parcelas" **a serem utilizadas nas transações com Cartão de Crédito. Sendo que, esta será carregada automaticamente no pop-up de recebimento.

Caso a marcação** "Receber antes de aprovar a nota"** esteja assinalada, na concretização de uma venda será apresentado um pop-up de recebimento com cartão para que o recebimento aconteça antes do envio da nota para a SEFAZ.

[[voltar ao topo]](#top)

## Tipos de Negociação

No [Cadastro de Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), na aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas), é necessário configurar uma parcela com um tipo de título correspondente à uma transação TEF.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408403050007)

**Importante:** ao confirmar uma nota por meio da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), para realizar o recebimento automático é necessário que a marcação **"Baixa na confirmação"** (também presente na aba Parcelas) esteja realizada.

[[voltar ao topo]](#top)

## Modelo de Impressão do Comprovante

É parte do processo realizar para os clientes a impressão de comprovantes de recebimento. Esta impressão acontece com base em um arquivo modelo previamente configurado e vinculado ao sistema. Vejamos:

 

#### Criação do modelo de comprovante

Na construção do modelo a ser utilizado, que deve ser no formato **".txt"**, você pode trabalhar com três variáveis que representam os três modelos de comprovantes gerados:

- 

**&cupomEstabelecimento**

- 

**&cupomCliente**

- 

**&cupomReduzido**

**Observação:** o layout do cupom reduzido é montado e retornado pela própria integradora, o sistema apenas o imprime.

Tem-se também a função **"moverLinhas"**, que será utilizada na centralização da impressão do comprovante. Esta função recebe dois parâmetros:

moverLinhas(string texto, int colunas)

onde,

string texto = texto a ser impresso

int colunas = quantidade de colunas para realização da tabulação à direita

Além disso, temos a função **"guilhotinaDaruma"**, que permitirá que sejam efetuados cortes dos comprovantes:

guilhotinaDaruma()

#### Vínculo do modelo de comprovante no sistema

Uma vez configurado o modelo de comprovante de recebimento, este será trabalhado no sistema, por meio do parâmetro **"Modelo para impressão de comprovantes TEF - MODIMPCOMPTEF"**, informe o nome do arquivo que foi criado na instrução anterior juntamente com sua extensão, por exemplo, modeloTEF.txt.

Além disso, o caminho correspondente ao diretório em que o modelo de comprovante foi salvo, deve ser inserido no parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**, por exemplo, C:\Modelo\

#### Exemplo de modelo de comprovante

Um modelo de comprovante pode ser elaborado associando as variáveis e funções descritas acima, de acordo com a necessidade e processo de cada empresa. Vejamos um exemplo de modelo criado e sua respectiva impressão:

![clip4524.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408403336855)

![clip4527.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408403261079)

Para que ocorra a impressão dos comprovantes, a impressora necessita estar configurada no cadastro de impressoras do Windows com a nomenclatura **"IMPRESSORATEF"**.

![clip5465.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/4408423544087)

**Importante:** a impressão de comprovantes foi validada a princípio somente no modelo de impressora Daruma DR800; este fato não caracteriza que outros modelos de impressora não poderão suportar esta demanda.

[[voltar ao topo]](#top)

## Recebimento

Para que as transações financeiras sejam processadas, é necessário que o aplicativo de recebimento "Emulador" esteja devidamente instalado e configurado na máquina/estação que irá executar a operação, ou seja, máquina/estação onde o Sankhya Om estiver sendo executado.

- 

**CTFClient (Auttar):** O aplicativo CTFClient da Auttar deve estar devidamente instalado e configurado.

**Importante:** a instalação e configuração deste aplicativo é de responsabilidade da AUTTAR, ou conforme negociação da empresa com os mesmos.

- 

**Pay&GO:** O aplicativo de servidor como também do Client da Pay&GO devem estar devidamente instalados e configurados.

![clip5469.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/4408403428887)

- 

**SiTef:** O aplicativo Client SiTef da SiTef deve estar devidamente instalado e configurado.

#### SitDemo - Console

![clip5412.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/4408403513239)

#### Emulador SitTef Client

![clip5415.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/4408403519639)

**Observação:** caso queira realizar determinada alteração em recebimentos com cartão na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), basta ligar o parâmetro **"Permite editar/excluir tít. receb. administrativo? - PERMEDITRECADM"**. Porém, é importante ressaltar que se não houver a conferência de lançamentos do cartão e baixa manual na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753), poderão ocorrer inconsistências nos lançamentos e/ou recebimentos.

[[voltar ao topo]](#top)

## Layout de Processamento de Arquivo

Para que ocorra o processamento dos arquivos de conciliação das transações TEF, é necessário criar a partir de um modelo já pré-configurado o layout de processamento nos formatos em que a Administradora de Crédito retorna. Na tela [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054), tem-se duas hipóteses:

1)Para o modelo Auttar a GetNet já disponibiliza um modelo pré configurado:

Nesta tela, por meio do botão **"Outras Opções..."** tem-se a opção **"Criar arquivo a partir de um modelo"**, que ao ser acionada abre um pop-up com esta mesma nomenclatura para escolha do modelo Auttar e criação do modelo.

2)Para as outras Administradoras (Pay&GO e SiTef) o layout deverá ser criado. Deste modo, a rotina de conciliação de cartões já pode ser utilizada.

É possível realizar a configuração para o processamento do arquivo de retorno de outras Administradoras, desde que as transações estejam registradas na tabela TEF (TGFTEF) e se encontrem nos padrões adequados. As variáveis disponíveis atualmente para identificação/processamento do arquivo de retorno são:

- NSU_ADQUIRENTE - NSU (Número Serial Único) gerado pela Autorizadora;

- QTD_PARCELAS - Quantidade de parcelas da venda, quando a venda for parcelada;

- •NRO_PARCELA - Número da parcela que está sendo paga;

- DT_MOVTO - Data do pagamento no formato DD/MM/AAAA;

- VLR_TRANSACAO - Valor total da transação em R$ no formato 9999999999999.99;

- VLR_PARCELA ou VLR_PARCELA_LIQ - Valor total pago da transação;

- VLR_TAXA_AUTORIZACAO - Taxa (R$) cobrada do cliente pela Autorizadora.

**Nota:** a configuração referente à posição das variáveis citadas acima respeitará a ordem a qual forem inseridas no layout. Deste modo, o campo com a sequência 1 corresponde a posição 1 do arquivo de retorno; o campo 2 corresponderá à posição 2 e assim sucessivamente. Sendo assim, é necessário verificar as posições de cada um dos campos a serem processados.

[[voltar ao topo]](#top)

## Conciliação de Cartões

O objetivo desta rotina é permitir de forma automatizada a realização da baixa e a conciliação bancária das movimentações financeiras que utilizam como forma de pagamento o cartão, seja ele de crédito ou de débito. Esse processo acontece com base em um extrato de pagamento, onde a operadora de cartão demonstra os valores repassados ao estabelecimento comercial considerando as operações de um determinado período. Vejamos abaixo as premissas para que este procedimento ocorra:

1)Possuir título(s) não baixados lançados no sistema, que estejam aguardando o processamento do arquivo para que a baixa seja realizada;

2)Realizar o preenchimento dos campos pertinentes a tela [Conciliação de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334);

![image__3_.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408403655191)

Ao clicar nos botões **"Prévia"**, **"Processar"** ou **"Log"**, a tela é direcionada para os detalhes do log executando a finalidade correspondente ao botão acionado; pode-se retornar aos dados da baixa, clicando no botão **"Processamento"**.

Ao clicar no botão Prévia, o sistema realiza uma antecipação dos dados do arquivo de retorno da Administradora e informa que o tipo é uma prévia.

![image__4_.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408403869975)

Caso exista algum erro no processamento do arquivo de retorno de cartão, a mensagem correspondente ao problema encontrado será apresentada na tela. São possíveis mensagens:

- 

Não foi possível processar o arquivo. A estrutura do layout não é adequada a estrutura do arquivo ou não foram encontrados os identificadores correspondentes.

- Não foi encontrado o NSU gerado pela Autorizadora (campo NSU_ADQUIRENTE).

- Campo NSU_ADQUIRENTE não configurado no layout.

- Não foram encontradas transações (TGFTEF) para o NSU {XXX}.

- Foram encontrados múltiplos títulos para o NSU {XXX}.

- Financeiro não encontrado.

- Título já foi baixado.

- O valor de baixa do título {XXX} está diferente do valor da transação {XX,XX}.

- O arquivo de retorno não foi encontrado.

- A empresa de baixa é obrigatória.

- A conta de baixa é obrigatória.

- O Tipo de Operação de baixa é obrigatório.

- O lançamento obrigatório.

- O layout de configuração é obrigatório.

[[voltar ao topo]](#top)

## Suporte Técnico

Abaixo são apresentados os meios para contato de cada administradora em caso de dúvidas ou problemas.

#### Pay&Go

Integração via troca de arquivos | [www.ntk.com.br](https://www.ntk.com.br)

Telefone: (11) 3040-9988

Isaque Alves - Desenvolvimento | Suporte Técnico

E-mail: [isaque@paygo.com.br](mailto:isaque@paygo.com.br) | suporte.desenv@ntk.com.br

Telefone: 11 3044-9988 | 0800 737 2255

#### SiTef

Integração via troca de arquivos | [www.skytef.com.br](http://www.skytef.com.br)

Telefone: (11) 2175-9500

Cláudia Paiva - Gerente de Contas

E-mail: claudia.paiva@skytef.com.br

Telefone: (11) 2175-9532 | (11) 2175-9500 | (11) 4550-1450 | (11) 94508-6306

Henrique Lissoni - Suporte Técnico

E-mail: henrique.lissoni@skytef.com.br | suporte.tef@skytef.com.br

Telefone: (11) 2175-9501 | (11) 2175-9500 | (11) 4550-1450

#### Auttar

Integração via WebSocket - [www.auttar.com.br](https://www.auttar.com.br)

Telefone: 4003-5251

Ricardo Vargas - Comercial

E-mail: ricardo.vargas@auttar.com.br

Telefone: (51) 99142-0985 | (51) 3455-9513

Vitor Menezes - Operações

E-mail: vitor.menezes@auttar.com.br

Telefone: (51) 4003-1680 | (51) 4020-4005  | *Opção-3

[[voltar ao topo]](#top)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16807818673687)

 Acesse também:

[Integração com TEF AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873)


---

### 🔗 Links e Referências Internas:

- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)
- [Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394)
- [Mapa de Cartões AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602474)
- [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)
- [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#painelprincipal)
- [Fast Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abafastservice)
- [Preferências de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto)
- [Cadastro de Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)
- [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)
- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)
- [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054)
- [Conciliação de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334)
- [Integração com TEF AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873)