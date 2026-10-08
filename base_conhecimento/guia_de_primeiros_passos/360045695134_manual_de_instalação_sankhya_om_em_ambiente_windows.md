# Manual de Instalação Sankhya Om em Ambiente Windows

> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045695134-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Windows](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045695134-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Windows)  
> **ID do Artigo:** `360045695134` | **Seção:** Guia de Primeiros Passos | **Última Atualização:** 2026-07-29T14:57:36Z

---

O manual a seguir contém as instruções para a instalação do **Sankhya Om** para Banco de Dados Oracle e SQL Server em Ambiente Windows.

#### ****

**[Introdução](#Introdu%C3%A7%C3%A3o)**

**[Download de Arquivos para a Aplicação do Sankhya Om](#DownloaddeArquivosparaaAplica%C3%A7%C3%A3odoSankhyaOm)**

**[Procedimento para Banco de Dados Oracle](#ProcedimentoparaBancodeDadosOracle)**

**[Configuração do Wildfly](#Configura%C3%A7%C3%A3odoWildfly)**

**[Configuração para Banco de Dados Oracle](#Configura%C3%A7%C3%A3oparaBancodeDadosOracle)**

**[Configuração para Banco de Dados SQL Server](#Configura%C3%A7%C3%A3oparaBancodeDadosSQLServer)**

**[Instalação do pacote Sankhya Om](#Instala%C3%A7%C3%A3odopacoteSankhyaOm)**

**[Configuração da Porta Wildfly](#Configura%C3%A7%C3%A3odaPortaWildfly)**

**[Configuração de memória do Wildfly](#Configura%C3%A7%C3%A3odemem%C3%B3riadoWildfly)**

**[Inicialização automática do Wildfly Produção (Serviço do Windows)](#Inicializa%C3%A7%C3%A3oautom%C3%A1ticadoWildflyProdu%C3%A7%C3%A3o(Servi%C3%A7odoWindows))**

**[Inicialização do Wildfly](#Inicializa%C3%A7%C3%A3odoWildfly)**

**[Conexão da aplicação Sankhya Om](#Conex%C3%A3odaaplica%C3%A7%C3%A3oSankhyaOm)**

| Manual de Instalação |
| --- |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

####  

### **Introdução**

O **Sankhya Om** é uma aplicação JEE (Java Enterprise Edition) e, por isso, utiliza o Wildfly como servidor de aplicação JEE. O Wildfly, por sua vez, é uma aplicação Java que requer uma instalação prévia do Java na máquina servidora.

A configuração do Wildfly é facilitada pelo [Gerenciador de Pacotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580034-Melhores-pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-e-atualiza%C3%A7%C3%A3o-via-Gerenciador-de-Pacotes), que simplifica tarefas como configuração de memória, arranjo de portas, diretório de extensões, aplicação de patches de segurança, entre outras.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17153070413335)

 O Gerenciador de Pacotes não suporta mais o processo de atualização e instalação de pacotes do **Sankhya Om** (pkgs); essa responsabilidade agora é exclusiva do [WPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-W-via-WPM) que é uma aplicação Web, um painel de instalação do **Sankhya Om**, que é acessado dentro do ambiente do Wildfly.

![Instalação Sankhya Om em Ambiente Windows.png](https://ajuda.sankhya.com.br/hc/article_attachments/22894266883991)

A seguir, conheça os detalhes de como baixar e instalar o JDK, Wildfly, Gerenciador de Pacotes, bem como as configurações necessárias no sistema operacional e como acessar o WPM e instalar uma versão do **Sankhya Om**.

[[voltar ao topo]](#top)

### **Download de Arquivos para a Aplicação do Sankhya Om**

Para efetuar o download do Wildfly, acesse [http://downloads.sankhya.com.br/downloads?app=WildFly&c=1](http://downloads.sankhya.com.br/downloads?app=WildFly&c=1) 

Caso queira baixar a última versão disponível do download do JDK8, Gerenciador de Pacotes e do pacote com **"Sankhyaom_x.xx.xxxxx.pkg"** acesse à [Central de downloads Sankhya](http://downloads.sankhya.com.br/).

**Nota:** o download do arquivo JDK8 deverá estar de acordo com a versão do Sistema Operacional.

[[voltar ao topo]](#top)

### **Procedimento para Banco de Dados Oracle **

Para a instalação, deve-se conectar no Banco de Dados Oracle via sqlplus. Caso queira verificar o parâmetro **opens_cursors** insira o comando:

```text
SQL> show parameter open_cursors
NAME TYPE VALUE
----------------------------------- ----------- ------------------------------
open_cursors integer 300

Ajustar parâmetros do Oracle:
SQL> alter system set open_cursors=2000;
System altered.
SQL> exit
```

**Observação:** caso este retorne o **valor <2000**, efetue o procedimento de ajustar os parâmetros do Oracle, sendo este:

```text
[oracle@oracletestes ~]$ sqlplus "/as sysdba" 
```

####  

#### 
**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312857824151)

 ****Adição da variável JAVA_HOME**

Para a execução desta, deve-se clicar no botão direito do mouse do seu computador e, em seguida, selecionar as opções de acordo com a ordem exibida a seguir:

**Propriedades > Configurações Avançadas do Sistema > Variáveis de ambiente.**

Posteriormente, na aba **"Variáveis do sistema"**, clique na opção **"Novo"** .

Considere o seguinte exemplo quando o Windows possui 64bits:

![Adição da variável JAVA_HOME- Imagem 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154041975703)

**Observação:** a versão do Java irá variar conforme a instalação, como por exemplo, **"jdk1.8.0_xxx C:Program Files\Java\jdk1.8.0_152"**.

Windows 32 bits:

![Adição da variável JAVA_HOME- Imagem 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154041978391)

 

#### 
**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312877938711)

 ****Instalação do Gerenciador de Pacotes**

Para esta etapa, primeiramente execute a descompactação do arquivo "**pkg-man_windows_x_xxx.zip localizado na pasta c:\sankhya"**.

Depois, execute a instalação do gerenciador de pacotes. Quando a instalação for finalizada, clique na opção **"Avançar"** e instale este na pasta "**c:\sankhya"**.

Aguarde a cópia dos arquivos e a sua finalização.

 

#### 
**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312877939735)

**** Instalação do Wildfly teste e treina**

Execute a descompactação do arquivo **"Wildfly_10.0.0_Sankhya_mod_XXXX.zip"** em** "c:\sankhya"**, e a pasta **"wildfly_producao"** será criada;

Duplique a pasta **"wildfly_producao"** mude os nomes para** "wildfly_teste"** e **"wildfly_treina"**.

 

#### 
**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312877940375)

 ****Execução do Gerenciador de Pacotes**

Selecione o botão **"Iniciar"** do windows e entre em **"Todos os Programas\Sankhya OM Gerenciador de Pacotes"** e clique em **"Gerenciador de Pacotes"**;

Em seguida, cole as DLL na pasta **"C:\windows\SysWOW64"**.

[[](#top)[voltar ao topo]](#top)

### **Configuração do Wildfly**

É necessário realizar o procedimento abaixo para as bases de Produção, Teste e Treina.

No início da instalação, tem-se a tela:

![Configuração do Wildfly.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154327610135)

Para este cenário, digite à opção **4**;

Em seguida, digite o servidor de aplicações, sendo este **"wildfly_producao"**;

O diretório de instalação neste exemplo será** "C:\sankhya\wildfly_producao"**.

[[voltar ao topo]](#top)

### **Confi****guração para Banco de Dados Oracle**

Para realizar as etapas no seu Banco de Dados Oracle, será necessário executar o procedimento descrito abaixo para Bases de Produção, Teste e Treina.

Para o início das configurações, tem-se as opções abaixo:

![Configuração para Banco de Dados Oracle-Imagem 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154382385431)

Neste caso, digite o número **2** referente à opção **"Selecionar Servidor"**.

Em seguida, será exibida as opções para a seleção do Servidor de Aplicações, sendo elas:

- [1] wildfly_produção;

- [2] wildfly_teste;

- [3] wildfly_treina

- [4] Retonar ao menu anterior.

Digite a opção **1**;

Para o servidor selecionado, será exibido as opções:

![Configuração para Banco de Dados Oracle-Imagem 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154382390679)

Digite a opção **1. **Posteriormente, tem-se as opções:

- [1] Oracle;

- [2] Ms SQL Server (Driver JTDS);

- [3] Ms SQL Server (Driver Ms);

- [4] Para saber mais sobre JTDS e Ms.

Selecione o Banco de Dados correspondente à opção **[1] Oracle**.

Digite o IP do servidor correspondente. Por exemplo:

192.168.0.148 

Ou digite o **localhost** caso o servidor de aplicação esteja junto ao servidor de Banco de Dados.

Depois, digite o número da porta.

Pra o nome do serviço digite **XE**, neste as letras sempre deverão ser maiúsculas.

Em seguida insira o usuário do Banco de Dados. O usuário **SANKHYA** poderá ser digito com letras maiúsculas ou minúsculas.

Digite a senha, e para a pergunta que será exibida em seguida digite **S**.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17153070413335)

 Caso ocorra um erro no teste de conexão, faça a revisão das suas configurações.

[[voltar ao topo]](#top)

### **Confi****guração para Banco de Dados SQL Server**

Para bases de Produção, Teste e Treina, o procedimento abaixo deverá ser realizado.

No início das configurações tem se as opções:

- [1] Instalação/atualização expressa do Sistema;

- [2] Selecionar Servidor;

- [3] Listar Servidores registrados;

- [4] Registrar Servidor;

- [5] sair.

Digite o número **2**, correspondente à opção** "Selecionar Servidor"**.

Depois, selecione o Servidor de Aplicação **1**.

Em seguida, para as configurações para o servidor "**wildfly_producao"** tem-se:

![Configuração para Banco de Dados SQL Server-Imagem 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154484616343)

Insira o número **1**.

Depois escolha um Banco de Dados.

![Configuração para Banco de Dados SQL Server-Imagem 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154500900375)

Digite **2** ou **3**. Sendo que, à opção **2** utilizará drivers do Java, destacamos que esta deverá ser uma preferência de uso. Na opção **3**, será utilizado os drivers da microsoft.

Posteriormente digite o IP do servidor do Banco de Dados. Considere abaixo um exemplo para a sua inserção:

192.168.0.148

ou **localhost**, caso o servidor de aplicação esteja junto ao servidor do Banco de Dados.

Digite o número da Porta e o Nome da Instância.

**Nota:** a instância do SQL Server deverá ser informada apenas se esta estiver nomeada.

Em seguida, digite o nome da base do Banco de Dados do SQL Server. Por exemplo:

**SANKHYA_PROD**

Faça a inserção do usuário **SANKHYA**, este poderá conter letras maiúsculas ou minúsculas.

Depois digite a senha, responda a pergunta a ser exibida com a letra **S**.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17153070413335)

 Caso ocorra erro no teste de conexão, execute a revisão das configurações.

[[voltar ao topo]](#top)

### **Instalação do pacote Sankhya Om**

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17092886764183)

 Para conferir o passo a passo de como instalar o pacote **Sankhya Om** via WPM, consulte o artigo: [Atualização do sistema Sankhya Om via WPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#top).

[[voltar ao topo]](#top)

### **Configuração da Porta Wildfly**

Será necessário realizar o procedimento abaixo para as bases de Produção, Teste e Treina.

![Configuração da Porta Wildfly-Imagem 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154569057303)

Das opções a serem disponibilizadas acima, digite a opção **2**;

Referente à Seleção do Servidor de Aplicações, tem-se:

![Configuração da Porta Wildfly-Imagem 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154618139159)

![Configuração da Porta Wildfly-Imagem 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154569069719)

Para tal, digite opção **1**.

Logo, teremos:

![Configuração da Porta Wildfly-Imagem 4.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154569072279)

**Importante:** não utilize a porta 8080.

Por padrão Sankhya, pode-se utilizar as portas:

- Porta 8180 para Base Produção;

- Porta 8280 para Base Teste;

- Porta 8380 para Base Treina.

[[voltar ao topo]](#top)

### **Con****figuração de memória do Wildfly**

Primeiramente, deve-se selecionar o servidor. Para tal ação, digite **2** para a seleção da opção a que refere-se este número;

Em seguida, selecione um Servidor de Aplicação, portanto digite o número **1** da opção **"wildfly_producao"**.

![Configuração de memória do Wildfly-Imagem 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154671793687)

Para esta etapa digite o número **7**, a que refere-se à opção de **"Configuração de Memória"**;

Referente ao Ambiente de Execução desta configuração, digite o número **1**, que corresponde a opção **"Editar configurações de memória (XMX e XMS)"**.

Em seguida, tem-se:

![Configuração de memória do Wildfly-Imagem 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154659246103)

Referente a esta etapa, destacamos que a quantidade memória inicial e máxima do Wildfly deverão ser menores que a disponível no sistema operacional. É recomendável que se considere a quantidade de memória utilizada por outros processos na máquina, inclusive no sistema operacional.

[[voltar ao topo]](#top)

### **Inicialização automática do Wildfly Produção (Serviço do Windows)**

Esta opção fará o registro do wildfly como serviço do Windows para inicialização automática.

Para o início desta, tem-se as opções:

- [1] Instalação/atualização expressa do Sistema;

- [2] Selecionar Servidor;

- [3] Listar Servidores registrados;

- [4] Registrar Servidor;

- [5] Sair.

Digite a opção **2**;

Depois, selecione a opção **1** referente ao Servidor de Aplicação wildfly_producao;

Posteriormente, tem-se as opções:

![Inicialização automática do Wildfly Produção.png](https://ajuda.sankhya.com.br/hc/article_attachments/17154693779223)

Digite a opção **9**.

[[voltar ao topo]](#top)

### **Inicialização do Wildfly**

Para abrir os serviços do windows, abra o executar e digite "**services.msc"**.

Inicialize os serviços **"wildfly_producao"**,** "wildfly_teste"**e** "wildfly_treina"**.

Para tal ação, clique na aba **"Logon"**.

Em seguida pesquise o administrador em **"Digite o nome do objeto a ser selecionado"** e clique em **"Verificar nomes**";

Digite a senha da conta e clique em **"Aplicar"**.

Posteriormente, clique com o botão direito no serviço de cada base e clique em **"Iniciar"**.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17153070413335)

 Certifique-se de verificar se o logon estava como administrador.

[[voltar ao topo]](#top)

### **Conexão da aplicação Sankhya Om**

Para esta etapa, abra seu navegador, e para um melhor desempenho sugerimos o Google Chrome como navegador padrão para solução Java. deve-se então, alterar a porta configurada para seu respectivo ambiente a que deseja-se conectar. Por exemplo:

- **Produção:** [http://ipdoservidor:8180/mge](http://ipdoservidor:8180/mge)

- **Teste:** [http://ipdoservidor:8280/mge](http://ipdoservidor:8280/mge)

- **Treina:** [http://ipdoservidor:8380/mge](http://ipdoservidor:8380/mge)

**Observação:** caso a aplicação WEB não seja exibida, certifique-se que o wildfly foi inicializado. Do contrário, pode ter ocorrido um erro ao iniciar a aplicação e será necessário verificar o log.

Quando o login for efetuado no **Sankhya Om** pela primeira vez, uma licença será solicitada. Assim, acesse o [Sankhya Place](https://ajuda.sankhya.com.br/hc/pt-br/articles/4422517129623) por meio do sistema Sankhya ou por meio de uma página da web, e busque pela **"Chave de Cliente"** disponibilizada:

![Sankhya Place-chave do cliente.png](https://ajuda.sankhya.com.br/hc/article_attachments/17155306416663)

Em seguida, retorne na área do cliente e clique em **"Administração"**, logo acesse a tela [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor).

Na aba **"Autorização de Acesso"**, campo **"ID do Cliente"** copie a chave do cliente e clique em **"Salvar":**

![Administração do Servidor- aba Autorização de acesso.png](https://ajuda.sankhya.com.br/hc/article_attachments/17155447713943)

Navegue pelo **Sankhya Om** em telas do cliente para verificar se não há erros no sistema. Como, por exemplo, nas telas de [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) e [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras).

No **Sankhya Om**, faça a alteração da senha. Realize o acesso ao WPM por meio do endereço do **Sankhya Om** adicionando a extensão** "/wpm"** ao final do endereço na barra de endereço do navegador. Ao abrir este, ficará como [http://endereçodoskw/wpm](http://endere%C3%A7odoskw/wpm). Quando acessar o WPM, este estará como o exemplo [http://ipservidor:8180/wpm](http://ipservidor:8180/wpm).

Caso não seja possível executar a atualização pelo WPM, acesse a aba **"Configurações"**, seção **"Opções"** e desligue a marcação **"Utilizar Repositório Alternativo"** . Depois, faça a atualização manualmente.

Faça o download do arquivo em [http://downloads.sankhya.com.br/](http://downloads.sankhya.com.br/) e copie para a pasta **"C:\sankhya\SankhyaOM"** Gerenciador de Pacotes\pkgs e execute o Gerenciador de pacotes.

Posteriormente, informe o Servidor de Aplicação em que será executado o pacote de atualização do WPM. O sistema irá solicitar que as configurações de conexão com o Banco de Dados sejam realizadas.

Caso esse servidor já esteja configurado, o sistema irá solicitar a confirmação dessa configuração.

[[voltar ao topo]](#top)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17092886764183)

 Acesse também: 

[Premissas e Pré-requisitos para implantação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045373654-Premissas-e-Pr%C3%A9-requisitos-para-implanta%C3%A7%C3%A3o)

[Manual de Instalação Sankhya Om em Ambiente Linux](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-SankhyaW-em-Ambiente-Linux)


---

### 🔗 Links e Referências Internas citadas neste Artigo:

- [Gerenciador de Pacotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580034-Melhores-pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-e-atualiza%C3%A7%C3%A3o-via-Gerenciador-de-Pacotes)
- [WPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-W-via-WPM)
- [http://downloads.sankhya.com.br/downloads?app=WildFly&c=1](http://downloads.sankhya.com.br/downloads?app=WildFly&c=1)
- [Central de downloads Sankhya](http://downloads.sankhya.com.br/)
- [Atualização do sistema Sankhya Om via WPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#top)
- [Sankhya Place](https://ajuda.sankhya.com.br/hc/pt-br/articles/4422517129623)
- [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor)
- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)
- [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras)
- [Premissas e Pré-requisitos para implantação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045373654-Premissas-e-Pr%C3%A9-requisitos-para-implanta%C3%A7%C3%A3o)
- [Manual de Instalação Sankhya Om em Ambiente Linux](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-SankhyaW-em-Ambiente-Linux)