# Produto não consta nesse endereço com a data informada

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733354-Produto-n%C3%A3o-consta-nesse-endere%C3%A7o-com-a-data-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733354-Produto-n%C3%A3o-consta-nesse-endere%C3%A7o-com-a-data-informada)  
> **ID:** `360043733354` | **Última Atualização:** 2026-07-22T15:59:20Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16364355404951)

 MENSAGEM**

Produto não consta nesse endereço com a data informada.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16364355407511)

 SITUAÇÃO**

Ao realizar a tarefa de Movimentação pró-ativa, informando data de validade do produto, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16364355409815)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16364341747991)

 Necessário que a data de validade do produto conste igualmente nas tabelas TGWEST (*Estoque no Endereço*) e TGWESTVAL (*Estoque Validade WMS*). Para isso, faça o inventário dos produtos no WMS ou lance uma nota de entrada, que as duas tabelas serão alimentadas.

Esta funcionalidade é padrão do sistema, não pode ser desabilitada.

- *WMS » Inventário » Inventários*

Para gerar as Tarefas de Inventário, acesse esta rotina.

- *Comercial » Consulta » Portal de Compras*

Se optar pela criação de uma Nota de Compra, faça o lançamento gerando a tarefa de Armazenagem.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16364355413143)

 Após os ajustes, efetue a tarefa de Movimentação Pro-Ativa novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16364355415959)

 CAUSA**

Com a implantação do controle de validade no Picking a partir do release 3.29, é necessário que a data de validade dos produtos controlados pelo WMS esteja inserida nas tabelas TGWEST (*Estoque no Endereço*) e TGWESTVAL (*Estoque Validade WMS*).

Se constar somente na TGWEST, será emitido o erro ao movimentar o produto.