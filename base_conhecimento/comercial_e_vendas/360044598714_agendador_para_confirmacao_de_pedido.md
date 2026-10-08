# Agendador para Confirmação de Pedido

> **Módulo:** Comercial e Vendas | **Subseção:** Comercial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598714-Agendador-para-Confirma%C3%A7%C3%A3o-de-Pedido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598714-Agendador-para-Confirma%C3%A7%C3%A3o-de-Pedido)  
> **ID:** `360044598714` | **Última Atualização:** 2026-07-29T14:21:46Z

---

```text
**

![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311768097431)

 Módulo:** Comercial > Avançado > Agendadores
```

O objetivo dessa tela é confirmar e validar as liberações de limites para pedidos que entram no banco de dados, por meio de integração com sistemas de mobilidade, como, por exemplo, o WMW, que inclui os pedidos não confirmados no banco de dados do sistema.

Note, inicialmente, a **"Descrição agendamento" **e o campo **"Ativo"**, onde informa-se o nome mais adequado para o agendamento e determina-se sua disponibilidade de utilização, respectivamente. O campo **"Nro. agendamento"** será alimentado automaticamente à medida que os cadastros forem realizados.

![essencial](https://ajuda.sankhya.com.br/hc/article_attachments/16023671022615)

 Essa rotina só funciona para Pedidos de Venda (TIPMOV = P).

**Importante: **a confirmação dos pedidos através dessa rotina não irá disparar a impressão dos mesmos, independentemente da configuração realizada na TOP.

Para facilitar sua navegação nas funcionalidades dos campos dessa tela, acesse os links abaixo:

#### ****

[Aba Horários](#abahorrios)[Aba Frequência Agendamento](#abafrequnciaagendamento)

[Aba Configurações](#abaconfiguraes)

| Funcionalidades da Tela |  |
| --- | --- |
|  |  |
|  |  |

  

![ag-para-conf-pedido-aba-geral.png](https://ajuda.sankhya.com.br/hc/article_attachments/21130879838871)

 

### 
**Aba Horários**

Através dessa aba, determine quando será a **"Próxima execução"** do agendamento, bem como a **"Data Final de Execução"** em que ele será executado.

![aba-horarios.png](https://ajuda.sankhya.com.br/hc/article_attachments/21130929962007)

[[voltar ao topo]](#top)

### 
**Aba Frequência Agendamento**

Na aba Frequência Agendamento, deve-se configurar os **"****Horários"**, os **"D****ias"**, **"S****emanas"** ou **"M****eses"** de execução.

Na opção Horários, defina em quais horários a tarefa será executada.

Tem-se a seguir, as três opções de agendamento disponíveis:

- 
**Diário:** significa que a tarefa será executada diariamente;

- 
**Semanal: **aqui defina em quais dias na semana a tarefa será executada;

- 
**Mensal:** será possível determinar em quais dias no mês a tarefa será executada.

![aba-freq-ag.png](https://ajuda.sankhya.com.br/hc/article_attachments/21130935407255)

[[voltar ao topo]](#top)

### 
**Aba Configurações**

Essa aba permite a configuração de um ou mais e-mail's que serão notificados com a numeração de pedidos confirmados, solicitações de liberação e pedidos com erro. Para inserção de mais de um e-mail para ser notificado, basta separá-los por vírgula (**,**) ou ponto e vírgula (**;**). 

O filtro personalizado poderá ser utilizado para uma filtragem mais detalhada de pedidos, porém, por padrão, o sistema irá buscar Pedidos de Venda Pendentes e que não foram confirmados. Por exemplo, configurar o filtro para ser feita a confirmação dos títulos em um determinado período.

Por meio do campo **"Ordenação"**, determine dentre as opções abaixo, qual será a estruturação de confirmação dos pedidos:

- 
**Do mais novo para mais velho:** serão confirmados, primeiramente, os pedidos mais novos; 

- 
**Do mais velho para o maia novo: **por essa opção, os pedidos mais velhos serão confirmados inicialmente.

![aba-configuracoes.png](https://ajuda.sankhya.com.br/hc/article_attachments/21130935425943)

Abaixo, confira um exemplo de e-mail configurado para notificação; ele será exibido na caixa de entrada da seguinte forma:

Título: PEDIDOS CONFIRMADOS AUTOMATICAMENTE EM: __/__/____

Corpo:

PEDIDOS CONFIRMADOS

XXX – XXX

PEDIDOS COM SOLICITAÇÃO DE LIBERAÇÃO

XXX – XXX

PEDIDOS COM ERRO

XXX - Mensagem erro: A nota XXX já foi confirmada

XXX – Mensagem erro: A nota XXX já foi confirmada

Onde **"XXX"** representa a numeração dos pedidos tratados pela rotina.

Quando não houver nenhum registro para qualquer um dos casos, será exibida a seguinte mensagem no e-mail:

PEDIDOS CONFIRMADOS

NENHUM PEDIDO CONFIRMADO

PEDIDOS COM SOLICITAÇÃO DE LIBERAÇÃO

NENHUMA LIBERAÇÃO SOLICITADA

PEDIDOS COM ERRO

SEM MENSAGEM DE ERRO

**Observação:** a mensagem de erro acima, sobre a nota ter sido confirmada, é apenas um exemplo, pois Pedidos Confirmados não passarão pela rotina.

[[voltar ao topo]](#top)