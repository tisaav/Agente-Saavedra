# Ao fazer uma transferência entre a empresa Y para a empresa Z o preço de custo no item está ficando zerado, mesmo tendo custo na empresa Z

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4409753435927-Ao-fazer-uma-transfer%C3%AAncia-entre-a-empresa-Y-para-a-empresa-Z-o-pre%C3%A7o-de-custo-no-item-est%C3%A1-ficando-zerado-mesmo-tendo-custo-na-empresa-Z](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409753435927-Ao-fazer-uma-transfer%C3%AAncia-entre-a-empresa-Y-para-a-empresa-Z-o-pre%C3%A7o-de-custo-no-item-est%C3%A1-ficando-zerado-mesmo-tendo-custo-na-empresa-Z)  
> **ID:** `4409753435927` | **Última Atualização:** 2026-07-22T15:21:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16091266519191)

 MENSAGEM**:

Ao fazer uma transferência entre a empresa Y para a empresa Z o preço de custo no item está ficando zerado, mesmo tendo custo na empresa Z.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16091250832151)

 SOLUÇÃO:**

Para a resolução do incidente, analise as configurações do parâmetro **"EMPCSTTRANS".** Este parâmetro foi criado com default 'S. 

**Ligado:** nas transferências da central interna o sistema utiliza nos itens da nota, os custos da empresa de destino, empresa da negociação.

**Desligado:** utiliza os custos da empresa origem. Este parâmetro afeta o funcionamento das empresas que controlam custos por empresa, parâmetro **"CUSTOPOREMP"**.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16091266537495)

 CAUSA:**

Caso a configuração realizada no parâmetro EMPCSTTRANS esteja como desligada e não tenha custo na empresa de origem, vai acontecer o problema do valor do custo ficar zerado na transferência.