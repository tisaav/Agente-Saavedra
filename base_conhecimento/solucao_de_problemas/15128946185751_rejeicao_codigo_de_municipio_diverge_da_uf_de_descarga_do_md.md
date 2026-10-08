# Rejeição: Código de Município diverge da UF de descarga do MDF-e

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15128946185751-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Munic%C3%ADpio-diverge-da-UF-de-descarga-do-MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/15128946185751-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Munic%C3%ADpio-diverge-da-UF-de-descarga-do-MDF-e)  
> **ID:** `15128946185751` | **Última Atualização:** 2026-08-06T17:29:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969208057111)

 MENSAGEM:**

Rejeição: Código de Município diverge da UF de descarga do MDF-e.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969208060055)

 SOLUÇÃO:**

Verifique o valor do campo **"UFFim"** e os valores do campo **"****cMunDescarga"** dentro do grupo infMunDescarga. Para o(s) campo(s) cMunDescarga veja se as 2 posições da esquerda do código do município de descarregamento que identifica o código da UF de descarga estão de acordo com o que foi informado no campo UFFim.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969197137047)

 CAUSA:**

Ocorre ao gerar MDF-e com UF de descarga divergente da UF de carga.