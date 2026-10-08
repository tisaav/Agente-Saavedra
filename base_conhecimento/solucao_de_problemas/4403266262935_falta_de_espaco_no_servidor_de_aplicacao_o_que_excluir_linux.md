# Falta de espaço no servidor de aplicação, o que excluir? (Linux)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4403266262935-Falta-de-espa%C3%A7o-no-servidor-de-aplica%C3%A7%C3%A3o-o-que-excluir-Linux](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403266262935-Falta-de-espa%C3%A7o-no-servidor-de-aplica%C3%A7%C3%A3o-o-que-excluir-Linux)  
> **ID:** `4403266262935` | **Última Atualização:** 2026-07-22T15:23:59Z

---

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343614550551)

 ATENÇÃO: **

Recomendamos que solicite a equipe de TI da Empresa que execute o procedimento abaixo, programando um horário que não irá interromper a operação da empresa, ou avisando aos usuários sobre a manutenção e que o sistema ficará fora do ar, por alguns instantes.

O servidor de aplicação geralmente tem um espaço de armazenamento limitado, e com o tempo e uso da aplicação **SankhyaOm**, este espaço vai ficando cheio até sua totalidade máxima (100%), com isso surge a dúvida: o que posso excluir nesta partição?

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343630947351)

 SOLUÇÃO:**

#### **Verifique o espaço em disco:**

com usuário root ou mgeweb:

*df -h*

 

*

![df_-h_100.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/4403265694743)

*

 

No exemplo acima é possível notar que a partição 'vg00-lvbarra' do tipo ext4 montado no diretório / está com 100% gerando erros ao acessar o sistema, realizar impressões, diretório inválido, entre outros.

 

#### **Altere o usuário para mgeweb:**

*su -l mgeweb *

*(Dica com root não irá solicitar senha para troca de usuário)

 

#### **Exclua pacotes de instalações antigas do Gerenciador de Pacotes:**

*ls*

*cd sankhyaW_gerenciador_de_pacotes/pkgs*

*(Dica cd sankhyaW digite TAB para autocompletar)

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403265869079)

 

*ls *(Para Listar os arquivos para exclusão)

 

* 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403265888535)

*

 

#### **Exclua os pacotes de instalações (pkgs) antigas:**

*rm jiva-w_3.30b640.pkg sankhya-w_3.29b507.pkg sankhya-w_4.7b656.pkg (Enter)*

*ls (Para listar novamente e confirmar a exclusão)*

 

#### **A cada atualização do sistema o Wildfly cria um ponto de restauração com o mesmo tamanho do pacote de instalação, realize a exclusão e deixe somente o arquivo da última versão:**

*cd (retorna ao diretório raiz e permite a utilização da tela TAB para autocompletar)*

*cd wildfly_producao/sk-restore-points*

*ls*

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403273257879)

 

*rm -rf 4.7b415/ 4.7b599/*

*(Dica para exclusão de pastas utilizamos a função **r** (recursive) e **f** (force))

*ls (Para confirmar a exclusão)*

 

#### **Remova pkgs baixados pelo WPM (Web Package Manager):**

*cd*

*cd sankhyaw-wpm/pkgs/*

*ls*

 

*

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403266072983)

*

 

*rm sankhya-w_4.7b656.pkg*

**(Dica verifique também se não existe a pasta wildfly_producao/sankhyaw-wpm/pkgs e realize o mesmo procedimento de exclusão)*

 

#### **Pare a aplicação e remova as pastas temporárias:**

*ps -ef | grep wildfly_producao*

*kill -9 [numero serviço]*

seta para cima para voltar o comando:

*ps -ef | grep wildfly_producao*

e conferir e o sistema está parado:

 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403266092823)

 

Acesse o diretório para exclusão das pastas temporárias:

*cd wildfly_producao/standalone*

*ls*

*rm -rf log/ sysmon/ tmp/*

 

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403273325463)

 

#### **Inicie o sistema novamente e verifique o espaço que foi liberado:**

*cd*

Opção 1:

*jb_startprod (caso não tenha o aliás criado iniciar utilizar a segunda opção)*

**Opção 2:**

*nohup /home/mgeweb/wildfly_producao/bin/standalone.sh -bmanagement 0.0.0.0 >& /dev/null &*

 

#### **Verificando o espaço liberado no procedimento:**

*df -h*

 

*

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403266181015)

*

Neste exemplo nossa partição / que estava com 100% ficou agora com 86% e com 4,7gb livres.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343630949783)

 OBSERVAÇÃO:**

Este procedimento é geralmente executado pela Equipe de TI da Empresa, que possui permissões de **ADMINISTRADOR.**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343614560151)

CAUSA:**

Mensagem apresentada devido à partição do HD em que o **SankhyaOm** está instalado ter chegado a 100% de ocupação.