# Eventos de Campos

> **Módulo:** Plataforma e Integrações | **Subseção:** Flow  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4403799538199-Eventos-de-Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403799538199-Eventos-de-Campos)  
> **ID:** `4403799538199` | **Última Atualização:** 2026-07-29T15:08:55Z

---

```text

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313314694935)

 **Versão:** a partir da 4.2
```

Os Eventos de Campos são ações personalizadas que permite manipular dados nos campos de um formulário (embarcado, formatado e nativo) na inicialização e/ou nas tarefas, com o objetivo de nos instruir durante o preenchimento do mesmo. Essas ações podem ser definidas em 3 momentos, sendo eles:

- 
**Evento de entrada: **No momento que o campo receber o "foco" (clicar no campo), a ação será executada.

- 
**Evento de saída: **No momento que o campo perder o "foco" (ao sair do campo), a ação será realizada.

- 
**Evento de alteração:** No momento que o campo tiver seu conteúdo alterado, a ação será feita.

Com eventos de campos é possível executar ações como: validação do conteúdo informado ao sair do campo, preenchimento de um conteúdo automaticamente quando o campo receber foco, ou então, a partir de dados de outros campos do formulário, ter histórico de campo, etc.

Nesse artigo, você terá acesso sobre:

1. 
[Caso de Uso](#casodeuso)                                                                       

1. [Configurações e Resultados](#configura%C3%A7%C3%B5eseresultados)

1. [Demais informações sobre os Eventos de Campos](#demaisinforma%C3%A7%C3%B5esobreoseventosdecampos)

#### **Caso de Uso**

Na imagem abaixo, temos a representação do processo de [Adiantamento de Viagem](https://drive.google.com/drive/folders/1w6yYzFz0WlgMFDWqZlipUEZLVG6z-UiE) de uma Empresa, o qual utiliza eventos de campos na inicialização do processo.

![flow6.png](https://ajuda.sankhya.com.br/hc/article_attachments/4403852668055)

****

| Processo de Adiantamento de Viagem |
| --- |

Esse processo permite que qualquer colaborador solicite um adiantamento de viagem acima de R$20,00 para o seu líder imediato. Caso seja inserido um valor menor, o campo apresentará um erro contendo uma mensagem e somente será possível prosseguir quando for informado um valor acima do permitido.

Quando o valor solicitado for menor ou igual à R$100,00, a forma de pagamento será realizada em dinheiro e, acima desse valor, a empresa realiza uma transferência bancária; para isso, ao informar o valor do adiantamento, um determinado campo do formulário (embarcado) é preenchido com essa informação.

Na solicitação, existe o campo **"Observações"**, para que o colaborador informe o tipo de despesa. Assim, ao clicar no campo, será apresentado um template para guiá-lo a preencher as informações.

Após solicitar o adiantamento, o processo seguirá para aprovação/reprovação.

[[voltar ao topo]](#top)

#### **Configurações e Resultados**

**Validação do valor de adiantamento menor que R$20,00**

Para atender essa regra, utilizamos o evento de alteração de campo, que dará um erro no campo contendo uma mensagem, para o caso em que informamos o valor do adiantamento menor do que R$20,00.

Para isso, acessamos as configurações avançadas do formulário formatado **"AD_SOLICITACAOADIANTAMENTO"** e, sem seguida, selecionamos o campo do formulário **"VALORADIANTAMENTO"**, clicamos nas configurações avançadas do campo e abrimos a aba **"Eventos de Alteração"**, conforme demonstramos abaixo:

![flow7.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4403857702039)

****

| Configurações avançadas de campo do Evento de Alteração |
| --- |

**Observação:** para que o cenário acima ocorra, é necessário escrever o script abaixo, contemplando as seguintes informações:

```text
****

**

```

| var valor = getCampo("VALORADIANTAMENTO");if (valor <20){    //Sinaliza visualmente o erro no campo contendo uma mensagem     erroCampo("O valor solicitado deve ser maior que R$20,00.");    } |
| --- |

No nosso exemplo, a colaboradora Juliane informou um valor de adiantamento de R$18,00. Então, conforme a regra, foi apresentado um erro no campo:

![flow8.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4403903233047)

****

| Solicitação de adiantamento com valor menor do que R$20,00. |
| --- |

Então, a função **erroCampo** utilizada nesse exemplo sinaliza um erro no campo contendo uma mensagem. Para esse mesmo caso, poderíamos utilizar a função **mensagemErroCampo**, a qual apresentaria um pop-up contendo uma mensagem de erro, ambas funções e somente conseguiríamos seguir com a solicitação no momento em que fosse informado um valor acima do permitido.

**Definição de conteúdo no campo "FORMAPAGAMENTO" (campo do formulário embarcado) a partir do valor solicitado (campo do formulário formatado)**

Para atender essa regra, iremos utilizar o evento de saída. Quando o valor do adiantamento for menor ou igual à R$100,00, a forma de pagamento será em dinheiro e, maior que esse valor, será realizada uma transferência bancária.

**Nota:** essa informação será inserida no campo FORMAPAGAMENTO do formulário embarcado.

Inicialmente, acessamos as configurações avançadas do formulário formatado **"AD_SOLICITACAOADIANTAMENTO"**. Em seguida, selecionamos o campo do formulário **"VALORADIANTAMENTO"**, acessamos as configurações avançadas desse campo e clicamos na aba **"Eventos de Saída"**. Observe abaixo: 

![flow9.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4403897565335)

****

| Configurações avançadas de campo do Evento de Saída |
| --- |

Assim, para que esse cenário ocorra, devemos escrever o script abaixo com as seguintes informações:

```text
****

```

| var valor=getCampo("VALORADIANTAMENTO");if(valor <= 100){ //Define valor a um campo. Para manipular um campo do formulário embarcado, o campo deve estar precedido da palavra 'embarcado'    setCampo("embarcado.FORMAPAGAMENTO", "Dinheiro");    }else{      setCampo("embarcado.FORMAPAGAMENTO", "Transferência bancária");    } |
| --- |

Em nosso exemplo acima, a colaboradora Juliane informou um valor de adiantamento de R$1000,00. Dessa maneira, conforme a regra, a forma de pagamento será através de transferência bancária e essa informação constará no campo **"Forma de pagamento"** do formulário embarcado, como podemos observar logo abaixo:

![flow10.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4403897584279)

****

| Solicitação de adiantamento com forma de pagamento via transferência bancária |
| --- |

 

**Definição de conteúdo no campo "Observações"**

Para essa regra, utilizaremos o evento de entrada, onde o colaborador deve informar o tipo de despesa no campo **"Observações"**. Para isso, ao clicar no campo, será apresentado um template para guiá-lo no preenchimento dessas informações. 

Então, acessamos as configurações avançadas do formulário formatado **"AD_SOLICITACAOADIANTAMENTO"**, selecionamos o campo do formulário **"OBSERVACOES"**, clicamos no botão de configurações avançadas desse campo e abrimos a aba** "Eventos de Entrada"**, conforme demonstramos abaixo:

![flow11.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4403903438231)

****

| Configurações avançadas de campo do Evento de Entrada |
| --- |

Para termos o cenário acima, devemos escrever o script abaixo:

```text
**

**

```

| //Verifica se o campo está vazioif(getCampo("OBSERVACOES") == undefined){    //Define um conteúdo para o campo    setCampo("OBSERVACOES", "Informe o(s) tipos(s) de despesa(s) (passagem, alimentação, curso, etc):");} |
| --- |

**Observação:** utilizamos o **"if"** para que, quando for inserida uma informação e ela for salva, ao clicar novamente no campo, não sejam perdidas as informações já inseridas, ou seja, é para manter as informações.

Na solicitação do adiantamento de viagem, ao clicar no campo Observações, será apresentado um template para preenchimento:

![flow12.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4403897665815)

****

| Solicitação de adiantamento com conteúdo no campo "Observações" |
| --- |

[[voltar ao topo]](#top)

#### **Demais informações sobre os Eventos de Campos**

As funções **erroCampo**, **mensagemErroCampo**, **getCampo**, **setCampo** estão todas disponíveis para o uso em eventos de campos, o qual estão detalhadas no help do script.

É importante ressaltar que, nesse contexto, é possível utilizar apenas a linguagem **JavaScript**.

Ao utilizar uma dessas funções, caso o nome do campo esteja precedido da palavra Embarcado, será possível referenciar um campo do formulário embarcado, ou seja, pode-se manipular campos do formulário embarcado a partir de formulários formatado/nativo.

No contexto **"Evento de Alteração"** também estão disponíveis as variáveis oldValue (valor do campo antes da alteração) e newValue (valor do campo após alteração).

[[voltar ao topo]](#top)