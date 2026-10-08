# Títulos Renegociados não podem ter Receita/Despesa ou Provisão ou Valor do Desdobramento alterados.

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360051731454-T%C3%ADtulos-Renegociados-n%C3%A3o-podem-ter-Receita-Despesa-ou-Provis%C3%A3o-ou-Valor-do-Desdobramento-alterados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051731454-T%C3%ADtulos-Renegociados-n%C3%A3o-podem-ter-Receita-Despesa-ou-Provis%C3%A3o-ou-Valor-do-Desdobramento-alterados)  
> **ID:** `360051731454` | **Última Atualização:** 2026-07-22T15:29:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18864606568727)

 MENSAGEM**:

[CORE_E02408] Títulos Renegociados não podem ter Receita/Despesa ou Provisão ou Valor do Desdobramento alterados.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18864606586007)

 SOLUÇÃO:**

- As alterações desejadas serão permitidas somente após desfazer a renegociação vinculada a tal título.

- Cabe analisar os motivos pelos quais essa alteração será realizada. (Lembre-se que caso sejam ajustes de valores, no momento da baixa temos os campos "desconto e/ou juros").

Caso deseje desfazer a renegociação, seguem as orientações:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18864606602391)

 Para o título que deseja desfazer a renegociação, busque na movimentação financeira o campo **'Nro Renegociação****'.**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15935821040919)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18864630997655)

 Acesse a tela 'Renegociação de títulos'* (Financeiro » Rotinas)*, no filtro do lado direito "Renegociação", digite o 'Nro Renegociação' localizado no Item 1.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18864631020567)

 Na parte inferior serão apresentados os dados da renegociação gerada, basta clicar na opção **DESFAZER**.

 

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18864631035799)

 **Feito isso o título voltará a apresentar as informações originais, que antecederam sua renegociação,  e não mais impedirá as alterações.

 

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15935867710743)

 CAUSA:**

Bloqueio inserido ao tentar alterar informações de títulos renegociados, sem que a renegociação tenha sido desfeita. Esse comportamento do sistema é para manter a integridade dos valores com vinculo no titulo original.