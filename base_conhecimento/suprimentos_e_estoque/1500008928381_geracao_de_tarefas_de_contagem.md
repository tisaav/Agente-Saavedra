# Geração de Tarefas de Contagem

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Gera%C3%A7%C3%A3o-de-Tarefas-de-Contagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Gera%C3%A7%C3%A3o-de-Tarefas-de-Contagem)  
> **ID:** `1500008928381` | **Última Atualização:** 2026-07-29T14:12:44Z

---

Através da tela Geração de Tarefas de Contagem, que pode ser acessada pelo menu **"WMS > Inventário"**, criamos as tarefas que serão executadas posteriormente por quem utiliza o Coletor SuperWaba.

Para dar início na geração de tarefas de contagem, primeiramente você deve possuir um [Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS#invent%C3%A1rios1) cadastrado. 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500013713501)

Informe ao lado esquerdo da tela, o **"Inventário"** cadastrado inicialmente. Você também pode realizar um filtro por **"Empresa"**,** "Produto"**, **"Grupo de Produtos"**,** "Fornecedor"**, **"Depositante"**, **"Marca"**, **"Faixa de Endereços"**, **"Endereços com Contagem Pendentes"**, **"Tipo de Endereços"**, **"Lado do Endereço"**, **"Última data de contagem"** e **"Ocorrências"**.

Após definir os filtros desejados, clique no botão **"Aplicar"** para que sejam exibidos na grade os endereços que serão contados, sendo que você pode ainda utilizar os botões 

![Botão Remover Selecionados FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16978551054231)

 **"Remover selecionados"** e 

![Botão Remover Não Selecionados FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16978535216407)

 **"Remover NÃO selecionados"** para retirar algum endereço da grade.

Escolhendo o endereço, o próximo passo é clicar no botão 

![botão-gerar-tarefas-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16978549426455)

 **"Gerar tarefas"**. Através do pop-up **"Geração de Tarefas"**, você determina o usuário que irá contar os endereços definidos na grade; somente esse usuário poderá proceder com a contagem no Coletor. No gif abaixo demonstramos como fazer o procedimento:

![inventario4.gif](https://ajuda.sankhya.com.br/hc/article_attachments/16978471108759)

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16978572058775)

 Caso seja necessário alterar o usuário, utilize o botão 

![botão-substituir-usuários-FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16978549427991)

**"Substituir Usuários"** localizado no alto da tela.

**Importante:** para o [Inventário Rotativo](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS#invent%C3%A1riorotativo), nesse pop-up você poderá determinar também, além do Usuário, como será gerada a contagem, se por **"Endereço"** ou por **"Produto específico"**; optando por essa segunda opção, você deve especificar o produto, de modo que, nesse caso, são contados em todos os endereços onde existe estoque do referido produto.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16978485829527)

 Observações importantes a respeito da Geração de Tarefas:**

- 

Ao realizar a confirmação da geração de tarefas, será verificado se existem tarefas pendentes que não sejam de inventário, para os endereços em que estão sendo geradas. Caso sejam encontrados endereços com pendências, será exibido o pop-up **"Tarefas Pendentes"** constando o endereço e a pendência.

- 

No pop-up de Tarefas Pendentes, temos os seguintes botões:

O botão** "Somente para endereços sem pendências"** que irá gerar as tarefas apenas para os endereços que não contenham pendência; e o botão** "Cancelar" **que, quando acionado, cancelará a geração de tarefas.

- 

O parâmetro **"Permitir tar. de contagem em end. com pendências - WMSPERMCONTEP"** quando habilitado, exibe o botão **"Continuar mesmo assim"**, possibilitando que você prossiga com a geração de tarefas de contagem nos endereços com pendências. Optando pelo prosseguimento, as tarefas serão geradas, mas a sua contagem não será permitida até que sejam sanadas as pendências constantes.

Feita a geração das tarefas, agora é necessário trabalhar com o [Coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112173). O responsável deve acessar o Coletor SuperWaba e escolher a função **"****Contagem de estoque****"**; em seguida, acionar o botão **"Tarefa"**, informar o **"Endereço"** onde será inserido o estoque do produto, a **"Quantidade"** de produto contada no estoque e o **"Produto"** correspondente ao estoque contado:

![inventario5.gif](https://ajuda.sankhya.com.br/hc/article_attachments/16978485837463)

**Observação:** não existindo nada no endereço, clique em **"End. Vazio"**:

Ao final, será exibida a mensagem ***"Item lido com sucesso!"***.

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16978572058775)

 Se existir mais de um produto no endereço, realize a leitura do código de barras de todos eles com suas devidas quantidades

Para concluir a Contagem de Estoque, clique no botão **"Enviar"** para ser apresentada a Quantidade informada e o respectivo Produto e, logo em seguida, clique novamente no botão Enviar.

Caso não existam mais tarefas em aberto, será exibida a mensagem **"Não há tarefas em aberto/adequadas para o usuário/Equipamento"**, finalizando então essa etapa:

![inventario6.gif](https://ajuda.sankhya.com.br/hc/article_attachments/16978485840663)

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16978471124887)

 Acesse também:

[Histórico de Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120373)

[Como fazer o ajuste de estoque por inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Como-fazer-o-ajuste-de-estoque-por-invent%C3%A1rio-no-WMS)

[Como realizar o processo de inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS)


---

### 🔗 Links e Referências Internas:

- [Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS#invent%C3%A1rios1)
- [Inventário Rotativo](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS#invent%C3%A1riorotativo)
- [Coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112173)
- [Histórico de Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120373)
- [Como fazer o ajuste de estoque por inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Como-fazer-o-ajuste-de-estoque-por-invent%C3%A1rio-no-WMS)
- [Como realizar o processo de inventário no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS)