# Divergências no Registro de Conferência - WMS

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012384422-Diverg%C3%AAncias-no-Registro-de-Confer%C3%AAncia-WMS)  
> **ID:** `1500012384422` | **Última Atualização:** 2026-07-29T14:12:57Z

---

Conforme mencionamos no artigo sobre o processo de [Registo de Conferência no Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias), pode ser que em algum momento hajam divergências durante a conferência. Aqui nesse artigo trataremos sobre elas. 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311489515927)

[#registrodeavaria](#registrodeavaria)

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311489516567)

[#registrocomsobra](#registrocomsobra)

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311483541527)

[#registrodefalta](#registrodefalta)

**Clique nas imagens abaixo para verificar sobre cada uma das divergências:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |

### 
Registro de Avaria

No Registro de Conferência é possível evitar que na mesma U.M.A sejam alocados produtos em bom estado com produtos avariados, fazendo com que sejam geradas as tarefas de Armazenagem somente da quantidade **"não avariada"**.

Essa configuração é feita através do parâmetro **"Verificar avaria no fechamento da UMA no registro. - VERAVAFEUMARC"**.

Para registrar uma Avaria, você deve informar no Coletor, no momento do [registro de conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#tarefaregistrodeconfer%C3%AAncia), a quantidade total daquele produto e informar o quanto daquele total está avariado, diferente da conferência convencional, onde é informada a *quantidade + avaria = quantidade total do produto*. Observe abaixo:

![diverg1.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019868981)

Após ser feito o registro da Avaria, é possível visualizar através do botão 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500019856101)

 da tela [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias), que o sistema gerou a tarefa apenas para a quantidade não avariada **(25)**:

![diverg3.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019600902)

Para fazer a tratativa dessa Avaria, devemos [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca) pelo botão 

![Botão Outras Opções.. FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16978228252311)

 **"Outras Opções..."** da tela Recebimento de Mercadorias, conforme demonstramos abaixo:

![diverg4.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019601282)

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458188032535)

 **Você poderá **"Devolver Avaria"** através do botão 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500019601342)

, onde será gerada a Nota de Devolução com a quantidade avariada, ou pode **"Aceitar Avaria"**, clicando no botão 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500019601422)

. No nosso caso acima, aceitamos a Avaria.

Ao finalizar a tratativa de divergência aceitando a avaria, o próximo passo é gerar a tarefa de armazenagem para o endereço de avaria na tela [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento).

**Observação:** para que a tarefa de armazenagem seja gerada é necessário que no cadastro do [Endereço de Avaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral) o campo **"Situação do Estoque"** esteja com a opção **"Bloqueado" **selecionada.

![diverg5.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019876741)

Agora que as tarefas foram geradas, o produto está pronto para ser armazenado, tanto a quantidade avariada quanto a que não está:

![diverg7.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019607982)

Após finalizar a tarefa de [armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#armazenagem), processe novamente o recebimento para validar a conferência e, posteriormente libere a doca, da mesma forma como demonstramos no artigo [Processar Recebimento e Liberar a Doca](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca).

[[voltar ao subtítulo]](#registrodeavaria) [[voltar ao topo]](#top)

### 
Registro com Sobra

O Registo de Conferência tem uma particularidade de alertar o conferente quando a quantidade conferida do produto está maior do que a quantidade negociada na Nota. Para isso ocorrer, basta desligar o parâmetro **"Permitir contar a maior no Registro de Conferência - PERMCONTREGCON"**.

No nosso exemplo, a quantidade negociada na Nota foi de 50 unidades e, no momento da conferência informamos 60 unidades. Assim, com o parâmetro acima desligado, quando for identificada a sobra na conferência, será gerada a mensagem abaixo:

![diverg8.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019884641)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458188032535)

 No pop-up da mensagem acima, se optarmos por **"Sim"**, o sistema aceitará a quantidade informada, mesmo com divergência e, caso clicarmos em **"Não"**, o cursor voltará para o campo **"Quantidade"** para iniciar a conferência de outro produto ou já resolver a divergência do primeiro e assim, seguir com a conferência.

Após ser feito o registro da Sobra, você consegue visualizar através do botão 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500019856101)

 da tela [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias), a tarefa gerada para o produto após a conferência:

![diverg9.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019885241)

Para realizar a tratativa dessa Sobra, devemos [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca) pelo botão **"Outras Opções..."** da tela Recebimento de Mercadorias, assim como demonstramos abaixo:

![diverg10.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019980741)

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458188032535)

 **Você poderá **"Devolver Tudo"**, ou seja, todos os itens da nota, onde será gerada a Nota de Devolução com a quantidade total da nota de compra, **"Devolver Item"** através do botão 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500019711202)

 para devolver apenas a quantidade do item selecionado, ou poderá **"Aceitar Diferença"**, clicando no botão 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500019614622)

, para que seja lançada uma nota de compra para alimentar o estoque fiscal, armazenando a quantidade a mais. No nosso caso acima, aceitamos a Sobra.

