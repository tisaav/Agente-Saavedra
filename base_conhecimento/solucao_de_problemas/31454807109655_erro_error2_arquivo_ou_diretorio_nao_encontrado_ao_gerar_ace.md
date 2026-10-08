# Erro: "error=2, Arquivo ou diretório não encontrado" ao gerar Acesso Remoto

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31454807109655-Erro-error-2-Arquivo-ou-diret%C3%B3rio-n%C3%A3o-encontrado-ao-gerar-Acesso-Remoto](https://ajuda.sankhya.com.br/hc/pt-br/articles/31454807109655-Erro-error-2-Arquivo-ou-diret%C3%B3rio-n%C3%A3o-encontrado-ao-gerar-Acesso-Remoto)  
> **ID:** `31454807109655` | **Última Atualização:** 2026-07-24T12:43:53Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31454816397975)

 MENSAGEM:**

error=2, Arquivo ou diretório não encontrado

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31454807104663)

 SITUAÇÃO:**

Ao configurar um acesso remoto no sankhya OM, que use um servidor Linux, pode aparecer a mensagem citada acima, o que indica que o comando netstat não está disponível no sistema.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31454807105559)

 SOLUÇÃO:**

Para que o acesso remoto funcione corretamente, é necessário que o utilitário netstat esteja disponível no sistema operacional. Este comando faz parte do pacote net-tools, que pode ser instalado via YUM ou outro gerenciador de pacotes, dependendo da distribuição Linux em uso.

 

### **Instalação do pacote**

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31455341831831)

 ****Verifique a distribuição e versão do Linux: **

Antes de seguir com a instalação, é recomendável confirmar qual sistema está sendo utilizado. Para isso:

- Abra o programa Putty;

- Configure o endereço do servidor de aplicação;

- Informe usuário e senha para o login;

- Execute o seguinte comando:

 

```text
cat /etc/os-release
```

O resultado deve trazer algo como:

```text
NAME="CentOS Linux"
VERSION="7 (Core)"
```

 

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32769825140631)

 **Dica: **caso esteja utilizando uma **distribuição diferente** (ex: Ubuntu, Debian), o comando de instalação será diferente. **Exemplos:**

- Ubuntu/Debian:

```text
sudo apt install net-tools
```

 

- CentOS/RHEL:

```text
sudo yum install net-tools
(ou dnf em versões mais recentes)
```

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31455332894743)

 ****Instale o pacote net-tools no servidor Linux (CentOS 7):**

```text
sudo yum install net-tools
```

 

### **Correção de possível erro**

Se ao executar o comando acima for exibido um erro "404 ao instalar o net-tools no CentOS", como exemplo abaixo:

 

```text
http://mirror.centos.org/centos/7/os/x86_64/repodata/repomd.xml: [Errno 14] HTTP Error 404 - Not Found
One of the configured repositories failed (CentOS-7 - Base)...
```

 

**Significa que a versão do CentOS** (ex: 7.7) **está **utilizando repositórios **desatualizados. Para resolver, faça os seguintes ajustes nos repositórios do YUM:**

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31455341831831)

 **Edite o arquivo principal de repositórios:

```text
sudo vi /etc/yum.repos.d/CentOS-Base.repo
```

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31455332894743)

 **Substitua as linhas com `baseurl=` para apontar para o repositório de arquivos antigos (Vault):

```text
baseurl=http://vault.centos.org/7.7.1908/os/x86_64/
baseurl=http://vault.centos.org/7.7.1908/updates/x86_64/
baseurl=http://vault.centos.org/7.7.1908/extras/x86_64/
baseurl=http://vault.centos.org/7.7.1908/centosplus/x86_64/
```

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31455332897687)

 Comente ou remova as linhas que começam com mirrorlist=;

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31455332905367)

 Garanta que enabled=1 esteja ativado para os repositórios em uso;

**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31455341838103)

** Limpe o cache e refaça a instalação:

 

```text
yum clean all
yum makecache
yum install net-tools
```

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31454816400791)

 CAUSA:**

O erro ocorre devido à ausência do pacote **"net-tools"** no servidor Linux. O sistema Sankhya utiliza o comando **"netstat"**, que faz parte deste pacote, para validar e estabelecer a conexão remota. Quando o **"net-tools"** não está instalado, o sistema não consegue localizar o arquivo executável necessário, resultando na mensagem **"error=2, Arquivo ou diretório não encontrado"**.Este problema é específico de ambientes Linux e pode ocorrer tanto em bases de produção quanto em bases de teste ou treinamento, desde que o servidor não possua o pacote instalado.