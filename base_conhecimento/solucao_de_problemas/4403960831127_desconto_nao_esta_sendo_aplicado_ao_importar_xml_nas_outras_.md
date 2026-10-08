# Desconto não está sendo aplicado ao importar xml nas Outras Opções da Central de Compras

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4403960831127-Desconto-n%C3%A3o-est%C3%A1-sendo-aplicado-ao-importar-xml-nas-Outras-Op%C3%A7%C3%B5es-da-Central-de-Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403960831127-Desconto-n%C3%A3o-est%C3%A1-sendo-aplicado-ao-importar-xml-nas-Outras-Op%C3%A7%C3%B5es-da-Central-de-Compras)  
> **ID:** `4403960831127` | **Última Atualização:** 2026-07-22T15:23:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16345691928727)

 MENSAGEM:**

Foi realizado um pedido (sem desconto), mas o fornecedor concedeu desconto posteriormente ao enviar o Xml. Sistema não está trazendo o desconto do item ao importar o Xml na Central de Compras.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16345708108695)

 SOLUÇÃO: **

Utilizando a opção Importar Xml de nota fiscal eletrônica (Substituindo Itens) o sistema irá considerar o desconto dado pelo Fornecedor em cima do Pedido lançado no sistema sem descontos.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15128354787479)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16345691933591)

 CAUSA:**

Isso acontece quando se utiliza de outra opção de importação de xml (Importar Xml de nota fiscal eletrônica), senão a adequada. Quando se fatura um pedido e faz a importação do XML da nota faturada a opção correta a ser utilizada é **"Importar Xml de nota fiscal eletrônica (Substituindo Itens)"**. Pois, se o pedido não possuía desconto, mas depois o Fornecedor concedeu ao enviar o XML, é preciso substituir o item do pedido pelo item do XML para que o sistema considere o desconto.