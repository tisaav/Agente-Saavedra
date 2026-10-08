# Como atualizar o Wildfly em sistema operacional Windows

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38109965528087-Como-atualizar-o-Wildfly-em-sistema-operacional-Windows](https://ajuda.sankhya.com.br/hc/pt-br/articles/38109965528087-Como-atualizar-o-Wildfly-em-sistema-operacional-Windows)  
> **ID:** `38109965528087` | **Última Atualização:** 2026-07-22T14:02:03Z

---

É fundamental manter o **Wildfly sempre atualizado** para a versão mais recente (**23 mod_03**). Isso garante a compatibilidade do ambiente Sankhya com as últimas versões do **JDK** e demais componentes de infraestrutura, além de proporcionar **ganhos de desempenho, estabilidade e segurança**, reduzindo o risco de falhas em produção.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407553303)

 OBSERVAÇÃO: **O procedimento de atualização deve ser realizado **apenas por Administradores de Sistemas** com conhecimento em Windows, ou pela equipe da **Cloud**, caso o ambiente esteja hospedado em nuvem. Antes de iniciar, é obrigatório **validar a versão do JDK** em uso. O Wildfly 23 é compatível com **JDK 8u421** (preferencialmente) até **JDK 11**. Essa versão deve estar **instalada e ativada no servidor** para garantir o correto funcionamento do ambiente.

 

#### **Procedimento de Instalação**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010373911)

 Acesse o servidor** onde o Wildfly atual está instalado e pare o serviço da aplicação Sankhya.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010374935)

  Logue-se como `administrador` e acesse a pasta aonde está instalado o wildfly.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109965485335)

  Crie um backup do diretório atual do Wildfly:

```text
windows + R >> services.msc
```

 

![image - 2026-02-03T154606.973.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407556631)

 

![image - 2026-02-03T154710.486.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407561367)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010379415)

 Acesse o portal **“Downloads Sankhya Wildfly”** utilizando o seu **Sankhya ID**.

 

![image - 2026-02-03T154813.712.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368150551)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109965488151)

 Faça o download do pacote correspondente ao seu banco de dados:

- 

****[''Wildfly 23.0''](https://downloads.sankhya.com.br/downloads?app=WildFly&c=1)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38109965490327)

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010380951)

 Descompactação do pacote:

- 

Extraia o pacote **wildfly_producao** utilizando o **WinRAR** ou qualquer outro gerenciador de arquivos compatível.

- 

Após a descompactação, o diretório resultante deverá conter:

 

![image - 2026-02-03T162701.253.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407565591)

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010382999)

 Configure o servidor no **PKG (SankhyaW Package Manager)**:

- 