Finalizado o registro de conferência com sobra, já podemos executar as tarefas de [Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#armazenagem) no Coletor. Observe abaixo como fazemos o processo:

![diverg11.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019981321)

Ao concluir o processo de Armazenagem, na tela Recebimento de Mercadorias, a situação do recebimento será alterada para **"Armazenado"**.

Por fim, basta que você faça a Liberação da Doca:

![diverg12.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019981721)

[[voltar ao subtítulo]](#registrocomsobra) [[voltar ao topo]](#top)

### 
Registro de Falta

No Registro de Conferência com Falta, podem ocorrer 2 situações: a [Falta Parcial](#faltaparcial) e a [Falta Total](#faltatotal). Nesse tópico, trataremos sobre elas.

**Falta Parcial**

A Falta Parcial de um produto é identificada no momento do Registro de Conferência e segue os mesmos procedimentos que o registro de [Avaria](#registrodeavaria) e com [Sobra](#registrocomsobra) para sua tratativa.

No exemplo abaixo, a quantidade da nota é de 100 unidades e, no momento da conferência, fizemos a contagem de apenas 50 unidades:

![diverg14.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019983761)

Agora, o próximo passo é [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca). Quando ocorrer a falta parcial, caso a tratativa seja **"Recontar"**, essa recontagem deve ser feita informando a própria U.M.A,. Observe abaixo como fazer:

![diverg15.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019983921)

Após ser executada a recontagem, podemos finalizá-la clicando no botão **"Fechar U.M.A"**; assim, o sistema irá sobrepor a primeira tarefa de Armazenagem gerada com 50 unidades, enviando 100 unidades para armazenagem:

![diverg16.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019713502)

Ao invés de fazer a Recontagem, você poderá **"Devolver Falta"** através do botão 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500019988521)

. Quando for acionado, será gerada uma nota de Devolução de Compra com a quantidade apresentada com falta.

Finalizada a tratativa da divergência de falta parcial, os produtos já podem ser [armazenados](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#armazenagem) e a [doca liberada](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca):

![diverg18.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019713942)

[[voltar ao subtítulo]](#registrodefalta)

**Falta Total**

Demonstraremos agora a Falta Total no processo de Registro de Conferência. No nosso exemplo, lançamos uma nota com dois produtos e enviamos para o WMS. Após isso, ao executar a tarefa de [registro de conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#tarefaregistrodeconfer%C3%AAncia), registramos a entrada apenas de um dos produtos da nota: 

![diverg19.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019986021)

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458188032535)

 **Ao final da conferência, são apresentadas as **"Qtde itens recebimento: 2"** e **"Qtde. Itens conferidos: 1"** e a mensagem ***"Este recebimento possui 1item(s) pendente(s) de conferência. Ao acionar o Finalizar este(s) produto(s) será(ão) tratado(s) com divergência de falta"***.

Após registrar os produtos, iremos [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca) para tratar as divergências. Em nosso exemplo, iremos realizar a Recontagem do produto:

![diverg20.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019987041)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458188032535)

 Diferente da [Falta Parcial](#faltaparcial), quando se tem a Falta Total de um produto, o sistema gera uma Unidade de Movimentação de Armazenagem - U.M.A interna (que pode ser consultada na tabela TGWRCON) para realizar a recontagem; então, essa U.M.A deve ser bipada para o início da tarefa de recontagem.

No nosso caso, a U.M.A criada foi a **"REC718150"** (onde REC=Recebimento, 718=Número do Recebimento e 150=Código do Produto):

![diverg22.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500019737542)

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458188032535)

 **A U.M.A é criada devido o produto não ter sido alocado à uma U.M.A durante a conferência e, caso esse recebimento tivesse mais produtos não conferidos, seriam criadas U.M.A's internas para cada produto.

No caso que demonstramos acima, realizamos a Recontagem e informamos a quantidade correta, ou seja, de 100 unidades; porém, poderíamos ter optado por **"Devolver Falta"**, através do botão 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500019988521)

.

Concluída a tratativa de divergência de falta total, os produtos já estão prontos para serem armazenados e a doca liberada:

![diverg23.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500020008921)

**Observação:** Quando o produto estiver em uma ou mais UMAs na doca e ainda possuir tarefas abertas e fechadas, ao acionar o botão [Recontar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#recontar), será criada uma tarefa de recontagem da(s) UMA(s) na doca e no endereço de destino. Desse modo, ao acessar o coletor TotalCross você pode conferir o **"Endereço"**, a **"UMA"** e o **"Produto"** que será recontado.** **

[[voltar ao subtítulo]](#registrodefalta) [[voltar ao topo]](#top)

**

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16977727344023)

 Saiba mais sobre as configurações e etapas do Registro de Conferência acessando a documentação [Registro de Conferência no Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias).**


---

### 🔗 Links e Referências Internas:

- [Registo de Conferência no Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias)
- [registro de conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#tarefaregistrodeconfer%C3%AAncia)
- [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias)
- [Processar o Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#processarrecebimentoeliberardoca)
- [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento)
- [Endereço de Avaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral)
- [armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011931322-WMS-Registro-de-Confer%C3%AAncia-no-Recebimento-de-Mercadorias#armazenagem)
- [Recontar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#recontar)