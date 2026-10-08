# A TOP só pode ser alterada para outra TOP do mesmo tipo de atualização de BEM

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/6278817833239-A-TOP-s%C3%B3-pode-ser-alterada-para-outra-TOP-do-mesmo-tipo-de-atualiza%C3%A7%C3%A3o-de-BEM](https://ajuda.sankhya.com.br/hc/pt-br/articles/6278817833239-A-TOP-s%C3%B3-pode-ser-alterada-para-outra-TOP-do-mesmo-tipo-de-atualiza%C3%A7%C3%A3o-de-BEM)  
> **ID:** `6278817833239` | **Última Atualização:** 2026-08-03T21:19:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16429657768727)

 MENSAGEM: **

[CORE_E01490] A TOP só pode ser alterada para outra TOP do mesmo tipo de atualização de BEM.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16429679146647)

 CAUSA:**

Ocorre quando a TOP que está tentando alterar, tem a informação incompatível no campo Atualização do Bem da TOP atual que está selecionando na Central para nota/pedido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16429657774871)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16429679132567)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:

- Aba: **"Estoque"**

- Campo: **"Atualização do Bem"**
Ambas as TOP's (Top 'atual' e top que está tentando inserir) devem estar configuradas com a mesma informação no campo acima.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/6278845738135)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16429657786519)

 Após o ajuste, será possível modificar a TOP na nota/pedido.

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17646367503127)

 **OBSERVAÇÃO: **

Na nova TOP, o campo 'Atualização do Bem' - aba Estoque deverá ser o mesmo da TOP antiga. Caso não seja, realize o ajuste ou gere o lançamento com a TOP desejada para evitar a necessidade de alterar o registro.