# Evento de liberação de Confirmação de nota (Evento 18) não pode possuir valor diferente de 1

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10211172773399-Evento-de-libera%C3%A7%C3%A3o-de-Confirma%C3%A7%C3%A3o-de-nota-Evento-18-n%C3%A3o-pode-possuir-valor-diferente-de-1](https://ajuda.sankhya.com.br/hc/pt-br/articles/10211172773399-Evento-de-libera%C3%A7%C3%A3o-de-Confirma%C3%A7%C3%A3o-de-nota-Evento-18-n%C3%A3o-pode-possuir-valor-diferente-de-1)  
> **ID:** `10211172773399` | **Última Atualização:** 2026-07-22T15:04:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19034869099031)

 MENSAGEM:**

[CORE_E02841] Evento de liberação de Confirmação de nota (Evento 18) não pode possuir valor diferente de 1.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19034840092567)

 SITUAÇÃO:**

Ao tentar fazer a liberação de um lançamento a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19034840104727)

 CAUSA:**

Ocorre quando é alterado o valor a ser liberado entretanto, o evento configurado é o 18 de confirmação de nota.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19034869117847)

 SOLUÇÃO:**

O evento 18 é usado apenas para solicitar liberação para confirmação do pedido, e não considera valores.

Caso deseje que seja possível alterar o valor ou necessite alterar o valor do pedido/nota, configure para esse processo o evento 44 ao invés do evento 18. Pois, a permissão de alteração de valores está condicionada ao evento 44.