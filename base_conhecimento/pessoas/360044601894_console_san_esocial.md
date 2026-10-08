# Console San eSocial

> **Módulo:** Pessoas+ | **Subseção:** Antes de Começar no eSocial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601894-Console-San-eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601894-Console-San-eSocial)  
> **ID:** `360044601894` | **Última Atualização:** 2026-09-26T00:46:16Z

---

O [eSocial](https://www.gov.br/esocial/pt-br) (Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas) é uma base de dados do governo federal que reunirá as informações trabalhistas, previdenciárias, tributárias e fiscais da utilização de mão de obra onerosa em todo o território nacional. As informações armazenadas no eSocial deverão atender às necessidades dos órgãos governamentais usuários do sistema no limite de suas respectivas competências, formando uma base única de dados.

Tem-se abaixo os órgãos envolvidos:

- 

Receita Federal do Brasil;

- 

Ministério do Trabalho e Emprego;

- 

Ministério da Previdência Social;

- 

Instituto Nacional do Seguro Social;

- 

Justiça do Trabalho;

- 

Caixa Econômica Federal.

O San eSocial é o programa que executará a extração destas informações na empresa. Bem como a assinatura em lote e o envio dos arquivos.

#### ****
[Passos iniciais](#passosiniciais)
[Executável de Instalação para Windows](#executveldeinstalaoparawindows)
[Descompactação dos Arquivos no Diretório de Destino](#descompactaodosarquivosnodiretriodedestinowindowsoulinux)
[Botões no topo da tela](#botesnotopodatela)
[Envio das Informações](#enviodasinformaes)
[San-eSocial na Central do eSocial](#h_01KJAGZA8FBAJ0HFZGC3TNRV0Q)

| Funcionalidades do San eSocial |
| --- |
|  |
|  |
|  |
|  |
|  |
|  |

### 
******Passos iniciais**

A utilização deste programa dependerá dos seguintes procedimentos:

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/29207799714327)

 Realizar a baixa do arquivo no site [Sankhya](http://downloads.sankhya.com.br/) na parte de Aplicações, de acordo com seu respectivo sistema operacional;

![central-douwnloads-sanesocial.gif](https://ajuda.sankhya.com.br/hc/article_attachments/35936115451671)

 

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/29207799714327)

 Instalar o programa San eSocial no servidor ou máquina local.

**Importante:** para clientes que são Cloud, a instalação deve ocorrer no servidor do banco de dados (não é local). Além disso, para instalar o programa, deve-se solicitar o DBA.

Essa instalação é realizada de duas maneiras, nos tópicos seguintes tem-se a descrição e procedimentos de cada uma delas.

[[voltar ao topo]](#top)

### 
******Executável de Instalação para Windows**

Através deste método, o programa é configurado para iniciar automaticamente ao ligar a máquina.

Ao executar o processo de instalação através de um duplo clique sobre o arquivo, é apresentado o **"Assistente de Instalação do SanEsocial"** com seu passo a passo:

![assistente-instalacao-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35936341283351)

Ao clicar em **"Avançar"** indica-se a pasta onde será armazenado o San eSocial:

![pasta-destino-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35936572450327)

Neste passo, é apontada a pasta do menu onde serão criados os atalhos do programa:

![atalhos-sanesocial-instalacao.png](https://ajuda.sankhya.com.br/hc/article_attachments/35936572453015)

Em seguida, é solicitada a seleção dos detalhes a respeito da forma pela qual os serviços precisam ser instalados. A opção **"Instalar o serviço "sanesocial-service""** quando marcada, indicará que o San eSocial será implantado ao final da instalação.

![terminar-instalacao-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35936525515031)

Ao final, a instalação é concluída com sucesso e requisita-se o fechamento do programa de instalação.

[[voltar ao topo]](#top)

### 
******Descompactação dos Arquivos no Diretório de Destino (Windows ou Linux)**

Utilizando-se desta forma de instalação, será preciso configurar o serviço para que a inicialização seja automática.

![arquivo-compactado-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35936658483607)

Após descompactar o arquivo, por meio de um duplo clique sobre o arquivo, executa-se o "sanesocial-service" para dar início ao serviço.

![descompactacao-san-esocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35936721532183)

[[voltar ao topo]](#top)

### 
******Configurando o Console**

Realizada a inicialização do serviço por uma das formas apresentadas acima, o próximo passo é acessar o console para configurar o certificado e o banco de dados. Através do endereço [http://localhost:8778/index.html](http://localhost:8778/index.html), tem-se o acesso à página inicial do San eSocial onde se informa o usuário "admin" e a senha "admin" para executar o login no sistema.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16747223033495)

 O usuário e a senha "admin" são padrões do sistema. Deste modo, não podem ser alterados.

Ao executar o login, são apresentadas na tela as abas responsáveis pelas configurações pertinentes ao sistema. Sendo elas:

[Aba Certificados](#abacertificados)[Aba Configurações](#abaconfiguraes)

[Aba Cfg. BD](#abacfg.bd)[Aba Fila](#abafila)

[Aba Processos](#abaprocessos)[Aba Registro de Execuções](#abaregistrodeexecues)

[Aba Histórico de Scripts](#abahistricodescripts)

|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |

 

******Aba Certificados**

Esta aba possibilita a configuração dos certificados digitais da Empresa, que serão empregados na assinatura dos lotes de arquivos contendo as informações da empresa.

![sanesocial-home.png](https://ajuda.sankhya.com.br/hc/article_attachments/35936968859543)

Localizado no lado esquerdo da tela, o painel **"CNPJ/CPF"** exibe os certificados já cadastrados no sistema.

Por meio do botão** "+ Certificado"** executa-se a inserção de novos certificados no sistema. Uma vez que, para configurar um certificado, os campos abaixo deverão ser preenchidos:

**Arquivo:** utilizando o botão** "Selecionar arquivo"** indica-se o arquivo original do certificado digital tipo A1 (extensão "pfx").

**Importante:** o arquivo do certificado digital não pode ser exportado via Sannfe, somente o arquivo original com extensão "pfx" é permitido.

**CNPJ/CPF**: informa-se o CNPJ ou CPF da empresa detentora do certificado em questão.

**Senha**: neste campo é indicada a palavra-chave do certificado.

Após realizar o preenchimento dos campos, aciona-se o botão 

![botão Salvar.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16747256319127)

 **"Salvar"** e as informações acerca do certificado digital serão carregadas na seção **"Informações do Certificado"**.

**Nota:** quando a empresa possuir filiais, não será necessário que sejam inseridos os certificados digitais dos CNPJs de cada filial. O certificado digital da matriz deve assinar todos os lotes gerados, inclusive os lotes das filiais.

 

#### 
******Aba Configurações**

Nesta aba são realizadas as configurações de URLs para envio e consulta de processamento dos lotes de arquivos.

![configuracoes-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35937057244311)

O campo **"Versão do Schema"** deve ser configurado somente com a última versão vigente do eSocial.

 

#### 
******Aba Cfg. BD**

Aqui são realizadas as configurações para conexão com o banco de dados utilizado pela empresa.

![config-bd-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35937071131543)

Através da opção **"Banco"**, seleciona-se o tipo de banco de dados utilizado pela empresa, sendo apresentadas as opções **"Oracle"** e **"SQL"**.

Informa-se no campo **"Nome do banco de dados"** a descrição do banco.

Indica-se por meio do campo **"Usuário"** o utilizador com permissão de acesso ao banco de dados.

No campo **"Senha"** é apontada a palavra-chave de acesso ao banco de dados.

O endereço de IP onde está localizado o banco de dados será descrito no campo **"Host"**.

O campo **"Sid"** é alimentado conforme a opção apontada na opção **"Banco"**. Deste modo, informa-se aqui orcl para Oracle e sql para SQL.

Ao finalizar o preenchimento dos dados, aciona-se o botão** "Salvar"** para que o sistema execute a validação do acesso ao banco de dados. Caso seja verificado que alguma informação está incorreta, será exibida a seguinte mensagem de erro:

***"Não foi possível conectar ao banco de dados, verificar os dados informados."***

Ocorrendo a validação das informações, o acesso ao banco de dados será realizado com êxito e a mensagem abaixo será apresentada:

***"Salvo com sucesso."***

Uma vez realizadas todas essas configurações, o sistema transmitirá todos os arquivos que já estiverem preparados para envio pelo MGE. Recomenda-se que a tela Central do Esocial no MGE seja acessada somente após a execução das referidas configurações.

 

#### 
******Aba Fila**

Através desta aba, tem-se a visualização dos eventos que estão pendentes, finalizados e os tipos de erros que ocorreram nos envios realizados dentro de determinada referência e determinada sequência. Ao preencher os campos conforme os dados pertinentes a empresa, aciona-se o botão **"Pesquisar"** para que as informações sejam apresentadas.

![aba-fila-config-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35937146492439)

Notando-se a presença de eventos Pendentes, é possível que existam eventos Não Finalizados de um grupo inferior; sendo assim, é necessário cancelar o envio dos eventos pendentes e gerá-los novamente.

 

#### 
******Aba Processos**

Esta aba é de uso exclusivo da Sankhya.

![aba-processos-config-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35937173828759)

 

#### 
******Aba Registro de Execuções**

Esta aba exibirá o endereço e o nome do computador que está executando o San eSocial, bem como os dados do computador que esteve executando-o anteriormente. Sendo que, o San eSocial só funciona quando há somente um computador com ele configurado.

![registro-config-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35937231068439)

 

#### 
******Aba Histórico de Scripts**

Nesta aba, pode-se visualizar a data da última atualização de script, a quantidade de erros e quais os objetos que não foram executados devido a qualquer tipo de erro.

![script-config-sanesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/35937284953495)

[[voltar ao topo]](#top)

### 
******Botões no topo da tela**

A seguir estão os botões que executam funções essenciais para o San eSocial:

**Atualizar Script**: este botão tem como funcionalidade atualizar as informações do eSocial no banco de dados que está sendo utilizado para enviar os dados para o governo. Deste modo, é de suma importância manter os scripts atualizados.

**Baixar Log e Log**: através destes botões, efetua-se a baixa do arquivo de log do sistema (exibe todos os processamentos realizados na máquina, sendo essencial para manutenções) e visualização das últimas 1000 linhas do log em tempo real.

**Pausar**: este botão, quando acionado, tem-se uma pausa temporária no serviço do San eSocial, ou seja, o processamento dos eventos já iniciados e a busca dos novos eventos da fila serão suspensos.

**Reiniciar**: tem como finalidade recomeçar o serviço quando o mesmo estiver pausado, retomando assim o processamento das informações geradas pelo MGE e as informações que já tiveram seu processamento iniciado. Além disso, este botão pode ser aplicado quando o serviço não estiver pausado. Nestes casos, tem-se a reinicialização dos serviços que recuperam informações perdidas durante panes no sistema do governo e durante problemas de envio.

**Cancelar Envio**: por meio deste botão, realiza-se o cancelamento de todos os eventos pendentes da fila.

**Gerar Dados Envio**: este botão, ao ser acionado, efetiva a geração dos dados para envio ao eSocial.

**Versões**: realiza a verificação da existência de novas versões do San eSocial. Quando encontradas, pode-se efetuar a atualização do sistema para a versão mais atual.

**Recuperar Arquivos de Retorno**: aciona-se este botão nos casos em que é necessário recuperar mensagens de retorno dos eventos S-5001 e afins (os eventos retornados pelo governo informando os valores declarados para cada folha enviada). Sendo assim, este botão irá recuperar os eventos que foram perdidos devido a instabilidades.

[[voltar ao topo]](#top)

### 
******Envio das Informações**

O despacho das informações será realizado somente quando o serviço **"sanesocialservice"** se encontrar **"Em execução"**.

![san25.png](https://ajuda.sankhya.com.br/hc/article_attachments/8879312108311)

[[voltar ao topo]](#top)

### **San-eSocial na Central do eSocial**

Para acessar o **San eSocial** pela tela **Central do eSocial** via opção **SanEsocial**, realize os passos abaixo:

![sanesocial-centralesocial.png](https://ajuda.sankhya.com.br/hc/article_attachments/38631159588375)

1. Acesse a tela **Preferências** **(**Configurações > Avançado) e configure os parâmetros:

  - 
**Link para acesso ao SaneSocial - FPCONSOLE:**** **insira o endereço completo do Console do San-eSocial.

  - 
**Interno -** **FPATUALIZAENV: **este parâmetro controla a atualização automática do San-eSocial.

  - 
**Valida CPF dos Funcionário? - FPCPFREPETE: **controla a validação de CPF dos funcionários, importante para o eSocial.

1. Acesse a Central do eSocial (Pessoal+ > Rotinas Folha) e clique na opção SanEsocial, o sistema abririrá uma nova aba no navegador com o Console do San-eSocial.

 [[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Sankhya](http://downloads.sankhya.com.br/)