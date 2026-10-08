# Abertura de telas do sistema no Flow

> **Módulo:** Plataforma e Integrações | **Subseção:** Flow  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4414744773911-Abertura-de-telas-do-sistema-no-Flow](https://ajuda.sankhya.com.br/hc/pt-br/articles/4414744773911-Abertura-de-telas-do-sistema-no-Flow)  
> **ID:** `4414744773911` | **Última Atualização:** 2026-07-29T15:11:21Z

---

```text
**

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313343950999)

**
```

| Versão disponível: A partir da 4.10 |
| --- |

Neste artigo, trataremos da abertura de telas no SankhyaFlow, isto é, como utilizar uma tela nativa do sistema como meio de apresentar e colher informações na inicialização do processo (solicitação) e nas tarefas de usuário.

Este processo é utilizado em rotinas com alto grau de complexidade, onde é impossível de serem representadas por um formulário no SankhyaFlow, como por exemplo, a tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), que disponibiliza diversos recursos importantes e ao mesmo tempo poderosos para o usuário, como a Consulta de Produtos, Ficha de parceiros, a Inicialização de itens (carregando preço), Cálculo de Impostos, entre outras.

**Importante:** ao utilizar qualquer tela de outro módulo como formulário de um determinado processo no SankhyaFlow, serão consumidas tanto a licença do módulo SankhyaFlow (Lista de Tarefas) quanto do módulo cuja tela pertence.

Desse modo, trataremos neste artigo os seguintes pontos:

- [Caso de Uso](#casodeuso)

- [Configurações](#configura%C3%A7%C3%B5es)

- [Resultados](#resultados)

- [Demais informações](#Demaisinforma%C3%A7%C3%B5es)

#### **Caso de uso**

Apresentaremos aqui o caso de uso do processo** "Pedido de vendas simplificado"**.

![Processo_Pedido_de_Vendas_Simplificado.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414779846807)

**Processo Pedido de vendas simplificado**

Este processo normalmente é iniciado por um vendedor que identifica a necessidade de registrar no ERP a negociação realizada anteriormente em forma de pedido de venda. Ao confirmar o pedido, caso exista liberação de limite, como por exemplo, desconto do produto acima do permitido, o pedido é direcionado para a tarefa: **"****Liberar limites"**, onde o usuário liberador irá liberar ou negar os limites deste pedido.

Caso o usuário liberador recuse a liberação do limite, o pedido é direcionado para a tarefa: **"****Refazer pedido"**, onde o solicitante poderá:

- Alterar o pedido, conforme informado na liberação (observação do liberador);

- Ou então, cancelar a solicitação realizando a exclusão do pedido.

Por fim, caso não tenha mais nenhum impedimento do pedido (liberação pendente), o solicitante é notificado sobre a finalização da sua solicitação.

[[voltar ao topo]](#top)

#### **Configurações**

Para que na inicialização do processo o vendedor lance os pedidos de venda no ERP, vamos configurar no processo a tela: **"****Pedido de venda"**, na aba** "Formulário/Telas"**, sub-aba **"Telas"**: 

![Pedido_de_Venda.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4414768929175)

**Adicionando a Tela Pedido de Venda no processo**

**Observação: **o usuário modelador poderá configurar uma mesma tela para ter diferentes comportamentos no processo e tarefa, como a geração, multiplicidade e a visualização de diferentes registros por tarefas, para isto, temos as configurações globais da tela (**"****Quantidade de registros"**,** "Escopo"**,** "Política de reentrância"**), e os acessos que serão detalhados no final deste tópico.

Neste exemplo, como estamos utilizando a tela no Processo (inicialização), os campos Escopo e Política de reentrância serão do tipo: **"****Processo" **e **"****Recuperar dados anteriores"**, e no campo Quantidade de registros, o usuário poderá inserir um único registro, conforme imagem abaixo:

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414856883351)

**Configurações globais da tela**

**Inserindo a tela ****Liberação de limites**** na tarefa de usuário**

Para que o usuário possa liberar ou negar as liberações de limites pendentes dos pedidos que forem lançados, vamos configurar na tarefa **"Liberar limites"** a tela: **"****Liberação de Limites"**, na aba **"Formulário/Telas"**, sub-aba **"Telas"**:

![Libera__o_.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4414851008023)

**Adicionando a tela Liberação de Limites na tarefa.**

**Filtro de tela **

Como a tela de Liberação de limites é de consulta, não é possível saber quais foram os registros gerados nesta instância de processo. Então, para que o usuário visualize apenas as liberações pendentes que foram geradas nessa instância de processo, vamos configurar um filtro personalizado para a tela. Desse modo, com a tela selecionada, clique no botão **"****Filtro de tela"**.

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414864245399)

**Filtro de tela.**

Neste exemplo, será filtrado apenas as liberações de limite do pedido (registros) gerado na instância do processo, conforme imagem abaixo: 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414851281943)

**Filtro personalizado na tela**

```text
**this.NUNOTA IN (SELECT NUNOTA FROM TGFCAB_TNF WHERE TNF_IDINSTPRN = ${IDINSTPRN})**
```

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16089009513495)

 **Informações adicionais:**

- O filtro de tela pode ser realizado em qualquer tela;

- Está disponível as variáveis abaixo para o modelador utilizar no filtro, de acordo com o contexto em que a tela for inserida (processo e tarefa): 

- 

    - ** Id Instância do Processo;**

    - ** Id Instância da Tarefa;**

    - ** Id Tarefa;**

    - 
** Id temporário de inicialização:** Utilizado apenas no contexto de processo (inicialização).

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414851307543)

