# Top informada no modelo de nota de ajuste de Saída PRÓPRIO não pode atualizar estoque com/de Terceiros

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24459142879383-Top-informada-no-modelo-de-nota-de-ajuste-de-Sa%C3%ADda-PR%C3%93PRIO-n%C3%A3o-pode-atualizar-estoque-com-de-Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/24459142879383-Top-informada-no-modelo-de-nota-de-ajuste-de-Sa%C3%ADda-PR%C3%93PRIO-n%C3%A3o-pode-atualizar-estoque-com-de-Terceiros)  
> **ID:** `24459142879383` | **Última Atualização:** 2026-07-22T14:46:43Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24459142871447)

 **MENSAGEM:**

[INV_E00008] Top informada no modelo de nota de ajuste de Saída PRÓPRIO não pode atualizar estoque com/de Terceiros.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24459114694679)

SOLUÇÃO:**

Para solucionar o erro siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24511328264343)

 Acesse a tela **"Empresa" **(Caminho: Comercial » Preferências » Empresa), vá até a aba **"Estoque/preço";**

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24511328268695)

 **Em seguida, busque pelo campo **"Modelo ajuste de Saída de Estoque" **e veja a TOP vinculada no modelo de nota/pedido;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24511285518615)

 Depois, acesse a tela **"Tipos de Operação - TOP"**, procure pela TOP identificada no modelo de nota/pedido e veja se ela está configurada movimentar estoque de terceiro, nos campos **"Estoque com/de Terceiros"** e **"Estoque MP de Terceiros"**, da aba "Estoque de terceiros da TOP", com uma configuração diferente de 'Não controla'. Caso tenha, altere a Top e vincule novamente no modelo de nota/pedido.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24459114696087)

CAUSA:**

O erro é apresentado ao vincular no campo Modelo ajuste de Saída de Estoque, da aba Estoque/preço, das Preferências da empresa, que não movimenta estoque de terceiros, uma TOP que está configurada para movimentar.