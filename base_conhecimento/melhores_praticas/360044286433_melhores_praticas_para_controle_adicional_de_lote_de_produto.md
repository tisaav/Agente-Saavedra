# Melhores Práticas para controle Adicional de Lote de Produtos no WMS

> **Módulo:** Melhores Praticas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044286433-Melhores-Pr%C3%A1ticas-para-controle-Adicional-de-Lote-de-Produtos-no-WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044286433-Melhores-Pr%C3%A1ticas-para-controle-Adicional-de-Lote-de-Produtos-no-WMS)  
> **ID:** `360044286433` | **Última Atualização:** 2026-07-22T15:59:04Z

---

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16840433188119)

 Para um melhor controle adicional de lote de produtos no WMS, siga as orientações abaixo.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16840433195031)

 Acesse: *Configurações » Avançado » Preferências*

**"LOTEDTVAL - Usar data de validade junto com Lote?"**

**"LOTEDTFAB - Usar data de Fabricação junto com Lote?"**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16840433197335)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*

Aba: **"Geral"**

Campos:

- 

**"Utiliza data de Fabricação":** marque

- 

**"Utiliza data de Validade":** marque

Aba: **"Medidas e Estoque"**

     Sub-aba: **"Medidas"**

Como o produto é controlado pelo WMS, informe os valores nos campos

- 

**"Peso Bruto":**

- 

**"Peso Líquido":**

- 

**"Metros Cúbicos":**

     Sub-aba: **"Estoque"**

Informe valor no campo:

- 

**"Prazo validade/tolerância":** em dias

- 

**"Controlado pelo WMS":** marque

- 

**"Utiliza data de Fabricação":** marque

- 

**"Utiliza data de Validade":** marque

     Sub-aba: **"Controle Adicional"**

- 

**"Controlado por":** lote

Aba:** "WMS"**

Campos:

- 

**"Usar controle adicional no WMS":** marque

 Informe os campos referentes ao tempo de vida do produto, para que o sistema saiba qual lote deve pegar no momento do envio para expedição.
Informar o tempo em dias nos campos: 

- 

**"Shelflife":**

- 

**"Shelflife mínimo":**

- 

**"Fragmenta lote no envio para separação":** marque, caso for enviar uma quantidade fracionada do lote, ou seja, se tiver 10 UN do lote armazenada no endereço e for expedir apenas 1 UN, o campo** "Fragmenta lote"** no envio para separação precisa estar marcado

 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16840419854743)

 **Considerações** **de uma Movimentação de Entrada de Mercadoria controlado por Lote no WMS** 

 Durante a entrada, informe o lote do produto e as datas de fabricação e validade para que o sistema possa fazer o cálculo do vencimento e explodir o lote que vai vencer primeiro.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14658035284759)

 

Informe também as datas de fabricação e validade através do botão **"Outras opções"** do item -> **"Informações de Controle Adicional"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14658067269015)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14658068730263)

 

- Após inserir essas informações a nota não deve ser confirmada. Envie a nota para o recebimento(WMS). 

- Na atividade de conferência será solicitado o lote e depois a data de validade ou fabricação: 

-  Salve e siga com os processos normais de armazenagem no WMS. 

 

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16840419856279)

 **Considerações de uma Movimentação de Saída de Mercadoria controlado por Lote no WMS** 

*Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*

Aba: **"Geral"**

Para a TOP do Tipo de Movimento 'P-Pedido de Venda'
Atualização do Estoque = 'Reservar'

Aba: **"Validações"**

Campo **"Validar Estoque p/ Reservar"**: desmarque

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14658121467159)

 

-  Ligue o parâmetro: **"LOTEENVIOWMS - Lote automático no envio para o WMS?"**. Este parâmetro possibilita que no envio para o WMS o sistema escolha os lotes considerando o FIFO. 

-  Assim, no envio para o WMS, o sistema irá explodir o item no Pedido gravando os lotes encontrados, buscando o de menor validade e assim por diante, até atender a quantidade do Pedido (se no Pedido houver produto com lote armazenado no WMS, este item de Produto não deverá ter seu campo CONTROLE (LOTE) preenchido. O pedido deverá ser confirmado e poderá ser enviado pelos processos normais de envio ao WMS). 

-  Feitas essas configurações, o processo de expedição seguirá o fluxo normal do WMS. Ao enviar o pedido, tendo estoque disponível do produto, será gravado o lote direto no pedido.