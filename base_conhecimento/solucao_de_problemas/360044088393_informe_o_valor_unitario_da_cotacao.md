# Informe o valor unitário da cotação

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088393-Informe-o-valor-unit%C3%A1rio-da-cota%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088393-Informe-o-valor-unit%C3%A1rio-da-cota%C3%A7%C3%A3o)  
> **ID:** `360044088393` | **Última Atualização:** 2026-07-22T16:01:39Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170383713175)

 MENSAGEM:**

Informe o valor unitário da cotação.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170383715735)

 SITUAÇÃO:**

Ao tentar importar o Pedido do MGE para o Importação, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170383717271)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170383719191)

 Acesse: *MGEImport » Arquivos » Produtos*

Aba: **Medidas e Estoque** - Campo "**Decimais p/ valor(Importação)" **

 

![produtos7.png](https://ajuda.sankhya.com.br/hc/article_attachments/14692474805783)

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17855159369879)

 IMPORTANTE:**

Este campo está disponível apenas no módulo MGEImportação

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170418786711)

 Após o ajuste efetue novamente a importação do pedido e confira os valores unitários do(s) produto(s).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16170383724567)

 CAUSA:**

Ocorre quando o valor unitário está com poucas casas decimais, então a conversão da moeda estrangeira para a moeda real não é feita de forma a chegar um valor aceitável, pois a dizima foi desprezada.