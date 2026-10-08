# Não há espaço disponível no dispositivo

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360057227714-N%C3%A3o-h%C3%A1-espa%C3%A7o-dispon%C3%ADvel-no-dispositivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057227714-N%C3%A3o-h%C3%A1-espa%C3%A7o-dispon%C3%ADvel-no-dispositivo)  
> **ID:** `360057227714` | **Última Atualização:** 2026-07-22T15:26:54Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251883616919)

 MENSAGEM**:

[COM_E00510] Não há espaço disponível no dispositivo.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251883633559)

 CAUSA:**

Mensagem apresentada devido a partição do HD em que o SankhyaOm está instalado ter chegado a 100% de ocupação.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251854187671)

 SOLUÇÃO:**

Mensagem apresentada devido a partição do HD em que o SankhyaOm está instalado ter chegado a 100% de ocupação. Para solução, o tópico 1 citado abaixo poderá ser seguido para LINUX e os tópicos 2 e 3 para ambos (Linux e Windows):

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251883624215)

 Verifique no /home/mgeweb/ se existe um arquivo 'nohup.out' e se utiliza o sanesocial. Acesse a pasta dele e localize este arquivo. É possível apagar em ambos os locais (**análise específica para sistema operacional Linux)**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453246985751)

 Ainda sobre este arquivo para o sanesocial e para o wildfly, para não gerá-lo, é importante que se tenha no aliás de configuração de start do SankhyaOm e do Sanesocial o comando /dev/null;

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453246985751)

 Por exemplo, se o Sanesocial estiver instalado em: /home/mgeweb ao iniciá-lo com: home/mgeweb/sanesocial/./sanesocial-service start > /dev/null;

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453246985751)

 Então, o arquivo nohup.out não vai ser gerado;

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453246985751)

 Para facilitar o trabalho, pode-se criar um aliás para que o comando de start seja executado sem ter que decorar isso.

 

Portanto, crie no .bash_profile do linux os comandos de start e stop e, dessa forma, ele utilizará sempre estes para não gerar o arquivo. Para abrir o .bash_profile, faça login no servidor com o usuário mgeweb e no /home/mgeweb execute vi .bash_profile

Neste arquivo observa-se que os comandos de start e stop do Sankhya-W estão lá já listados, então vá até o fim deste arquivo e coloque as configurações abaixo. Feito isso, saia do terminal, entre novamente e reinicie o sanesocial com os novos comandos, para parar: stopsan e iniciar: startsan

**#CONFIGURACAO START STOP SANESOCIAL**

alias startsan='/home/mgeweb/sanesocial/./sanesocial-service start > /dev/null'

alias stopsan='/home/mgeweb/sanesocial/./sanesocial-service stop'

 

Observe também se neste mesmo arquivo .bash_profile tem a configuração para start do Sankhya, está também com o dev/null. Ficando assim:

alias jb_startprod=' killprod; rmltwprod; nohup /home/mgeweb/wildfly_producao/bin/standalone.sh -bmanagement 0.0.0.0 >& /dev/null &'

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251854193815)

 Além deste arquivo, é possível apagar os pacotes de atualização antigos do sistema que podem estar na pasta /home/hde/sankhyaw-wpm/pkgs, diretamente nesta pasta ou pelo atualizador do sistema (WPM) acessando as opções: Exibir todas as versões > aba Disponíveis localmente > Deletar todos arquivos de atualização.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251883631127)

 Os logs antigos do SankhyaOm também podem ser apagados na pasta do wildfly: Wildfly > standalone > log.