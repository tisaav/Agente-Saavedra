# Processo de Inventário

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Processo-de-Invent%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Processo-de-Invent%C3%A1rio)  
> **ID:** `1500007989601` | **Última Atualização:** 2026-07-29T14:12:37Z

---

O inventário é a prática por meio da qual realizamos a contagem e a conferência de todos os itens disponíveis em estoque. Além disso, checamos os resultados, comparando-os às quantidades informadas no controle feito através do Sankhya Om.

Na tela Inventários, localizada no menu **"WMS > Inventário"** de nosso sistema, podemos definir o **"Tipo"** de inventário que será realizado, sua data e hora inicial e final, a **"Empresa"** utilizada e ainda, adicionar alguma **"Observação"** importante.

Para verificar como é feito o processo de cada um dos tipos de inventários, acesse os links abaixo:

[Inventário de Implantação](#invent%C3%A1riodeimplanta%C3%A7%C3%A3o)                     [Inventário Rotativo](#invent%C3%A1riorotativo)                        [Inventário Global](#invent%C3%A1rioglobal)

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500011677742)

## 
Inventário de Implantação

Um inventário de implantação, ao ser configurado, tem a função principal de atualizar o saldo de estoque inicial no WMS e no ERP, possibilitando as movimentações futuras desses itens.

Portanto, para que você consiga fazer o processo de Inventário de Implantação com sucesso, realize primeiramente as configurações descritas abaixo:

1. Na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), cadastre os endereços de picking que receberão os produtos que terão o saldo inicial inserido;

1. Na tela de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), cadastre devidamente os produtos que terão seu saldo de estoque incluído e se atente para a aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms), onde você deverá incluir o endereço de picking que o produto será alocado;

1. Inclua também, um [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos) que será utilizado para geração da nota responsável pela inserção de estoque. Sendo assim, você deve utilizar um **"Tipo de Operação - TOP"** que dê entrada no estoque.

Realizadas as configurações acima, você já pode iniciar o processo de Inventário. Trouxemos um fluxograma para te auxiliar na execução do processo, bastando que você clique em cada uma das etapas abaixo:

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311467238423)

[#invent%C3%A1rios1](#invent%C3%A1rios1)

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311467240855)

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311496775319)

[#gera%C3%A7%C3%A3odetarefasdecontagem1](#gera%C3%A7%C3%A3odetarefasdecontagem1)

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311467242519)

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311496779671)

[#contagemdeestoque](#contagemdeestoque)

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311496781335)

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311496781975)

[#consultadeprodutos](#consultadeprodutos)

![mceclip9.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311496783383)

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311467251991)

[#ajustedeestoque](#ajustedeestoque)

![mceclip9.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311496783383)

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311467252503)

[#ajustedeestoqueporinvent%C3%A1rio](#ajustedeestoqueporinvent%C3%A1rio)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |

Na tela Inventários do Sankhya Om, faça a inclusão de um novo inventário, selecionando a opção **"Implantação"** no campo **"Tipo"**:

![inventario.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500011794922)

Em seguida, na tela Geração de Tarefas de Contagem, inclua o inventário cadastrado no passo anterior conforme demonstramos abaixo:

![inventario4.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500012095801)

Após gerar as tarefas, acesse o Coletor com o usuário responsável pela tarefa de Contagem de Estoque, clique no botão **"Tarefa"**, informe o **"Endereço"** onde será inserido o estoque do produto, a **"Quantidade"** de produto contada no estoque e o **"Produto"** correspondente ao estoque contado:

![inventario5.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500012284742)

Ao final, será exibida a mensagem ***"Item lido com sucesso!"***.

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16978837965207)

 Repita o procedimento acima para todos os produtos que terão seu estoque incluído.

Para concluir a Contagem de Estoque, clique no botão **"Enviar"** para ser apresentada a Quantidade informada e o respectivo Produto e, logo em seguida, clique novamente no botão Enviar.

Caso não existam mais tarefas em aberto, será exibida a mensagem **"Não há tarefas em aberto/adequadas para o usuário/Equipamento"**, finalizando então essa etapa:

![inventario6.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500012635401)

No próximo passo, você deverá acessar a tela Ajuste de Estoque por Inventário, informar o Inventário cadastrado no início do processo, escolher o item na grade à direita e clicar no botão 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500012285202)

 **"Implantar Estoque"**. Será aberto o pop-up **"Ajuste de Estoque"**, onde você poderá definir os endereços que serão desbloqueados, bem como se o inventário será fechado. Definidos os ajustes, basta clicar no botão **"Gerar Ajuste"**. Observe abaixo como é feito esse processo:

![inventario7.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500012635821)

Concluindo a etapa acima, acesse a tela Ajuste de Estoque no Sankhya Om, preenchendo os campos obrigatórios e informando o Inventário criado na primeira etapa de nosso processo. Após isso, clique no botão **"Ajustar"** para que seja exibido o pop-up **"Notas Geradas"** contendo a numeração da nota responsável pela inclusão do estoque fiscal dos produtos e dê um duplo clique sobre ela; assim, será aberta a [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) para que você a confirme. No gif abaixo, demonstramos essa etapa para você:

![inventario8.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500012285602)

Por fim, na tela Consulta de Produtos você poderá verificar se o produto que teve seu estoque incluído está de fato com o saldo alimentado:

![inventario9.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500012285942)

