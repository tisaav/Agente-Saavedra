# Cotação - Gerar Pedidos

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597114-Cota%C3%A7%C3%A3o-Gerar-Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597114-Cota%C3%A7%C3%A3o-Gerar-Pedidos)  
> **ID:** `360044597114` | **Última Atualização:** 2026-07-29T13:45:56Z

---

Ao clicar no botão **"Gerar Pedidos" **da tela [Cotação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113993), será aberta uma tela contendo o resumo do pedido a ser gerado

![Gerar_pedido.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4406188508439)

A grade superior **"Fornecedores"**, apresenta as informações do cabeçalho do pedido a ser gerado, como empresa, centro de resultado, natureza, projeto e tipo de negociação. 

Já a grade inferior **"Itens da Cotação"**, exibe os dados dos itens que serão gerados no pedido de compra. Ambas as grades permitem a remoção dos registros selecionados ou não selecionados, através dos botões 

![Botão Remover Selecionados FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16967055519127)

 **"Remove todas as linhas selecionadas"** e 

![Botão Remover Não Selecionados FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16967055522583)

**"Remove todas as linhas não selecionadas"**, respectivamente.

**Nota:** caso o parâmetro **"Conf. Automaticamente pedidos da Cot.? - COTACPEDCONF"** esteja ativado, os pedidos de compra serão gerados automaticamente já confirmados.

**Observação:** quando um produto estiver aprovado e outro cancelado, ao acionar o botão Gerar pedido tem-se que este será gerado normalmente e a cotação será fechada, desde que o parâmetro **"Fechar Cotação na Geração de Pedidos? - FECHARCOTGERPED"** encontre-se habilitado (padrão). Por outro lado, caso você deseje que a cotação não seja fechada, basta desabilitar o parâmetro.

Acesse os links abaixo para conhecer as demais funcionalidades dessa tela:

[Botão Transferir Itens](#Bot%C3%A3otransferiritens)                                                             [Gerando o Pedido](#GerandooPedido)

[Número da cotação no Pedido de Compra](#N%C3%BAmerodacota%C3%A7%C3%A3onopedidodecompra)                      [Reabrindo uma Cotação](#Reabrindoumacota%C3%A7%C3%A3o)

### 
Botão Transferir Itens

O botão **"Tranferir Itens"** localizado na grade inferior Itens da Cotação, será  utilizado na transferência dos itens aprovados de um fornecedor para outro. Para isso, o novo fornecedor para o qual o item será transferido, deve ter respondido o preço do produto em questão, caso contrário não será possível realizar a transferência.

Para acionar este botão, selecione primeiramente o fornecedor na grade superior e em seguida, os itens que deseja transferir na grade inferior. Ao clicar no botão, serão apresentados os fornecedores que responderam os itens selecionados. 

![Screenshot_6.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/5097398387991)

O campo** "Precificação"**, indica se o fornecedor respondeu a todos os itens selecionados ou não; se estiver igual a **"Total"** ele respondeu todos, se estiver igual a** "Parcial" **respondeu somente alguns itens. Para visualizar quais itens o fornecedor respondeu, clique no botão **"Visualizar produto"**.

Feita a seleção dos fornecedores que irão receber os itens selecionados, basta clicar no botão **"Transferir"**. Ao fazer isso, o sistema altera a situação dos fornecedores envolvidos na transferência dos itens de modo que, o novo fornecedor passa a ter a situação igual a **"Aprovado"** e o antigo fornecedor terá a situação alterada para **"Respondido"**.

[[voltar ao topo]](#top)

### 
Gerando o Pedido

Para gerar o pedido de compra, selecione um fornecedor na grade superior e em seguida clique no botão **"Gerar pedido"**. 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4406189790359)

Nesse momento, o sistema irá apresentar uma tela contendo informações do cabeçalho do pedido de compra a ser gerado. Vale lembrar que qualquer uma das informações pode ser alterada.

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/4406189997335)

**Nota:** quando a grade **"Moeda"** estiver preenchida com moedas estrangeiras, no ato da geração do pedido só será aceito o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de moeda (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), campo **"Operação em Moeda"**).

A princípio as informações apresentadas são originadas da cotação, mas caso não estejam preenchidas, você pode inserir ou até mesmo modificar um dado já existente.

Ao confirmar as informações, o pedido de compra é gerado com a apresentação do seu número único, e com isso, a situação da cotação do produto é alterada para **"Fechada"**.

**Observação:** o valor de frete apresentado no resumo de pedidos não é gerado no pedido de compra, ele é utilizado apenas para fins informativos.

[[voltar ao topo]](#top)

### 
Número da cotação no Pedido de Compra

Caso seja necessário realizar a rastreabilidade da cotação no pedido de compra, você pode criar um campo adicional na tabela de itens, através da tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294), tabela TGFITE.

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/4406201058071)

No campo **"Expressão"**, você pode inserir a seguinte informação:

#type.sql#

SELECT MAX(NUMCOTACAO) FROM TGFITC WHERE NUNOTACPA =

TGFITE.NUNOTA AND SEQNOTACPA = TGFITE.SEQUENCIA

Além disso, através do botão **"Atributos"** será apresentado o pop-up **"Atributos de campo adicional"**, onde você deverá assinalar as marcações** "Visível" **e** "Somente Leitura"**:

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/4406201026967)

Dessa forma, o número da cotação será apresentado na grade de itens do pedido de compra; essa configuração serve para que o usuário tenha ciência de qual cotação gerou o item do pedido de compra.

**Nota:** alterações realizadas no pedido de compra não refletem na cotação que gerou o pedido, por isso, caso as informações do item gerado no pedido estejam diferentes do que está na cotação, indica-se que o pedido de compra pode ter sido editado.

**Importante:** a configuração descrita acima, trata da apresentação do número da cotação apenas na grade de Itens. Os pedidos gerados pelo módulo Cotação, não irão apresentar em seu Cabeçalho a numeração da cotação, pois um pedido pode corresponder à várias cotações e vice-versa.

[[voltar ao topo]](#top)

### 
Reabrindo uma Cotação

Caso o item gerado no pedido seja excluído, ele terá sua situação alterada para **"Aprovado"** na rotina de Cotação. Caso o pedido de compra seja excluído, todos os itens do pedido terão a situação modificada para Aprovado. Isso caracteriza a reabertura de uma cotação anteriormente fechada pela geração do pedido de compra.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Cotação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113993)
- [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)
- [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294)