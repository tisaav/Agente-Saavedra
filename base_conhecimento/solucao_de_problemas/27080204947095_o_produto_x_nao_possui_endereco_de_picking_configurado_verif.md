# O Produto: X não possui endereço de Picking configurado. Verifique com o Gerente do WMS Pedido: XXXX

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/27080204947095-O-Produto-X-n%C3%A3o-possui-endere%C3%A7o-de-Picking-configurado-Verifique-com-o-Gerente-do-WMS-Pedido-XXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/27080204947095-O-Produto-X-n%C3%A3o-possui-endere%C3%A7o-de-Picking-configurado-Verifique-com-o-Gerente-do-WMS-Pedido-XXXX)  
> **ID:** `27080204947095` | **Última Atualização:** 2026-07-22T14:40:11Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27080204918423)

 **MENSAGEM:**

[WMS_E00770] O Produto: X não possui endereço de Picking configurado. Verifique com o Gerente do WMS Pedido: XXXX

O produto deve estar vinculado em um endereço do Tipo: Picking e que 'Permite Expedição'. Esse cadastro é feito na Rotina: WMS >> Cadastros >> Endereço de Armazenamento

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27080204922135)

SOLUÇÃO:**

Verifique com o gerente do WMS qual o endereço de picking que o produto pertence e valide se o mesmo se encontra disponível. Caso não exista endereço vinculado, acesse a tela **"Endereço de Armazenamento"** na aba **"Produto"**, defina a relação permitir e faça o vínculo do produto no endereço de picking. 

 

![expediç~~ao.gif](https://ajuda.sankhya.com.br/hc/article_attachments/27080224897303)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27080224898967)

CAUSA:**

Ocorre ao tentar enviar um pedido para expedição no qual um ou mais produtos estão sem endereço de pincking vinculado ou em endereço de picking bloqueado na tela de endereço de armazenamento.