# Address already in use: JVM_Bind

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360053414433-Address-already-in-use-JVM-Bind](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053414433-Address-already-in-use-JVM-Bind)  
> **ID:** `360053414433` | **Última Atualização:** 2026-07-22T15:29:01Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524322451095)

 MENSAGEM**:

Address already in use: JVM_Bind

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524322459159)

 CAUSA**:

Ocorre quando outra aplicação já está utilizando a porta 10050 (porta padrão utilizada pelo SAS), sendo necessário alterar a porta de comunicação do SAS, ou encerrar a aplicação que está utilizando a porta 10050.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524334895895)

 SOLUÇÃO**:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524334897559)

 Identificar se a porta 10050 está em uso por outro aplicativo, via prompt de comando(CMD).

1.1- Abra o prompt de comando clicando em Iniciar / Executar e Digite CMD e pressione Enter;

1.2-Digite o comando: **netstat -o -n –a**

Será apresentado o Endereço de IP, seguido da porta (0.0.0.0:10050) e o processo(PID)

![2020-09-10.png](https://ajuda.sankhya.com.br/hc/article_attachments/360088733454)

1.3-Agora será preciso, encontrar qual é a aplicação que está trabalhando na porta 10050. Uma dica de comando, pode ser usado, conforme exemplo abaixo.

Descobrir quais aplicações estão trabalhando na porta  10050.
**netstat -o -n -a | findstr  0.0:10050**
**0.0  são os dois números finais do IP 0.0.0.0 e 10050 é a porta**

![2020-09-10__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/360089886813)

No exemplo, foi encontrado apenas uma aplicação utilizando a porta consultada, e também o número do processo(PID) que é 12148

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524322481943)

 Abra o Gerenciador de Tarefas clicando em Iniciar / Executar e digite taskmgr e pressione Enter;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524334909847)

 Selecione a Aba Detalhes,

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524334912023)

 Consulte pela coluna PID qual o processo que esta executando na porta consultada no passo 1

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524334921367)

 Se a aplicação que esta usando a porta 10050 não for o SAS, é possível alterar a configuração do SAS para rodar em outra porta, para isso

5.1-Acesse o diretório onde esta instalada o SAS [<SAS_HOME>/conf/sas.cfg]
Na pasta CONF, abra o arquivo SAS.cfg em um bloco de nota e edite o ultimo trecho
server.port=**10051
**ou para outra porta acima de 10050

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524322505367)

 Configurações » Avançado » Preferências
Altere a porta do parâmetro **IP do servidor de acessos - IPSERVACESS**, para a nova porta configurada no item 5
Exemplo: **IPDOSERVIDOR:10051**

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18524322511127)

 Execute a inicialização novamente do SAS, reinicie a aplicação do Sistema(WildFly).