**Variáveis do filtro personalizado no contexto de tarefa**

As tabelas para controle de vínculo com o Flow possuem um sufixo **"****TNF"** no nome da tabela, por exemplo: **"****TGFCAB_TNF"** e os campos de ligação do Flow possuem um prefixo, como por exemplo: **"****TNF_IDINSTPRN"**.

**Inserindo a tela ****Pedido de venda**** na tarefa de usuário**

Quando a liberação de limites for negada, para que o solicitante possa realizar as devidas alterações no pedido, vamos configurar na tarefa **"****Refazer pedido"** a tela **"****Pedido de Venda"**:

![Pedido_de_venda.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414851319703)

**Tela Pedido de Venda inserida na tarefa**

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/42313376807319)

|  | Como precisamos recuperar as informações inseridas na inicialização, iremos manter a configuração global da tela (Quantidade de registros, Escopo, Política de reentrância). |
| --- | --- |

**Configuração de acessos**

Para a tarefa Refazer Pedido, o solicitante poderá apenas **"A****lterar"** ou **"Excluir"** o pedido. Assim, vamos configurar os acessos desta tela, na aba **"Formulários/Telas"**, sub-abas **"Telas"**, por meio do botão **"Configurações da tela"**, conforme gif abaixo:

![Acessos.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4414851355543)

**Configuração dos acessos**

Para as demais telas que foram definidas na inicialização do processo (tela Pedido de Venda) e na tarefa de Liberar limites (tela Liberação de Limites) vamos manter os acessos padrões que são: **"****Incluir"**,** "Alterar"**,** "Excluir"**,** "Consultar" **e **"Numeração"**. Por padrão, esses acessos já vêm ligados ao inserir qualquer tela, caso o modelador queira alterar essa configuração, será possível, exceto o acesso de Consultar, que sempre estará ligado e desabilitado.

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16089009513495)

 **Informações adicionais:**

- 
Os acessos às telas do Sankhya Om que estão sendo utilizadas pelo SankhyaFlow, devem ser definidos no processo. Caso o usuário tenha acesso às telas fora do SankhyaFlow (definidos na tela de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854)), os mesmos não refletiram no processo.

