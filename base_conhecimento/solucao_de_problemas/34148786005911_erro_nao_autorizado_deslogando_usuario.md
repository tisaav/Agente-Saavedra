# Erro “Não Autorizado” deslogando usuário

> **Módulo:** Solucao de Problemas | **Subseção:** Erros Internos  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34148786005911-Erro-N%C3%A3o-Autorizado-deslogando-usu%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/34148786005911-Erro-N%C3%A3o-Autorizado-deslogando-usu%C3%A1rio)  
> **ID:** `34148786005911` | **Última Atualização:** 2026-09-04T17:31:30Z

---

![Erro de sessão](https://ajuda.sankhya.com.br/hc/article_attachments/34148785996567)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34148785995927)

**MENSAGEM**

Erro: "Não autorizado" ou encerramento aleatório de sessões.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34148756032279)

**SITUAÇÃO**

Durante o uso do sistema operando com o layout Flex, o usuário recebe a mensagem **"Não autorizado"** e é desconectado automaticamente. Usando o layout HTML, o usuário é desconectado de forma repentina ou apresenta encerramento aleatório de sessões antes do tempo pré-definido de inatividade, mesmo estando ativo no sistema.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34148756032663)

**SOLUÇÃO**

A atualização do WildFly é uma atividade de infraestrutura que deve ser executada por um profissional com conhecimento técnico em banco de dados e servidores de aplicação. O Service Desk não realiza este procedimento.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34148756033303)

**Atualize o WildFly:**

- 

Verifique a versão do **"WildFly"**. Para garantir a compatibilidade com as versões atuais do sistema, é fundamental utilizar o **WildFly 23 mod_03** (disponível na [Central de Downloads Sankhya](https://downloads.sankhya.com.br/downloads?app=WildFly&c=1)). Selecione a versão correspondente ao seu banco de dados (Oracle ou SQL Server).

 

- [Como atualizar o Wildfly - Linux?](https://ajuda.sankhya.com.br/hc/pt-br/articles/35196444326423-Como-atualizar-o-Wildfly-Linux)

- [Como atualizar o Wildfly em sistema operacional Windows](https://ajuda.sankhya.com.br/hc/pt-br/articles/38109965528087-Como-atualizar-o-Wildfly-em-sistema-operacional-Windows)

![Observação](https://ajuda.sankhya.com.br/hc/article_attachments/34180140765847)

**Observação:** Caso não tenha conhecimento técnico para realizar a instalação, entre em contato com o time de TI ou com os responsáveis pelo servidor.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34148785998359)

**Configurações adicionais:**

- 

Se você utilizou o **WildFly 23 mod_03** oficial da Central de Downloads, não é necessário configurar manualmente o parâmetro **"disable-session-id-reuse"**, pois esta versão já possui o **"disable-session-id-reuse=true"** nativo na seção **"servlet-container"** do arquivo standalone.xml.

- 

Caso esteja utilizando outra versão, adicione o parâmetro **"disable-session-id-reuse=true"** na seção **"servlet-container"** do arquivo standalone.xml, localizado em:

/home/mgeweb/wildfly_producao/standalone/configuration
 

![Configurações WildFly](https://ajuda.sankhya.com.br/hc/article_attachments/34324362124183)

**Importante:** Para salvar essa alteração, é necessário que o sistema esteja parado.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34148785998743)

**Alteração do arquivo undertow-core-2.2.5.Final.jar:**

- 

Dentro do servidor de aplicação, acesse o caminho abaixo, renomeie o arquivo **"undertow-core-2.2.5.Final.jar"** para **"undertow-core-2.2.5.Final_OLD.jar"**. Após renomear, baixe o novo arquivo [clicando aqui](https://drive.google.com/file/d/1sR-mpmKfX6q2Uxhg6QmYDGpV7UXvCsU7/view?usp=sharing) e mova para o diretório:

wildfly_producao\modules\system\layers\base\io\undertow\core\main
 

**Importante:** Este arquivo só pode ser alterado se o Wildfly realmente estiver atualizado para a versão 23.0. O sistema deve estar parado para salvar a alteração.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34148785999127)

**Atualize o Módulo Financeiro:**

- 

Após reiniciar o servidor, acesse a tela **"Administração do Servidor"** (Configurações >> Infraestrutura >> Administração do Servidor) e clique em **"Atualizar Sistema"**. Na aba **"Atualizações de módulos"**, faça a atualização do **"Financeiro BFF"** para a última versão.

- 

Essa atualização inclui correções relacionadas ao erro e não exige reinicialização adicional.

![Atualização de módulos](https://ajuda.sankhya.com.br/hc/article_attachments/34344337612055)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34148786003223)

**CAUSA**

O encerramento inesperado de sessões ocorre devido a incompatibilidades do servidor WildFly com as versões atuais do sistema. Quando a atualização é realizada sem a versão correta (WildFly 23 mod_03) ou sem as configurações de persistência de sessão, o sistema apresenta falhas de autenticação **"Não Autorizado"**, desconexões aleatórias ou consumo indevido de licenças.


---

### 🔗 Links e Referências Internas:

- [Central de Downloads Sankhya](https://downloads.sankhya.com.br/downloads?app=WildFly&c=1)
- [Como atualizar o Wildfly - Linux?](https://ajuda.sankhya.com.br/hc/pt-br/articles/35196444326423-Como-atualizar-o-Wildfly-Linux)
- [Como atualizar o Wildfly em sistema operacional Windows](https://ajuda.sankhya.com.br/hc/pt-br/articles/38109965528087-Como-atualizar-o-Wildfly-em-sistema-operacional-Windows)