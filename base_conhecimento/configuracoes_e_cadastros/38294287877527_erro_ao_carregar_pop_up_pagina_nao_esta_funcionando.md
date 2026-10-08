# Erro ao carregar pop-up "Página não está funcionando"

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38294287877527-Erro-ao-carregar-pop-up-P%C3%A1gina-n%C3%A3o-est%C3%A1-funcionando](https://ajuda.sankhya.com.br/hc/pt-br/articles/38294287877527-Erro-ao-carregar-pop-up-P%C3%A1gina-n%C3%A3o-est%C3%A1-funcionando)  
> **ID:** `38294287877527` | **Última Atualização:** 2026-09-10T20:36:09Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38294287860887)

 **MENSAGEM**

Está Página não está funcionando 

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38294287861911)

 SITUAÇÃO**

Ao tentar abrir algum **pop-up **do sistema, o mesmo fica em branco ou apresenta a mensagem "está página não está funcionando".

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38586624637975)

 ATENÇÃO**:** **

O procedimento a seguir deve ser executado **exclusivamente por um Administrador de Sistemas com conhecimento em Linux** ou pela **equipe de Cloud**, caso o ambiente esteja hospedado em nuvem. Antes de iniciar, é **obrigatória a verificação da versão do WildFly em uso**. As configurações descritas neste procedimento **aplicam-se somente ao WildFly versão 23**. A execução em versões diferentes pode causar falhas na inicialização, comportamentos inesperados ou indisponibilidade do ambiente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38586624638999)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38294287863319)

 Acesse o arquivo** standalone.xml **dentro do servidor aplicação.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38294287863703)

 Dentro do arquivo localize linha descrita como "**server name="**  

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38294316366743)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38294287864727)

 Localize o **listener** configurado, que pode estar como **HTTP** ou **HTTPS**, especialmente se houver certificado SSL autoassinado configurado diretamente no **WildFly**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38294316367383)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38294287866263)

 Na mesma linha, adicione o seguinte parâmetro:

```text
 allow-unescaped-characters-in-url="true"
```

**Exemplo**:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38294287866647)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38294287867415)

 Após realizar a alteração, salve o arquivo. Caso esteja utilizando o **vi** na linha de comando, execute `:wq!` para salvar e sair.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38586379869207)

 Em seguida, reinicie o **WildFly** para que a configuração seja aplicada.

```text
jb_startprod
```

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38294316369815)

CAUSA:**

O erro acontece por uma limitação do **Undertow**, servidor utilizado pelo **WildFly**, que não permite alguns caracteres especiais na URL, como as chaves `{}`.

```text
Referencia: https://datatracker.ietf.org/doc/html/rfc1738#page-3
```

 

O Undertow aplica essa restrição nas versões do WildFly, pois quando a URL de um pop-up é construída, podem ser utilizados caracteres especiais como `{}`, o que faz com que a requisição seja bloqueada.

 

![image - 2026-02-23T163650.079.png](https://ajuda.sankhya.com.br/hc/article_attachments/38586379869463)

 

Para permitir o uso desses caracteres e contornar essa limitação do servidor, deve ser adicionado o parâmetro `allow-unescaped-characters-in-url="true" `.

Alguns exemplos de telas que utilizam esse tipo de pop-up são:

- 

Portal de Importação XML

- 

Módulo Java

- 

Construtor de Componentes BI

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38294316371351)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38294287869591)