- 
Além dos acessos padrões, algumas telas tem os seus acessos especiais (representados em *itálico*), que são os acessos específicos de cada tela, por exemplo, a tela de Pedido de Venda, um de seus acessos especiais é: *Rateio.*

- Pode ser configurado diferentes acessos, quando utiliza-se a mesma tela em mais de uma tarefa e no processo.

**[[voltar ao topo]](#top)**

#### **Resultados**

Conforme configurações realizadas anteriormente, vamos agora apresentar o lançamento de um pedido de vendas com liberação de limites, utilizando as telas Pedido de Vendas e Liberação de limites pelo Flow.

Na inicialização do processo o solicitante realiza o lançamento do pedido, inserindo os dados na grade **"Cabeçalho****"**:

-  Tipo de negociação (1);

-  Parceiro (2); 

- Tipo Operação (3);

- Empresa (1).

Após salvar o cabeçalho, preenche a grade **"****Itens"** informando: 

- Produto (5);

-  Quantidade (20);

-  Vlr. unitário (R$5,00);

- % desconto (7%), 

Feito isso, após salvar os Itens, ele confirma o pedido.

Na confirmação do pedido é percebido que o desconto do produto informado é diferente do limite permitido (5% limite permitido, 7% limite inserido), desta forma, é realizada a solicitação desta liberação de limite, onde o solicitante informou o liberador (Juliane) e finalizou o lançamento do pedido clicando no botão** "Iniciar"**:

![Lan_amento_do_pedido_de_vendas.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4414851458327)

**Lançamento do pedido de vendas**

Neste momento o pedido já foi criado, mesmo que o processo não tenha sido iniciado. A inicialização somente conclui as informações necessárias para dar sequência no  processo.

Então, após iniciar a solicitação, o processo seguiu para a tarefa de **"****Liberar limites"**. Juliane, responsável pela liberação deste limite, acessou a tarefa na Lista de tarefas e habilitou na tela a marcação **"****Sou o liberador"**, ao clicar em **"****Aplicar"**, visualizou o pedido 88 referente a esta solicitação, para liberar ou negar o limite:

![Libera__o_de_limite.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4414844411159)

**Liberação de limite**

Neste caso, Juliane negou o limite, solicitando para que o percentual seja ajustado para o limite permitido de 5% :

![Libera__o_de_limite_negada.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4414844454167)

**Liberação de limite negada**

Devido o limite ter sido negado, ao finalizar a tarefa o processo seguiu para a tarefa **"Refazer pedido"**.

**Observação:** quando for configurado na tela de cadastro de [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), para **"Notificar solicitante de liberações"**, ele poderá receber notificações tanto via e-mail quanto sistema, sobre a liberação ou não do limite, constando a observação do liberador caso tenha.

Neste caso de uso, o usuário solicitante foi notificado que a sua solicitação do pedido 88 foi negada, constando na observação do liberador a mensagem para ajustar o percentual de desconto do produto para 5%:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414745018007)

**Notificação sobre a liberação de limite**

Então, conforme notificação recebida, o solicitante acessou a tarefa Refazer pedido na Lista de Tarefas e realizou o ajuste do percentual de desconto para 5%:

![Ajuste_do_pedido.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4414851650711)

**Ajuste do pedido**

Assim, após o solicitante finalizar a tarefa Refazer pedido, como não existe mais nenhuma liberação de limite pendente, a sua solicitação foi finalizada, onde o mesmo foi notificado via e-mail: 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414863521815)

**Envio do email (visualizado na tela "****Fila"****)**

[[voltar ao topo]](#top)

#### **Demais informações **

As configurações globais da tela são **"****Quantidade de registros"**,** "Escopo"**,** "Política de reentrância"**. Trataremos a seguir, sobre cada uma delas.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414769178519)

**Configurações globais da tela**

