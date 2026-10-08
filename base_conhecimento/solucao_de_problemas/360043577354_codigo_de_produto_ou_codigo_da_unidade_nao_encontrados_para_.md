# Código de produto ou Código da unidade não encontrados para alguns itens do XML ou o XML contém produtos que utilizam controle adicional de estoque

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577354-C%C3%B3digo-de-produto-ou-C%C3%B3digo-da-unidade-n%C3%A3o-encontrados-para-alguns-itens-do-XML-ou-o-XML-cont%C3%A9m-produtos-que-utilizam-controle-adicional-de-estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577354-C%C3%B3digo-de-produto-ou-C%C3%B3digo-da-unidade-n%C3%A3o-encontrados-para-alguns-itens-do-XML-ou-o-XML-cont%C3%A9m-produtos-que-utilizam-controle-adicional-de-estoque)  
> **ID:** `360043577354` | **Última Atualização:** 2026-07-22T16:01:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192773291927)

 MENSAGEM**:

Código de produto ou Código da unidade não encontrados para alguns itens do XML ou o XML contém produtos que utilizam controle adicional de estoque.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192780000407)

 SOLUÇÃO**:

Identifique no DANFE/XML da nota de compra quais são as unidades dos produtos (Ex.: UN, CX, PC, TN, etc.). 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192780003991)

 Acesse o cadastro dos **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), identifique o campo: **"Unid. Compra"** e verifique se a Unidade de Compra corresponde com a Unidade dos produtos no XML da Nota de Compra.

 

![produtos5.png](https://ajuda.sankhya.com.br/hc/article_attachments/14679401935255)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192780006039)

 Caso a compra foi em Unidade Alternativa, acesse a aba: **Unidades Alternativas** do cadastro de produtos e verifique se a unidade alternativa está cadastrada e ativa.

 

![produtos6.png](https://ajuda.sankhya.com.br/hc/article_attachments/14679389606679)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192780008343)

 Após os ajustes, volte na Importação de XML e vincule o código do produto juntamente com a unidade cadastrada no sistema e que seja igual à unidade do XML.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192806855063)

 CAUSA**:

Ocorre quando a Unidade do XML da Compra não é igual à Unidade de Compra dos Produtos ou Unidade Alternativa.