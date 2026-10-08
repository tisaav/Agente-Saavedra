# Existe dois rateios iguais com tipo de aferição diferente, não sendo possível distribuir os rateios nos títulos de destino de forma correta.

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15826721115927-Existe-dois-rateios-iguais-com-tipo-de-aferi%C3%A7%C3%A3o-diferente-n%C3%A3o-sendo-poss%C3%ADvel-distribuir-os-rateios-nos-t%C3%ADtulos-de-destino-de-forma-correta](https://ajuda.sankhya.com.br/hc/pt-br/articles/15826721115927-Existe-dois-rateios-iguais-com-tipo-de-aferi%C3%A7%C3%A3o-diferente-n%C3%A3o-sendo-poss%C3%ADvel-distribuir-os-rateios-nos-t%C3%ADtulos-de-destino-de-forma-correta)  
> **ID:** `15826721115927` | **Última Atualização:** 2026-07-22T14:56:04Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15826721101719)

 MENSAGEM:**

[CORE_E02349] Existe dois rateios iguais com tipo de aferição diferente, não sendo possível distribuir os rateios nos títulos de destino de forma correta.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15826704694039)

 CAUSA:**

Ocorre devido alguma personalização inserir um tipo de aferição para para veículos definidos como 'N'.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15826700964119)

 SOLUÇÃO: **

Quando se configura o veículo para não usar aferição, o sistema já bloqueia o campo de aferição da tela de rateio.

Se você não apontar nada no campo aferição e só montar o rateio de um pedido, e nada de rateio no outro, o erro não acontece.. Ou seja, se o campo fica bloqueado (já que o veículo está configurado para não usar aferição).

Sendo assim, é muito provável que, algum objeto personalizado ou integração  tenha informado algo no campo aferição do veículo, que é apresentado na tela de rateio.

O sistema hoje não consegue de forma nativa recalcular as aferições, onde os pedidos tenham O TIPO DE AFERIÇÃO diferentes.