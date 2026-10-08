# Área de Separação

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o)  
> **ID:** `360044613054` | **Última Atualização:** 2026-09-26T06:33:51Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311555309591)

 Módulo: **WMS > Cadastros 
```

**Importante:** esta tela será apresentada para utilização, apenas se o parâmetro **"Separação por Área de Conferência no WMS? - SEPAREACONFWMS"** estiver ativado.

Nesta tela, devem ser realizados os cadastros das Áreas de Separação a serem utilizadas na rotina WMS.

[Preenchimentos iniciais](#preenchimentosiniciais)[Aba Geral](#abageral)

[Aba Impressão de Etiquetas](#abaimpressodeetiquetas)[Aba Endereços](#abaendereos)

[Aba Separadores](#abaseparadores)[Separação agrupada por produto - Coletor](#separaoagrupadaporproduto-coletor)

[Mensagens personalizadas...](#mensagenspersonalizadas)

|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |

## 
Preenchimentos iniciais

Primeiramente, para realização do cadastro de uma nova área de separação, informe ou tenha de forma automática, o preenchimento do campo **"Cód. Área Separação"**; esta definição é realizada no botão **"Configuração da tela"**, acessado pelo ícone 

![botão-configuração-da-tela-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16837709969687)

.

No campo **"Descrição"**, informe o nome destinado a área de separação.

O campo **"Cód. Área Conferência"**, está destinado a definir a Área de Conferência relacionada à Área de Separação que está sendo cadastrada.

No campo **"Tipo Separação"**, determine o tipo de separação que será realizado na referida Área de Separação, dentre duas possibilidades:

- Por Produto;

- Por Pedido.

## 
Aba Geral

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360086265973)

Defina no campo **"Posição na esteira de**** separação"**,** **o local correspondente à Área de Separação em questão, na esteira de separação; esta configuração é válida em separações Flow Rack. Temos as seguintes opções:

- 
**Nenhuma:** Esta opção não corresponde à separação Flow Rack;

- 
**Inicial:** Por esta opção, a Área de Separação em questão está localizada na parte inicial da esteira;

- 
**Intermediária:** Temos aqui que a Área de Separação está localizada na parte mediana da esteira;

- 
**Terminal:** Por esta opção, a Área de Separação em questão está localizada na parte final da esteira.

Os produtos pertencentes à uma área de separação por esteira, sendo ela com posição inicial, intermediaria ou final os quais sejam relacionados a mesma área de conferência, irão para uma mesma separação.

No coletor de dados, a função **"Separação por Esteira"** executará tais separações, da seguinte forma:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360086266233)

Ao se iniciar a separação por esteira serão exibidas quais posições você tem permissão para realizar as separações.

![clip7280.png](https://ajuda.sankhya.com.br/hc/article_attachments/8895999033367)

Caso o executante efetue a tentativa de puxar uma tarefa na posição intermediária ou final de uma separação, que ainda não tenha sido iniciada na posição inicial, a rotina não apresentará nenhuma tarefa. Quando iniciada a separação, será exibida a tela com o resumo da referida separação.

![clip7281.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896003943831)

Para se iniciar uma tarefa, é necessário que seja aberto um UMA (Unidade de Movimentação e Armazenagem) através do botão **"U.M.A"**.

![clip7282.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896003342359)

Após o procedimento de abertura, volte e acione o botão **"Tarefa"** para buscar as tarefas disponíveis para essa posição na esteira. Iniciando a separação a partir de qualquer outra posição que não seja a inicial, será necessário informar o(s) UMA(s) que foi(foram) iniciado(s) na separação:

![clip7283.png](https://ajuda.sankhya.com.br/hc/article_attachments/8895995393559)

Caso as tarefas da posição anterior da esteira correspondentes a esse checkout não tenham sido iniciadas ou concluídas, a seguinte mensagem será exibida:

***"O U.M.A "xxxxxx" ainda possui tarefas em uma área anterior da esteira."***

**Observação:** na separação do pedido, pode-se também verificar os detalhes adicionais do produto a ser separado. Para essa ação, basta clicar no botão 

![botao-destalhes-do-produto.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/14030566667671)

 (SuperWaba) e ao iniciar a tarefa de separação (TotalCross).

A marcação **"Agrupar pedidos"** permite que os produtos que pertencem à uma referida Área de Separação e se encontram em pedidos que possuem a mesma ordem de carga, sejam agrupados em uma única separação **"Mãe"**. Essa ligação de separações filhas e mães acontece por meio da tabela TGWSVAR.

Nesse processo de agrupamento, as informações da separação mãe não são exibidas na rotina de [Expedição de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias), apenas as informações das filhas serão exibidas. Abaixo, temos um exemplo do procedimento desta marcação:

O produto 1 está nos pedidos 30 e 31; esses pedidos irão gerar duas separações por pedido, durante o envio da onda ocorrerá o agrupamento destes na separação mãe. Caso o pedido 30 solicite 10 unidades deste produto e o pedido 31 solicite 5 unidades, o item de tarefa da separação mãe deverá então conter a solicitação de 15 unidades desse produto.

**Nota:** nas tarefas de separação, você pode realizar a personalização de mensagens aos usuários que realizarem essas tarefas. Para tal ação, na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294) digite a trigger de sua preferência na tabela TGWTEC com sua mensagem, uma vez que, se esta for inserida com o caractere **#** em seu início, será exibida no momento em que a tela de separação do coletor é aberta, caso contrário, a mensagem será apresentada somente quando a tarefa de separação for selecionada.

 

**Seção Separação agrupada por produto**

Efetuando a marcação **"Utiliza separação agrupada por produto"**, você estará determinando que nesta Área de Separação será feito o uso da separação agrupada por produto. Esta marcação aumenta a eficiência e produtividade ao possibilitar que operadores separem múltiplos pedidos em um único deslocamento, minimizando o tempo percorrido sem demanda. O sistema guia o usuário para a separação solicitando os endereços de checkouts necessários, que na verdade são representados pelo equipamento físico (caixa, carrinho, gaiola com divisórias ou contêineres de separação). Na ilustração abaixo, você poderá observar o equipamento e as configurações exemplares para este caso:

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360096942414)

Informe no campo** "Quantidade máx. de checkouts por separação" **a quantidade máxima de checkouts a serem utilizados por separação.

A informação do campo** "Peso máx. do checkout por separação"** se refere ao peso máximo permitido que o operador pode separar por vez.

Insira no campo** "Volumetria máx. do checkout por separação (M3)"**, a volumetria máxima das caixas utilizadas na separação. A volumetria será calculada através das seguintes informações da caixa:

A - Altura da caixa

L - Largura da Caixa

P - Profundida da caixa

Fórmula: A x L x P = X m³

Informe no campo** "Quantidade de Checkouts por Pedido"** a quantidade de checkouts que poderão ser realizados por pedido em uma separação agrupada.

Preencha o campo** "Quantidade de pedidos por separação"** com a quantidade de pedidos que poderão ser agrupados por vez.

Quando selecionada a marcação **"Volume Contínuo?"**, fará com que, que a cada item lido, o volume seja fechado e, da mesma forma, seja aberto o próximo volume de forma automática.

**Observação:** para que você consiga editar volumes de produtos recontados de áreas de separação de volume contínuo, realize a marcação Volume Contínuo? dessa tela e habilite os parâmetros **"Detalha volumes com volume contínuo na recontagem? - DTVOLCOMVCREC"** e **"Detalhar volumes em conferências p/pedido no WMS? - DETALHAVOLWMS"**. Dessa forma, durante a recontagem, você poderá editar os volumes gerados durante a contagem inicial, independente se a opção **"V.C"** do coletor está ou não realizada.

Na tela **"Conferência por Pedido"** do Emulador **"SuperWaba"**, esta mesma marcação estará habilitada, de acordo com a configuração realizada na tela Área de Separação. Caso você opte por desmarcá-la, o sistema trabalhará no modo padrão, ou seja, realizará a conferência manualmente e não de forma automática.

**Nota:** esta rotina só poderá ser realizada após a habilitação do parâmetro **"Detalhar volumes em conferências p/pedido no WMS? - DETALHAVOLWMS"**.

**Importante:** este cadastro é dependente também da marcação **"Utiliza separação agrupada por produto" **localizada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893) em sua aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), seção **"Utiliza separação agrupada por produto"**. Veja abaixo como funcionam as opções contidas nesta marcação:

- 
**Sim, conforme área de separação:** Esta opção irá realizar o agrupamento conforme marcação na área de separação.

- 
**Sim, conforme empresa:**  Esta opção irá realizar o agrupamento para todas as áreas de separação igualmente, conforme marcação para a empresa, na própria tela com os campos disponibilizados na sequência da tela.

- 
**Não usa:** Esta opção irá desligar o mecanismo de agrupamento, inclusive por área de separação se houver marcação já estabelecida.

Para verificar as separações agrupadas, consulte a tela [Gerência WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS) onde haverá a tarefa considerada mãe e as tarefas filhas. A tarefa que será executada no coletor serão as filhas e a tarefa mãe é apenas um controle deste agrupamento, sendo posteriormente cancelada.

Na imagem a seguir você poderá visualizar um exemplo contendo a separação mãe 693, e as filhas 689, 690 e 691 em processo de separação:

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360099283633)

[[voltar ao topo]](#top)

**Seção Subdivisão tarefas de separação**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34508278453015)

 As configurações de **"Separação agrupada por produto"** e **"Subdivisão de tarefas de separação"** são incompatíveis e não podem ser utilizadas em conjunto.

![wilker.png](https://ajuda.sankhya.com.br/hc/article_attachments/34508278453911)

Quando tratar-se de uma área por produto será possível realizar a quebra de tarefas, considerando a norma palete quando a soma de quantidades entre os pedidos atinjam a quantidade suficiente para um palete para que que mais de um usuário possa realizar a tarefa de separação simultaneamente cada qual com seu palete fechado. 

Isso poderá ser feito na sub-aba **“Subdivisão tarefas de separação”**, nele existe o campo **“Quebra por Norma/Palete”** do tipo liga/desliga, ao utilizar a opção ligado, terá a função de quebrar as tarefas de expedição em áreas por produto em um mesmo endereço, de acordo com a norma palete, permitindo que mais de um usuário possa realizar a separação do mesmo item.

**Observação:** a regra de Quebra por Norma/Palete não está contemplada na separação por área, separação esteira e separação balcão.

Se o **“Tipo de Separação”** estiver selecionado com o tipo **“Por pedido”** o campo Quebra por Norma/Palete ficará ofuscado, no entanto, caso esteja selecionado com o tipo **“Por produto”** o campo ficará aberto para o usuário selecioná-lo.

No campo **"Quantidade de SKU's por separação"**, defina a quantidade máxima de SKU's que cada separação terá.

Insira no campo **"Quantidade Tolerância de SKU's por separação"**, a quantidade máxima de SKU's que poderá ser somada à quantidade do item anterior, seguindo as regras abaixo:

- Sempre fragmentar as separações pela quantidade definida no campo Quantidade de SKU's por separação;

- Caso a quantidade de SKU's do pedido seja maior do que a definida no campo Quantidade de SKU's por separação, o sistema verificará se essa quantidade está dentro do valor do campo Quantidade Tolerância de SKU's por separação; se sim, então será gerada apenas uma separação.

Trouxemos um exemplo:

Quantidade de SKU's por separação = 1;
Quantidade Tolerância de SKU's por separação = 1;
Quantidade pedido = 4;
O sistema deverá gerar duas separações com 2 pedidos.

[[voltar ao topo]](#top)

## 
Aba Impressão de Etiquetas

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360086266473)

Nesta aba, temos os campos **"Impressora da Etiqueta de Volume"** e **"Modelo de Etiqueta de Volume"**, onde devem ser informadas a impressora a ser utilizada na impressão e o modelo de etiqueta, respectivamente. O modelo de etiqueta deve ser anteriormente inserido na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

O campo **"Imprimir etiqueta no fechamento do volume"** está diretamente ligado à marcação **"Usa impressão de etiqueta ao fechar volume" **([Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms)) e temos as seguintes opções para seleção neste campo:

- 
**Sim, conforme área de separação:** Com esta opção selecionada e a marcação habilitada, fará com que o sistema imprima a etiqueta a cada volume conferido fechado.

- 
**Sim, conforme empresa:** Estando esta opção desligada e a marcação habilitada, fará com que o sistema somente imprima as etiquetas de volume ao final da conferência, ou seja, esta opção inibirá a ação da marcação.

- 
**Não usa:** Caso a marcação esteja desabilitada, esta opção não terá nenhuma ação.

[[voltar ao topo]](#top)

## 
Aba Endereços

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085090334)

Nesta aba, informe nos campos **"Cód. End. Ini."** e **"Cód. End. Final"**, o intervalo dos endereços que compreendem a Área de Separação em questão. Os endereços aqui apresentados, são os cadastrados na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313), cuja a marcação **"Exclusivo p/ Conferência"** não esteja realizada.

[[voltar ao topo]](#top)

## 
Aba Separadores

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085090414)

Nesta aba, através do campo **"Cód. Separador"**, informe o separador responsável que atuará na área de separação. Você pode cadastrar mais de um separador, dependendo das funções que serão desempenhadas. Poderão ser inseridos neste campo, as pessoas vinculadas às tarefas desejadas; este vínculo é previamente realizado na tela [Configurações por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354), na aba **"Tarefas Permitidas"**, onde a pessoa para ser apresentada para escolha, deve ter a tarefa **"Separação"** à ela vinculada.

**Observação:** se o separador responsável não estiver cadastrado em nenhuma área de separação, ele conseguirá visualizar tarefas de todas as áreas existentes, no entanto, caso este usuário já esteja definido para uma área especifica, ele somente visualizará as tarefas vinculadas a essa área.

[[voltar ao topo]](#top)

## 
Separação agrupada por produto - Coletor

Ao iniciar uma tarefa de separação agrupada, teremos no coletor a seguinte tela:

![clip5992.png](https://ajuda.sankhya.com.br/hc/article_attachments/8895993534743)

Esta tela é exibida pois, a rotina de agrupamento da separação, já calcula a quantidade de checkouts (caixas) necessários para essa separação agrupada; basta informar aqui os chekouts que serão utilizados na separação.

Ao informar o endereço de origem e o produto, será exibida a seguinte tela:

![clip5993.png](https://ajuda.sankhya.com.br/hc/article_attachments/8895965943063)

       

![clip5994.png](https://ajuda.sankhya.com.br/hc/article_attachments/8895965156247)

Como tratamos aqui de uma separação agrupada, você deve separar os produtos apenas com as quantidades e checkouts que pertencem aquele pedido.

**Observação:** em relação à data de validade, a rotina de Separação considerará a menor data de validade no estoque do endereço.

**Nota:** para realizar o agrupamento da separação de forma automática, habilite o parâmetro **"Agrupamento de separação automático - WMSSEPAGRUAUTO"**.

**Observação:** ao realizar o agrupamento no momento da separação por pedidos, para que o sistema não utilize produtos vinculados a uma Área de Separação quando a marcação Agrupar pedidos (aba [Geral](#abageral)) estiver desabilitada, ligue o parâmetro **"Permitir separação flowrack parcial? - SEPFLOWRACKPARC"**.

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26809641128599)

** Influência do parâmetro WMSEXIGENROPL nesta rotina. **

Com o parâmetro **"Informar número do palete em separações agrupadas - WMSEXIGENROPL"** ativado, ao executar uma tarefa de separação pelo **"Coletor WMS Android"** em cenários de grandes volumes e várias sequências de endereços, será possível rejeitar a próxima tarefa e destinar o que já foi separado diretamente para a doca. Nesse momento, o coletor solicitará o código do Container, e a tarefa executada será remanejada para uma nova separação, mantendo o restante de tarefas pendentes na separação original.

![Influência do parâmetro WMSEXIGENROPL.gif](https://ajuda.sankhya.com.br/hc/article_attachments/26809667714071)

Assim, cada separação terá seu próprio Container, garantindo que cada uma possa ser conferida de forma individual posteriormente na doca de expedição.

Informações complementares sobre o parâmetro WMSEXIGENROPL: 

- Funciona apenas para o tipo de separação Por Produto. Separações Por Pedido não estão contempladas nesse fluxo.

- Se a área estiver configurada para separação por produto, o recurso Separação Pulmão funciona. Se configurada para separação por pedido, o parâmetro não será aplicado.

- Este parâmetro não suporta Separação Balcão.

- A conferência será realizada exclusivamente com base no container. Para cada container, será esperado que contenha exatamente o que foi separado e alocado para ele.

- Cancelamentos de expedição, como a retirada de notas já enviadas para expedição, só podem ser realizados se a separação ainda não tiver sido iniciada.

- A criação da etiqueta do container deverá seguir a necessidade do cliente, podendo utilizar código bidimensional ou código de barras. É importante que os códigos não se repitam em nenhuma circunstância. Vale destacar que o processo não é fornecido nativamente.

- Um container não pode ser conferido por mais de um conferente ao mesmo tempo.

- Diversas validações serão realizadas para verificar se um container já existe, está em uso, foi utilizado anteriormente, já foi conferido ou está em processo de recontagem.

- 

O uso do parâmetro WMSEXIGENROPL ligado, concede acesso exclusivo e compatível apenas com o Coletor WMS Android. Este parâmetro não é compatível com o produto Super Waba.

- 

Além disso, esse parâmetro não é suportado em conjunto com os parâmetros:

  - Busca manual de tarefas de separação? - BUSCAMANTARSEP;

  - Habilita controle de produtos com peso variável - PESOVARWMS;

  - Campos para informações adicionais da tarefa. - WMSINFOADTAREFA.

- 

Também não é aplicável com as seguintes marcações da aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa):

  - 

Permite outro usuário continuar separação;

  - 

Utiliza explosão de lote na separação;

  - 

Utiliza cód. de barras concatenado.

- Esse é um recurso novo e ainda está em fase de testes. Assim, pode haver casos de uso não compreendidos em suas totalidades.

[[voltar ao topo]](#top)

## 
Mensagens personalizadas no coletor de Dados

**Nota:** esta é uma rotina idealizada para ser configurada por um profissional que domine as linguagens de programação PL/SQL.

No **Sankhya Om**, você pode configurar determinadas mensagens para que estas sejam exibidas no coletor de dados do WMS, de forma que, sejam apresentadas quando a tarefa é mostrada no coletor e também, ao informar o endereço, pois, assim, informações relevantes ou inerentes ao processo no ato da execução da tarefa sejam exibidas.

Portanto, você poderá configurá-las da seguinte maneira:

Quando a tarefa for apresentada na tela do seu coletor, para que a mensagem de sua preferência seja exibida, pode-se realizar a criação de uma trigger personalizada inserindo uma mensagem de até 99 caracteres no campo **"AD_MSGCOLETOR"** da tabela **"TGWTEC"** do [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294), conforme a regra de negócio, sendo que, este também pode ser configurado em um evento Java.

Essa rotina pode ser definida com inúmeras regras de negócio. Desse modo, considere o exemplo de uma trigger abaixo:

**create or replace TRIGGER TRG_INC_UPD_TGWTEC BEFORE INSERT OR  **
            UPDATE ON TGWTEC FOR EACH ROW
                      BEGIN
                      :NEW.AD_MSGCOLETOR :=** 'Necessário um envelope plástico (Venda **

**                       do tipo**** E Commerce), colete-o antes de executar a separação';**

**            END;**

Em seguida, observe a mensagem a ser exibida:

![mensagem_1.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4408237518871)

Após a configuração, temos também, alguns exemplos de mensagens:

**Processo de separação**
***"Para esta separação é necessário um envelope plástico (Venda do tipo E Commerce), colete-o antes de executar a separação."***

**Processo de separação por esteira**
***"Esta é uma separação especial. Disponibilize caixa personalizada junto às mercadorias separadas."***

**Processo de armazenagem**
***"Verifique se o palete físico não possui datas diferentes. Recebimento com mais de uma data para este produto."***

Além disso, essas mensagens também podem ser exibidas quando a leitura do endereço da tarefa for efetuada; para essa ação, basta inserir o caractere '**#**' antes da mensagem no campo AD_MSGCOLETOR da tabela TGWTEC da tela Dicionário de Dados. Abaixo, observe um exemplo de trigger na especificação aqui exposta:

**create or replace TRIGGER TRG_INC_UPD_TGWTEC BEFORE INSERT OR**

UPDATE ON TGWTEC FOR EACH ROW

         BEGIN

         :NEW.AD_MSGCOLETOR := **'#*****Produto com alto índice de avarias, cuidado ao movimentá-lo.*****';**

END;

Após a configuração acima, você poderá visualizar a seguinte mensagem:

![mensagem_2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4408248941847)

Conforme a regra de negócio na trigger, pode-se personalizar inúmeras mensagens para diversas aplicações, como, por exemplo, no processo de reabastecimento. Observe:

***"Atenção! Produto com mais de uma data no endereço, colete a de menor disponibilidade."***

Lembre-se que este serviço de mensagens, pode ser aplicado nos seguintes processos:

- Tarefas de Armazenagem;

- Transferência;

- Reabastecimento e;

- Tarefas de Separação (Convencional, balcão, por área e por esteira).

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Expedição de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias)
- [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms)
- [Gerência WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS)
- [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313)
- [Configurações por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354)