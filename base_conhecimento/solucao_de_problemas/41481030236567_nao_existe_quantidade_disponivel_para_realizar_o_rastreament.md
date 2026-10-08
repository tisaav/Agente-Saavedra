# Não existe quantidade disponível para realizar o rastreamento. Produto X...

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/41481030236567-N%C3%A3o-existe-quantidade-dispon%C3%ADvel-para-realizar-o-rastreamento-Produto-X](https://ajuda.sankhya.com.br/hc/pt-br/articles/41481030236567-N%C3%A3o-existe-quantidade-dispon%C3%ADvel-para-realizar-o-rastreamento-Produto-X)  
> **ID:** `41481030236567` | **Última Atualização:** 2026-07-22T13:26:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006726039)

**** ****MENSAGEM**

Não existe quantidade disponível para realizar o rastreamento. Produto X...

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481030210455)

**** ****SITUAÇÃO**

O erro é apresentado durante a confirmação de notas em movimentações internas (transferência de local), paralisando o faturamento da empresa. O sistema bloqueia a operação indicando falta de estoque para o rastreamento de lote, mesmo quando o saldo físico no Sankhya está correto e condizente com o WMS do cliente.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006728727)

**** ****SOLUÇÃO**

Para liberar o faturamento e corrigir o rastreamento de forma eficiente, realize o processo utilizando a **Cópia de Estoque** em vez de rastrear toda a vida útil do produto. Siga o passo a passo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481030213143)

 Acesse a tela **''****Cópia de Estoque''** (Inventário » Relatórios » Cópia de Estoque).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481030214039)

 Configure os filtros desejados (como o código do produto com erro ou grupo de produtos) para que a rotina considere apenas as informações relevantes.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006731031)

 Clique em **''****Executar Cópia''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006732695)

 Acesse a tela **''****Ativar/Reprocessar Rastreamento de Estoque/ST''** (Livros Fiscais » Avançado » Rastreamento de Estoque/ST » Ativar/Reprocessar Rastreamento de Estoque/ST).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006733975)

 Clique na opção **''****Filtros''**** **e informe os dados do produto que será corrigido.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481030229783)

 Acesse a opção **''****Preferências''** e parametrize o rastreamento para utilizar os dados da cópia.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006735639)

 É obrigatório informar no campo **''****Data Cópia Estoque''** a mesma data utilizada no momento da execução da cópia de estoque (Passo 3).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006736663)

 Clique em **''****Aplicar''** e, em seguida, em **''****Processar''**.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006737687)

 Após o processamento, as tabelas de rastreamento (TGFITS) assumirão o saldo consolidado, e a movimentação de transferência poderá ser confirmada sem erros.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41481006738327)

**** ****CAUSA**

Ao utilizar o processamento padrão de "vida útil", o sistema exige a análise de todo o histórico de movimentações (entradas e saídas) desde o cadastro do item, o que pode travar caso haja alguma inconsistência histórica nas tabelas TGFITS e TGFVAS. A execução a partir de uma Cópia de Estoque cria uma nova "linha de base", desconsiderando o histórico passado e focando apenas no saldo atual disponível na TGFEST.