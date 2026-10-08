# Liberação de Limites

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites)  
> **ID:** `360044601034` | **Última Atualização:** 2026-09-01T20:04:14Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310752071959)

 **Módulo:** Configurações > Avançado  
```

O sistema coordena algumas operações através do controle de Liberação de Limites por alçada, ou seja, determinadas pessoas/usuários possuem atribuições para que algumas rotinas no sistema prossigam ou sejam barradas. Por exemplo, caso alguém esteja lançando uma Nota de Venda e queira conceder ao cliente um percentual de desconto, cujo valor ultrapasse o limite previamente estipulado, através da Liberação de Limites, é necessário que uma segunda pessoa (liberador) avalie o caso e autorize ou não a concessão do desconto.

Para saber mais sobre as funcionalidades dessa rotina, acesse os links abaixo:

[Como conceder a um usuário Permissões de Liberação?](#comoconcederaumusuriopermissesdeliberao)

[Como a liberação de um evento é solicitada?](#comoaliberaodeumeventosolicitada)

[Como notificar o solicitante quando uma liberação for analisada?](#comonotificarosolicitantequandoumalibera%C3%A7%C3%A3oforanalisada?)

[Trabalhando na tela Liberação de Limites](#trabalhandonatelaliberaodelimites)

[Botão Outras Opções](#botooutrasopes...)

[Usuário Solicitante de Liberação](#usuriosolicitantedeliberao)

[Parâmetros que influenciam a rotina de Liberação](#parmetrosqueinfluenciamarotinadeliberao)

[Tipos de liberação disponíveis no Sankhya OM](#tiposdeliberaodisponveisnosankhyaom)

## Como conceder a um usuário Permissões de Liberação?

Na tela [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), temos o botão** 

![Botão Outras Opções.. FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641020489367)

 ****"Outras Opções..."** que possui dentre as suas funcionalidades, a opção **"Limites para Liberação"**; ao acioná-la, será aberto o pop-up **"Limites para Liberação - <Nome do usuário>"** para que sejam cadastrados os eventos que o usuário em questão poderá liberar, com seus respectivos limites.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500003615362)

**Observação:** nos casos em que o campo **"Data limite de acesso"**, presente na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao) também da tela Cadastro de Usuários, estiver preenchido com uma data anterior à data atual, e este participar da rotina de Liberação por Alçada (for liberador de algum evento), quando o sistema solicitar essa liberação, mesmo que ele possua a configuração para liberar o evento, não será solicitado e/ou apresentado seu usuário como um dos liberadores.

**Nota:** se um liberador não for definido, a liberação de limite será disponibilizada para todos os liberadores que possuírem o evento vinculado ao seu usuário, independente dos valores e percentuais de limites definidos. Assim, quando um liberador específico for definido, essa liberação deixará de ser apresentada para os demais e poderá ser exibida apenas para aquele liberador em particular.

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/21152744293143)

 O e-mail de liberação de limites será enviado apenas para o usuário liberador que foi selecionado; caso contrário, nenhum usuário receberá o e-mail.

[[voltar ao topo]](#top)

## Como a liberação de um evento é solicitada?

Tomaremos como exemplo, a tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas); no lançamento de um documento (pedido/nota) cujo [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) se encontra com Atraso de Pagamento, ao confirmar o referido documento, será aberto o pop-up **"Liberações solicitadas"**, apresentando a solicitação em questão; nele, a informação principal a ser definida é o Usuário Liberador, ou seja, aquele que irá analisar a solicitação e permitir ou não a continuidade no processo.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500003667421)

Através de um duplo clique na linha do evento, serão apresentados detalhes da solicitação:

![atraso.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500003615762)

Nesse pop-up, os únicos campos que podem ser ajustados são **"Valor solicitado"**, **"Liberador"** e **"Observações"**; nesse último, podem ser acrescentadas informações relevantes correspondentes à solicitação. Nesse campo, quando os eventos forem [10 - Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#10-estoque) e [25 – desconto por item da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#25-descontoporitemdanota), o sistema apresenta e grava as seguintes informações:

*Empresa + Descrição Produto + Descrição CONTROLE + Descrição Local (caso possuam estes tipos de controle)*

A marcação **"Notificação" **pode ser realizada caso você queira enviar a solicitação de liberação via e-mail para o Usuário Liberador. No momento do lançamento do pedido/nota, sendo solicitada a liberação de limites, será encaminhado um e-mail para o liberador, desde que as configurações de envio e recebimento de e-mail necessárias estejam efetuadas ([Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP), [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494-Servidor-SMTP) e e-mails corretos no cadastro de ambos os [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025239834-Usu%C3%A1rios)).

**Nota:** em relação ao evento 10 - Estoque , as informações do produto só serão registradas no campo **"Observações"** se, no [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de destino, o campo "Atualização do Estoque", presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), estiver configurado com a opção "Baixar". Caso o Tipo de Operação - TOP  de destino esteja com a opção **"Reservar"** configurada, será registrada somente a informação de **"Estoque Insuficiente"**.

[[voltar ao topo]](#top)

## Como notificar o solicitante quando uma liberação for analisada?

Ao processar uma liberação de limites, você poderá enviar uma mensagem ao solicitante informando-o via e-mail, ou notificação no Sankhya Om que o evento foi liberado, liberado parcialmente, negado, ou ainda, quando a liberação for removida.

Para tal ação, é necessário que na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao) do [Cadastro do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874) do solicitante, o campo **"Notificar solicitante de Liberações"** esteja preenchido com uma das opções disponíveis, sendo elas **"Por e-mail"**, **"Por notificação no SankhyaOm"** ou **"Ambos"**.

Assim, para o envio de e-mails, você pode realizar a criação de um modelo personalizado por meio da tela [Modelos de E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133), sendo que este deve ser vinculado no campo **"Modelo de E-mail p/ Liberação e Limites"** da aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa). Se um modelo não for definido, um modelo padrão de e-mail que será enviado; além de que, é necessário que haja a **"Conta SMTP"** no Modelos de E-mail para a definição do remetente da mensagem. Sendo assim, o sistema observará a seguinte hierarquia para o envio do e-mail de notificação:

1. Primeiramente, será verificado se o Modelo de E-mail possui configuração no campo **"Conta SMTP"**;

1. Caso não haja, a Conta SMTP vinculada às Preferências da Empresa do usuário liberador que conferida;

1. Se a Conta SMTP não for encontrada no Modelo de E-mail ou Preferências da Empresa, o sistema buscará as configurações na tela [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494);

1. Caso a conta remetente não tenha sido identificada, a notificação não será enviada para a fila de mensagens.

[[voltar ao topo]](#top)

## Trabalhando na tela Liberação de Limites

Primeiramente, para apresentação das solicitações pertinentes à cada Liberador na grade principal da tela, é necessário que eles informem, obrigatoriamente, seu **"Usuário"** e sua correspondente **"Senha"**. Junto a estes campos, temos a marcação **"Sou o liberador"**; ao selecionar essa marcação, quando forem informados o Usuário e Senha e, posteriormente a tela Liberação de Limites sendo fechada, quando ela for reaberta, os campos Usuário e Senha já serão apresentados salvos, agilizando assim o processo de liberação.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500003615962)

É necessário que você atente-se que as configurações efetuadas na tela [Configurações de Login](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603234-Valida%C3%A7%C3%A3o-de-Configura%C3%A7%C3%B5es-do-WMS) irão afetar o usuário e senha que foram informados aqui.

Uma vez informados o Usuário Liberador e sua respectiva Senha, será possível filtrar as solicitações de liberação com base em alguns critérios. São eles:

**Nro Único**** -** Cada linha presente na grade se refere a um documento trabalhado no sistema (pedidos/notas, receitas/despesas); por meio de seu Número Único, podemos buscar o documento em específico com maior rapidez. Por esse número, também serão localizadas as notas correspondentes às solicitações de liberação de conferência.

**Período de Solicitação**** -** Podemos ter situações em que as liberações não precisam ocorrer de imediato, possibilitando ao Liberador, uma análise mais detalhada de cada caso; essas solicitações podem ser filtradas, agrupando-as de acordo com o período que foram realizadas; para isso, informe aqui uma Data Inicial e Final que englobe as solicitações desejadas.

**Apresentar**** -** Nesse campo, você pode determinar qual o status das liberações a serem apresentadas na grade, dentre as seguintes alternativas:

- Tudo;

- Pendentes;

- Negadas;

- Valor liberado menor que solicitado;

- Não Liberados.

1. 
O status Valor liberado menor que solicitado trata-se de uma requisição que foi liberada previamente, cujo o valor de seu pedido/nota foi inferior ao solicitado. Assim, esta solicitação encontra-se pendente para que seja feita uma nova liberação.

1. Caso você utilize o status Não Liberados, serão apresentadas todas as notas pendentes de liberações que não tiveram nenhum tipo de liberação, seja ela parcial ou não.

**Filtro de solicitantes**** -** É possível ainda, por essa seção, buscar as solicitações de liberação relacionadas à cada pessoa/usuário que a requisitou, bastando para isso, inseri-los no quadrante através do botão **"Adicionar"**.

Definidos os filtros desejados, clique em **"Aplicar"**, assim, serão exibidas na grade as solicitações de liberação feitas para o usuário que informou sua senha.

Você pode visualizar todas as informações repassadas pelo Liberador para auxiliar na tomada de decisão através do campo **"Observação Complementar"**. Para isso, selecione a linha desejada e clique sobre a lupa presente no próprio campo, dessa forma, será exibido um pop-up com o texto completo da observação. Caso selecione uma linha que não possui nenhuma informação nesse campo, ao clicar na lupa, o sistema não realizará nenhuma ação.

Podemos visualizar no alto da tela, alguns botões que tem por objetivo auxiliar no processo de liberação. Trataremos abaixo sobre cada um deles: **"Detalhes Conferência"**: Esse botão será habilitado apenas quando a solicitação de liberação for pertencente ao processo de conferência; ao acioná-lo, o sistema irá exibir um pop-up composto pelas informações do pedido e da conferência. Nele, temos uma coluna de diferença (quantidade de produtos do pedido - quantidade de produtos conferidos), sendo que, caso essa coluna tenha um valor diferente de "0" (zero), a linha ficará com a coloração **vermelha**. A coluna Quantidade do Pedido exibe a quantidade que ainda resta no pedido (Qtd negociada - Qtd cortada - Qtd entregue).

![Botão-Análises.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641111099159)

 **"Análises"**: O botão Análises é habilitado de acordo com a configuração realizada na opção **"Componentes de BI por Evento"** presente no botão [Outras Opções...](#botooutrasopes...). Serão apresentados para uso nesse botão, os [Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI) vinculados à cada evento.

![botão-Detalhes.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641188487191)

 **"Detalhes"**: O botão Detalhes será habilitado para uso somente se a linha selecionada se tratar de uma nota; ao acioná-lo, é aberto o pop-up de nome **"Detalhes da Nota"**, onde são apresentadas informações importantes a respeito do documento, como Empresa, Número, Série, Parceiro, Tipo de Operação - TOP etc.

**Observação:** o botão Detalhes ficará desabilitado quando o registro selecionado for originado da tela [Venda Assistida](https://ajuda.sankhya.com.br/hc/pt-br/articles/4466143201431-Venda-Assistida#top).** **

![Botão Ações FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16641229970839)

 **"Ações"**: Ao acionar este botão, serão apresentadas as ações que permitem a execução de liberações específicas que foram cadastradas anteriormente no [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773) ou no [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493) através da aba **"Ações"**.

![botão Ficha-de-Parceiro.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641283707799)

 **"Ficha de Parceiro"**: Quando esse botão for acionado, fará com que seja aberta a tela [Ficha de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601934-Ficha-de-Parceiros), já apresentando as informações pertinentes ao Parceiro relacionado à linha selecionada. O acionamento desse botão auxilia em uma eventual análise rápida da situação do Parceiro junto à Empresa.

![botão Rentabilidade.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641301870487)

 **"Rentabilidade"**: O botão Rentabilidade exibe o pop-up **"Análise de Rentabilidade"**, para que você visualize a rentabilidade dos produtos Com Custo ou Sem Custo separados em duas abas com essa mesma nomenclatura. Além disso, você poderá clicar em cada linha referente à cada item da nota, analisando a rentabilidade deles separadamente. No topo do pop-up, será apresentada a opção Mostrar rentabilidade da nota, que permite novamente a análise da rentabilidade de todo o título. Essa análise permite ao gerente e/ou vendedor decidirem sobre a concessão ou não de um desconto especial em determinado Pedido ou Nota, apresentando qual será a sua rentabilidade final, considerando este desconto.

**Observação:** o botão Rentabilidade ficará desabilitado quando o registro selecionado for originado da tela [Venda Assistida](https://ajuda.sankhya.com.br/hc/pt-br/articles/4466143201431-Venda-Assistida#top).** **

![botão Liberar-limites.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641644920727)

 **"Liberar"**: Esse botão é o responsável por conceder a liberação solicitada; o mesmo ocorre se, ao invés de acioná-lo, for dado um duplo clique sobre a linha desejada. As duas formas de liberação diferenciam-se em um aspecto: o botão, logo após ser acionado, apresenta o pop-up **"Liberar limites"** onde você pode ajustar o Valor liberado e acrescentar alguma Observação Liberador; pelo duplo clique na linha, nenhum pop-up é aberto e a solicitação é atendida em sua totalidade, ou seja, o Liberador autoriza a continuidade do processo de acordo com o que foi requerido pelo Solicitante. Porém, após a primeira liberação utilizando o duplo clique, caso haja solicitação de uma nova liberação para notas não confirmadas, a função do duplo clique removerá a liberação feita anteriormente para inserir a nova.

**Observação:** para evitar que a liberação de limites ocorra de forma indevida ao clicar duas vezes sobre o registro, ligue o parâmetro **"Na Liberação de Limites, avisar no duplo clique - AVISACLIQUELIB"**, assim, o sistema exibirá o pop-up Liberar Limites para que o evento solicitado seja analisado.

![botão Negar-liberação-limites.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641740608407)

 **"Negar..."**: Através do botão Negar, faremos a recusa da solicitação; ao acioná-lo, é aberto o pop-up **"Negar liberação de limites"** para que o Liberador possa acrescentar alguma Observação que, geralmente, é uma justificativa da não liberação do que foi solicitado.

Na [Consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597754-Consulta-de-Libera%C3%A7%C3%A3o-de-Limites) e na Liberação de Limites, você irá visualizar apenas os seus registros, que foram vinculados à regra configurada na [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053). Abaixo, trouxemos um exemplo:

Vinculamos uma regra na Central de Certificações para o João acessar (campo **"Permissão"** = **"Permitido"**) apenas os registros que possuam o Centro de Resultado = Vendas e a Natureza = Almoxarifado. Assim, quando João acessar as telas de Consulta e/ou Liberação de Limites, ele visualizará somente os registros que tenham o Centro de Resultado igual à Vendas e a Natureza igual à Almoxarifado.

**Observação:** se existir uma regra configurada para João não acessar (campo Permissão = **"Proibido"**) os registros que tenham o Centro de Resultado igual à Vendas e a Natureza igual à Almoxarifado, ele não conseguirá visualizar apenas esses registros, sendo apresentados todos os outros.

**Importante:** a Consulta e a Liberação de Limites não irão aplicar regras da Central de Certificações que sejam instância primária e secundária, apenas com instância única.

[[voltar ao topo]](#top)

## Botão Outras Opções...

Abaixo, trataremos sobre as funcionalidades disponíveis no botão 

![Botão Outras Opções.. FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641020489367)

 **"Outras Opções..."** dessa tela:                                                  

[Eliminar pendências de notas...](#eliminarpendnciasdenotasjconfirmadas)[Confirmar notas selecionadas](#confirmarnotasselecionadas)

[Confirmar todas as notas...](#confirmartodasasnotassempendnciadeliberao)[Descontos financeiros por parceiro...](#descontosfinanceirosporparceiro...)

[Abrir a Central...](#abriracentral...)[Eliminar pendências de Autorização...](#eliminarpendnciasdeautorizaodepagamentosjpagas)

[Exibir Saldo Metas/Orçamentos...](#exibirsaldometasoramentos...)[Exibir aprovações/reprovações...](#exibiraprovaesreprovaesdestefinanceironota...)

[Componentes de BI por Evento](#componentesdebiporevento)[Reprocessar conferência](#reprocessarconferncia)

[Editar Observação](#editarobservao)[Configurações...](#configuraes...)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

**Eliminar pendências de notas já confirmadas**

Esta opção, quando acionada, percorre os registros já liberados mas que ainda se encontram pendentes de notas já confirmadas, e registra o **"Vlr. Solicit. Anterior"** no **"Valor Solicitado"** zerando assim o valor da solicitação anterior. A opção Eliminar pendências de notas já confirmadas evita que registros de notas já confirmadas e que não podem ser mais alteradas, sejam apresentadas desnecessariamente na grade. 

**Nota:** ao utilizar essa opção, as pendências são removidas e o último limite inserido no item é mantido, mesmo que a nota já esteja confirmada.

[[voltar ao subtítulo]](#botooutrasopes...)

**Confirmar notas selecionadas**

Essa opção sempre será apresentada habilitada para eventos vindos da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237294-Central-de-Vendas). Ao acioná-la, o sistema irá **"Confirmar" **as notas selecionadas na grade. Porém, se a nota selecionada estiver pendente de alguma liberação, a seguinte mensagem de aviso será exibida: 

***"Nenhuma nota foi confirmada, pode haver liberações pendentes."***

É possível selecionar mais de uma nota para confirmação e, caso alguma delas esteja pendente, ao selecionar essa opção, serão confirmadas somente as notas liberadas; serão apresentadas apenas as numerações das notas que foram confirmadas.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16641746870551)

O Sankhya Om também permite confirmação da nota pela tela de liberações para o evento [18 - Confirmação de Nota](#18-confirmaodenotahttps://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#18-confirmaodenota).

Como já citamos, o documento poderá ser confirmado através dessa opção; sendo um Pedido, se o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) estiver com a marcação **"Fatura Produtos com Estoque na Confirmação"** (aba Estoque) e o campo **"TOP p/Faturamento"** (Pedido de Venda) ou **"TOP p/Devolução" **(Pedido de Requisição) estiver preenchido (aba Geral), o sistema irá proceder com o faturamento e não será aberto o pop-up **"Preparação de Nota"**; no caso de uma Nota, caso ela esteja liberada e com sua numeração preenchida, ela será diretamente confirmada. 

[[voltar ao subtítulo]](#botooutrasopes...)

**Confirmar todas as notas sem pendência de liberação**

O acionamento dessa opção realiza a confirmação de todas as notas presentes na grade que não possuem pendências de liberação, desde que todas elas estejam com suas respectivas numerações preenchidas. 

[[voltar ao subtítulo]](#botooutrasopes...)

**Descontos financeiros por parceiro...**

Essa funcionalidade ainda não foi implementada. 

[[voltar ao subtítulo]](#botooutrasopes...)

**Abrir a Central...**

Quando você acionar essa opção, a tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) ou a tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) serão abertas já posicionando no registro em questão, ou seja, sendo um pedido e/ou nota, é aberta a Central de Vendas/[Venda Assistida](https://ajuda.sankhya.com.br/hc/pt-br/articles/4466143201431), e sendo um título de receita/despesa, será aberta a Movimentação Financeira. 

[[voltar ao subtítulo]](#botooutrasopes...)

**Eliminar pendências de Autorização de Pagamentos já pagas**

Essa opção, quando acionada, retira da tela os títulos que tenham sido liberados com base no evento [24 - Autorização de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#24autorizaodepagamento) e estejam baixados, mantendo apenas aqueles que ainda se encontram pendentes e aguardando liberação. 

[[voltar ao subtítulo]](#botooutrasopes...)

**Exibir Saldo Metas/Orçamentos...**

A utilização dessa opção está ligada ao módulo **"Controle Orçamentário e Metas/W"**; ela estará habilitada apenas se sua empresa possuir a licença para esse módulo. Ao acioná-la, será aberto o pop-up **"Resultados do Orçamento"**, onde poderão ser consultadas as transações que compõe o Saldo da meta, exibindo as metas orçadas, autorizadas, valores antecipados, valores transferidos, crédito de saldo dos meses anteriores, valores já realizados, valores já aprovados, valores ainda disponíveis para utilização e valores aguardando aprovação.

As configurações realizadas nos seguintes parâmetros, podem alterar os valores apresentados no referido pop-up:

- **Considerar impostos retidos no valor da nota? - CONSIMPRETNOTA;**

- **Nível p/Aprov.Suplementação de Orçamento - NIVAPROVSUPL;**

- **Nível p/Aprov.Antecipação de Orçamento - NIVAPROVANTECIP;**

- 
**Nível p/Aprov.Transferência de Orçamento - NIVAPROVTRANSF**. 

[[voltar ao subtítulo]](#botooutrasopes...)

**Exibir aprovações/reprovações deste Financeiro/Nota...**

Essa funcionalidade ainda não foi implementada. 

[[voltar ao subtítulo]](#botooutrasopes...)

**Componentes de BI por evento**

Na tela de Liberação de Limites é possível vincular um evento à um Componente de BI. Por exemplo, podemos criar um Componente de BI que apresente as vendas diárias de um determinado Grupo de Vendedores, onde se deseja verificar os percentuais de desconto que estes vendedores estão concedendo em suas negociações, de modo que, várias liberações de desconto por item na nota são solicitadas no decorrer do dia (evento [25 - Desconto por item da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#25-descontoporitemdanota)); sempre que for solicitada a liberação do evento em questão, o botão **"Análises"**, que falamos no tópico [Trabalhando na tela Liberação de Limites](#trabalhandonatelaliberaodelimites), será habilitado e apresentará o Componente de BI a ele relacionado.

**Importante:** esta opção e suas respectivas configurações são liberadas somente para o usuário SUP. Assim, não existe uma configuração de acesso para liberação de uso a outros usuários.

Ao acionar essa opção, será aberto o seguinte pop-up:

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500003616102)

Clicando em **"Novo"**, informe o Evento Liberação e o Componente de BI que deseja relacionar. Depois de Salvar a inserção, novamente na tela Liberação de Limites, no botão **"Análises"**, serão disponibilizados para geração, os Componentes de BI que foram vinculados aos eventos a serem liberados e que estão selecionados na grade. 

[[voltar ao subtítulo]](#botooutrasopes...)

**Reprocessar conferência**

Essa opção poderá ser utilizada apenas se uma solicitação de liberação for realizada para o evento [64 - Corte/divergência de pedido (Conferência)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#64-cortedivergnciadepedidoconferncia). Feita a liberação da solicitação pelo Usuário Liberador, se não existirem mais solicitações de liberação para essa conferência, selecionando essa opção, o sistema irá refazer o corte; caso não existam itens com quantidade maior ou produtos não constantes no pedido, o sistema realizará o corte e finalizará a conferência como **"OK"**.

Em casos onde você queira alterar a quantidade negociada em pedidos ou notas ou, inserir ou remover itens, após a nota ter sido conferida e finalizada como **"OK"**, o sistema irá marcar essa conferência como finalizada e divergente. Nesse caso, também será necessário Reprocessar a Conferência ou então, fazer uma nova conferência para seguimento no processo.

[[voltar ao subtítulo]](#botooutrasopes...)

**Editar Observação**

Através dessa opção, será possível visualizar a observação do solicitante e realizar a inserção ou alteração da observação pertinente ao usuário liberador.

![mceclip9.png](https://ajuda.sankhya.com.br/hc/article_attachments/360102496834)

Ao selecionar mais de uma nota, será apresentada a seguinte mensagem:

***"Se forem informados valores para os campos abaixo, eles serão utilizados em todos os registros que foram selecionados."***

**Observação:** a observação poderá ser visualizada no campo **"Observação liberador"** somente quando se tratar de uma única nota. Ou seja, para múltiplas notas essa informação só será apresentada no campo Observação liberador localizado na grade principal da tela.

[[voltar ao subtítulo]](#botooutrasopes...)

**Configurações...**

O acionamento dessa opção abrirá o seguinte pop-up:

![mceclip10.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500003616242)

Abaixo, temos suas funcionalidades:

Por meio do campo **"Intervalo de tempo p/ atualização automática"**, podemos determinar um intervalo de tempo que será utilizado pelo sistema para atualizar os dados a serem exibidos na tela. Essa informação terá efeito somente se o tempo inserido for maior que "0" (zero). Esse intervalo pode ser inserido apenas com valores múltiplos de "5" (cinco). Clicando nos botões Filtro, Aplicar, Detalhes da Nota, Ficha de Parceiro, Rentabilidade ou Negar..., uma nova contagem de tempo será iniciada. Por exemplo:

Informando 10 segundos nesse campo, a cada 10 segundos, o sistema efetuará automaticamente a atualização da tela de liberação, dispensando a utilização do botão Aplicar.

Através do campo **"Filtro de períodos"**, podemos definir a partir de qual data será considerada pelo sistema para o agrupamento das solicitações de liberação e consequente apresentação destas na tela, de acordo com as seguintes opções:

- Hoje;

- Últimos 7 dias;

- Últimos 30 dias;

- Últimos 60 dias;

- Sem filtro (pode demorar mais).

**Nota:** a opção definida nesse campo irá preencher automaticamente o campo **"Período de Solicitação"**, quando a tela Liberação de Limites for aberta.

Acionando a marcação **"Ver Itens da Nota"**, teremos na tela de Liberação, a apresentação da grade **"Itens da Nota"** que exibirá os produtos correspondentes à cada documento selecionado na grade principal.

De acordo com o documento selecionado, serão destacados em **amarelo** na grade Itens da Nota, as linhas pertinentes aos itens que motivaram determinado evento de Liberação de Limites, ou seja, os produtos que impulsionaram a solicitação de liberação.

Se você selecionar a marcação **"Recarregar a cada liberação/negação"**, ao proceder com uma **"Liberação"** ou **"Negação"** de solicitação, o sistema automaticamente irá atualizar/recarregar os dados na tela.

Através da marcação **"Tentar confirmar a nota automaticamente"**, ao realizar a liberação de um evento, caso não existam mais solicitações de liberação, a nota será confirmada automaticamente. Caso existam outras liberações a serem feitas, não será exibida uma mensagem; você só será notificado quando não existirem mais eventos e a nota for confirmada.

**Observação:** a marcação acima é acionada apenas quando a nota for confirmada na tela Liberação de Limites, ou seja, não pode ser habilitada na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) nem por meio da liberação de e-mail.

Sendo o documento um Pedido, se o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP) estiver com a marcação **"Fatura Produtos com Estoque na Confirmação"** (aba Estoque) e o campo **"TOP p/Faturamento" **(Pedido de Venda) ou **"TOP p/Devolução" **(Pedido de Requisição) estiver preenchido (aba Geral), o sistema irá proceder com o faturamento automaticamente; no caso de uma Nota, estando essa liberada e com sua numeração preenchida, ela será diretamente confirmada.

**Nota:** o sistema apenas confirma automaticamente as notas de eventos cuja origem são **"Cabeçalho de Nota"** (TGFCAB) e **"Itens da Nota"** (TGFITE); quando o evento possui origem no Financeiro, a liberação é lançada para o financeiro, portanto, a chave da liberação é o Número Único do Financeiro (NUFIN); nesse caso não é realizada a tentativa de confirmação da nota, pois não temos o Número da nota a se confirmar e sim o do Financeiro. Quando a liberação é do Cabeçalho ou Itens, a chave da liberação é o mesmo número único da nota, que é utilizado na confirmação.

A confirmação de notas pela tela de Liberação de Limites é influenciada pelo parâmetro **"Validar evento 18 após as outras validações? - VALEVE18ULTIMO"** (evento [18 - Confirmação de Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#18-confirmaodenota)). Esse parâmetro pode assumir duas configurações: 

- 
**Ligado: **Na [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), é solicitada liberação para o evento 18 e para os demais eventos. Na tela de Liberação de Limites são apresentados todos os eventos e a nota só é confirmada após a liberação dos eventos em questão. 

- 
**Desligado: **Na Central - Compras | Vendas | Mov. Internas, se for identificado que há liberação para o evento 18, o sistema não verifica se serão necessárias outras liberações e abre a tela de solicitação para esse evento. Na tela de Liberação de Limites, só será apresentado o evento 18 caso a marcação **"Tentar confirmar a nota automaticamente"** esteja habilitada. Ao liberar o evento 18, o sistema tenta confirmar a nota; não sendo confirmada, basta aplicar novamente o filtro na tela, pois as solicitações de liberação seguintes ao evento 18 serão feitas de forma automática. Após a confirmação do evento 18 e os eventos posteriores, a nota é confirmada automaticamente.

Quando a marcação **"Fazer compensação automática (caso exista)"** estiver habilitada e o cliente tiver créditos a serem compensados, a compensação será realizada automaticamente, sem questionar o usuário.

Optando pela marcação **"Apresentar as pendentes por** **padrão"**, quando a tela Liberação de Limites for aberta, a seção Apresentar é automaticamente definida com a opção **"Pendentes"**, agilizando assim a filtragem das solicitações.

Ao efetuar a marcação **"Aplicar o filtro ao abrir a tela"**, o usuário logado será considerado o Liberador (exceto o usuário "0" zero) e, portanto, ao sair e acessar novamente a tela de Liberação de Limites, os dados de Usuário e Senha não precisarão ser informados pelo usuário e a marcação Sou o liberador será apresentada assinalada.

[[voltar ao subtítulo]](#botooutrasopes...)[[voltar ao topo]](#top)

## Usuário Solicitante de Liberação

De maneira geral, um Usuário Solicitante de Liberação é aquele que não possui atribuições suficientes para seguimento em um processo, pois sua continuidade sem uma análise detalhada pode impactar em operações delicadas da empresa.

**Observação:** o SUP não poderá ser configurado como liberador, pois ele é utilizado para configuração, portanto é um usuário genérico, não sendo possível identificar quem está por trás daquela liberação. Logo, para ser efetiva a rastreabilidade das permissões concedidas, será necessário que um usuário especifico seja identificado.

Podem ocorrer situações em que o usuário logado não seja exatamente o solicitante da liberação; visando a adequação a esse tipo de caso, temos a possibilidade da criação de um campo adicional na tabela **"TGFCAB"** com o nome **"AD_REQUISIT"**, que deve ser configurado através da tela [Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).

Assim, o Usuário Solicitante de um Pedido/Requisição, Liberação em Cascata, Liberações Orçamentárias e no e-mail, será o mesmo informado no campo adicional criado, a fim de se manter o registro de quem solicitou a liberação. Além disso, o campo contendo a informação de quem é o real solicitante é exibido no formulário de Solicitação de Liberação e no formulário de Solicitação de Liberação Orçamentária.

**Observação:** para obtenção do **"CODUSUSOLICIT"** para o evento [44 - Liberação exigida pela TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#44-liberaoexigidapelatop), o sistema verificará inicialmente se na tela Configurador de layout da nota, a tabela TGFCAB apresenta o campo AD_REQUISIT; se possuir, a informação desse campo será utilizada para gravar a coluna **"TSILIB.CODUSUSOLICIT"** para o evento 44. Do contrário, será aplicado o código do usuário logado no momento em que a liberação for solicitada.

[[voltar ao topo]](#top)

## Parâmetros que influenciam a rotina de Liberação

O sistema considera a configuração do parâmetro **"Duração de liberação de Atraso/Limite crédito? - DIASTOLCREATR"** para validar ou não a nota novamente, para liberações de Limite de Crédito e Atraso feitas no pedido. Quando estiver habilitado, na confirmação de uma Nota originada de um Pedido já liberado, o sistema não solicitará liberação novamente.

No processo de Liberação de Limites em Cascata, temos uma configuração que implica na não solicitação de liberação para o mesmo usuário mais de uma vez, para o mesmo evento. Para que a solicitação/liberação sejam feitas apenas uma vez, por evento e por nota, faça uso do parâmetro **"O mesmo liberador libera uma única vez por nota - LIBNOTAUNICAVEZ"**, ativando-o.

Quando o parâmetro **"Validar limite de crédito com valor zero? - VALLIMCREDZERO"** estiver ligado, o sistema passa a validar o limite de crédito para parceiros com limite de crédito configurado como zero.

[[voltar ao topo]](#top)

## Tipos de liberação disponíveis no Sankhya OM

Acesse o link [Tipos de Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites) para verificar todos os tipos de liberação que encontram-se disponíveis no Sankhya OM.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)
- [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros)
- [10 - Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#10-estoque)
- [25 – desconto por item da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#25-descontoporitemdanota)
- [Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP)
- [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494-Servidor-SMTP)
- [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025239834-Usu%C3%A1rios)
- [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)
- [Cadastro do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)
- [Modelos de E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133)
- [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494)
- [Configurações de Login](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603234-Valida%C3%A7%C3%A3o-de-Configura%C3%A7%C3%B5es-do-WMS)
- [Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI)
- [Venda Assistida](https://ajuda.sankhya.com.br/hc/pt-br/articles/4466143201431-Venda-Assistida#top)
- [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773)
- [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493)
- [Ficha de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601934-Ficha-de-Parceiros)
- [Consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597754-Consulta-de-Libera%C3%A7%C3%A3o-de-Limites)
- [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237294-Central-de-Vendas)
- [18 - Confirmação de Nota](#18-confirmaodenotahttps://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#18-confirmaodenota)
- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)
- [Venda Assistida](https://ajuda.sankhya.com.br/hc/pt-br/articles/4466143201431)
- [24 - Autorização de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#24autorizaodepagamento)
- [64 - Corte/divergência de pedido (Conferência)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#64-cortedivergnciadepedidoconferncia)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)
- [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [18 - Confirmação de Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#18-confirmaodenota)
- [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas)
- [Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota)
- [44 - Liberação exigida pela TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#44-liberaoexigidapelatop)
- [Tipos de Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites)