# Controle de Produtos por Grade

> **Módulo:** Comercial e Vendas | **Subseção:** Comercial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045269813-Controle-de-Produtos-por-Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045269813-Controle-de-Produtos-por-Grade)  
> **ID:** `360045269813` | **Última Atualização:** 2026-09-15T11:37:45Z

---

A funcionalidade da grade de produtos é utilizada para facilitar o lançamento e consulta de produtos que possuam mais de uma variação de característica, como exemplo: uma camiseta que tenha um modelo único, mas possui cores e tamanhos diferentes, sapatos, meias, calças, entre outros.

**Importante:** os módulos [Cotação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113993), WMS, Produção, [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia) e a rotina [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354) não suportam o Controle de Produtos por Grade.

Desta forma, temos a tela Modelo de Grade, para que você possa atribuir uma descrição para a grade, as dimensões que irão compor a mesma, se o posicionamento da dimensão será em **"Linha"** ou em **"Coluna"**, as variações das dimensões e as abreviações para cada uma destas.

![modelo_grade.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360061447914)

**Observação:** não é permitido o cadastro de um Modelo de Grade contendo mais de duas dimensões.

Acionando a marcação **"Usar máscara no campo controle?"**, o campo Controle ficará no seguinte formato: 

- Abreviação_Variação_Linha/Abreviação_Variação_Coluna

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28454055331991)

 Onde:

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815584817175)

 Abreviação_Variação_Linha**: refere-se ao campo** "Abreviação" **do cadastro de variações da dimensão do tipo **"Linha"**.

![Imagens_ksnip_209_.png](https://ajuda.sankhya.com.br/hc/article_attachments/9218230279575)

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815584817175)

 Abreviação_Variação_Coluna: **refere-se ao campo **"Abreviação"** do cadastro de variações da dimensão do tipo **"Coluna"**.

![Imagens_ksnip_210_.png](https://ajuda.sankhya.com.br/hc/article_attachments/9218453383191)

Por exemplo, pela estrutura da grade apresentada nas imagens acima, a informação que será gravada no campo Controle, será** "P/AZ"**.

Quando a marcação estiver desligada, o formato utilizado será: 

- Abreviação_Dimensão_Linha:Abreviação_Variação_Linha/Abreviação_Dimensão_Coluna:Abreviação_Variação_Coluna. 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28454055331991)

 Por exemplo: **"TM:P/CR:AZ"**, onde:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815584817175)

 **"TM"** é a abreviação da linha e** "P" **é a abreviação da variação da linha:

![Controle_de_produtos.png](https://ajuda.sankhya.com.br/hc/article_attachments/9218729083415)

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16815584817175)

 **"CR"** é a abreviação da coluna e** "AZ"** é a abreviação da variação da coluna:

![Controle_de_produtos__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/9218759980951)

**Observação:** você pode cadastrar para um modelo de grade, a mesma variação para dimensões diferentes. Por exemplo, se na dimensão Coluna, você realizar o cadastro da variação "01", na dimensão Linha, pode-se cadastrar também uma variação denominada "01".

 

#### **Associar um Modelo de Grade à um Produto**

Através do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba **"Medidas e estoque"**, sub-aba **"Controle adicional"**, será possível vincular um Modelo de Grade à um Produto, conforme demonstrado abaixo:

![grade.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360090505694)

**Nota:** será possível associar apenas um Modelo de Grade à um único Produto.

**Observação:** através do botão **"Definir Grade padrão"** você poderá definir uma **"Configuração para Compra"** e uma **"Configuração para Venda"**, informando se estes movimentos utilizarão a grade padrão p/ quantidade mínima e/ou a grade padrão fechada.

**Nota:** optando apenas pelo uso da grade padrão para quantidade mínima, será permitido que você edite os itens da nota, podendo apenas aumentar a quantidade dos itens nas centrais, não permitindo a exclusão de um item específico, tendo que excluir todos os itens.

Efetuando a marcação **"Usar grade padrão p/ quantidade mínima"**, será exibida a quantidade mínima de itens, conforme a quantidade definida nas Centrais de Compras/Vendas e Carrinho de Compras.

Em relação à marcação **"Usar grade padrão fechada"**, quando você habilitá-la, será exigida a quantidade exata de itens, conforme definido nas Centrais de Compras/Vendas e Carrinho de Compras.

**Importante:** quando a marcação Usar grade padrão p/ quantidade mínima estiver realizada e você efetuar a marcação Usar grade padrão fechada, automaticamente a marcação Usar grade padrão p/ quantidade mínima será desabilitada. Este comportamento também ocorre de forma contrária.

**Nota:** o comportamento descrito acima só acontece quando você estiver efetuando as duas marcações dentro da grade Configurações para Compra ou da grade Configurações para Venda. Por outro lado, você poderá efetuar a marcação Usar grade padrão p/ quantidade mínima da grade Configurações para Compra e selecionar a marcação Usar grade padrão fechada da grade Configurações para Venda sem que uma desabilite a outra e vice-versa.

O botão **"Limpar"** possibilita que você apague os registros da tabela de forma mais fácil. Clicando neste botão, o cadastro da grade padrão voltará para o status inicial de cadastro.

O botão **"Confirmar"** apenas será habilitado se a grade estiver preenchida com algum valor e se a marcação Usar grade padrão p/ quantidade mínima ou Usar grade padrão fechada estiver selecionada.

Em relação ao botão **"Desvincular"**, este estará habilitado somente após a confirmação do cadastro da grade padrão.

 

#### **Lançamento de produtos com Modelo de Grade nas Centrais**

Ao realizar um lançamento de um Produto controlado por grade nas Centrais, será disponibilizado o botão 

![Botão Grade FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16815651400727)

 **"Grade"**. Acionando-se este botão, será possível inserir a quantidade desejada de itens para cada variação do Produto:

**

![grade.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360062386873)

**

Ao confirmar o lançamento, todos os itens do Produto serão exibidos em linhas distintas, podendo-se observar suas descrições completas e suas variações.

**Observação:** você poderá editar o lançamento feito anteriormente selecionando o item; assim, será disponibilizada novamente a grade conforme o lançamento realizado para que o mesmo possa ser editado.

 

#### **Como lançar produtos com grade no carrinho de compras**

Também será possível realizar o lançamento de Produtos controlados por grade no Carrinho de Compras, sendo que, a Consulta do Produto será realizada pelo código do produto e, ao selecionar o mesmo, será disponibilizado o detalhamento do estoque contendo as colunas e linhas com as respectivas dimensões e variações, onde pode-se adicionar o produto com sua variação através da grade **"Detalhes de estoque"**:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/360061486974)

**Nota:** ao imprimir o DANFE, os produtos controlados por grade serão exibidos de forma detalhada e cada variação do produto será exibida de forma separada.


---

### 🔗 Links e Referências Internas:

- [Cotação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113993)
- [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia)
- [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)