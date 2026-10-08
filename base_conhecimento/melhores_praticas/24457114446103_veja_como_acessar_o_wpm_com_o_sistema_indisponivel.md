# Veja como acessar o WPM com o sistema indisponível

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24457114446103-Veja-como-acessar-o-WPM-com-o-sistema-indispon%C3%ADvel](https://ajuda.sankhya.com.br/hc/pt-br/articles/24457114446103-Veja-como-acessar-o-WPM-com-o-sistema-indispon%C3%ADvel)  
> **ID:** `24457114446103` | **Última Atualização:** 2026-07-22T14:46:45Z

---

**Para acessar o WPM mesmo quando o sistema estiver indisponível, siga os passos abaixo:
**

 

### **Servidores Linux (WildFly):**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168374693399)

 Acesse o servidor de aplicações no qual o serviço Sankhya/WildFly está instalado;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168374697495)

 Pare o serviço do WildFly;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168383106327)

 Se o servidor tiver os aliás configurados, execute os seguintes comandos para parar e iniciar o serviço do WildFly utilizando o usuário mgeweb:

- 

  - Para parar a base de produção: killprod

  - Para parar a base de teste: killteste

  - Para parar a base de treinamento: killtreina

  - Para iniciar a base de produção: jb_startprod

  - Para iniciar a base de teste: jb_startteste

  - Para iniciar a base de treinamento: jb_starttreina 

(O start do serviço deve ser realizado apenas quando os arquivos sankhyaw.ear forem excluídos)

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168389020183)

 **Navegue até o diretório padrão de instalação do WildFly: */home/mgeweb/wildfly_producao/standalone/deployments* (esse diretório pode variar dependendo de como foi feita a instalação do WildFly no servidor).

 

**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168380623511)

 **Exclua os arquivos que contêm o nome *sankhyaw.ear*. No Linux, para excluir os arquivos, utilize o comando* rm -rf* juntamente com o nome dos arquivos. Exemplo: r*m -rf sankhyaw.ear sankhya.ear.deployed*

 

**

![Como acessar o WPM com o sistema indisponível 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169590043287)

**

 

****

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169188807831)

****Após a exclusão dos arquivos, inicie novamente o serviço do WildFly.

 

### **Servidores Windows (WildFly):**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168374693399)

 Acesse a tela “Serviços” do Windows;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168374697495)

 Localize o serviço do WildFly;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168383106327)

 Pare o serviço do WildFly;

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168389020183)

 Clique com o botão direito do mouse sobre o serviço e selecione “Propriedades”;

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168380623511)

 Identifique o diretório de instalação do WildFly;

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169188807831)

 Realize a exclusão dos arquivos `sankhyaw.ear` que constam no diretório `deployments`;

 

![Como acessar o WPM com o sistema indisponível 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169581471767)

** 

![Como acessar o WPM com o sistema indisponível 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169581475863)

 
 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169188828055)

 Após excluir esses arquivos, inicie novamente o serviço do Wildfly na tela "Serviços".
 
**

### **Registro de Novo Servidor (WPM) no Navegador Sankhya:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25168374693399)

 Abra o Navegador Sankhya e faça o registro de um novo servidor através botão **"Configurações"** no canto superior direito do Navegador Sankhya, e informe o IP/Link de Acesso ao sistema e adicione `/wpm` ao final. Exemplo:

- 

  - Para acessar o sistema: `localhost:8180/mge`

  - Para acessar o WPM: `localhost:8180/wpm`

**  

![Como acessar o WPM com o sistema indisponível 4.png](https://ajuda.sankhya.com.br/hc/article_attachments/25169590071063)

 
Após cadastrar o novo servidor do WPM (`localhost:8180/wpm`) no Navegador Sankhya, selecione o mesmo após os procedimentos terem sido realizados e, assim, conseguirá acessar o WPM normalmente, mesmo que o sistema esteja indisponível.
 

![Imagem](/attachments/token/B8LNqb1JSbb3Zui1iyYKC1Lit/?name=image.png)

 
**Observação:** O link *localhost* é apenas um exemplo. Em sua base, o link de acesso e IP provavelmente serão diferentes.**

Se mesmo seguindo essa orientações você não conseguir acessar o WPM, por favor, entre em contato com o Service Desk Sankhya para assistência adicional.