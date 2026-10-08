# O Envio não foi concluído para não fracionar o Estoque

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7784884226071-O-Envio-n%C3%A3o-foi-conclu%C3%ADdo-para-n%C3%A3o-fracionar-o-Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/7784884226071-O-Envio-n%C3%A3o-foi-conclu%C3%ADdo-para-n%C3%A3o-fracionar-o-Estoque)  
> **ID:** `7784884226071` | **Última Atualização:** 2026-07-22T15:13:07Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16540395981591)

 MENSAGEM**:

O Envio não foi concluído para não fracionar o Estoque.
Pedido: 

Verifique a configuração de endereços.

-------------------:
Pegas registradas:
Código: WMS_E00770

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16540411939863)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16540395987223)

 Vincule o picking correto com estoque do produto no cadastro do endereço ou transfira o estoque para o picking correto vinculado.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16540411942679)

 Use sempre a quantidade múltipla da unidade no estoque nos pedidos ou inventário do produto no picking para trabalhar com a unidade menor padrão como estoque.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16540411945111)

CAUSA:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16540395987223)

 No cadastro do produto, na aba **"WMS",** o picking vinculado ao produto não é o mesmo picking que está com o estoque na tela estoque/endereçamento WMS.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16540411942679)

 O picking está configurado em unidade maior do que a padrão e a quantidade negociada no pedido não é múltipla da unidade do estoque.