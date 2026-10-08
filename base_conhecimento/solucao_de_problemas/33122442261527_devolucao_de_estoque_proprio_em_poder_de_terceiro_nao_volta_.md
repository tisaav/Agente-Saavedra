# Devolução de estoque próprio em poder de terceiro não volta o produto para o estoque

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33122442261527-Devolu%C3%A7%C3%A3o-de-estoque-pr%C3%B3prio-em-poder-de-terceiro-n%C3%A3o-volta-o-produto-para-o-estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/33122442261527-Devolu%C3%A7%C3%A3o-de-estoque-pr%C3%B3prio-em-poder-de-terceiro-n%C3%A3o-volta-o-produto-para-o-estoque)  
> **ID:** `33122442261527` | **Última Atualização:** 2026-09-03T20:35:58Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/43231865331607)

**Mensagem**

Não possui estoque suficiente / Estoque com/de terceiros não pode ficar negativo.

O sistema também pode apresentar comportamentos como baixa incorreta (debitando de "Estoque próprio em poder próprio" ao invés de "Estoque próprio em poder de terceiros") ou falta de mensagem de estoque insuficiente.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/33122442259607)

**Situação**

Ao tentar dar baixa no estoque próprio ou emitir uma **"Nota Fiscal de Retorno de Industrialização"** ou **"Retorno de Remessa para Demonstração"**, o sistema apresenta a mensagem de estoque insuficiente ou que o estoque de terceiros não pode ficar negativo, mesmo havendo quantidade disponível em estoque. A situação ocorre quando o produto está registrado como estoque próprio em poder de terceiros e a **"TOP"** (Tipo de Operação) está configurada para realizar baixa em **"Estoque de Terceiro"** ou baixar simultaneamente o estoque próprio e o de terceiros, mas o produto não possui saldo disponível ou a configuração está divergente.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/33122467019159)

**Solução**

Para corrigir o problema e ajustar o saldo de estoque, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43231924864407)

 Verifique o saldo do produto. Acesse a tela **"Consulta de Estoque"** (INSERIR CAMINHO DA TELA) e filtre pelo produto, validando se há saldo disponível em **"Estoque Próprio em Poder de Terceiro"**.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43231924865047)

 Acesse a tela **"Tipos de Operação"** (Configurações >> Cadastros >> Tipos de Operação) e localize a TOP utilizada. Na aba **"Estoque"**, configure o campo **"Atualizar Estoque"**. Na aba **"Estoque de Terceiros"**, configure o campo **"Estoque com/de Terceiros"** (ATUALESTTERC) conforme a necessidade (ex: "Subtrair do Estoque próprio em poder de terceiros").

![image (110).png](https://ajuda.sankhya.com.br/hc/article_attachments/33238410925719)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43231865334295)

 Caso o saldo esteja zerado ou negativo, realize um **"Ajuste de Estoque"**. Acesse a tela **"Nota Fiscal"** (Comercial >> Movimentação >> Nota Fiscal) e selecione uma TOP de ajuste de estoque de entrada que atualize o **"Estoque Próprio em Poder de Terceiro"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43231924871703)

 Verifique em **"Preferências da Empresa"** (Comercial >> Preferências >> Empresa) o campo **"Local específico para estoque de terceiros"**. O local utilizado no lançamento deve ser igual ao definido aqui, ou deixe o campo vazio caso utilize múltiplos locais.

![image (100).png](https://ajuda.sankhya.com.br/hc/article_attachments/33238410927895)

![5](https://ajuda.sankhya.com.br/hc/article_attachments/43231865335191)

 Certifique-se de que a marcação **"Atualização de estoque de terceiros"** está habilitada na TOP e, se utilizar importação de XML, verifique se a opção **"Atualiza estoque a partir de confirmação"** está desmarcada.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/43231924872599)

 Após o ajuste e conferência das configurações, realize novamente a operação de baixa de estoque e verifique se o erro foi solucionado.

 

**Importante:** Não é possível cadastrar uma única TOP para realizar simultaneamente a baixa de estoque próprio em poder de terceiros e a baixa de estoque de terceiros em poder próprio. Consulte o setor contábil antes de realizar ajustes fiscais.

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/33122467025687)

**Causa**

- 

Parametrização inadequada do campo **"Estoque com/de Terceiros"** (ATUALESTTERC) no Tipo de Operação.

- 

Saldo insuficiente no **"Estoque Próprio em Poder de Terceiro"**.

- 

Entrada do produto lançada em **"Estoque Próprio"** ao invés de **"Estoque Próprio em Poder de Terceiro"**.

- 

Divergência de local de estoque entre **"Preferências da Empresa"** e o lançamento.

- 

Configuração de **"Atualização por confirmação"** impedindo a baixa imediata.