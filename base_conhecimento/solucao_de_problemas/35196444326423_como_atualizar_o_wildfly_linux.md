# Como atualizar o Wildfly - Linux?

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35196444326423-Como-atualizar-o-Wildfly-Linux](https://ajuda.sankhya.com.br/hc/pt-br/articles/35196444326423-Como-atualizar-o-Wildfly-Linux)  
> **ID:** `35196444326423` | **Última Atualização:** 2026-07-22T14:25:47Z

---

##### É fundamental manter o **Wildfly **sempre atualizado para a versão mais recente (versão 23 mod_03). Essa prática garante a compatibilidade do ambiente Sankhya com as últimas versões do JDK e demais componentes de infraestrutura. Além disso, a atualização traz ganhos de desempenho e estabilidade, reduzindo o risco de falhas em produção e fortalecendo a segurança da aplicação.

#####  

##### 
**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220906844055)

 ****IMPORTANTE: **O procedimento de atualização deve ser executado exclusivamente por um **DBA com conhecimento em Linux**, ou pela equipe da Cloud caso o ambiente esteja hospedado em nuvem. Antes de iniciar o processo, é obrigatório validar a versão do **JDK** em uso. O **Wildfly 23 é compatível com o JDK 8u421(preferencialmente deve-se utilizar essa) até o JDK 11**, portanto, essa versão deve estar instalada e ativada no servidor para que o ambiente funcione corretamente.

 

#### 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35196423331991)

 **Instalação**

##### **

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524491973271)

 Acesse o servidor** onde o Wildfly está instalado e pare o serviço da aplicação Sankhya.

##### 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35196423333527)

 Logue-se como `root` e acesse o usuário `mgeweb`.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35196423334167)

 Crie um backup do diretório atual do Wildfly:

```text
mv wildfly_producao wildfly_producao_OLD
```

 

![image - 2026-02-20T095121.178.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524464800151)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35196444300439)

  Acesse o portal de **Downloads Sankhya Wildfly** com seu Sankhya ID;

 

![image - 2026-02-20T095227.360.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524464800535)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35196444301079)

 Faça o download do pacote correspondente ao seu banco de dados. Copie o link do arquivo e baixe via `wget` e o servidor de aplicação no caminho `/home/mgewe`:

 

![image - 2026-02-20T095304.809.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524491978519)

 

```text
wget <link_copiado>
```

 

![image - 2026-02-20T095342.819.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524464801943)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35196444305047)

  Descompacte o pacote:

```text
unzip Wildfly_23.0_Sankhya_mod_03_oracle.zip
```

 

Caso o `unzip` não esteja disponível:

```text
sudo apt update
sudo apt install unzip
```

 

Arquivo** wildfly_producao **após descompactado: 

 

![image - 2026-02-20T095433.342.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524464803351)

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35196444305687)

 Configure o servidor no **PKG (SankhyaW Package Manager)**:

- 

Acesse `/home/mgeweb/sankhyaW_gerenciador_de_pacotes/bin/`

- 

Execute:

```text
./sankhyaw-package-manager
```

 

- 

**Selecione a opção 2:** Selecionar servidor

- 

**Selecione a opção 2:** Configurar arranjo de portas

- 

Escolha `wildfly_producao` (agora com Wildfly 23)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35196423339927)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35203441806999)

 

##### 
**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220906844055)

 ****IMPORTANTE:** O Wildfly altera a porta padrão para **8080**. Ajuste para a porta correta de produção (geralmente **8180**).

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35196423339671)

 Copie integralmente o arquivo `standalone.conf` do ambiente anterior (`wildfly_producao_old`) e substitua o arquivo correspondente no **WildFly 23**, assegurando a preservação completa das configurações de JVM.

- 

Com esse procedimento, **permanecem inalterados os parâmetros de memória**, as **configurações de Garbage Collector (GC)**, as **flags de performance**, as **variáveis de ambiente** e demais argumentos previamente definidos no **WildFly** antigo.

 

![image - 2026-02-20T095648.798.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524491983127)

 

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220906847255)

 Ajuste os dados de conexão do banco de dados conforme instruções do DBA.

 

![image - 2026-02-20T095744.795.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524491984279)

 

##### 
**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220906844055)

 ****IMPORTANTE:** Os dados acima são individuais. Verifique também a porta HTTP, a padrão é 8080, porém se for 8180, ajuste no PKG em "Configurar arranjo de portas".

#####  

![image - 2026-02-20T095913.816.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524491986199)

 

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220971499031)

 No diretório `/home/mgeweb/wildfly_producao/standalone/deployments`, garanta que apenas `mge-ds.xml` e `wpm.war` estejam presentes.

- 

Se `**mge-ds.xml**`** estiver ausente, reveja a configuração no PKG;**
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35196444309527)

 

- 

Também é **possível alterar a memória no WPM**, aba **"configurações".**

 

![11 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220971501463)

 Inicie o servidor com o alias:

```text
jb_startprod
```

 

![12 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35221016038295)

 **Acesse o WPM do Sankhya, seguindo o exemplo** **de link abaixo**, e configure a memória (se necessário). 

 

![image - 2026-02-20T100120.362.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524464807319)

 

- 

**Senha padrão do WPM:** `tecsis` (confirmar com responsável caso seja diferente). 

 

![image - 2026-02-20T100309.831.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524464808087)

 

![13 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220971504919)

 **Ajuste também os dados de conexão de banco **e salve as configurações.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35204428375447)

 

![14 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220971505943)

 **Instale a mesma versão do sistema utilizada anteriormente ou o último release da mesma versão.**

![15 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35220971507735)

 **Valide o funcionamento** do ambiente atualizado.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38524464811415)

 CAUSA**

A atualização do Wildfly é necessária para manter o ambiente **compatível com as versões atuais do JDK, do Java e do próprio Sankhya**, garantindo a continuidade do suporte técnico oficial. Além disso, a atualização corrige vulnerabilidades, melhora o desempenho e a estabilidade do servidor de aplicações.

Ambientes que permanecem em versões antigas podem apresentar:

- 

falhas de deploy;

- 

quedas repentinas durante o uso do sistema;

- 

incompatibilidade com novos recursos;

- 

instabilidade em alta carga;

- 

indisponibilidade de correções de segurança.

A não atualização compromete tanto o funcionamento do sistema quanto a segurança e a manutenção futura do ambiente.