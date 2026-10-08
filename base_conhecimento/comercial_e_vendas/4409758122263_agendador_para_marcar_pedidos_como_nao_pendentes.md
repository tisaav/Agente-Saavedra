# Agendador para marcar pedidos como não pendentes

> **Módulo:** Comercial e Vendas | **Subseção:** Comercial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4409758122263-Agendador-para-marcar-pedidos-como-n%C3%A3o-pendentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409758122263-Agendador-para-marcar-pedidos-como-n%C3%A3o-pendentes)  
> **ID:** `4409758122263` | **Última Atualização:** 2026-07-29T14:35:24Z

---

```text

```

| Módulo: Comercial > Avançado > Agendadores    Versão disponível: A partir da 4.10 |
| --- |

Por meio da tela Agendador para tornar pedidos não pendentes, você pode realizar agendamentos para tornar de forma automática os pedidos pendentes de compra e venda que não serão faturados, para não pendentes. Dessa forma, após a criação dos agendamentos, na tela [Controle de Jobs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594634) será criado um registro correspondente a tarefa configurada, para execução. 

 

![Marcador](/guide-media/01H53308M80KR451JCYHFRPM3P)

[Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854)****

|  |  | Para utilizar a tela, é necessário liberar o acesso na tela , Menu "Módulos > Comercial > Avançado > Agendadores > Agendador para tornar pedidos não pendentes". |  |
| --- | --- | --- | --- |

 

Clique nos links a seguir para conhecer as funcionalidades dessa tela:

[Aba Horários](#Abahor%C3%A1rios)                                                                      [Aba Frequência Agendamento](#Abafrequ%C3%AAnciaagendamento)

[Aba Configurações](#Abaconfigura%C3%A7%C3%B5es)                                                           [Aba TOP](#Abatop)

[Aba Histórico](#Abahist%C3%B3rico) 

 

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409761713943)

 

#### **Aba Horários   **

Nesta aba, preencha o campo **"Próxima execução em"** com a data e o horário da próxima execução, você pode informar também a **"Data Final de Execução"** e o horário final.

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409761745815)

[[voltar ao topo]](#top)

#### **Aba Frequência Agendamento**

Configure nesta aba, a frequência de execução do agendador por meio dos seguintes campos:

 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409761817239)

 

Informe inicialmente o horário da **"1° Execução"**, e caso seja necessário adicione mais execuções acionando o botão 

![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992924342807)

 **"Adicionar novo horário para execução" **ou remova todos os horários de execução por meio do botão 

![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992924343575)

 "**Remover todos os horários de execução"**.

Além do horário, você pode definir a frequência das execuções do agendador em:

- 

**Diário:** Clicando nesta opção, será efetuada diariamente;

- 

**Semanal** e **Mensal:** Selecionando uma destas opções, serão exibidas para marcação, os dias da semana e do mês, respectivamente. 

[[voltar ao topo]](#top)

#### **Aba Configurações**

Nesta aba, temos a seção **"Opções"**, onde você pode informar no campo** "E-mail para notificação de erros"** um ou mais e-mails, separados por ponto e vírgula (**;**), que será(ão) utilizado(s) para envio de notificação em caso de problemas na execução. A configuração da tela [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494) será utilizada para definir o remetente da mensagem.

Informe também, a quantidade de dias que será mantido o histórico por meio do campo **"****Qtd. dias para manter histórico"**.

 

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409765669911)

 

Na seção** "Filtros"**, você pode criar um filtro personalizado por meio do botão 

![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992908801559)

 **"Filtros"** e realizar a busca da **"Empresa"** desejada. 

**Nota:** quando um filtro for executado no agendador, o mesmo acrescenta a condição abaixo na consulta de busca de pedidos: 

```text
AND (CabecalhoNota.PENDENTE = 'S'
AND CabecalhoNota.TIPMOV in ('O')
AND CabecalhoNota.CODTIPOPER in (101)
AND CabecalhoNota.STATUSNOTA = 'L')
```

 

![essencial](https://ajuda.sankhya.com.br/hc/article_attachments/16024098848535)

 **ATENÇÃO: **Se nenhum dos filtros dessa aba forem informados, **todos os pedidos de compra e venda confirmados **da base serão afetados e o único critério que o sistema seguirá para determinar os pedidos que o agendador executará serão as configuração da aba [TOP](#Abatop)**.**

[[voltar ao topo]](#top)

#### **Aba TOP**

Informe primeiramente nesta aba, se o **"Tipo de Movimento"** será **"Pedido de Compra"**,** "Pedido de Venda"** ou **"Ambos"**. Desse modo, de acordo com a seleção efetuada, serão apresentadas na coluna **"Tops disponíveis"** as TOPs que estiverem ativas no [Cadastro de Tipos de Operações - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114).

 

![Tipo_de_movimento.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4409770066967)

 

Depois, para que as TOPs desejadas sejam transferidas para a coluna **"Tops Selecionadas"**, você pode selecioná-las e clicar no botão 

![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992908803095)

** "Mover campo p/ Classificados"** ou clicar duas vezes sobre elas.

 

![Tops_disponiveis-.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4409778056087)

[[voltar ao topo]](#top)

#### **Aba Histórico**

Com a configuração do agendamento finalizada, será apresentado nesta aba um registro com as seguintes informações básicas da execução: 

- Nro. Único do Agendamento

- Dh. Ini. Execução

- Dh. Fim Execução

- Qt. Pedidos

- Qt. Pedidos Não Pendentes

- Qt. Pedidos Pendentes

Caso seja encontrado algum impedimento durante a execução do agendamento, isto é, ao alterar o status de um ou mais pedidos, o sistema irá encaminhar um e-mail para o destinatário especificado no campo E-mail para notificação de erros  da aba [Configurações](#Abaconfigura%C3%A7%C3%B5es).

Por meio do botão 

![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992908803607)

 **"Ver detalhes"** será apresentado o pop-up **"Detalhes de pedidos"** com todos os pedidos do agendamento.

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409778116375)

 

As abas **"Pedidos não pendentes"** e **"Pedidos Pendentes"** deste pop-up, apresentam os campos** "Nro. Único pedido"**, **"TOP"**, **"Parceiro"**, **"Observação"**.

É importante ressaltar que essas abas só serão exibidas se durante a execução do agendamento, for apresentado pedidos alterados para não pendentes ou que ainda estejam pendentes. Além disso, se todos os pedidos forem alterados para não pendentes, ao acessar o pop-up Detalhes de pedidos, só será apresentada a aba Não pendentes.

Ao clicar duas vezes sobre o registro de um determinado pedido, você será direcionado para a [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) ou [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), exibindo o pedido selecionado. 

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Controle de Jobs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594634)
- [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854)
- [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494)
- [Cadastro de Tipos de Operações - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793)
- [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)