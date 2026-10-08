# Configuração de argumentos para Wildfly

> **Módulo:** Solucao de Problemas | **Subseção:** Acessos/Banco de Dados  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly)  
> **ID:** `8896725681943` | **Última Atualização:** 2026-07-22T15:11:41Z

---

Algumas vezes são necessárias algumas configurações específicas para a máquina virtual do Java, a JDK, a fim de mudar alguns comportamentos do sistema. Tais configurações são determinadas por argumentos que podem ter efeito no funcionamento geral do servidor de aplicações ou até mesmo mudar uma tratativa específica do sistema. 

Tais configurações são feitas no arquivo de inicialização do Wildfly e só entram em vigor após a reinicialização do serviço, a partir do próprio sistema operacional. 

Para fazer esta configuração num servidor Windows, acesse a pasta do Wildfly > bin > arquivo standalone.conf.bat e adicione uma nova configuração com esta sintaxe: 

set "JAVA_OPTS=%JAVA_OPTS% -Djava.io.tmpdir=C:\Sankhya\TEMP"

 

![Configuração](https://ajuda.sankhya.com.br/hc/article_attachments/15822526310807)

 

No exemplo em questão, o argumento -Djava.io.tmpdir está direcionando a geração de arquivos temporários para a pasta: C:\Sankhya\TEMP 

Para servidores de aplicação no ambiente linux, o caminho do arquivo é o mesmo: Pasta do Wildfly > bin, porém o arquivo a ser editado é o standalone.conf. A sintaxe também é diferente ficando desta forma: 

 

![Configuração](https://ajuda.sankhya.com.br/hc/article_attachments/15822526316439)

 

JAVA_OPTS="$JAVA_OPTS -Djava.io.tmpdir=/home/mgeweb/TEMP"

 

Feita a edição, salve o arquivo e reinicie o sistema a partir do servidor. 

Dentre os argumentos mais comuns utilizados pelo sistemas estão estes abaixo. Lembrando que sempre que for alterar ou adicionar algum além destes, tenha completa ciência dos impactos que podem gerar na operação do sistema: 

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.global.query.timeout**: Tempo de timeout de query. Ajustando quando ocorre o erro de "ORA-01013". Valor deve ser em segundos.

Exemplo: -Djape.global.query.timeout=600

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.session.timeout**: Tempo de timeout de sessão JAPE. Ajustado quando ocorre o erro "JapeSession timeout". Valor deve ser em milissegudos.

Exemplo: -Djape.session.timeout=600000

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.jdbc.check.select**: Validar/não validar a expressão select de relatórios e dashboards.

Exemplo: -Djape.jdbc.check.select=false

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -#GMT_BRASIL**

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -JAVA_OPTS="$JAVA_OPTS -Duser.timezone=GMT-3"** : ajustar timezone

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djboss.socket.binding.port-offset**: Offset da porta padrão do Wildfly. Soma-se o valor a 8080.

Exemplo: -Djboss.socket.binding.port-offset=100, dessa forma, a porta de conexão ao sistema será a 8180.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djboss.bind.address.management**: Bind de acesso ao JMX Console do Wildfly. É necessário para utilizar o JConsole e Visual VM.

Exemplo: -Djboss.bind.address.management=0.0.0.0

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Duser.language**: Força a linguagem do usuário. Exemplo: -Duser.language=pt

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Duser.country**: Força a região do usuário.

Exemplo: -Duser.country=BR 

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Dfile.encoding**: Força o encoding do sistema para o padrão ISO pt_br 

Exemplo: -Dfile.encoding=ISO8859-1

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Dskw.use.procedure.tgfnum**: Ativa/Desativa a numeração por procedure no sistema.

Exemplo: -Dskw.use.procedure.tgfnum=true

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Dskw.use.procedure.tgfnum.rule**: Lista de tabelas que serão numeradas por procedures.

Exemplo: -Dskw.use.procedure.tgfnum.rule=TGFCAB,TGFFIN,TGFMBC,TMDFMG,TMDAMG,TGFLNF

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.experimental.lock.strategy**: Estratégia diferencial de Lock.

Exemplo: -Djape.experimental.lock.strategy=1

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.experimental.always.reuse.jdbc.conn**: Ativar o reuso de conexões JDBC

Exemplo: -Djape.experimental.always.reuse.jdbc.conn=true

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.experimental.commit-type**: Tipo de commit

Exemplo: -Djape.experimental.commit-type=B

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.use.write.history**: Desligar a gravação de histórico do jape

Exemplo: -Djape.use.write.history=false

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Dsankhyaw.schedule.disable: **Desabilita a execução de jobs no sistema

Exemplo:  -Dsankhyaw.schedule.disable=false

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Dlogin.unico.ativo: **false : Ignora checagens do login unico ( [LoginUnico] Informações incompletas, o token não será gerado. Usuario....])

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.check.is.valid.connection=false: **Ignora checagens de conexão feitas pelo wildfly (SELECT FROM DUAL)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djape.sqlserver.use.native.query.getpk=true:** -- SQL Server para carga dos metadados mais rápida 

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

-Dskw.use.procedure.tgfnum.numnota=false:** Desabilita a utilização da procedure STP_NUMERAR_NOTA2

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 -Djava.io.tmpdir=**: Determina o diretório de arquivos temporários do sistema

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

** **Dsnk.authorization.layer.enable =** true

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

** **Dskw.cluster.nodes= **'IP 1,IP 2' declarar quais IPs estarão no modo cluster.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450872692247)

 Dskw.cluster.pref.run.job=** true declarar qual nó será o executor de jobs.