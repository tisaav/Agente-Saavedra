# Liberação de Limites Evento 61 

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8233035352087-Libera%C3%A7%C3%A3o-de-Limites-Evento-61](https://ajuda.sankhya.com.br/hc/pt-br/articles/8233035352087-Libera%C3%A7%C3%A3o-de-Limites-Evento-61)  
> **ID:** `8233035352087` | **Última Atualização:** 2026-08-28T19:40:47Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361674467991)

 MENSAGEM:**

61- Liberação de data de validade menor que o previsto.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361674468887)

SOLUÇÃO:**

Este evento está diretamente ligado ao parâmetro 'Mínimo de dias para validade dos produtos na entrada' (MINDIASVALENT). No lançamento de Notas de Compra, ao incluir um produto controlado por Lote e Data de Validade (parâmetro 'LOTEDTVAL' ligado), o sistema validará a Data de validade, informada para o produto, com a configuração definida no parâmetro MINDIASVALENT.
Se a Data de validade for menor ou igual a data atual mais os dias do parâmetro MINDIASVALENT, o sistema avisará ao usuário que a data está inválida. Se o usuário ainda assim confirmar a nota, será solicitado a liberação deste evento.
Os produtos, lotes e datas inválidas ficarão registrados na Observação da liberação. Após a liberação será possível confirmar a nota.
Se o usuário fizer alguma alteração na Data de validade de algum produto ou inserir um novo produto com data inválida, o sistema fará outra solicitação de liberação.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361689567639)

CAUSA:**

O evento 61 está diretamente ligado aos parâmetros, **"MINDIASVALENT"**,  **"LOTEDTVAL"** para o uso e correto funcionamento.