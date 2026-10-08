# Gerar Pedido p/Transf.entre Filiais

> **Módulo:** Comercial e Vendas | **Subseção:** Comercial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119953-Gerar-Pedido-p-Transf-entre-Filiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119953-Gerar-Pedido-p-Transf-entre-Filiais)  
> **ID:** `360045119953` | **Última Atualização:** 2026-07-29T14:33:34Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312145547031)

 Módulo: **Comercial > Rotinas               
```

Essa rotina gera um pedido de venda automático a partir de Pedido/Notas Pendentes e Confirmados de acordo com a Ordem de Carga informada nesse pedidos.

[Regras do pedido de venda gerado](#regrasdopedidodevendagerado)                                              [Considerações gerais](#considera%C3%A7%C3%B5esgerais)      

[Parâmetros que influenciam a rotina](#par%C3%A2metrosqueinfluenciamarotina)

Campos pertinentes à tela                             

Ao gerar vários Pedidos de venda, com uma mesma Ordem de Carga ao executar o pedido nessa rotina, será gerado um Pedido, já confirmado, contendo todos os itens desses diferentes Pedidos agrupados.

![GPVEF01.png](https://ajuda.sankhya.com.br/hc/article_attachments/360083559734)

O campo **"Empresa Origem"** irá exibir apenas empresas que estão ligadas a um Parceiro.

No campo **"Série"** informe a Série da Nota do Pedido de Venda a ser gerado.

**Nota:** caso a numeração da TOP estiver estipulada como **"Empresa/Série"**, a Série em questão deverá ser informada neste campo.

Em **"TOP de Pedido"**, você deverá informar a TOP utilizada para gerar o Pedido. Será necessário que esta esteja **"Ativa"**, seja do Tipo de Movimento Pedido de Venda; não deverá atualizar financeiro e nem estoque, ser deve ser NFe e a base de numeração não poderá ser manual. Caso uma TOP que não esteja nestas condições seja informada, o sistema emitirá a mensagem:

***"Tipo de Operação não existe ou não pode ser usado aqui:."***

O **"Tipo de Negociação"** será o Tipo de Negociação para a geração do Pedido, e este deverá estar Ativo.

Referente ao campo **"Empresa com O.C/Negociação"**, neste insira a Empresa que possui a Ordem de Carga criada e que possui Pedidos de Venda Pendentes para efetuar a geração. A tela de pesquisa trará somente as empresas ativas.

Em **"Ordem de Carga"** será apresentado as ordens de carga ligadas à empresa informada no campo Empresa O.C/Negociação.

**Observação:** esta deverá retornar apenas Ordens de Carga que obtenham Pedidos Pendentes na TFCAB. Assim, considere o exemplo:

Para a **"Empresa de O.C\Negociação: 2"** não há Pedidos de Venda Pendentes, portanto, a tela de pesquisa de Ordem de Carga estará vazia:

![GPCEF02.png](https://ajuda.sankhya.com.br/hc/article_attachments/360083550214)

Caso a marcação** "Considerar corte" **estiver selecionada, na soma da Quantidade dos itens será considerada a **"Qtd. Negociada"** - **"Qtd. Atendida"**. Caso desmarcada, será considerado na soma, somente a Qtd. Negociada dos Pedidos de Vendas pendentes.

Existe outro Pedido de Venda pendente e este não teve corte:

![GPCEF03.png](https://ajuda.sankhya.com.br/hc/article_attachments/360083550694)

Pedido de Venda gerado:

![GPCEF04.png](https://ajuda.sankhya.com.br/hc/article_attachments/360083550794)

Analisando o produto 183:

Pedidos de Venda Pendentes 4633, 4634

Pedido de Venda gerado 4635:

NUNOTA|CODPROD|QTDNEG|QTDENTREGUE|QTDCONFERIDA

4633     |183         |15        |0                    |10

4634     |183         |15        |0                    |0

4635     |183         |20        |0                    |0

Como foi solicitado considerar o corte, a quantidade negociada total do item será: 15+15-10 = 20.

Se existir no sistema um Pedido Pendente com uma OC, mas esse Pedido não possuir itens, a OC será apresentada no campo Ordem de Carga, porém o sistema não efetuará a rotina, apresentando a mensagem:

***"Nenhum pedido foi encontrado para a empresa e ordem de carga informada."***

[[voltar ao topo]](#top)

## 
Regras do pedido de venda gerado

A data de transferência será a data atual:

![GPCEF05.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084719813)

Na tela **"Empresas"**, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abageral) Usar o Parceiro ligado a Empresa da Ordem de Carga:

![GPCEF06.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084720753)

Pedido de Venda gerado:

![GPCEF07.png](https://ajuda.sankhya.com.br/hc/article_attachments/360084721253)

Usar o Tipo de Negociação e Tipo de Operação informado na tela, sendo eles a **"TOP de Pedido"** como Pedido de Venda e o **"Tipo de Negociação"** A prazo - 21 dias.

Ao concluir a rotina, a Ordem de Carga será gravada no campo **"Observação da Nota"** com o seguinte texto:

#### ***"ORDEM CARGA DE ORIGEM: 99, onde 99 é o número da ordem de carga."***

Se algum produto tiver Preço zerado o processo será abortado, apresentando mensagem dizendo que o produto não tem preço.

[[voltar ao topo]](#top)

## 
Considerações gerais

As TOP’s utilizadas nesta rotina não poderão atualizar o estoque nem o financeiro e a numeração não poderá ser manual.

Para **"Empresa Origem"** serão mostradas apenas empresas ligadas a um Parceiro.

O Pedido que será gerado, será gerado com o Parceiro ligado a Empresa da Ordem de Carga e o preço dos produtos nesse Pedido gerado, será definido de acordo com a Tabela de preços desse Parceiro (Parceiro da Empresa da OC/Negociação).

Se tiver algum Preço zerado o processo será abortado, apresentando mensagem dizendo que o produto não tem preço.

Ao realizar a rotina, a Ordem de Carga será gravada no campo **"Observação da TGFCAB"** no Pedido que foi gerado.

**Nota:** o campo Ordem de Carga desta rotina apresentará apenas Ordens de Carga que tenham **"Pedidos Pendentes"** no sistema.

No caso de existir no sistema um **"Pedido Pendente"** com uma OC, mas esse Pedido não possuir itens, a OC será apresentada na tela, porém o sistema não efetuará a rotina apresentando a mensagem:

***"Nenhum pedido foi encontrado para a empresa e ordem de carga, informadas".***

[[voltar ao topo]](#top)

## Parâmetros que influenciam a rotina

Se o parâmetro **"Fechar Ordem Carga ao gerar Pedido Transferência - FECHAOCTRANSF"** estiver ligado, ao executar a rotina o sistema o perguntará:

***"Esta ordem de carga ainda não foi fechada. Deseja fechá-la antes de gerar a transferência?"***

Se responder **"Sim"**, mudará o campo **"Situação da OC"** para fechada. Caso a resposta seja **"Não"**, o sistema emitirá a mensagem, de que foi efetuado o cancelamento a pedido do cliente.

Se habilitado o parâmetro **"Somente pedidos pendentes na trans. entre filiais - SOPENTRANSFIL"**, a rotina irá automaticamente criar, um Pedido de Venda já confirmado, somando os produtos encontrados a partir dos Pedidos Confirmados e pendentes, de acordo com a Ordem de Carga informada.

Se desligado será gerado um Pedido com todas as Notas de Venda da Ordem de Carga, independentemente da sua pendência.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abageral)