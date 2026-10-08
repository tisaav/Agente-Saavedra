# Valor inválido conforme a máscara, pois possui valor ZERO entre os níveis.

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9354941571479-Valor-inv%C3%A1lido-conforme-a-m%C3%A1scara-pois-possui-valor-ZERO-entre-os-n%C3%ADveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/9354941571479-Valor-inv%C3%A1lido-conforme-a-m%C3%A1scara-pois-possui-valor-ZERO-entre-os-n%C3%ADveis)  
> **ID:** `9354941571479` | **Última Atualização:** 2026-07-22T15:08:35Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18799398074007)

 MENSAGEM:**

[CORE_E01140] Valor inválido conforme a máscara, pois possui valor ZERO entre os níveis.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18799398079127)

 SITUAÇÃO:**

Ao cadastrar novos locais e alterar a máscara a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18799373559319)

 SOLUÇÃO:**

O comportamento do sistema é não permitir 0 entre os níveis, ou seja, deverá seguir a hierarquia conforme exemplo abaixo:
1.0.0.0 PAI
 1.1.0.0 FILHO
   1.1.1.0 NETO
     1.1.1.1 BISNETO

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9345383721239)

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18799373564951)

CAUSA:**

Ocorre ao cadastrar uma máscara incorretamente.