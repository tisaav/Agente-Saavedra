# Chave de acesso referenciada com modelo inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8369904619543-Chave-de-acesso-referenciada-com-modelo-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/8369904619543-Chave-de-acesso-referenciada-com-modelo-inv%C3%A1lido)  
> **ID:** `8369904619543` | **Última Atualização:** 2026-07-22T15:12:10Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594006437015)

 MENSAGEM:**

679-Rejeição: Chave de acesso referenciada com modelo inválido.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593981518999)

 SITUAÇÃO:**

Ao tentar transmitir a NF-e a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594006440215)

SOLUÇÃO:**

**1° Situação**

Quando for emitida uma NF-e e no Grupo de Documentos Fiscais Referenciados (NFref), no campo **"Chave NF-e Referenciada"**, for informada Chave de Acesso com modelo diferente de 55, 65 ou 59 , será retornada a rejeição "679 - Chave de Acesso referenciada com Modelo inválido ".

 

**Modelos permitidos:**

55 - Nota Fiscal Eletrônica;
65 - Nota Fiscal Eletrônica do Consumidor;
59 - SAT-CF-e.

Verifique na TOP de Origem (TOP da nota que está sendo devolvida), na aba **"NF-e/NFC-e",** modelo de Documentos e observe se este campo está preenchido com um destes modelos

55 - Nota Fiscal Eletrônica;
65 - Nota Fiscal Eletrônica do Consumidor;
59 - SAT-CF-e.

 

![Chave de acesso referenciada com modelo inválido 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16594006442775)

 

Caso a TOP esteja marcada com Modelo diferente destes listados acima, faça o ajuste do modelo da TOP, exclua e lança novamente a nota de origem, para que possa ser possível realizar a devolução.

 

**2° Situação**

Na central de Vendas/Compras,  campo **"Chave NF-e Referenciada"** deve estar preenchido com uma chave que possua modelo= 55,65,59.

Para verificar o modelo da chave, retire os primeiros 20 números dela e os dois seguintes serão o modelo de documento da nota referenciada

 

![Chave de acesso referenciada com modelo inválido 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593981527959)

 

Caso o campo do modelo esteja preenchido com algum que seja diferente de 55 ou 65, a chave referenciada deve ser consultada na SEFAZ para verificar se a mesma é uma chave existente.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450873959831)

 Para localizar corretamente a chave referenciada, utilize a opção dos Portais -> NF-e -> Gerar XML da NF-e e em arquivo para conferência, verifique na tag <NFref> a chave que está sendo referenciada.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450873959831)

Apenas as chaves de notas aprovadas podem ser referenciadas.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593981531543)

CAUSA: **

Ao emitir uma NF-e que faz referência a outro documento fiscal, foi informado um modelo não permitido pela SEFAZ e nesse caso a rejeição 679 irá ocorrer.