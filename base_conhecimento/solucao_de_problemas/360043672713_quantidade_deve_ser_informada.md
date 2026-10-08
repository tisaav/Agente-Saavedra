# Quantidade deve ser informada

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043672713-Quantidade-deve-ser-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043672713-Quantidade-deve-ser-informada)  
> **ID:** `360043672713` | **Última Atualização:** 2026-07-22T16:03:48Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118693294743)

 MENSAGEM:**

Quantidade deve ser informada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118693297303)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118706275607)

 Para lançamentos onde o campo quantidade deverá ser lançado zerado, por exemplo, notas de complemento de imposto, necessário ajustar o parâmetro abaixo:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118693308951)

 Tela **"Preferências"** *(Caminho de acesso: Configurações » Avançado)*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118693308951)

 Chave** "TOPQTDZERO - TOP para aceitar Qtd. igual a zero"**, informe no campo **"Texto"** o código do Tipo de Operação utilizado no lançamento.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14627826818199)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118693314711)

 Ajustado o parâmetro acima será possível incluir itens com quantidade = 0.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16118693317399)

 CAUSA:**

Ao realizar lançamentos informando itens com o campo quantidade = 0, sem a devida parametrização do parâmetro TOPQTDZERO, será apresentada a mensagem.