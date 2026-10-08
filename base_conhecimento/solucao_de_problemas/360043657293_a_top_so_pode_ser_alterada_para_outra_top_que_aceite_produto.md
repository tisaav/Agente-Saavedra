# A TOP só pode ser alterada para outra TOP que aceite produto repetido

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043657293-A-TOP-s%C3%B3-pode-ser-alterada-para-outra-TOP-que-aceite-produto-repetido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043657293-A-TOP-s%C3%B3-pode-ser-alterada-para-outra-TOP-que-aceite-produto-repetido)  
> **ID:** `360043657293` | **Última Atualização:** 2026-07-22T16:04:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137833571479)

 MENSAGEM:**

[CORE_E01491] A TOP só pode ser alterada para outra TOP que aceite produto repetido.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137847645079)

 SITUAÇÃO:**

Ao alterar a TOP de uma nota/pedido, ocorre a mensagem.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137847654295)

 CAUSA:**

Ocorre quando a TOP que está tentando alterar tem a informação incompatível no campo **"Aceitar Produto repetido"** da TOP atual da nota/pedido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137847646359)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137833579031)

 Acesse: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*:

- Aba: **"Estoque"**

- Campo **"Aceitar Produto Repetido":** use o Parâmetro Global
Ambas as TOP's devem estar configuradas com a mesma informação no campo acima.

![A_TOP_s__pode_ser_alterada_para_outra_TOP_que_aceite_produto_repetido.png](https://ajuda.sankhya.com.br/hc/article_attachments/14684343285271)

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137833582999)

 O campo **"Aceitar Produto Repetido" **serve para determinar se será ou não permitido lançar itens repetidos nos Portais. O sistema tem um parâmetro global, **"Aceita Produto Repetido -ACEITARPRODREP" **que, se estiver ativado, permitirá lançar produtos repetidos; se estiver desativado, não permitirá lançar produtos repetidos. Ainda nesse contexto, considerando que seja inserido o mesmo produto, porém com local de origem e/ou controles diferentes, a inclusão de forma repetida será concedida, independente dos parâmetros mencionados.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137833582999)

 Desse modo, temos no campo **"Aceitar Produto Repetido"** as seguintes alternativas:

- 
**Usar o parâmetro Global: **se estiver marcada, o sistema respeitará o que foi definido no parâmetro **"Aceita Produto Repetido -ACEITARPRODREP"**.

- 
**Sim: **Se estiver marcada, independente do parâmetro global será permitido lançar itens repetidos.

- 
**Não: **Se estiver marcada, independente do parâmetro global não será permitido lançar itens repetidos.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16137833585687)

 Após o ajuste, modifique a TOP na nota/pedido.