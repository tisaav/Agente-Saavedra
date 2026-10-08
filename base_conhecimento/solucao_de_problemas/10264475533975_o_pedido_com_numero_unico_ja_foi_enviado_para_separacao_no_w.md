# O pedido com número único já foi enviado para separação no WMS e não pode ter a ordem de carga alterada

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10264475533975-O-pedido-com-n%C3%BAmero-%C3%BAnico-j%C3%A1-foi-enviado-para-separa%C3%A7%C3%A3o-no-WMS-e-n%C3%A3o-pode-ter-a-ordem-de-carga-alterada](https://ajuda.sankhya.com.br/hc/pt-br/articles/10264475533975-O-pedido-com-n%C3%BAmero-%C3%BAnico-j%C3%A1-foi-enviado-para-separa%C3%A7%C3%A3o-no-WMS-e-n%C3%A3o-pode-ter-a-ordem-de-carga-alterada)  
> **ID:** `10264475533975` | **Última Atualização:** 2026-07-22T15:04:04Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15360329266839)

 MENSAGEM:**

[CORE_E05075] O pedido com número único já foi enviado para separação no WMS e não pode ter a ordem de carga alterada.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15360329269527)

 CAUSA:**

Ocorre quando se tenta alterar a ordem de carga de um pedido já enviado para separação no WMS.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15360371828375)

 SOLUÇÃO:**

Não é possível alterar uma OC de um pedido que já foi enviado para expedição.

Caso seja preciso alterar a ordem de carga, primeiro acesse a tela **Expedição de Mercadorias ***(Caminho de aceso à tela: WMS » Rotinas » Expedição de Mercadorias) e *cancele a expedição da OC do pedido enviado. Em seguida, vá até a tela **Formação de Carga*** (Caminho de acesso à tela: Comercial » Rotinas » Ordem de Carga » Formação de Carga) *e vincule uma nova OC. 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/10287957086743)