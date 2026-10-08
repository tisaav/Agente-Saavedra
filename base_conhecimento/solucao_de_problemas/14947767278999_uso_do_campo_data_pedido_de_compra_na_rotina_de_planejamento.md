# Uso do campo "Data Pedido de Compra" na rotina de Planejamento de Produção (MRP I)

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14947767278999-Uso-do-campo-Data-Pedido-de-Compra-na-rotina-de-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I](https://ajuda.sankhya.com.br/hc/pt-br/articles/14947767278999-Uso-do-campo-Data-Pedido-de-Compra-na-rotina-de-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I)  
> **ID:** `14947767278999` | **Última Atualização:** 2026-07-22T14:57:44Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610864642199)

 SITUAÇÃO:**
Para que serve e como usar o campo Data Pedido de Compra?

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610864645015)

 SOLUÇÃO:**
Para que este campo funcione corretamente, realize algumas configurações em outras telas.
 
 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610844021911)

** Acesse: *Configurações » Cadastros » Produtos » Produtos*

Selecione o produto que faz parte do Plano Mestre de Produção, aba **"Medidas e Estoque"**, selecione a sub aba **"Estoque"** e no campo **"Lead time de compra"** (este campo, indica o tempo que o produto leva para ser entregue) informe um valor numérico em dias.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14961956802455)

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610844023191)

** Acesse: *Produção » Cadastros » Processo Produtivo - Nova*

Configure o tempo das atividades:  insira o código do processo Processo Produtivo. Acesse o Roteiro, aba **"Geral",** no campo **"Tempo da atividade"** insira o tempo da sua atividade  e no campo **"Unidade de Tempo"**, insira o tempo.
 
Pode ser feito também pela Composição do Produto: *Produção » Cadastros » Composição do Produto, *aba **"Tempo de Processamento"**, conforme abaixo:
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14961965163415)

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610864652055)

 IMPORTANTE:**
Com esta configuração (Tela **"Composição do Produto"**), este tempo será apenas para o produto selecionado.
 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610844030999)

 **Acesse: *Produção » Rotinas » Planejamento de Produção (MRP I), *realize a configuração através do botão** "Configuração"**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14962014394391)

Verifique qual MPS será utilizado, então configure este registro. O importante é verificar se o **"****Tipo de demanda"** está como: **"Pedidos Firmes"** e o **"Tipo de período"** está como: **"Previsão de Entrega (Nota)"** ou **"Previsão de Entrega (Itens)".** Esta configuração indica de qual data da nota fiscal o cálculo será feito.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14961975782423)

 
**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610864656279)

 OBSERVAÇÕES: **
 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610844035351)

 O pedido de venda precisa ter a previsão de entrega da Nota ou do Item, de acordo com a configuração do  MPS (conforme passo anterior).

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610844035351)

Caso o campo** "Previsão de Entrega"** não esteja em seu Layout, o mesmo pode ser inserido utilizando a tela: **"Configurador de Layout da Nota"**.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610844035351)

Após todas estas configurações realizadas, então é possível ir no Planejamento de Produção e clicar no botão "MRP" para gerar as datas de compra.
 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610864658967)

 CAUSA:**
Ao clicar no botão de MRP na tela **"Planejamento de Produção (MRP I)"** é gerada a tela **"Necessidade de Materiais"**, que traz uma grid com o campo **"Data Pedido de Compra",** que informa a data indicada para realizar a compra dos materiais, considerando na data tempos de processamento de produção, tamanhos de lote e lead time.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14961878792855)