**Quantidade de registros: **Representa quantos registros o usuário poderá realizar na tela, sendo:

- **Único (opção padrão):** Apenas um registro poderá ser inserido;

- **Vários:** Vários registros poderão ser inseridos.

**Escopo: **Este campo possui as seguintes opções:

- 
**Processo**: Todos os registros inseridos na tela são visíveis em todas as tarefas da instância do processo que utilize a tela;

Quando for escopo de processo, as configurações Quantidade de registros e Política de reentrância são globais, ou seja, são iguais no processo e tarefas, caso seja alterada essas configurações no processo ou tarefa, a mesma será refletida em todas as demais tarefas/processo que utilize a tela.

- 
**Atividade**: Apenas os registros inseridos na atividade são visíveis na atividade em questão.

Quando for escopo de atividade, as configurações Quantidade de registros e Política de reentrância, podem ser alteradas para a tarefa em questão.

**Observação: **o modelador pode inserir a mesma tela no processo/tarefa, com diferentes tipos de escopo, ou seja, processo e atividade. 

**Política de reentrância:** É habilitado somente se Escopo for igual à Atividade, contendo as seguintes opções:

- 
**Recuperar dados anteriores**: Os registros que vão aparecer na atividade serão os registros de todas as instância daquela atividade que utilizou a tela.

- 
**Criar sempre um novo registro**: Os registros que vão aparecer na atividade serão os registros criados apenas naquela instância de atividade.

Nas configurações da tela (aba [Fomulários/Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047567214?flash_digest=75aac1ec4ff99f4ad0af4f482fd6d45b99c14aaf#nesta), sub-abas [Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047567214?flash_digest=75aac1ec4ff99f4ad0af4f482fd6d45b99c14aaf#sub-abatelasprocesso), **"Configurações de tela"**), quando adicionado alguma tela que esteja relacionado com a Central de notas (Pedido de Venda, Venda, Compra, Requisição, entre outras), o usuário modelador poderá definir um valor padrão para a TOP, ao lançar um documento, ou seja, durante a execução na inicialização/tarefa o campo virá preenchido automaticamente:

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414863639703)

**Configurando valor padrão para a TOP**

**Importante:** O flow trabalha com frame em relação a telas nativas como uma tela de uma tarefa. Há uma limitação do Navegador Sankhya para o retorno do popUp de seleção do xml da importação da nota para o frame incluído na tarefa do flow. Por isso, após fechar o popUp, nada acontece.

**Telas de cadastro sem instância mapeada**

Algumas telas de cadastro do sistema não tem instância mapeada, então para que seja possível criar o vínculo de registro com a instância de processo, podendo posicionar no registro quando necessário, o modelador poderá informar a instância desta tela, por meio do campo** "Nome da Instância"**.

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414863781143)

**Configurando Nome da Instância da tela**

Para encontrar o nome da instância de uma tela é necessário verificar pelo monitor de consulta: 

1. Ligue o monitor de consulta;

1. Acesse a tela que deseja (aguardar a tela carregar);

1. Desligue o monitor de consulta;

1. Baixe o log;

1. Com o arquivo baixado, abra o arquivo **"Monitor_Consulta.log"**;

1. 
Procure por: **loadRecords** (serviço que chama a tela). Na linha acima do serviço tem o nome da instância da tela (entity), conforme imagem abaixo.

Considere o seguinte exemplo:

- 
Tela: **Metas e Orçamentos » Configuração da Estrutura de Metas/Orçamentos**

- 
Nome da Instância: **"****ConfiguracaoMeta"**

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4414745203223)

**Log**

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)
- [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854)
- [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)
- [Fomulários/Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047567214?flash_digest=75aac1ec4ff99f4ad0af4f482fd6d45b99c14aaf#nesta)
- [Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047567214?flash_digest=75aac1ec4ff99f4ad0af4f482fd6d45b99c14aaf#sub-abatelasprocesso)