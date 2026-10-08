# A data de vencimento deve ser maior ou igual a data de negociação

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043132474-A-data-de-vencimento-deve-ser-maior-ou-igual-a-data-de-negocia%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043132474-A-data-de-vencimento-deve-ser-maior-ou-igual-a-data-de-negocia%C3%A7%C3%A3o)  
> **ID:** `360043132474` | **Última Atualização:** 2026-09-16T14:50:54Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145820257559)

 MENSAGEM:**

[CORE_E02204] A data de vencimento deve ser maior ou igual a data de negociação.

[CORE_E02805] A data de vencimento deve ser maior ou igual a data de negociação.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145820259607)

 SITUAÇÃO:**

Ao tentar efetuar o faturamento de um pedido ou alterar um pedido já confirmado, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145843755927)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145820275607)

 Acesse a tela **Tipos de Negociação** (*Comercial » Arquivo » Cadastros » Tipos de Negociação), *aba parcelas, Campo **"Vencto. Fixo"-** data de Vencimento Fixo. Aqui encontra-se uma data de vencimento fixo. Verifique com o setor financeiro e se for o caso, limpe o valor neste campo. Salve a alteração e, posteriormente, fature o pedido novamente.

 

**IMPORTANTE:**

A data informada no campo **"Vencto Fixo"** será usada como a data de vencimento em todas as notas que forem lançadas utilizando o tipo de negociação configurado, desconsiderando assim as configurações para cálculo do vencimento.

 

*

![A_data_de_vencimento_deve_ser_maior_ou_igual_a_data_de_negocia__o.png](https://ajuda.sankhya.com.br/hc/article_attachments/14691133367319)

*

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16145843766807)

 CAUSA:**

Esta mensagem ocorre quando se define um vencimento fixo, através do Tipo de Negociação. E o vencimento dos títulos já tenha sido calculados na nota/pedido e caso ocorra alguma alteração ou faturamento, no qual o sistema irá refazer o financeiro.