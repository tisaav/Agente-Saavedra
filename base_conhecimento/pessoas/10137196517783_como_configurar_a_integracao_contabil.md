# Como configurar a integração contábil?

> **Módulo:** Pessoas+ | **Subseção:** Configuração das Integrações Contábil e Financeira  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10137196517783-Como-configurar-a-integra%C3%A7%C3%A3o-cont%C3%A1bil](https://ajuda.sankhya.com.br/hc/pt-br/articles/10137196517783-Como-configurar-a-integra%C3%A7%C3%A3o-cont%C3%A1bil)  
> **ID:** `10137196517783` | **Última Atualização:** 2026-09-27T20:05:52Z

---

```text
 Módulo: Pessoal + > Cadastros 
```

 

As configurações contábeis são necessárias quando a empresa tem a integração entre a Folha de Pagamento com a Contabilidade. Diante disso, é necessária a interação entre as equipes para que o processo seja estruturado de maneira assertiva. Quando há essa necessidade, têm-se alguns cadastros a serem realizados previamente, sendo eles: [Grupo de Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/13756876583575), [Histórico Padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116113), [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054), [Fórmulas Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/10086051863063) e a associação de todos esses com os eventos da folha de pagamento.

Nesta tela são realizadas as configurações da integração contábil.
[Configurações](#h_01HBBFH4JEY85QP0GS9TF4Q3VQ)
[Exceções contábeis](#h_01HBBFH4JEVKC9ZA6EH8TB3X3N)

|  |
| --- |
|  |

 

![Configurações-de-integração-contabil.png](https://ajuda.sankhya.com.br/hc/article_attachments/17849932626071)

Antes, é importante ressaltar que essa tela conta com os seguintes botões que podem influenciar nesta rotina: 

**

![botão-atualizar-eventos-P+.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19933740051991)

 ****Atualizar Eventos**: este botão buscará da tabela de [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767), aqueles que estão marcados para integrar com contabilidade e se provisionar. Assim, irá fazer uma pré-configuração como um facilitador, onde será necessário apenas informar as contas contábeis, fórmulas e históricos padrões.

**

![botão-duplicar-P+.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17850188511255)

 ****Copiar Configurações**: por meio deste botão é possível realizar a cópia das configurações de um Registro Fiscal, grupo e até mesmo evento para o outro Registro Fiscal.

![Copiar-configuração-contabil.png](https://ajuda.sankhya.com.br/hc/article_attachments/17850293077143)

Caso a marcação **"Apagar TODA a configuração e copiar da origem integralmente" **seja acionada, todas as configurações do(s) registro(s) de destino serão excluídas para que as novas sejam copiadas. Já, se for ativada a marcação **"Sobrepor as linhas repetidas"**, todas as configurações do(s) registro(s) de destino serão substituídas pelas novas cópias. 

### **Configurações**

Para iniciar as Configurações de Integração Contábil, clique no card do **"Registro Fiscal"** da empresa que se deseja contabilizar, lembrando que, para cada Registro Fiscal ativo na empresa, deve-se criar uma configuração contábil. Em seguida, caso, selecione o **"Grupo de Contabilização"** para que a configuração dos Eventos com as contas sejam realizadas por grupo.

![Seleçao-registro-fiscal.gif](https://ajuda.sankhya.com.br/hc/article_attachments/17850719974295)

Depois, se o botão Atualizar Eventos tiver sido utilizado, será demonstrado em tela os Eventos que serão contabilizados, onde será necessário entrar um a um e realizar a inserção dos seguintes dados:

- 

**Conta Débito **e **Conta Crédito**: são as contas contábeis nas quais os Eventos serão debitados ou creditados. É bastante comum se agrupar vários eventos numa única conta contábil, como, por exemplo, Salários (Periculosidade, Insalubridade, Adicional noturno);

- 

**Histórico Débito **e **Histórico Crédito**: é imprescindível adicionar um histórico de débito e crédito para cada configuração contábil que for criada;

- 

**Fórmula Contábil**: consiste na fórmula que será utilizada na integração.

**Observação:** para que a rotina ocorra corretamente deverá ser configurado um par distinto de contas crédito e débito para cada um dos registros de provisão, não deixando que se repita nenhuma conta débito.

Salve as informações, acionando o botão 

![botão Finalizar-edição.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17850830448151)

 **"Finalizar Edição"**.  

![Editando-configuração-contabil.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855088170263)

Para ir ao próximo Evento a ser ajustado, utilize a seta 

![botão Ir para P+.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855236623767)

 para seguir, disposta na parte superior direita da tela.

Caso não tenha utilizado o botão Atualizar Eventos, será necessário clicar no botão 

![botão Novo P+.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855459891863)

 **"Adicionar Configuração Contábil" **e preencher os campos **"Evento"**, **"Tipo de Contabilização"**, Conta Débito e Conta Crédito, os respectivos Histórico Débito, Histórico Crédito e Fórmula Contábil.

É importante que, caso não saiba os códigos das contas, utilize a lupa para visão do plano de contas, onde poderá ser pesquisado ou até mesmo localizado entre as hierarquias.

![Hierarquia-contas-contabeis.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855542505495)

Esse processo poderá também ser importado, através da tela [Importador Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/9320434894871), para a tabela TFPCTB. É necessário ser realizado com bastante atenção para não gerar duplicidade de configuração e até mesmo a falta de dados.

### **Criando Exceções Contábeis**

Uma exceção é criada quando um Evento tem a configuração contábil diferente da configuração principal, se ocorre em um tipo de folha ou departamento específico.
Antes de cadastrar uma exceção é preciso definir seu tipo, se será **"Por Tipo de Folha"**, **"Por Departamento" **ou ambos.

Para isso, acesse a tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834) e configure o parâmetro **"Exceção para Contabilização - FPEXCECAOCTB"** com a opção que se enquadra à regra de contabilização da empresa.

Depois, na tela Configuração de Integração Contábil, acione o botão **"Visualizar Exceções"** para exibir as exceções criadas para contabilização das contas contábeis.

![Visualizar-exceçoes.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855988567063)

Após a visualização, caso queira cadastrar uma exceção, clique no botão 

![botão Novo P+.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855459891863)

 **"Adicionar Exceção"**. Preencha as informações do formulário, tais como **"Tipo de Folha"**, Conta Crédito, Conta Débito, Histórico Crédito e Histórico Débito e, em seguida, clique em Finalizar Operação.

**Nota:** é necessário ligar o parâmetro **"Desabilitar visualização árvore contas contábeis - FPDESVISARVCTB"** para desabilitar a visualização de dados em árvore hierárquica nos campos de contas contábeis.

![Cadastro-exceçoes-contas-contabeis.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855988583063)

Se desejar excluir uma exceção criada, basta utilizar o botão Visualizar exceção e clicar em **"Excluir Exceção"**.

![Excluir-exceção-conta-contabil.png](https://ajuda.sankhya.com.br/hc/article_attachments/17856071150359)

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Grupo de Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/13756876583575)
- [Histórico Padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116113)
- [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054)
- [Fórmulas Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/10086051863063)
- [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767)
- [Importador Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/9320434894871)
- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)