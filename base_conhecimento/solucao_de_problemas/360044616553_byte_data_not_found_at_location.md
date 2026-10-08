# Byte data not found at location

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616553-Byte-data-not-found-at-location](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616553-Byte-data-not-found-at-location)  
> **ID:** `360044616553` | **Última Atualização:** 2026-07-22T15:53:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582238855831)

 MENSAGEM:**

[CORE_E02510]: Byte data not found at location:/home/mgeweb/modelos/logo-sk.gif

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582238858263)

SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582238860823)

 Acesse a tela "**Preferências" ** *(Caminho de acesso: Configurações » Avançado):*

- Chave **"SERVDIRMOD'- Pasta de modelos para impressão"**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582253082519)

 O caminho definido no parâmetro acima deverá ser acessado na respectiva máquina/servidor.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582238867223)

 Ao localizar a pasta, a logo deverá constar com o mesmo nome referenciado no caminho do parâmetro.

 

**Exemplo:**

No endereço indicado no parâmetro abaixo está definido que deverá existir uma logo nomeada como **logo-sk**, dentro da pasta **'modelos'**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15412208939287)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582253088791)

 IMPORTANTE:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582238860823)

 Deve-se observar o tamanho (kb,Mb) da logomarca, para que não demore a gerar o relatório por ser uma logomarca muito grande.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582253082519)

 Outra opção indicada é o uso de Repositórios de Arquivos *(Caminho de acesso: Configurações » Avançado » Repositório de Arquivos)*, detalhes sobre o uso do repositório acesse o 'Manual' : [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582238867223)

 Se houver alteração no diretorio/caminho, como exemplo: Documento 112404: Byte data not found at location: **C:\Jiva\banco-do-brasil.png**

 

**Exemplo do diretório em um modelo:
**<image>
<reportElement x="3" y="8" width="112" height="47"/>
<imageExpression class="java.lang.String"><![CDATA["**C:\\Jiva\\banco-do-brasil.png**"]]></imageExpression>
</image>

 

Neste caso, faça o ajuste no modelo.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582253091095)

 CAUSA:**

Ao tentar emitir um relatório e/ou impressão de pedidos e notas, quando esse possuir uma logomarca e uma das situações mencionadas abaixo ocorrer, será apresentada a mensagem;

- Logomarca não esta inserida no diretório/caminho  informado no parâmetro SERVDIRMOD;

- Falta do diretório no parâmetro;

- Nome da logomarca diferente do nome setado no *.jrxml;

- Verifique também o parâmetro FREPBASEFOLDER, que não pode estar vazio, deve conter o caminho, caso esteja usando este para repositório da logo.


---

### 🔗 Links e Referências Internas:

- [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594)