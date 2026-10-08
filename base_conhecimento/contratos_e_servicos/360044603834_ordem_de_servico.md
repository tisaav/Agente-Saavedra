# Ordem de Serviço

> **Módulo:** Contratos e Serviços | **Subseção:** Contratos e Serviços  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o)  
> **ID:** `360044603834` | **Última Atualização:** 2026-07-29T14:03:14Z

---

```text
**

![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311191431831)

**
```

| Módulo: Contratos e Serviços > Ordem de Serviço |
| --- |

O módulo de Contratos e Serviços é uma solução para auxiliar a equipe de prestação de serviço que necessita de uma eficiente ferramenta de comunicação, gestão de atendimento e suporte.

Sua principal característica é a de dinamizar o processo de atendimento, com distribuição inteligente de carga das diferentes solicitações e, consequentemente, com expressivo ganho de escala.

A Ordem de Serviço (OS) é o principal recurso deste módulo. É por meio dela que se obtém indicadores para a análise de resultados. Os indicadores oferecidos pelo lançamento de uma OS, variam de acordo com a necessidade das empresas e, é justamente por isso, que o sistema tem flexibilidade na forma de lançamento.

Utilize a OS para descrever os problemas e soluções referentes a diversos assuntos, por exemplo, uma customização a ser criada.

**Importante:** o sistema fará uma validação no momento de salvar um item da OS, considerando o Executante, a Data/Hora Inicial e Final e o Parceiro iguais. Então, se já existir uma OS lançada nesse mesmo horário, será barrado e não permitirá salvar o item dessa OS. 

Abaixo, trataremos sobre as funcionalidades desta rotina:

[Componentes da tela](#componentesdatelaordemdeservi%C3%A7o)

[Modos de Visualização](#modosdevisualiza%C3%A7%C3%A3o)

[Serviços por Executante](#servi%C3%A7osporexecutante)

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085884414)

[[voltar ao topo]](#top)

## 
Componentes da tela

Conheça os componentes da tela, no video abaixo:

**Informações adicionais**

Para que seja encaminhada a Ordem de Serviço por e-mail, realize as seguintes configurações:

**1.** Configure o Servidor SMTP no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba [SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874#abasmtp), ou;

**2.** Na tela [Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP) deverá existir um Servidor SMTP configurado, ou ainda;

**Nota:** poderá ser apresentado alguns erros caso seja realizado o cadastro de um Servidor Gmail, visto que, em algumas ocasiões o serviço ou porta é bloqueado.

**3.** Na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834), em relação ao parâmetro **"Servidor (SMTP): - EMAILSERVSMTP"**, ao inserir um servidor no campo **"Texto"**, existirá um problema onde, ao informar um Servidor SMTP válido, o mesmo entrará em uma parte do código que não passará usuário e senha do servidor.

Assim, para utilizar este parâmetro, é necessário que o servidor aceite a requisição sem autenticação.

```text
**

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311191435799)

**

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311178781207)

**
**[Assinatura Digital](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112773)
```

| Dica: Para saber mais informações sobre o botão  "Opções para Assinatura Digital da Sub-OS" acesse a documentação . |
| --- |

 

[[voltar ao topo]](#top)

## 
Modos de Visualização

Algumas telas apresentam dois estados de visualização, o primeiro chamado de **"Modo de Edição"** e o segundo **"Modo Planilha"**, que podem ser alternados através do botão 

![OS26.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084939553)

 **"Alternar Layout"**.

**Nota:** tendo em vista que as informações de valores financeiros em mensagens de atraso deverão ser vistas apenas pela equipe do financeiro, utilize o parâmetro **"Mostra valor em atraso na Ordem de Serviço? - MOSTRAVLRATRASO"** para ocultar esta informação.

**Configurando o Modo Planilha**

Ao alternar a tela para o Modo grid, será apresentado o botão **"Configura a Visualização do Grid"** 

![OS27.png](https://ajuda.sankhya.com.br/hc/article_attachments/360083774254)

, ao acioná-lo, fará com que pop-up **"Configurações da tela"** seja aberto para configurar a apresentação dos campos na tela.

![Config._grade.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4422442763543)

Os **"Disponíveis"** são todos os campos que existem na tela de agenda no Modo Planilha. Para efetuar a configuração dos campos, selecione o campo desejado e clique no botão 

![mceclip13.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085886074)

**"Adiciona o campo"** para que o sistema carregue o campo na parte dos **"Escolhidos"**, em seguida, clique no botão **"Salvar"**.

![Adiciona_campo.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4422436511639)

Além disto, é possível redimensionar o tamanho dos campos que foram escolhidos. Para isso, selecione o campo a ser redimensionado e, no campo **"Nova Largura"**, informe o valor desejado. Este valor não pode ser inferior ao campo **"Largura Mínima"**. Após fazer todos os redimensionamentos dos campos, clique no botão Salvar ou Salvar e aplicar.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4422445306647)

**Observação:** caso você clique no botão Salvar, ao fechar a tela, será necessário clicar no botão Aplicar da tela para que as alterações sejam feitas.

**Ordenação dos campos no modo planilha**

Em todas as telas onde há o modo planilha, podemos fazer a ordenação crescente e decrescente. Para isto, basta clicar no título da coluna que deseja fazer a ordenação. Para saber qual coluna está ordenada, o sistema marca a coluna com uma seta, informando se é crescente ou decrescente:

![aa.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360087186013)

[[voltar ao topo]](#top)

## 
Serviços por Executante

Para inserir um **"Produto"** e um **"Serviço"** a um **"Executante"** acesse a tela **"Serviços por Executante"**.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4422446076183)

```text
**

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311191435799)

**[Serviços por Executante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113153)

```

| Dica: Acesse o artigo , para conhecer as funcionalidades desta tela. |
| --- |

[[voltar ao topo]](#top)

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16077864648727)

 Acesse também:

[Lançamento de OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS)

[Pendências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604254-Pend%C3%AAncias)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)
- [SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874#abasmtp)
- [Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP)
- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)
- [Assinatura Digital](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112773)
- [Serviços por Executante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113153)
- [Lançamento de OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604414-Lan%C3%A7amento-de-OS)
- [Pendências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604254-Pend%C3%AAncias)