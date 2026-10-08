# Processo de Integração

> **Módulo:** Imobiliária | **Subseção:** Imobiliária  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o)  
> **ID:** `360057141853` | **Última Atualização:** 2026-07-29T14:11:35Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311457841047)

 **Módulo:** Imobiliária > Rotinas    

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311461914263)

 **Versão disponível:** a partir da 3.31
```

Existem duas telas principais para que todo o processo de integração do Sankhya Om com os Portais Online seja funcional:

- Processo de Integração;

- 
[Tipos de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055936693-Tipos-de-Im%C3%B3veis).

Acesse os links abaixo para facilitar sua navegação nos processos de integrações:

[Tipos de Imóveis](#tiposdeim%C3%B3veis)                                                                           [Processo de Integração](#processodeintegra%C3%A7%C3%A3o)

[Gerar Requisição](#gerarrequisi%C3%A7%C3%A3o)

## 
Tipos de Imóveis

A primeira ação que você precisará fazer, é criar Tipos de Imóveis que estejam vinculados com os Portais disponíveis visto que, cada Portal Online tem seu estilo de requisição. Esse procedimento é realizado através da tela [Tipos de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055936693-Tipos-de-Im%C3%B3veis), aba **"Portais Web"**.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360093662254)

[[voltar ao topo]](#top)

## 
Processo de Integração

Após configurar os Tipos de Imóveis, crie um Processo de Integração. Essa etapa serve para filtrar os imóveis passados na requisição para o Portal. 

Na aba **"Processo de Integração"** estão todos os campos de combinação para gerar a requisição.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360095917073)

Acesse os links abaixo para verificar a configuração dos campos de Combinação:

[Sub-aba Portais](#sub-abaportais)          [Sub-aba Fontes](#sub-abafontes)           [Sub-aba Filtros](#sub-abafiltros)            [Sub-aba Ordenadores](#sub-abaordenadores) 

[Sub-aba Coletores](#sub-abacoletores)     [Sub-aba Tradutores](#sub-abatradutores)   [Sub-aba Geradores](#sub-abageradores)    [Outras sub-abas](#outrassub-abas)

**Sub-aba Portais**

Através desta sub-aba você cadastra novos portais. Caso os campos desta sub-aba sejam preenchidos, somente serão processados os imóveis inclusos em algum plano do Portal especificado.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360093666114)

[[voltar ao subtítulo]](#processodeintegra%C3%A7%C3%A3o) 

**Sub-aba Fontes**

Esta sub-aba tem o objetivo de selecionar, via SQL, os imóveis que irão para a requisição (faz um select no banco de dados).

**Nota:** Já existe um padrão a ser utilizado, porém, pode ser alterado por você.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/360095920593)

[[voltar ao subtítulo]](#processodeintegra%C3%A7%C3%A3o) 

**Sub-aba Filtros**

Nesta sub-aba, é feito o filtro via SQL, dos Imóveis encontrados em **"fontes"**.

**Observação:** Também já existe um padrão pré-definido, podendo ser alterado.

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/360095920733)

[[voltar ao subtítulo]](#processodeintegra%C3%A7%C3%A3o)

**Sub-aba Ordenadores**

Aqui você pode realizar a ordenação via SQL, dos dados filtrados pelas outras duas sub-abas: [Fontes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853#sub-abafontes) e [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853#sub-abafiltros).

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/360095920873)

[[voltar ao subtítulo]](#processodeintegra%C3%A7%C3%A3o) 

**Sub-aba Coletores**

Na sub-aba Coletores, deve ser passado o nome de uma classe em Java que possua a função de coletar as fotos dos imóveis filtrados.

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/360093666614)

[[voltar ao subtítulo]](#processodeintegra%C3%A7%C3%A3o) 

**Sub-aba Tradutores**

Nesta sub-aba é configurado o tradutor de determinado Portal. Os tradutores são feitos em Java e servem para passar os tipos e subtipos da aba **"Portais Web"** da tela [Tipos de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055936693-Tipos-de-Im%C3%B3veis) de uma forma diferente para a requisição

Um bom exemplo é quando o Portal exige os campos em inglês; assim, no campo **"Class Name"** deve ser informado o nome da Classe Java que realiza essa tradução.

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/360093666774)

[[voltar ao subtítulo]](#processodeintegra%C3%A7%C3%A3o)

**Sub-aba Geradores**

Esta sub-aba é de extrema importância. Nela, você deverá informar:

- Módulo de Integração (Classe);

- Nome da Classe (exemplo: br.com.sankhya.timimob.model.integracao.Controller);

- Codificação (exemplo: UTF-8, ISO-8859-1);

- Linguagem (exemplo: java/javascript);

- Nome da Pasta (onde serão salvos os arquivos das requisições);

- Nome do Arquivo (nome padrão ao gerar os arquivos das requisições);

- Extensão do Arquivo (sendo **"JSON"** ou **"XML"**).

**Importante:** Existem Portais que utilizam o padrão XML para receber os dados e outros que utilizam JSON, sendo que esses dois layouts são aceitos nesta tela de Processo de Integração.

**Nota:** Todos os campos já possuem um valor padrão, que é informado ao preencher um portal automaticamente através do botão 

![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15507731422871)

 **"Outras Opções"**.

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/360095921693)

[[voltar ao subtítulo]](#processodeintegra%C3%A7%C3%A3o)

**Outras sub-abas**

Na aba **"Planos"** você registra as especificações dos planos com os Portais, por exemplo, a quantidade de anúncios contratados.

![mceclip10.png](https://ajuda.sankhya.com.br/hc/article_attachments/360095923173)

A sub-aba **"Informações"** (localizada ao lado da sub-aba **"Combinação"**) permite que você veja se a requisição já foi gerada e os caminhos para acessar o arquivo. 

![mceclip11.png](https://ajuda.sankhya.com.br/hc/article_attachments/360093669134)

[[voltar ao subtítulo]](#processodeintegra%C3%A7%C3%A3o) [[voltar ao topo]](#top)

## 
Gerar Requisição

Para gerar a requisição, é necessário preencher os campos corretamente e clicar no botão 

![mceclip12.png](https://ajuda.sankhya.com.br/hc/article_attachments/360095925153)

 **"Processar"**. Neste momento, começará um processamento assíncrono, que permite que você utilize o sistema enquanto está acontecendo a execução:

![int.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360095926133)

Ao finalizar, uma notificação será exibida na área de notificações do sistema 

![mceclip13.png](https://ajuda.sankhya.com.br/hc/article_attachments/360095926313)

 e os caminhos do arquivo com a requisição ficam disponíveis na aba **"Informações"**.

Para finalizar, concluímos que a integração com o Portal escolhido está funcional e a Imobiliária deverá passar o link gerado para o Portal. Com isso, algumas vezes o Portal acessa o link e preenche os Imóveis, de acordo com o plano escolhido.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Tipos de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055936693-Tipos-de-Im%C3%B3veis)
- [Fontes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853#sub-abafontes)
- [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853#sub-abafiltros)