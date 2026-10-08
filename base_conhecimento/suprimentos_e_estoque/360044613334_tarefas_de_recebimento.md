# Tarefas de Recebimento

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento)  
> **ID:** `360044613334` | **Última Atualização:** 2026-07-29T14:14:45Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311548865047)

 Módulo: **WMS > Rotinas
```

Esta tela tem a função de gerar as tarefas de armazenagem seguindo as regras (algoritmos) configuradas como padrão para o sistema, produto ou grupo de produto. Você pode filtrar os recebimentos a partir dos filtros rápidos do painel do lado esquerdo, na grade são apresentados os dados dos recebimentos com a situação atual. Selecione o recebimento a ser armazenado e clique nos botões **"Gerar Tarefas"** ou **"Pré-visualizar"**.

**Nota:** quando estiver logado com um usuário configurado (ver [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053)) para uma determinada empresa, só será possível visualizar e gerar as tarefas de armazenamento, para as notas lançadas para esta determinada empresa.

Esta tela também está envolvida na rotina de [Armazenamento de Produtos Recebidos em Endereço Flutuante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112233).

Acesse os links abaixo para navegar nas funcionalidades desta rotina:

[Botão Gerar Tarefas](#bot%C3%A3ogerartarefas)                                                                         [Botão Pré-visualizar](#bot%C3%A3opr%C3%A9-visualizar)

[Botão Todos os produtos / Produtos selecionados](#bot%C3%A3otodososprodutos/produtosselecionados)                [Botão Tarefas Pendentes](#bot%C3%A3otarefaspendentes)

[Endereço de Conexão](#endere%C3%A7odeconex%C3%A3o)

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500000469702)

## 
Botão Gerar Tarefas

Ao clicar no botão 

![botão-gerar-tarefas-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16924216476695)

** "Gerar tarefas"** o sistema irá gerar as tarefas de armazenagem de acordo com as regras de armazenagem definidas. As tarefas geradas não são apresentadas, pois já estarão liberadas para execução. 

**Observação:** não será possível gerar uma tarefa de armazenagem com volumes alternativos inativos. À exceção de quando o endereço já possuir o produto na unidade inativa. Lembrando que as definições de regras são definidas pela tela [Configuração de Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234), e a definição das tarefas depende da configuração feita por esta tela.

Quando o parâmetro **"Endereçar produtos em endereços com permissão vazia. - WMSENDERPERMVAZ"** estiver habilitado (comportamento padrão) durante a geração das tarefas de armazenagem nesta tela, serão considerados todos os endereços que estiverem com a opção **"Permitir"** selecionada ([Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto), campo **"Produtos Relacionados"**), porém que não possuam qualquer produto vinculado a este e quando utilizada a regra de armazenagem para endereços vazios. Caso o parâmetro citado esteja desativado, não serão considerados os endereços que não possuem tal vinculo.

**Nota:** através da utilização do parâmetro **"Procedure p/tratar Cód.Barras - STPTRATACODBAR"**, será possível realizar a criação de uma função (desenvolvida manualmente) que irá tratar o código de barras lido pelo coletor de dados, retornando a informação corresponde ao produto. Esta função/procedure, deverá ser criada previamente no banco de dados, e seu nome deve ser inserido no parâmetro citado inicialmente. Esta configuração é melhor aproveitada em casos onde, o código de barras do fornecedor não possui um padrão por produto, pois o mesmo é composto por características do item. Em todas as tarefas que utilizam coletor (Consultas, Conferências, Inventário, Movimentações, Separações etc), o código de barras será lido e a função será "chamada" para tratar o código, retornando o produto esperado. Aconselhamos que a criação desta procedure seja realizada com o acompanhamento de um consultor Sankhya.

**Importante:** o parâmetro **"Ativar nova estratgia para retorno de avaria? - WMSNOVAESTATDEV"** deve estar desligado na realização de recebimentos que contenham avarias.

[[voltar ao topo]](#top)

## 
Botão Pré-visualizar

Ao clicar no botão 

![botão-pré-visualizar-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16925171272087)

** "Pré-visualizar"** será apresentada um pop-up com as sugestões de armazenagem feita pelo sistema de acordo com as regras de armazenagem definidas. Você poderá definir se irá gerar as tarefas de acordo com esta sugestão, e ainda visualizar os itens e quantidades que estão sendo armazenadas na aba **"Resumo Armazenagem"** e excluir algum produto pelo botão **"Remover Produtos"** na aba **"Detalhes Armazenagem"**. Para que as tarefas sejam geradas, após a definição realizada, clique no botão **"Salvar Tarefas"** na parte inferior do pop-up.

**Observação:** ao remover algum produto da grade de pré-visualização, este continuará na doca, você pode gerar a rotina de geração de tarefas de armazenagem novamente, porém, as tarefas geradas serão do tipo **"Transferência"**.

No pop-up **"Tarefas de Armazenagem para recebimento"**, temos as seguintes abas:

[Aba Detalhes armazenagem](#abadetalhesarmazenagem)                                             [Aba O que deseja fazer?](#abaoquedesejafazer?)

#### **Aba Detalhes armazenagem**

Esta aba, apresenta os detalhes das sugestões de armazenagem exibidas pelo sistema que poderão ser confirmadas gerando as tarefas, como endereço de destino, quantidade de origem e de destino, empresa, ID.palete e a estratégia (algoritmo) que foi utilizada. As tarefas de movimentação vertical serão geradas normalmente, no entanto, não serão exibidas nos detalhes da armazenagem.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/360101567353)

**Observação:** pode-se alterar/editar o Endereço de Armazenagem dando um duplo clique na linha correspondente ao endereço, e poderá pesquisá-los através da lupa, conforme apresentado abaixo:

![gif12.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500000477201)

Caso você defina um endereço diferente da sugestão do sistema, no momento de salvar a tarefa, serão verificadas as seguintes questões:

- Se o endereço escolhido está disponível;

- Se o endereço permite aquele produto;

- Se o endereço possui alguma proibição em relação ao produto e os que já estão armazenados;

- Se o endereço possui capacidade de peso e cubagem suficiente para armazenar o produto;

- Se o endereço estiver sendo completado, será validada se a regra de armazenagem de data de validade e lote são compatíveis e;

- Se o endereço escolhido está comprometido com outra tarefa que esteja pendente de execução.

**Observação:** com o parâmetro **"Preferência de data de validade minima no picking em tarefa do recebimento - WMSDTVALMINPICK"** habilitado, o sistema irá priorizar os produtos com a data de validade mínima para realizar o picking, ou seja, se houver 2 ou mais produtos com o mesmo lote/controle, mas com datas de validade diferentes, aquele com a data menor (mais próximo a vencer) será priorizado. 

[[voltar ao subtítulo]](#bot%C3%A3opr%C3%A9-visualizar)

#### **Aba O que deseja fazer?**

Esta aba, apresenta uma grade com o resumo da armazenagem, mostrando a quantidade que foi armazenada do produto e a quantidade que não foi armazenada, sendo que, quando o produto tem quantidade não armazenada maior que zero, a linha será apresentada em **vermelho**, para alertar que irá sobrar estoque na doca e que o sistema não pôde endereçar todo o produto (faltou endereço, pouco espaço no armazém).

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500000469882)

**Importante: **o campo **"Apresentar nas tarefas do WMS"**, presente na aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas) da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), têm influência apenas nas **"Tarefas de Separação"**.

**Nota:** o parâmetro **"Valida Status da NF-e nas Tarefas de Armazenagem - VALSTATUSNFE"** (default desligado) possibilita configurar o sistema para não armazenar produtos originados de uma devolução de venda que seja NF-e e não esteja Aprovada. Nesta tela (Tarefas de Recebimento), ao tentar gerar tarefas ou pré-visualizar e a(s) nota(s) sejam NF-e e não estejam aprovadas, você será notificado com uma mensagem:

***"Recebimento originado em uma NF-e ainda não aprovada pela SEFAZ. Não é possível gerar armazenagem antes de aprovar a nota."***

[[voltar ao subtítulo]](#bot%C3%A3opr%C3%A9-visualizar)[[voltar ao topo]](#top)

## 
Botão Todos os produtos / Produtos selecionados

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/360099352174)

Se você selecionar a opção **"Todos os produtos"** o sistema irá manter o comportamento atual, gerando as tarefas com a quantidade total da conferência. Se for indicada a opção **"Produtos selecionados"**, ao gerar as tarefas, o sistema abrirá o pop-up **"Seleção de produtos para armazenagem"**.

![gifff.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500000470082)

Na coluna **"Qtd. Armazenar"** informe a quantidade a ser armazenada; caso informada uma quantidade menor que a quantidade conferida, o sistema realiza um armazenamento parcial do produto; quando isso ocorre o sistema gera tarefa de transferência vinculada ao recebimento, portanto a função a ser utilizada no coletor será de transferência.

[[voltar ao topo]](#top)

## 
Botão Tarefas Pendentes

O botão 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/360102953133)

 **"Tarefas Pendentes"** abre um pop-up de mesmo nome, na qual as tarefas de movimentação vertical não são apresentadas. 

Você poderá cancelar as tarefas pendentes, através da opção **"Cancelar Tarefas Selecionadas"**.

![ggg.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360101567593)

[[voltar ao topo]](#top)

## 
Endereço de Conexão

É possível definir as informações relacionadas ao endereço de conexão nos relatórios personalizados; esta definição é feita através de dois novos campos no modelo de relatório (jrxml). Estas informações de endereço de conexão no relatório são obtidos através das variáveis ENDERECOVERTICAL (correspondente ao campo ENDERECO na tabela TGWEND) e DESCRENDVERTICAL (correspondente ao campo DESCREND também da tabela TGWEND). Para que este comportamento ocorra desta forma, considere os seguintes passos:

- 
Configure um modelo na tela [Modelos de Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993);

- 
Ajuste o modelo no parâmetro **"Modelo de etiqueta de palete - WMSMODETIQPAL"**;

- 
Configure para os endereços de pulmão em [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313), aba[Movimentação Vertical](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313#abamovimentaovertical), os endereços de conexão Preferencial e Secundário; além disso, marque o campo **"Utiliza endereço de conexão para Entrada"**;

- Uma compra será gerada, e a nota será enviada para o recebimento no WMS; realize a conferência no coletor.

- Através desta tela, visualize previamente as tarefas, a fim de se verificar para quais endereços serão gerados os armazenamentos; caso seja endereço de pulmão e este não possua endereço de conexão (movimentação vertical), configure estes para o endereço e gerar as tarefas de armazenagem;

- Ao final da geração das tarefas de armazenagem, será solicitada a impressão do relatório; neste será exibido o endereço de conexão no primeiro código de barras e o segundo código de barras irá exibir o endereço de destino como ocorre atualmente.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053)
- [Armazenamento de Produtos Recebidos em Endereço Flutuante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112233)
- [Configuração de Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613234)
- [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento)
- [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto)
- [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)
- [Modelos de Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993)
- [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313)
- [Movimentação Vertical](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313#abamovimentaovertical)