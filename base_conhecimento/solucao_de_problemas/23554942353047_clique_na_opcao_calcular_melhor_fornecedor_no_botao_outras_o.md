# Clique na opção 'Calcular melhor fornecedor' no botão outras opções para depois aprovar o fornecedor sugerido

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/23554942353047-Clique-na-op%C3%A7%C3%A3o-Calcular-melhor-fornecedor-no-bot%C3%A3o-outras-op%C3%A7%C3%B5es-para-depois-aprovar-o-fornecedor-sugerido](https://ajuda.sankhya.com.br/hc/pt-br/articles/23554942353047-Clique-na-op%C3%A7%C3%A3o-Calcular-melhor-fornecedor-no-bot%C3%A3o-outras-op%C3%A7%C3%B5es-para-depois-aprovar-o-fornecedor-sugerido)  
> **ID:** `23554942353047` | **Última Atualização:** 2026-07-22T14:48:13Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23554968648215)

 **MENSAGEM:**

[COTC_E00009]Clique na opção 'Calcular melhor fornecedor' no botão outras opções para depois aprovar o fornecedor sugerido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23554942343703)

SOLUÇÃO:**

Trata-se de uma comportamento do sistema, só pode ser aprovada a cotação quando a Situação de todos os itens está "Precificada". Caso seja necessário aprovar a cotação sem precificar um dos itens, é necessário cancelá-lo da cotação.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/23554942348183)

CAUSA:**

O erro é acionado quando o campo CODPARC ( Coluna = "Nome Parceiro (MELHOR FORNECEDOR)") está vazio; o campo fica vazio quando não há preço informado para o Produto com aquele fornecedor, assim quando calcula melhor fornecedor ele calcula para os itens que possuem preço informado para os fornecedores.