# Apenas a TOP configurada para Venda Balcão permite envio para o WMS sem OC

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26515516533655-Apenas-a-TOP-configurada-para-Venda-Balc%C3%A3o-permite-envio-para-o-WMS-sem-OC](https://ajuda.sankhya.com.br/hc/pt-br/articles/26515516533655-Apenas-a-TOP-configurada-para-Venda-Balc%C3%A3o-permite-envio-para-o-WMS-sem-OC)  
> **ID:** `26515516533655` | **Última Atualização:** 2026-07-22T14:41:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26515500510487)

 **MENSAGEM:**

[WMS_E00652] Apenas a TOP configurada para Venda Balcão permite envio para o WMS sem OC. Nota/Pedido nro único: X não é venda Balcão e não possui OC informada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26515516522647)

SOLUÇÃO:**

Acesse a tela **"Ordens de Carga"** e crie uma ordem de carga, antes de vincular na tela **"Formação de Carga"**.

Expedição convencional que não utiliza separação balcão necessita que uma Ordem de Carga esteja vinculado ao pedido para que seja enviado para expedição.

 

![Aviso Apenas a TOP configurada para Venda Balcão permite envio para o WMS sem OC 1.gif](https://ajuda.sankhya.com.br/hc/article_attachments/26560103446295)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26515500521367)

CAUSA:**

Ocorre quando se tenta enviar um pedido para expedição, diferente de separação balcão, sem vincular uma OC no pedido.