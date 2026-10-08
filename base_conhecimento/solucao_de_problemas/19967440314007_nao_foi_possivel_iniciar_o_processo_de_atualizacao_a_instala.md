# Não foi possível iniciar o processo de atualização. A instalação não será iniciada. O modo modular está ativo e este Wildfly não é compatível

> **Módulo:** Solucao de Problemas | **Subseção:** Acessos/Banco de Dados  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/19967440314007-N%C3%A3o-foi-poss%C3%ADvel-iniciar-o-processo-de-atualiza%C3%A7%C3%A3o-A-instala%C3%A7%C3%A3o-n%C3%A3o-ser%C3%A1-iniciada-O-modo-modular-est%C3%A1-ativo-e-este-Wildfly-n%C3%A3o-%C3%A9-compat%C3%ADvel](https://ajuda.sankhya.com.br/hc/pt-br/articles/19967440314007-N%C3%A3o-foi-poss%C3%ADvel-iniciar-o-processo-de-atualiza%C3%A7%C3%A3o-A-instala%C3%A7%C3%A3o-n%C3%A3o-ser%C3%A1-iniciada-O-modo-modular-est%C3%A1-ativo-e-este-Wildfly-n%C3%A3o-%C3%A9-compat%C3%ADvel)  
> **ID:** `19967440314007` | **Última Atualização:** 2026-07-22T14:51:22Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19967450393111)

 **MENSAGEM:**

Não foi possível iniciar o processo de atualização.
A instalação não será iniciada. O modo modular está ativo e este Wildfly não é compatível. Atualize o WildFly para versão mais recente em nosso site [http://downloads.sankhya.com.br/](http://downloads.sankhya.com.br/).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19967450430231)

 CAUSA:**

O WPM (Web Package Manager) está desatualizado, não está instalado, foi deletado ou está corrompido, sendo necessário refazer a instalação.

 

A rotina de atualização do Sankhya-W não está instalada
Não foi encontrado dentro do servidor de aplicações a instalação do Atualizador Automático do Sankhya-W.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19967440282775)

SOLUÇÃO:**

WPM é a sigla de Web Package Manager, que como o próprio nome sugere, é um atualizador de pacotes executado via web (browser).

 

#### **Ambiente Windows:**

Acesse o [http://downloads.sankhya.com.br](http://downloads.sankhya.com.br/) > Aplicações > WPM > Baixar .pkg

Localize a pasta **Sankhya-Om** Gerenciador de Pacotes > pkgs e coloque o arquivo baixado anteriormente:

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/19967440290455)

 

Retorne na pasta **Sankhya-Om** Gerenciador de Pacotes > bin e execute o sankhyaw-package-manager.exe

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/19967450411031)

 

**Opção [1]**

**Opção [S/N]: S**

Selecione o servidor que será atualizado via WPM

Selecione o pacote de atualização

[1] sankhya-w_atualizador-web-X.Xbxx.pkg

 

O processo de atualização do sistema foi executado com sucesso!

 

#### **Ambiente Linux:**

Acesse o servidor de aplicação onde está o **Sankhya-W** com usuário mgeweb:

 

Baixe o pacote em [http://downloads.sankhya.com.br](http://downloads.sankhya.com.br/) > Aplicações > WPM > Baixar .pkg e transfira para o servidor via WinSCP ou FileZilla para o diretório:

 /home/mgeweb/sankhyaW_gerenciador_de_pacotes/pkgs

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/19967450413975)

 

Ou pegando link ao fazer o download via Navegador Chrome (ctrl + J e botão direito 'Copiar endereço do link'):

 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/19967450417175)

 

E dentro da pasta pkgs, dar o seguinte comando: (exemplo de link)

$ wget [https://downloads-sankhya-wpm.s3.amazonaws.com/sankhya-w_atualizador-web-9.0b54.pkg](https://downloads-sankhya-wpm.s3.amazonaws.com/sankhya-w_atualizador-web-9.0b54.pkg)

 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/19967440300055)

 

Agora com o pacote baixado e na pasta pkgs, acesse o Gerenciador de Pacotes:

$ pwd

 /home/mgeweb/sankhyaW_gerenciador_de_pacotes/pkgs

$ cd ..

$ cd bin

$ ./sankhyaw-package-manager

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/19967450411031)

Siga os mesmo passos do início do artigo.

O processo de atualização do sistema foi executado com sucesso!


---

### 🔗 Links e Referências Internas:

- [http://downloads.sankhya.com.br/](http://downloads.sankhya.com.br/)