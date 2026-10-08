# Aplicativo IREPORT 4.0 não abre no computador

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110194-Aplicativo-IREPORT-4-0-n%C3%A3o-abre-no-computador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110194-Aplicativo-IREPORT-4-0-n%C3%A3o-abre-no-computador)  
> **ID:** `360044110194` | **Última Atualização:** 2026-09-02T18:45:45Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585146508823)

 SITUAÇÃO:**

Não é possível abrir o aplicativo [IREPORT 4.0](https://downloads-sankhya-tools.s3-sa-east-1.amazonaws.com/iReport-4.0.1.zip) no computador. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585111140119)

 SOLUÇÃO:**

Para correção seguir os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585146527511)

 É necessário baixar o Instalador do JRE 7 e executar a instalação normalmente.

Encontre o diretório onde foi instalado a JRE 7.

Exemplo: **C:\Program Files (x86)\Java\jre7**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585111150231)

 Acesse a Pasta onde foi extraído/instalado o Ireport 4.0.

Exemplo: **C:\iReport-4.0.1**

Acesse a pasta 'ETC' e abra o arquivo 'ireport.conf' em um Bloco de Notas ou Notepad++

Tem um trecho com a seguinte informação: #jdkhome="/path/to/jdk"

Retire o **#** e informe o caminho onde foi instalado a JRE7.

jdkhome="**C:\Program Files (x86)\Java\jre7**"

Salve o arquivo alterado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585146547479)

 Abra o Ireport 4.0 novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585146556823)

 CAUSA:**

O aplicativo Ireport 4.0 aceita as funcionalidades do JAVA 8, porém precisa que esteja instalado a JRE 7.

Ocorre em computadores que atualizaram o JAVA para o 8 ou Superior. A Instalação da JRE 7 em nada influenciará em outras funcionalidades do JAVA no Computador.

Deve ser efetuado em computadores que utilizam o Ireport 4.0 (Única versão homologada pela Sankhya), para criação/manutenção de relatórios/modelos *.jrxml, utilizado pelo SankhyaW.