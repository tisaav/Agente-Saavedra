# Ressuprimento Preventivo

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120193-Ressuprimento-Preventivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120193-Ressuprimento-Preventivo)  
> **ID:** `360045120193` | **Última Atualização:** 2026-08-04T14:00:08Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311567510551)

 Módulo: **WMS > Rotinas
```

O Ressuprimento Preventivo é um importante procedimento envolvido na rotina de um armazém, que permite a verificação e o abastecimento de todos os seus endereços antes do início das separações de mercadoria, aprimorando assim o processo; o gestor de armazenagem poderá comandar reabastecimentos preventivos anteriormente ao começo da operação de separação de produtos.

![tela Ressuprimento Preventivo.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16923950255383)

Nesta tela serão apresentados todos os endereços de picking de acordo com o seu percentual de completude atual, levando em consideração os filtros que forem aplicados.

No lado esquerdo da tela, além da possibilidade de criação de filtros personalizados para apresentação das informações, você pode preencher os seguintes campos para filtragem:

O campo** "Empresa"** é de preenchimento obrigatório, onde você informa a Empresa a qual os produtos pertencem.

Você pode buscar os endereços de picking através do **"Produto"** neles contido.

De forma aliada ao produto informado no campo anterior, você também pode buscar os endereços informando a **"Marca"** dos itens.

Através do campo **"Faixa de endereço"** é possível também buscar os endereços através de um determinado trecho destes endereços.

Pelo campo** "% de completude"** você pode buscar por endereços, de acordo com seu percentual de preenchimento atual do estoque em relação a sua capacidade máxima.

A marcação** "Apresentar também pickings sem estoque para ressuprimento"** quando efetuada, exibe na grade os pickings que não possuam estoque em outros endereços de pulmão disponíveis para ressuprimento; as linhas contendo esses pickings aparecerão em vermelho.

 

#### **Seção Preferências para Geração de Tarefas**

O campo** "Priorização de endereços de origem" **possui duas possibilidades de definição, a saber:

- Aqueles com mais estoque;

- Aqueles com menos estoque.

No campo** "Considerar como estoque na origem" **temos duas possibilidades de definição:

- 
**Qtd. atual no endereço:** Mostra a quantidade nos pulmões de acordo com a quantidade no estoque menos as saídas pendentes no mesmo, ou seja, o estoque real. 

- 
**Qtd. futura (Estoque + Ent. Pendentes):** Exibe a quantidade de estoque nos pulmões de acordo com o estoque futuro. 

Determinando os filtros desejados e clicando em **"Aplicar"**, serão apresentados na grade os endereços que irão passar pelo ressuprimento. No campo **"Qtd. Sug (UN.PK)"**, informe o valor a ser ressuprido, sendo que, caso este extrapole a quantidade suficiente nos outros estoques para ressuprimento, a seguinte mensagem será apresentada:

***"Quantidade informada superior ao estoque do produto no endereço de reabastecimento".***

Na parte superior da tela, temos alguns botões facilitadores do processo de ressuprimento. São eles:

Os botões 

![Botão Remover Selecionados FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16923839727255)

** "Remover selecionados"** e 

![Botão Remover Não Selecionados FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16923839730071)

 **"Remover NÃO selecionados"**, realizam a retirada da grade de endereços que não irão participar do ressuprimento.

Ao acionar o botão

![botão-executante...-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16924028248471)

 **"Executante..."** será aberta a seguinte tela: 

![pop-up Executante da tarefa.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16923946831255)

Determine aqui um executante para a tarefa, onde temos a marcação **"Todos os produtos"** que, ao ser acionada, atribui para todos os produtos na grade que terão os ressuprimentos gerados, o executante informado. Temos também a marcação **"Produtos selecionados"** que, quando assinalada, define o executante da tarefa apenas para as linhas selecionadas na grade.

 O botão 

![botão-gerar-tarefas...-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16924093640727)

 **"Gerar Tarefas..."** quando acionado, temos a exibição de um novo painel na tela, além de uma nova grade contendo quais foram as tarefas geradas; neste novo painel, é possível **"Remover"** tarefas selecionadas ou não selecionadas, **"Confirmar"** e **"Cancelar"** tarefas, ou ainda modificar o endereço de origem.

**Observação: **quando o parâmetro **"Permite Reabastecimento p/ Estoq. Min zero no WMS? - REABESTZEROWMS"** estiver ligado, será feito o reabastecimento quando o endereço estiver configurado com o estoque mínimo igual a zero. Se estiver desligado, o reabastecimento só será gerado se o estoque mínimo do endereço for maior do que zero.