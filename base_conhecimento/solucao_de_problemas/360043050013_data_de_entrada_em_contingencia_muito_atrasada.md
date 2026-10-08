# Data de entrada em contingência muito atrasada

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050013-Data-de-entrada-em-conting%C3%AAncia-muito-atrasada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050013-Data-de-entrada-em-conting%C3%AAncia-muito-atrasada)  
> **ID:** `360043050013` | **Última Atualização:** 2026-07-22T16:09:53Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474027879831)

 MENSAGEM:**

[569-Rejeição]: Data de entrada em contingência muito atrasada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474024209943)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

Acesse a tela de "**Manutenção de contingência"** (Caminho de acesso:* Comercial » Avançado » Manutenção de Contingência*) e identifique a data de criação da contingência, que deve ser inferior a 30 dias, da data da NF-e.

Esta Rejeição ocorre também quando não há um registro de Manutenção de contingência cadastrada, então considere cadastrar.

Após o cadastro, gere o Lote da NF-e novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16474024213399)

 CAUSA:**

Quando for emitida uma NF-e com Data/Hora de Entrada em Contingência com atraso maior que 30 dias da Data de Emissão será retornado a rejeição.