No Inventário de Implantação, o sistema limpará o estoque do endereço antes de implantar, portanto, o mesmo endereço não poderá participar de mais de um Inventário de Implantação, visto que o primeiro será removido quando o segundo for ajustado. Sendo assim, nesse tipo de inventário, a marcação **"Permite apenas contagem por produto"** existente tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento) não será respeitada.

[[voltar ao subtítulo]](#invent%C3%A1riodeimplanta%C3%A7%C3%A3o) [[voltar ao topo]](#top)

## 
Inventário Rotativo

Outro tipo de inventário é o Rotativo. Ele tem o objetivo de fornecer dados atuais a respeito dos saldos de estoque no WMS, fazendo com que esses saldos sejam corretamente conferidos e/ou atualizados para mais ou para menos conforme o caso, possibilitando as movimentações futuras dos itens.

Para que você consiga fazer o processo de Inventário Rotativo, realize também as [configurações](#configura%C3%A7%C3%B5es) que descrevemos no tópico sobre o [Inventário de Implantação](#invent%C3%A1riodeimplanta%C3%A7%C3%A3o).

**Importante:** o passo a passo do processo de Inventário Rotativo são os mesmos do Inventário de Implantação, porém, tendo o [Ajuste de Estoque de Inventário](#ajustedeestoqueporinvent%C3%A1rio) como sua última etapa.

**Observação:** para esse tipo de inventário, na tela Inventários do Sankhya Om, você deve selecionar a opção **"Rotativo"** no campo **"Tipo"**:

![inventario2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500011795002)

**Nota:** na etapa de [Geração de Tarefas de Contagem](#gera%C3%A7%C3%A3odetarefasdecontagem1) desse tipo de inventário, a contagem poderá ser por **"Endereço"** ou por **"Produto específico"**.

**Importante:** caso a [Contagem de Estoque](#contagemdeestoque) do produto tenha sido realizada com divergências para mais ou para menos, você deverá fazer o ajuste do estoque correspondente ao item, ou seja, se a contagem foi para menos, gera-se uma nota de saída para retirada do estoque; se para mais, deve-se gerar uma nota de entrada no estoque, para que o estoque contado fique coerente com o estoque real do WMS.

O procedimento acima é realizado na tela [Consulta Estoque com Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias) de nosso sistema. Para isso, preencha os campos e marcações obrigatórios e clique em **"Aplicar"**; na grade, serão apresentados os endereços com seus respectivos estoques originados da contagem. Em seguida, clique no botão **"Gerar Nota de Ajuste"** para que seja exibido um pop-up contendo o número único da nota de saída ou entrada do estoque, conforme cada caso.

[[voltar ao subtítulo]](#invent%C3%A1riorotativo) [[voltar ao topo]](#top)

## 
Inventário Global

O terceiro tipo de inventário que temos é o Global e tem o mesmo objetivo do [Inventário Rotativo](#invent%C3%A1riorotativo), que é de fornecer dados atuais a respeito dos saldos de estoque no WMS.

Para fazer o processo de Inventário Global, você também deve realizar as [configurações](#configura%C3%A7%C3%B5es) que descrevemos no tópico sobre o [Inventário de Implantação](#invent%C3%A1riodeimplanta%C3%A7%C3%A3o).

O passo a passo do processo de Inventário Global são os mesmos do Inventário de Implantação, porém, tendo o [Ajuste de Estoque de Inventário](#ajustedeestoqueporinvent%C3%A1rio) como sua última etapa, assim como no Inventário Rotativo.

**Observação:** assim como nos outros tipos de inventários, você deve acessar a tela Inventários do Sankhya Om e fazer a inclusão de um novo inventário, mas nesse, selecionando a opção **"Global"** no campo **"Tipo"**:

![inventario3.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500012095101)

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16978837965207)

 Nos Inventários Rotativo e Global você poderá confirmar o Ajuste no Estoque gerado acessando a tela [Estoque / Endereçamento WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS).

**Importante:** a única diferença entre o inventário [Rotativo](#invent%C3%A1riorotativo) e o Global é que, nesse último, no pop-up **"Contagem de Estoque"** do botão **"Gerar Ajuste" **da tela Ajuste de Estoque por Inventário, são apresentadas as opções **"Apenas produto com no mínimo X contagens dentro do inventário"** e **"... e com as X últimas contagens iguais"**:

![inventario11.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500012286422)

[[voltar ao subtítulo]](#invent%C3%A1rioglobal) [[voltar ao topo]](#top)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16978865764631)

 Acesse também:

[Histórico de Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120373-Hist%C3%B3rico-de-Ajuste-de-Estoque)

[Como fazer o ajuste de estoque por inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Como-fazer-o-ajuste-de-estoque-por-invent%C3%A1rio-no-WMS)

[Como gerar as tarefas de contagem no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Como-gerar-as-tarefas-de-contagem-no-WMS)


---

### 🔗 Links e Referências Internas:

- [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento)
- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)
- [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms)
- [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)
- [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)
- [Consulta Estoque com Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613094-Consulta-Estoque-com-Ocorr%C3%AAncias)
- [Estoque / Endereçamento WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS)
- [Histórico de Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120373-Hist%C3%B3rico-de-Ajuste-de-Estoque)
- [Como fazer o ajuste de estoque por inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Como-fazer-o-ajuste-de-estoque-por-invent%C3%A1rio-no-WMS)
- [Como gerar as tarefas de contagem no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Como-gerar-as-tarefas-de-contagem-no-WMS)