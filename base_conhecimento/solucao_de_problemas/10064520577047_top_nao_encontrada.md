# TOP não encontrada

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10064520577047-TOP-n%C3%A3o-encontrada](https://ajuda.sankhya.com.br/hc/pt-br/articles/10064520577047-TOP-n%C3%A3o-encontrada)  
> **ID:** `10064520577047` | **Última Atualização:** 2026-07-22T15:04:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039139351)

 MENSAGEM:**

[CORE_E03183] TOP não encontrada.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918047565975)

 SITUAÇÃO:**

Ao realizar a importação de um XML a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039153943)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039158679)

 Realize os lançamentos de CT-e, no **Portal de Importação de XML** *(Comercial » Rotinas » Portal de importação de XML)*, o sistema sempre vai pegar a TOP de movimentação Financeira configurado nas Preferências para Importar o CT-e. 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/10064368029079)

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/10064316732183)

 

Grid do Portal de Importação de XML. 

![3.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039168407)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918047592471)

 Caso utilize a Opção de Importar CT-e com Cabeçalho e TOP de movimento de compra, marque o campo: "Importar CT-e com Cabeçalho", na tela de Preferencias para Importação do CT-e,  e desligue o parâmetro: TOPDIGIMPXMLCTE.

![4.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918047593879)

![5.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039190679)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039192727)

 Ao realizar o processo acima, a TOP será atribuída "APENAS" na tela de central de Compras. 

![6.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918047610519)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039209111)

 Na tela de Portal de Importação de XML prevalecerá a TOP informada. 

![7.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918047619223)

Ou seja, a TOP é convertida apenas na tela de Central de compras, considerando configurações acima. 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039218711)

 OBSERVAÇÃO: **

Se desejar que a tela do Portal de Importação de XML fique com o mesmo layout da Central de Compras, será necessário fazer a alteração manualmente. Acesse o [Portal de importação de XML – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) para maiores informações.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18918039223703)

CAUSA:**

Ocorre quando a TOP para importação do CT-e não é devidamente informada na tela Portal de Importação de XML.


---

### 🔗 Links e Referências Internas:

- [Portal de importação de XML – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)