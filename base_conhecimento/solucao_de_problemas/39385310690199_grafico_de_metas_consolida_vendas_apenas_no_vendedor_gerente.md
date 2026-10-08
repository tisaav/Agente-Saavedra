# Gráfico de Metas Consolida Vendas Apenas no Vendedor 'Gerente'

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39385310690199-Gr%C3%A1fico-de-Metas-Consolida-Vendas-Apenas-no-Vendedor-Gerente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39385310690199-Gr%C3%A1fico-de-Metas-Consolida-Vendas-Apenas-no-Vendedor-Gerente)  
> **ID:** `39385310690199` | **Última Atualização:** 2026-08-25T03:57:04Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39385363496215)

 **Mensagem**

O dashboard "Gráfico Metas" exibe todas as vendas agrupadas em um único vendedor (geralmente o gerente), em vez de separar por vendedor individual.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39385310673431)

 **Situação**

Ao acessar Comercial » Gráficos » Gráfico Metas, os valores aparecem consolidados em um único vendedor, mesmo com as Metas Simplificadas de Vendas configuradas corretamente e movimentações de venda existentes para cada vendedor no período. O esperado é ver o resultado detalhado por vendedor.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39385363497623)

 **Solução**

Para corrigir a consolidação incorreta das vendas, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39385310676247)

 Acesse "Configuração de Estrutura de Metas/Orçamentos" (Metas e Orçamentos » Configuração de Estrutura de Metas/Orçamentos).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39385363499287)

 Selecione a meta (deve ser do **Tipo Comercial,** em metas Financeiras esses campos não existem). Abra a aba **"Propriedades"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39385363500695)

 Abra a aba **"Propriedades"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39385310680855)

 No quadro de duas listas, arraste **"Vendedor/Comprador"** para a lista **"Campos Significativos"**. Se **"Gerente"** estiver nessa mesma lista e você não quiser o agrupamento por gerente, arraste-o de volta para **"Campos Disponíveis"**.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39385310681751)

 Salve e volte em **Planejamento de Metas/Orçamentos**, localize a meta e clique em **"Atualização de Realizado"** para reprocessar.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42972536553239)

 Confira no dashboard **"Gráfico de Metas"** se os valores passaram a aparecer por vendedor.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39385310685079)

 **Causa**

Esse comportamento ocorre pela forma como a meta foi configurada em "Configuração de Estrutura de Metas/Orçamentos" (Metas e Orçamentos):

- O campo **Vendedor** não está marcado para compor o agrupamento do realizado; e/ou

- O campo **Gerente** está marcado, fazendo o sistema agrupar pelo gerente em vez do vendedor; ou

- O cadastro de vendedores está com o campo **Gerente** preenchido igual para vários vendedores, o que faz o agrupamento por gerente "esconder" o detalhe por vendedor.