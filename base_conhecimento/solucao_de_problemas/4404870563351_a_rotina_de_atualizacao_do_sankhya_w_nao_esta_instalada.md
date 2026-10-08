# A rotina de atualização do Sankhya-W não está instalada

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4404870563351-A-rotina-de-atualiza%C3%A7%C3%A3o-do-Sankhya-W-n%C3%A3o-est%C3%A1-instalada](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404870563351-A-rotina-de-atualiza%C3%A7%C3%A3o-do-Sankhya-W-n%C3%A3o-est%C3%A1-instalada)  
> **ID:** `4404870563351` | **Última Atualização:** 2026-07-22T15:22:53Z

---

WPM é a sigla de Web Package Manager, que como o próprio nome sugere, é um atualizador de pacotes executado via web (browser).

 

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16369490899351)

 MENSAGEM**:

A rotina de atualização do Sankhya-W não está instalada
Não foi encontrado dentro do servidor de aplicações a instalação do Atualizador Automático do Sankhya-W.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16369490901271)

 SOLUÇÃO:**

 

#### **Ambiente Windows:**

Acesse o [http://downloads.sankhya.com.br](http://downloads.sankhya.com.br) > Aplicações > WPM > Baixar .pkg

Localize a pasta **Sankhya-Om** Gerenciador de Pacotes > pkgs e coloque o arquivo baixado anteriormente:

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4404875229591)

 

Retorne na pasta **Sankhya-Om** Gerenciador de Pacotes > bin e execute o sankhyaw-package-manager.exe

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4404875254167)

 

**Opção [1]**

**Opção [S/N]: S**

Selecione o servidor que será atualizado via WPM

Selecione o pacote de atualização

[1] sankhya-w_atualizador-web-X.Xbxx.pkg

 

O processo de atualização do sistema foi executado com sucesso!

 

#### **Ambiente Linux:**

Acesse o servidor de aplicação onde está o **Sankhya-W** com usuário mgeweb:

 

Baixe o pacote em [http://downloads.sankhya.com.br](http://downloads.sankhya.com.br) > Aplicações > WPM > Baixar .pkg e transfira para o servidor via WinSCP ou FileZilla para o diretório:

 /home/mgeweb/sankhyaW_gerenciador_de_pacotes/pkgs

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15694886950423)

 

Ou pegando link ao fazer o download via Navegador Chrome (ctrl + J e botão direito 'Copiar endereço do link'):

 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4404870165015)

 

E dentro da pasta pkgs, dar o seguinte comando: (exemplo de link)

$ wget [https://downloads-sankhya-wpm.s3.amazonaws.com/sankhya-w_atualizador-web-9.0b54.pkg](https://downloads-sankhya-wpm.s3.amazonaws.com/sankhya-w_atualizador-web-9.0b54.pkg)

 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4404870253591)

 

Agora com o pacote baixado e na pasta pkgs, acesse o Gerenciador de Pacotes:

$ pwd

 /home/mgeweb/sankhyaW_gerenciador_de_pacotes/pkgs

$ cd ..

$ cd bin

$ ./sankhyaw-package-manager

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4404875254167)

Siga os mesmo passos do início do artigo.

O processo de atualização do sistema foi executado com sucesso!

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16369490902935)

 CAUSA:**

O WPM (Web Package Manager) não está instalado, foi deletado ou está corrompido, sendo necessário refazer a instalação.


---

### 🔗 Links e Referências Internas:

- [http://downloads.sankhya.com.br](http://downloads.sankhya.com.br)