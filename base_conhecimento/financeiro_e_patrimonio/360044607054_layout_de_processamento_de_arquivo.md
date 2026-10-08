# Layout de Processamento de Arquivo

> **Módulo:** Financeiro e Patrimônio | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054-Layout-de-Processamento-de-Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054-Layout-de-Processamento-de-Arquivo)  
> **ID:** `360044607054` | **Última Atualização:** 2026-07-22T15:38:23Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370593623191)

 Módulo: **Financeiro> Rotinas
```

Através desta rotina realiza-se a configuração do layout a ser utilizado na execução da baixa dos arquivos de retorno pertinentes às transações com cartão de crédito e/ou débito.

O campo **"Número Único"** representa a numeração identificadora do arquivo.

O nome do arquivo de retorno que está sendo criado é indicado por meio do campo **"Descrição"**.

No campo **"Tipo Arquivo"** serão apresentadas as seguintes opções:

- 
**Delimitado por caractere:** Nesse tipo de layout os campos são separados por caracteres especiais, como, por exemplo "|";

- 
**Largura fixa:** Geralmente são layouts cujos campos tem posição específica (posição inicial e final).

Quando o arquivo é do tipo **"Delimitado por caractere"**, o campo **"Separador campos" **é habilitado para definição do caractere separador das informações (campos).

Através do campo **"Tipo terminador reg."** determine o tipo de terminador do registro. São disponibilizadas as opções **"Windows"**, **"Unix"** e **"Específico"**.

O campo **"Terminador registro"** estará disponível para os tipos de terminador configurados como **"Específico"**, possibilitando assim a sua indicação.

**Nota:** o processamento do arquivo de retorno da [Conciliação de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334) será realizado, a considerar que as informações em cada linha do arquivo são referentes a títulos distintos.

 

[Botões no topo da tela](#botesnotopodatela)                                     [Filtro Personalizado](#filtropersonalizado)

[Filtros rápidos](#filtrosrpidos)                                                    [Criando o arquivo de retorno...](#criandooarquivoderetornoconformelayoutauttar)

[Variáveis de identificação...](#variveisdeidentificaodoarquivoderetorno)
 

![layout_processamento_1.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758627445271)

## Botões no topo da tela

Os botões localizados no topo da tela desempenham uma função primordial na execução desta rotina. Vejamos abaixo o comportamento de cada um deles:

**

![botão Ir para página inicial.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370847192343)

 Ir para a Página inicial:** este botão apresenta a **"Tela inicial"** do Layout de Processamento de Arquivo.

![Botão Mostrar esconder painel de filtros FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16511156008343)

 **Mostrar/esconder painel de filtros:** este botão proporciona a exibição do painel ou ocultação do mesmo.

![botão Modo-formulário.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370800660247)

 **Modo formulário [F6]:** através deste botão, alterna-se a visualização da tela entre modo grade e modo formulário; além disso, configura-se a grade da maneira desejada, ou seja, pode-se selecionar, ordenar ou ocultar as colunas da melhor maneira que atender à você.

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370847200919)

 **Cadastrar Arquivo retorno cartão:** por meio deste botão, é efetuado o cadastro de um novo arquivo de retorno.

![botao-anterior-e-proxima-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16511283282455)

 **Anterior e Próximo:** teremos aqui os botões de navegação entre os registros já cadastrados.

![Botão Excluir.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370847203095)

 **Excluir: **acionando-se este botão, realiza-se a eliminação do registro selecionado na tela.

![botao-duplicar FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16370847205527)

 **Duplicar: **ao clicar neste botão, duplica-se o registro selecionado criando um novo com as configurações correspondentes àquele selecionado anteriormente.

![botão Atualizar.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16370800666135)

 **Atualizar: **este botão quando acionado, recarrega toda a tela.

![Botão Pesquisar Registros FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511290490775)

 **Pesquisar Registros: **utiliza-se este para realizar uma busca específica ao número único do registro informado.

![Botão Abrir query de exportação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16511333654551)

 **Abrir query de exportação:** acionando-se este botão, tem-se a exibição do pop-up **"Editor de Consulta"** que permite indicar a fonte de dados e informar a query de exportação. Além disso, é possível realizar o teste da query, executando-a e, deste modo, visualizando o seu resultado.

![botao-exportar-grade-para-pdf-FINAL.jpg](/guide-media/01H6743AM7C5181E5VX745E5ZA)

 **Exportar grade para PDF:** neste botão são exibidas opções de exportação e visualização das informações da tela. Pode-se **"Exportar para PDF"**, **"Exportar para planilha"** ou **"Exportar para cubo"**.

![botao-anexo-FINAL.jpg](/guide-media/01H6748806TF4YTBWEJSKWJX68)

 **Anexo: **através deste botão, pode-se adicionar algum documento relevante para a rotina.

![Botão Outras Opções.. FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370800674967)

 **Outras Opções: **é apresentada neste botão a opção **"Criar arquivo a partir de um modelo"**, sua funcionalidade é a geração de um novo arquivo de processamento. 

![botão-configuração-da-tela-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16370800676887)

 **Configuração da Tela: **este campo propicia as seguintes funcionalidades:

- Localizar o(s) campo(s) desejado(s) através de sua parcial/total descrição;

- Determinar como será a numeração dos arquivos de retorno que forem criados; de forma automática ou manual como também a numeração inicial dos mesmos;

- Iniciar um tour para conhecer o novo layout de telas do sistema.

[[voltar ao topo]](#top)

## 
Filtro Personalizado

![layout_processamento_2.png](https://ajuda.sankhya.com.br/hc/article_attachments/8759102673815)

O botão 

![botão Cadastrar-filtro.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16370842439447)

 **"Cadastrar Filtro"** quando acionado, apresenta os campos para a criação do filtro. São disponibilizados os seguintes recursos:

- Criar um novo filtro;

- Editar;

- Deletar;

- Habilitar/Desabilitar.

Por meio do botão **"Aplicar"** efetua-se a execução de todos os filtros criados (personalizados ou não) e o carregamento dos dados na tela.

A seção **"Filtro personalizado"** destina-se a habilitar/desligar os filtros já cadastrados.

[[voltar ao topo]](#top)

## 
Filtros rápidos

![layout_processamento_3.png](https://ajuda.sankhya.com.br/hc/article_attachments/8759128919959)

O quadrante **"Filtros rápidos"** permite uma busca focada e ágil do(s) arquivo(s) de retorno desejado(s). Abaixo temos a descrição dos campos que auxiliam nessa pesquisa:

A localização de um arquivo de retorno específico pode ser efetuada através do campo **"Nro. Único"**, essa numeração é gerada internamente e é única para cada registro.

É possível filtrar os arquivos por aquele que efetuou o seu cadastrado, essa funcionalidade está disponível por meio do campo **"Usuário"**.

Tem-se ainda o recurso de limpeza destes dados, ao acionar o botão **

![Botão Limpar Filtros FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16370842446615)

** **"Filtros"**, todos os filtros rápidos serão apagados.

[[voltar ao topo]](#top)

## 
Criando o arquivo de retorno conforme layout AUTTAR

Inicialmente, deve-se acionar o botão Outras Opções localizado no lado superior direito da tela e em seguida clicar na opção **"Criar arquivo a partir de um modelo"**:

![layout_processamento_4.png](https://ajuda.sankhya.com.br/hc/article_attachments/8759244998295)

Será aberto um pop-up de mesma nomenclatura, comportando o modelo da AUTTAR pré-configurado pelo sistema. Deve-se selecionar o referido modelo e executar o carregamento do arquivo por meio do botão **"Criar"**:

A correta formação do arquivo será representada por um pop-up informando que o arquivo foi inserido com sucesso.

Por fim, será carregado na tela o arquivo de retorno com seus respectivos dados.

**Importante:** ao realizar esta inclusão através do modelo acima citado, não é necessário proceder com nenhuma alteração, tendo em vista que todas as parametrizações já estão validadas junto à AUTTAR.

[[voltar ao topo]](#top)

## 
Variáveis de identificação do Arquivo de Retorno

É possível realizar a configuração para processamento do arquivo de retorno de outras **"Administradoras"**, desde que as transações estejam registradas na tabela TEF (TGFTEF) e estejam nos padrões adequados. As variáveis disponíveis atualmente para identificação/processamento do arquivo de retorno são:

- 
**NSU_ADQUIRENTE **- NSU (Número Serial Único) gerado pela Autorizadora;

- 
**QTD_PARCELAS **- Quantidade de parcelas da venda, quando a venda for parcelada;

- 
**NRO_PARCELA **- Número da parcela que está sendo paga;

- 
**DT_MOVTO **- Data do pagamento no formato DD/MM/AAAA;

- 
**VLR_TRANSACAO **- Valor total da transação em R$ no formato 9999999999999.99;

- 
**VLR_PARCELA** ou **VLR_PARCELA_LIQ **- Valor total pago da transação;

- 
**VLR_TAXA_AUTORIZACAO **- Taxa(R$) cobrada do cliente pela Autorizadora.

**Nota:** a configuração da posição das variáveis descritas acima, irá respeitar a ordem em que forem inseridas no layout, ou seja, o campo com a sequência 1 corresponde a posição 1 do arquivo de retorno, o campo 2 à posição 2 e assim sucessivamente. Deste modo, ao realizar esta configuração é necessário verificar-se atentamente as posições de cada um dos campos a serem processados.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Conciliação de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334)