# Saiba mais sobre o controle Adicional de Lote de Produtos no WMS

> **Módulo:** Melhores Praticas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580414-Saiba-mais-sobre-o-controle-Adicional-de-Lote-de-Produtos-no-WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580414-Saiba-mais-sobre-o-controle-Adicional-de-Lote-de-Produtos-no-WMS)  
> **ID:** `360044580414` | **Última Atualização:** 2026-07-22T15:51:03Z

---

Para um melhor controle adicional de lote de produtos no WMS, siga as orientações abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229608983)

 Acesse: *Configurações » Avançado » Preferências*

**"LOTEDTVAL - Usar data de validade junto com Lote?"**

**"LOTEDTFAB - Usar data de Fabricação junto com Lote?"**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229613207)

 Acesse *Configurações » Cadastros » Produtos » Produtos*, aba **Geral **e marque os campos: **"Utiliza data de Fabricação"**, **"Utiliza data de Validade"**. 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229615895)

 Na aba **Medidas e Estoque**, sub-aba **Medidas**, como o produto é controlado pelo WMS, informe os valores nos campos: **"Peso Bruto"**, **"Peso Líquido"**, **"Metros Cúbicos"**.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427213721751)

 Na sub-aba **Estoque**, informe valor no campo **"Prazo validade/tolerância"** (Em dias) e marque os campos: **"Controlado pelo WMS"**, **"Utiliza data de Fabricação"**, **"Utiliza data de Validade"**.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229622039)

 Na sub-aba **Controle Adicional** preencha o campo **"Controlado por" **=  Lote**.**

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427213729687)

 Acesse a aba **WMS **e marque o campo **"Usar controle adicional no WMS".**

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229634199)

 Informe os campos referentes ao tempo de vida do produto, para que o sistema saiba qual lote deve pegar no momento do envio para expedição.

Coloque o tempo em dias nos campos: 

- **"Shelflife"**:

- **"Shelflife mínimo"**:

- **"Fragmenta lote no envio para separação"**: marque, caso for enviar uma quantidade fracionada do lote, ou seja, se tiver 10 UN do lote armazenada no endereço e for expedir apenas 1 UN, o campo Fragmenta lote no envio para separação precisa estar marcado

 

#### **Considerações** **de uma Movimentação de Entrada de Mercadoria controlado por Lote no WMS**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229608983)

 Durante a entrada, informe o lote do produto, as datas de fabricação e validade para que o sistema possa fazer o cálculo do vencimento e trazer o lote que vai vencer primeiro.

 

![central_de_compras.png](https://ajuda.sankhya.com.br/hc/article_attachments/14495054140695)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229613207)

 Informe também as datas de fabricação e validade através do botão** "Outras opções"** do item **->** **"Informações de Controle Adicional"**

 

![central_de_compras2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14495055395095)

 

![inf_adicionais.png](https://ajuda.sankhya.com.br/hc/article_attachments/14495075018647)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229615895)

 Após inserir essas informações a nota não deve ser confirmada. Envie a nota para o recebimento(WMS): 

 

![portal_de_vendas2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14495076012823)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427213721751)

 Na atividade de conferência será solicitado o lote e depois a data de validade ou fabricação:

 

 

![05.png](https://ajuda.sankhya.com.br/hc/article_attachments/360060934514)

 

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229622039)

 Salve e siga com os processos normais de armazenagem no WMS. 

 

####  **Considerações de uma Movimentação de Saída de Mercadoria controlado por Lote no WMS** 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229608983)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*, aba **Geral**, para a TOP do Tipo de Movimento 'P-Pedido de Venda' 'Atualização do Estoque': Reservar.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229613207)

 Na aba **Validações **desmarque o campo **"****Validar Estoque p/ Reservar"**.

 

![TOP2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14495153241879)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16427229615895)

 Ligue o parâmetro: **"LOTEENVIOWMS (Lote automático no envio para o WMS?)"**. Este parâmetro possibilita que no envio para o WMS o sistema escolha os lotes considerando o FIFO. 

 Assim, no envio para o WMS, o sistema irá trazer o item no Pedido gravando os lotes encontrados, buscando o de menor validade e assim por diante, até atender a quantidade do Pedido. Se no Pedido houver produto com lote armazenado no WMS, este item de Produto não deverá ter seu campo **"CONTROLE (LOTE)"** preenchido. O pedido deverá ser confirmado e poderá ser enviado pelos processos normais de envio ao WMS.

 

 Feitas essas configurações, o processo de expedição seguirá o fluxo normal do WMS. Ao enviar o pedido, tendo estoque disponível do produto, será gravado o lote direto no pedido.