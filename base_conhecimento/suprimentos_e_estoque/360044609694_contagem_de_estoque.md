# Contagem de Estoque

> **Módulo:** Suprimentos e Estoque | **Subseção:** Inventário  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694-Contagem-de-Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694-Contagem-de-Estoque)  
> **ID:** `360044609694` | **Última Atualização:** 2026-07-29T14:49:26Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312598916119)

 Módulo: **Inventário > Arquivo
```

**Importante:** a Cópia, a Contagem e o Ajuste de Estoque no Sankhya Om foram realizadas de uma maneira diferenciada do MGE Inventário. O sistema agora, identifica o que são cópias e o que são contagens, permitindo assim, que seja feita a cópia e a contagem no mesmo dia, sendo obrigatório fazer a cópia antes da contagem. Dessa forma, não será possível integrar o Sankhya Om com o MGE Inventário, ou seja, a rotina inteira deve ser feita somente pelo Sankhya Om, ou somente pelo MGE.

A Contagem do Estoque é realizada a partir de uma cópia de estoque que é realizada na tela [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514-C%C3%B3pia-de-Estoque). Essa cópia, por sua vez, é retirada do estoque de uma determinada empresa e se comporta como uma "fotografia" do estoque naquele momento, para que seja realizada a contagem com base em um estoque estático e não de um estoque que esteja em andamento, visto que, enquanto alguém está fazendo uma contagem, a empresa pode continuar realizando vendas e compras de produtos. A cópia é realizada para que seja espelhado aquele estoque, daquele instante, e você consiga realizar a contagem do estoque realizado por esta cópia. Sendo assim, como dito anteriormente, antes de acessar a tela de Contagem de Estoque, é necessário realizar a Cópia do Estoque.

[Configurações Iniciais](#configura%C3%A7%C3%B5esiniciais)[Botões de controle](#bot%C3%B5esdecontrole)

[Assistente de Filtros](#assistentedefiltros)[Atalhos](#atalhos)

[Parâmetros que influenciam esta rotina](#par%C3%A2metrosqueinfluenciamestarotina)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

           

![contagem_de_estoque_2.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758471366295)

## 
Configurações Iniciais

Ao abrir a tela, o sistema te questionará qual das seguintes opções você deseja:

- [Realizar uma nova contagem de estoque](#realizarumanovacontagemdeestoque);  

- [Alterar uma contagem de estoque existente](#alterarumacontagemdeestoqueexistente) ou;  

- [Realizar uma implantação de saldo](#realizarumaimplanta%C3%A7%C3%A3odesaldo).

Os produtos que não foram implantados, não aparecerão na tela e, para incluí-los, é necessário que você acione no botão **"****Novo**** (F8)"**, caso não estejam nesta tela.

 

**Realizar uma nova contagem de estoque**

Abaixo, temos um exemplo da opção **"Realizar uma nova contagem de estoque"**:

Depois de selecionada a opção Realizar uma nova contagem de estoque e clicar em **"Próximo"**, o sistema te questionará qual cópia de estoque será utilizada como base para realizar a contagem; selecione a cópia que desejada através de um duplo clique sobre a linha, ou clique em **"Próximo"**.

![contagem_de_estoque_3.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758476839319)

No próximo passo, o sistema questionará se já foi realizada outra contagem para essa cópia de estoque. Escolha entre as opções **"Não, essa é a 1ª Contagem" **ou **"Sim"** (caso já exista e se esteja somente recontando o estoque). Caso você escolha a primeira opção, será solicitada a data da contagem que, geralmente é a data do dia que está realizando a mesma. Porém, caso você queira informar uma data diferente, o procedimento poderá ser realizado.

![contagem_de_estoque_4.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758524001431)

De acordo com as contagens e recontagens, o sistema realiza uma contagem deste procedimento (começando de 1 a n vezes). Essa recontagem pode ser necessária quando há divergências na quantidade encontrada no estoque físico e a quantidade que está no sistema.

Exemplo: A contagem é realizada, porém você decide que a mesma não é necessária ou que deverá contar o estoque novamente. Neste caso, não será necessário realizar uma nova cópia de estoque ou efetuar outro procedimento; basta acessar a contagem novamente e proceder normalmente, informando que já está realizando uma nova contagem para aquela mesma Cópia de Estoque.

Ao clicar em **"Concluir"** o sistema pegará a cópia que foi realizada e trará todos os produtos que estavam no estoque naquele momento, de acordo com as definições configuradas na tela de [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514-C%C3%B3pia-de-Estoque). Sendo assim, serão apresentados todos os produtos gerados na cópia e com estoque zerado, para que você realize a contagem.

![contagem_de_estoque_5.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758515613079)

A data da contagem obedecerá à data informada anteriormente no campo **"Data da Contagem"**.

Nesta tela, é possível visualizar a unidade que você está realizando a contagem, o controle (local) do produto, o Tipo (se é um estoque próprio ou de terceiros), o parceiro (caso seja estoque de terceiros, informe o parceiro neste campo) e a empresa proprietária do estoque deste produto.

**Nota:** os campos referentes à Data da contagem e a **"Empresa"**, não poderão ser modificados. As colunas são fixas porque está sendo realizada uma contagem, justamente referente à uma cópia de estoque feita para uma determinada empresa, (verificando-se na tela de Cópia de Estoque, você pode verificar que é utilizada uma empresa para a geração da cópia, então será a partir desta empresa que será realizada a contagem).

Caso ocorra algum problema com esta contagem e você queira realizar uma recontagem, é necessário acionar o botão **"Nova contagem"**, realizar uma nova contagem de estoque, marcar a cópia de estoque referente à contagem que está fazendo e, ao invés de clicar em Não, essa é a 1ª contagem, selecione a opção Sim e escolha a última contagem realizada. Feito isso, o sistema montará novamente a grade com os produtos e com o estoque zerado, mas agora será uma segunda contagem. Realize a recontagem de todos os produtos normalmente e confirme a operação.

Na realização do procedimento de Contagem, caso o produto seja controlado por lote, existe a possibilidade de informar sua **"Data de Validade"** diretamente na grade onde os produtos estão sendo exibidos pois, temos a coluna com esta nomenclatura disponível (Dt. Validade).

Além disso, caso o parâmetro **"VALDTFABVAL - Validar data fabricação/validade na contagem?"** esteja ativado, na realização da Contagem, depois de inseridos e confirmados os dados pertinentes ao Estoque e à Data de Validade, será aberto o pop-up **"Ajuste de Datas de Fabricação/Validade"**, onde você pode incluir e/ou ajustar as Datas de Fabricação e Validade dos respectivos produtos.

Se o controle do produto da contagem for por Grade, o botão **"Grade**" será exibido para que você selecione a variação deste. Uma vez que, a configuração desse controle será realizado na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba **"Medidas e estoque"**, sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional).

[[voltar ao subtítulo]](#configura%C3%A7%C3%B5esiniciais) 

**Alterar uma contagem de estoque existente**

Abaixo, temos um exemplo da opção **"Alterar uma contagem de estoque existente"**:

![contagem_de_estoque_6.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758518498967)

Marcando esta opção, defina qual a Cópia de Estoque você pretende realizar a alteração na contagem. Feito isso, clique em **"Próximo"**.

![contagem_de_estoque_7.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758590513047)

O sistema apresentará as contagens que foram realizadas para aquela cópia. Marque a contagem que você deseja realizar a edição e clique em **"Concluir"**.

![contagem_de_estoque_8.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758570715799)

A grade será montada novamente com os produtos para a edição da contagem.

Observemos que o campo **"Estoque"**, desta vez, não virá zerado e sim com a quantidade informada na contagem anterior, de modo que este seja alterado conforme sua necessidade. Note no canto direito da tela, a informação que a grade refere-se à edição da 1ª contagem.

![contagem_de_estoque_9.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758629818263)

**Observação: **na realização de uma contagem de estoque, ou alteração de uma contagem de estoque já existente, caso o produto que está sendo contado possua **"Controle Adicional de estoque"**, será possível editar o campo **"Controle"** do produto em questão. Para os produtos que não possuem Controle Adicional de Estoque, o campo Controle permanecerá bloqueado para edição.

[[voltar ao subtítulo]](#configura%C3%A7%C3%B5esiniciais) 

**Realizar uma implantação de saldo**

Por fim, temos um exemplo da opção **"Realizar uma implantação de saldo"**:

![contagem_de_estoque_10.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758631475735)

Ao utilizar esta opção, você deve informar a **"Empresa"** e a **"Data da contagem"**, sendo que não será necessário informar uma cópia como base para contagem.

![contagem_de_estoque_11.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758629058711)

Ao passar para o próximo passo, será possível realizar as contagens referentes ao dia e empresa informados no passo anterior.

Na tela de Ajuste de Estoque, escolha a **"Data da Contagem"** igual a que foi selecionada anteriormente, e a **"Data de Cópia"** igual a qualquer dia que não exista uma cópia; deste modo, o sistema realizará o cálculo como **"X"** para a contagem e** "0"** para a cópia, além de lançar as Notas de Entrada para os produtos.

[[voltar ao subtítulo]](#configura%C3%A7%C3%B5esiniciais) [[voltar ao topo]](#top)

## 
Botões de controle

![contagem_estoque.png](https://ajuda.sankhya.com.br/hc/article_attachments/8757516499095)

**

![configuração](https://ajuda.sankhya.com.br/hc/article_attachments/15507751141143)

 Configurar grade****:** Possibilidade de configurar a grade de acordo com as preferências/necessidades do usuário.

**

![primeiro.png](https://ajuda.sankhya.com.br/hc/article_attachments/15507751146519)

 Primeiro:** Selecionará a primeira linha da grade.

**

![anterior.png](https://ajuda.sankhya.com.br/hc/article_attachments/15507751148439)

 Anterior:** Posicionará em uma linha anterior da que estiver selecionada na grade.

**

![próximo.png](https://ajuda.sankhya.com.br/hc/article_attachments/15507751150487)

 Próximo:** Posicionará a próxima linha da que estiver selecionada na grade.

**

![último.png](https://ajuda.sankhya.com.br/hc/article_attachments/15507777976855)

 Último:** Posicionará a última linha da grade.

**

![nova](https://ajuda.sankhya.com.br/hc/article_attachments/15507777980695)

 Nova contagem****:** Através deste botão, a primeira tela da contagem de estoque será reaberta para que você informe o que deseja fazer (Realizar uma nova contagem de estoque, Alterar uma contagem de estoque existente ou Realizar uma implantação de saldo).

![Novo.png](/guide-media/01H3HQYTEGBQCDM5065HS0DXWM)

 **Cadastrar Contagem de Estoque: **Insere uma nova linha com um novo produto na grade. Essa nova linha será criada com algumas informações replicadas referentes à linha imediatamente anterior a selecionada, informações como: data da contagem, local, tipo, parceiro e empresa. Caso você adicione uma nova linha, mas não informe o produto e acesse o campo de unidade, o sistema irá emitir uma mensagem alertando que você deve informar um produto antes da unidade, visto que existem unidades específicas para cada produto. Exemplo: Caixa, litro, peças etc.

**

![excluir.png](https://ajuda.sankhya.com.br/hc/article_attachments/15507751163671)

 Remover****:** Este botão retira linhas na grade. Esta remoção refere-se à **"Contagem"** e não ao estoque, ou seja, se tiver sido realizada uma ou mais contagens e remover-se a linha, o que será removido será a contagem efetuada.

Exemplo: Contou-se um determinado produto e sua quantidade é 5. Acrescentou esse valor no campo **"Estoque"**. Caso seja necessário desfazer esta contagem, seja por contagem equivocada ou por outro motivo, basta remover a linha. Se alterá-lo, por exemplo, para **"0"** (zero), isso não irá retirar a contagem e sim informar que tem zero produto no estoque. Se for necessário remover uma contagem, exclua a linha da grade.

**

![salvar.png](/guide-media/01GW9MP07TRCTSCNWXRYG6853X)

 Salvar****:** Salva os registros da tela.

**

![remover.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758377331735)

 Cancelar****:** Cancela a operação. Exemplo: Se você informar uma quantidade Y para um determinado produto no campo Estoque e não acionar os botões de Confirmar nem Rejeitar, clicando no botão **"Cancelar"**, o campo volta a apresentar o valor anterior, cancelando assim o último procedimento realizado.

**

![atualizar.png](https://ajuda.sankhya.com.br/hc/article_attachments/15507751165719)

 Atualizar****:** Atualiza dados da tela.

**

![botao-exportar-grade-para-pdf FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/17800333879575)

 Exportar grade para PDF****:** Possibilidade de exportar a grade como PDF, exportar como planilha ou visualizar em cubo.

Além desses botões, existem outros dois que são de confirmação ou de rejeição das alterações realizadas pois, enquanto outras pessoas estão trabalhando na grade, essas alterações não são salvas no banco de dados.

Depois de realizadas todas as alterações necessárias, clique no botão 

![confirmar.png](https://ajuda.sankhya.com.br/hc/article_attachments/15507751170327)

 **"Confirmar" **para que as informações sejam salvas no banco de dados. Caso seja necessário desfazer todas as modificações realizadas, utilize do botão  

![rejeitar.png](https://ajuda.sankhya.com.br/hc/article_attachments/15507778001815)

 **"Rejeitar"**.

**Observação:** Caso você realize a alteração da unidade de um registro na edição de uma contagem, ao Confirmar esta, o sistema incluirá uma nova linha com outra unidade do produto alterado.

A caixa de busca 

![digite](https://ajuda.sankhya.com.br/hc/article_attachments/15507811836311)

 consegue localizar produtos específicos que estão na grade. Dessa forma, é possível digitar o código ou informar uma parte de sua descrição para que o mesmo seja selecionado na grade.

[[voltar ao topo]](#top)

## 
Assistente de Filtros

Você pode estabelecer um **"Filtro Personalizado"**, a partir do assistente de filtros desta tela, que permite, inclusive, a contagem de estoque por **"Marca"** de Produto, entre outros critérios, visando também o ajuste de inventário.

![filtros.png](https://ajuda.sankhya.com.br/hc/article_attachments/8758351288343)

[[voltar ao topo]](#top)

## 
Atalhos

Uma vez posicionado na grade, onde são apresentados os dados da contagem, você pode utilizar alguns atalhos do teclado, a saber:

**CTRL + E:** Edita a linha selecionada da grade.

**CTRL + X:** Remove a linha selecionada na grade.

**CTRL + A:** Adiciona uma linha na grade.

**CTRL + F:** Se estiver editando alguma linha e você teclar **"CTRL + F"**, será aberta uma tela de consulta. Teclando em **"Enter"** serão apresentados os produtos.

 

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251666850327)

 **Informações adicionais:**

Mesmo que na contagem a unidade original do produto seja, por exemplo, Unidade, isso não impedirá que você realize a contagem de outra unidade.  

Temos um exemplo com o Produto **"Prego"**: Em uma empresa X, a unidade padrão para este produto é caixa e, por ventura, ao fazer a contagem do estoque, constatou-se que não havia no estoque caixas para o mesmo e sim, algumas unidades do prego. Neste caso, ao invés de utilizar na contagem uma caixa, pode-se utilizar a unidade alternativa (UN ao invés de CX que é unidade padrão, por exemplo).

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/16251666861079)

 Mesmo que a contagem seja feita em outra unidade, você não poderá excluir a linha existente na cópia com a unidade padrão, pois o sistema a utiliza como referência para realizar o ajuste.

Outra funcionalidade que existe para facilitar a visualização, são às **"setinhas"** localizadas à frente do código das colunas Produto, Local, Parceiro, Unidade e Empresa. Isso significa que, ao posicionar o cursor do mouse em cada uma delas, será apresentada sua respectiva descrição.

[[voltar ao topo]](#top)

## 
Parâmetros que influenciam esta rotina 

Ao ativar o parâmetro** "Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL"**, será habilitado o Controle adicional de estoque por Local.

De forma semelhante ao parâmetro anterior, o parâmetro **"Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE"** ao ser acionado, habilita o Controle adicional de estoque por Controle.

O parâmetro** "Descrição para Referência - DESCRREF"** permite a modificação da nomenclatura do campo **"Referência"**, que pode ser visualizado na grade desta tela.

O parâmetro **"Máscara para quantidade de produtos - _MQTD" **define, através da mascará informada no campo texto, a quantidade de casas decimais que serão usadas para o campo **"Estoque"**. Exemplo: Em quatro casas decimais deve-se informar ###,###,###0.0000.

Caso seja realizada mais de uma [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514) num mesmo dia, é necessário que o parâmetro **"Exclui contagem ao exlcuir a cpia? - INVEXCCONTCOPIA"** esteja ligado para que a Contagem de Estoque também seja substituída por uma nova cópia.

[[voltar ao topo]](#top)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251666863127)

 Acesse também:

[Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633)

[Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514-C%C3%B3pia-de-Estoque)


---

### 🔗 Links e Referências Internas:

- [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514-C%C3%B3pia-de-Estoque)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)
- [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional)
- [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514)
- [Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633)