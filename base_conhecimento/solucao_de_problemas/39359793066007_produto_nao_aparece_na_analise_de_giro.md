# Produto não aparece na análise de giro

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39359793066007-Produto-n%C3%A3o-aparece-na-an%C3%A1lise-de-giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/39359793066007-Produto-n%C3%A3o-aparece-na-an%C3%A1lise-de-giro)  
> **ID:** `39359793066007` | **Última Atualização:** 2026-08-31T01:42:39Z

---

O item possui saídas registradas no sistema, mas não aparece na **"Análise de Giro"**.

 

### 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39359793061527)

 **SITUAÇÃO**

Ao gerar a **"Análise de Giro"** (Comercial Consulta Análise de Giro), o usuário identifica que um produto específico, mesmo possuindo várias saídas registradas no período analisado, não é apresentado na análise. 

 

### 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39359793063191)

 **SOLUÇÃO**

Para resolver esta situação, execute os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39359793063703)

 Verifique se o **"Tipo de Operação (TOP)"** utilizado nas vendas está configurado corretamente para ser considerado na **"Análise de Giro"**. Acesse a tela **"Tipos de Operação"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) e confirme se o campo **"Análise de Giro"** está marcado com o valor Venda(Saída).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39359793064727)

 Verifique se o produto possui linha de custo cadastrada. Acesse a tela **"Variação de Custos"** (Comercial » Consulta » Variação de Custos de Produtos) e consulte se existe custo registrado para o item para o período que está sendo analisado. 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39359820123159)

 Verifique se o produto está com a marcação para calcular giro, no cadastro de produtos (campo Calcular giro pelo agendador, na aba Medidas e Estoque, sub-aba Estoque). 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39359820123287)

 Caso o produto não possua linha de custo, realize a limpeza da consolidação na tabela **"TGFGIR1"**. Após criar a linha de custo, execute novamente a consolidação da **"Análise de Giro"**.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39359820123543)

 Retorne à tela **"Análise de Giro"** e verifique se o produto passou a apresentar o giro corretamente nos períodos analisados.
 

 

### 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39359793064983)

 **CAUSA**

As principais causas para o produto não aparecer na **"Análise de Giro"** são:

- 

**"TOP"** não configurada: o **"Tipo de Operação"** utilizado nas vendas não está marcado para ser considerado na **"Análise de Giro"**.
 

1. 

Ausência de linha de custo: o produto não possui custo cadastrado, impedindo que as sugestões de giro sejam calculadas corretamente.
 

1. 

Agendador inativo: o agendador de consolidação da **"Análise de Giro"** não está em funcionamento, impedindo a atualização dos dados.
 

1. 

Consolidação desatualizada: a tabela de consolidação precisa ser limpa e reprocessada após correções nos cadastros.