Acesse o diretório: `c:\sankhya\sankhyaW_gerenciador_de_pacotes\bin\`

- 

Execute o comando: `sankhyaw-package-manager.bat`

- 

No menu do PKG:

Selecione a **opção 2: Selecionar servidor**

Em seguida, selecione a **opção 2: Configurar arranjo de portas**

- 

Escolha o servidor **wildfly_producao** (agora com Wildfly 23).

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38109965493527)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38110010383895)

 

##### 
**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109965482775)

 IMPORTANTE: **O** **Wildfly altera a porta padrão para **8080**. Ajuste para a porta correta de produção (geralmente **8180**).

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109965494039)

 Acesse o diretório `c:/sankhya/wildfly_producao` e abra o arquivo `standalone.conf.bat` do novo Wildfly.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010385687)

 Em seguida, copie as configurações de **memória** e **argumentos** do arquivo `standalone.conf.bat` do Wildfly antigo (`wildfly_producao_old`) e cole no novo, replicando todas as definições necessárias.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38109965495703)

 

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010387223)

 Ajuste os dados de conexão do banco de dados conforme instruções do DBA.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38110010386583)

 

##### 
**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109965482775)

 IMPORTANTE:** Os dados informados acima são individuais. Verifique também a **porta HTTP**: o padrão é **8080**, mas se estiver configurada como **8180**, ajuste-a no PKG em **Configurar arranjo de portas**.

 

![image - 2026-02-03T163559.098.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407566615)

 

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010387223)

 No diretório `C:/sankhya/wildfly_producao/standalone/deployments`, verifique se **apenas** os arquivos `mge-ds.xml` e `wpm.war` estão presentes.

- 

Se o arquivo `mge-ds.xml` estiver ausente, revise a configuração correspondente no PKG.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38110010388247)

 

- Também é **possível alterar a memória no WPM**, aba **"configurações".**

 

#### **Inicialização automática do Wildfly Produção (Serviço do Windows)**

##### Esta opção registra o **Wildfly** como serviço do Windows, permitindo a **inicialização automática**. Antes de prosseguir, é necessário **desinstalar o serviço antigo**, se houver.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368157591)

 Para iniciar o processo, o menu apresenta as opções:

1. 

Instalação/atualização expressa do Sistema;

1. 

Selecionar Servidor;

1. 

Listar Servidores registrados;

1. 

Registrar Servidor;

1. 

Sair.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368159383)

 Digite a **opção 2**: **''Selecionar Servidor''**;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407573399)

 Em seguida, selecione a **opção 1**, referente ao **Servidor de Aplicação wildfly_producao**;

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407577239)

 Após isso, o sistema apresentará novas opções para prosseguir com o registro do serviço.

 

![Inicialização automática do Wildfly Produção.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010388759)

 

- Digite a opção **10**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368165655)

 Em seguida, **repita o primeiro passo**:

- 

Menu inicial:

1. 

Instalação/atualização expressa do Sistema

1. 

Selecionar Servidor

1. 

Listar Servidores registrados

1. 

Registrar Servidor

1. 

Sair

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368167063)

 Digite a **opção ****2: ''Selecionar Servidor''**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368168087)

 Depois, selecione a **opção 1**, referente ao **Servidor de Aplicação wildfly_producao**

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109965494039)

 O sistema exibirá novas opções para prosseguir com o registro ou configuração do serviço:

 

![Inicialização automática do Wildfly Produção.png](https://ajuda.sankhya.com.br/hc/article_attachments/38110010388759)

 

- Digite a opção **9**.

 

#### **Inicialização do Wildfly**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368157591)

 Abra o **Executar** (atalho: `Win + R`) e digite:

```text
services.msc
```

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368159383)

 Localize e **inicialize** os serviços:

- 

`wildfly_producao`;

- 

`wildfly_teste`;

- 

`wildfly_treina`.

 

![image - 2026-02-03T165631.235.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368170391)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407573399)

 Clique na aba **“Logon”** do serviço desejado.

 

![image - 2026-02-03T165719.262.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407586327)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407577239)

 No campo **“Digite o nome do objeto a ser selecionado”**, digite **administrador** e clique em **“Verificar nomes”**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38109965507095)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407587863)

 Digite a **senha** da conta e clique em **“Aplicar”**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368167063)

 Em seguida, clique com o **botão direito** sobre cada serviço (`wildfly_producao`, `wildfly_teste`, `wildfly_treina`) e selecione **“Iniciar”**.

 

![image - 2026-02-03T170113.287.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407588759)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407553303)

 OBSERVAÇÃO: **Verifique se o logon do serviço está configurado com a conta **administrador**.

 

#### **Reinicialização após falha**

Após configurar a **inicialização automática** do serviço do Wildfly, é importante **configurar a recuperação** do serviço em caso de falhas:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368157591)

 Abra as **propriedades do serviço** e acesse a aba **''****Recuperação''**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368159383)

 Configure as opções de recuperação conforme o exemplo abaixo:

 

![image - 2026-02-03T170246.464.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368178455)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407573399)

 Clique em **“Aplicar”** para salvar as alterações.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407577239)

 Acesse o WPM seguindo o exemplo do link fornecido e configure a **memória do Wildfly**, se necessário.

 

![image - 2026-02-03T170400.985.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368180503)

 

- 

**Senha padrão do WPM:** `tecsis` (confirme com o responsável caso seja diferente).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407587863)

 Ajuste os **dados de conexão do banco** e **salve as configurações**.

 

![image - 2026-02-03T170741.637.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141407593879)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368167063)

 Ajuste os **dados de conexão do banco** no WPM e **salve as configurações**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38109965510039)

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38141368168087)

 Instale a **mesma versão do sistema** utilizada anteriormente ou o **último release** da mesma versão.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38109965494039)

 Valide o **funcionamento do ambiente atualizado**.

 

#### **Importância da atualização do Wildfly**

A atualização do **Wildfly** é essencial para manter o ambiente **compatível com as versões atuais do JDK, do Java e do Sankhya**, garantindo a continuidade do **suporte técnico oficial**.

Além disso, a atualização oferece benefícios como:

- 

Correção de vulnerabilidades;

- 

Melhora no desempenho;

- 

Maior estabilidade do servidor de aplicações.

Ambientes que permanecem em versões antigas podem apresentar:

- 

Falhas no **deploy**;

- 

Quedas inesperadas durante o uso do sistema;

- 

Incompatibilidade com novos recursos;

- 

Instabilidade em cenários de alta carga;

- 

Indisponibilidade de **correções de segurança**.

A não atualização compromete **o funcionamento do sistema, a segurança e a manutenção futura do ambiente**.


---

### 🔗 Links e Referências Internas:

- [''Wildfly 23.0''](https://downloads.sankhya.com.br/downloads?app=WildFly&c=1)