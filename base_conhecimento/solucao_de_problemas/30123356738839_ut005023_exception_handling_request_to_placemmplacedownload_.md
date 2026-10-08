# "UT005023: Exception handling request to /placemm/place/download: java.lang.OutOfMemoryError: Java heap space"

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30123356738839--UT005023-Exception-handling-request-to-placemm-place-download-java-lang-OutOfMemoryError-Java-heap-space](https://ajuda.sankhya.com.br/hc/pt-br/articles/30123356738839--UT005023-Exception-handling-request-to-placemm-place-download-java-lang-OutOfMemoryError-Java-heap-space)  
> **ID:** `30123356738839` | **Última Atualização:** 2026-07-22T14:36:31Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30123356728727)

 **MENSAGEM:**

"UT005023: Exception handling request to /placemm/place/download: java.lang.OutOfMemoryError: Java heap space"

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30891465970071)

 SITUAÇÃO:**

Esse erro ocorre ao **tentar instalar ou atualizar um add-on** no SankhyaOM. Durante esse processo, o sistema precisa alocar memória para manipular os arquivos e concluir a instalação, mas pode falhar devido a **limitações de memória disponíveis no ambiente**.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30123356729751)

SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31046593462167)

 ****Garanta que o ambiente atenda aos requisitos mínimos** recomendados para o SankhyaOM. O ideal é que o servidor tenha **pelo menos 4GB de RAM** para um funcionamento adequado.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31046599839639)

 Método 1: Configuração via WPM (recomendado)**

- 

Acesse o **WPM** no SankhyaOM;

- 

Vá até a aba **Configurações;**

- 

Na seção **Configurações de memória do WildFly**, ajuste os valores de:

  - 

**Memória inicial (MB):** defina um valor adequado (exemplo: 4096 MB).

  - 

**Memória máxima (MB):** ajuste conforme necessário (exemplo: 8192 MB).

- 

Clique em **Salvar** e reinicie o servidor.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31046599839639)

 Método 2: Configuração manual no arquivo **

- 

No Windows, edite o arquivo `standalone.conf.bat` e ajuste a linha:

```text
set "JAVA_OPTS=%JAVA_OPTS% -Xms4096m -Xmx8192m"

```

 

- 

No **Linux**, edite o arquivo standalone.conf que está localizado em:

```text
/home/mgeweb/wildfly_XXXX/bin/standalone.conf
```

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31046599841687)

 Reinicie o servidor** para aplicar as mudanças e tente novamente executar a instalação ou atualização do add-on.

 

**Atenção: os valores citados são apenas exemplos. A definição ideal deve considerar a quantidade total de RAM disponível no servidor e a demanda do ambiente.**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30123356730391)

CAUSA:**

O erro **"Java heap space"** indica que o Java atingiu o limite máximo de memória alocada, impossibilitando a execução da operação. Isso pode ocorrer por diversos motivos, incluindo:

- 

**Baixa quantidade de memória RAM disponível** no servidor/máquina onde o SankhyaOM está rodando.

- 

**Configuração inadequada da memória da JVM**, limitando a alocação necessária para processar a instalação do add-on.