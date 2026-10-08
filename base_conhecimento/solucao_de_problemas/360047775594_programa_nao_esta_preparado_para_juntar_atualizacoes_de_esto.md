# Programa não está preparado para juntar Atualizações de Estoque diferentes

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360047775594-Programa-n%C3%A3o-est%C3%A1-preparado-para-juntar-Atualiza%C3%A7%C3%B5es-de-Estoque-diferentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047775594-Programa-n%C3%A3o-est%C3%A1-preparado-para-juntar-Atualiza%C3%A7%C3%B5es-de-Estoque-diferentes)  
> **ID:** `360047775594` | **Última Atualização:** 2026-07-22T15:31:47Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667058902807)

 MENSAGEM:**

[CORE_E04632] Programa não está preparado para juntar Atualizações de Estoque diferentes.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667058912535)

 CAUSA:**

Mensagem será apresentada ao tentar juntar/faturar documentos que possuem atualizações de estoque diferentes [Campo ATUALESTOQUE].

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667058922135)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667018375191)

Verifique dentre todos os documentos que estão sendo faturados, quais os 'Tipos de Operação' utilizados.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18667058930839)

 Acesse a tela **Tipos de Operação-TOP** *(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)* e verificar para as TOP'S utilizadas como está configurado o campo **"Atualização do Estoque"** [Aba Estoque].

- 
**NÃO** será permitido "juntar/faturar" **documentos que possuem atualizações de estoque distintas**.

- Dessa forma, reavalie essa marcação, e realize os ajustes necessários.

**Importante:**

- Os documentos lançados com a TOP que teve essa informação alterada, deverão ser **lançados novamente** para que a nova informação do campo seja lida. 

- Caso a configuração de atualização de estoque das TOP'S de fato devam ser diferentes, será necessário que o faturamento desses documentos ocorra de forma separada [Juntando apenas os que possuem a mesma "atualização de estoque"].