# Rejeição 452: Solicitada resposta assíncrona para lote com somente uma NFC-e

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16791792860567-Rejei%C3%A7%C3%A3o-452-Solicitada-resposta-ass%C3%ADncrona-para-lote-com-somente-uma-NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/16791792860567-Rejei%C3%A7%C3%A3o-452-Solicitada-resposta-ass%C3%ADncrona-para-lote-com-somente-uma-NFC-e)  
> **ID:** `16791792860567` | **Última Atualização:** 2026-07-22T14:54:26Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16791792848535)

  MENSAGEM:**

Rejeição 452: Solicitada resposta assíncrona para lote com somente uma NFC-e

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16791745594135)

 SOLUÇÃO:**

Para enviar o XML de forma "Síncrona"(em que é permitido o envio de apenas uma nota), siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36596523970839)

 Acesse a tela **"Empresa" ** (Comercial » Preferências » Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36596555625751)

 Busque e selecione a empresa da nota que recebeu a rejeição 452.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36596555627031)

 Vá até a aba **"Documentos eletrônicos"**, sub aba "**NF-e/NFC-e", **depois selecione a seção** "NFC-e" **e nela marque a opção **"Usar modo síncrono para envio do XML?".**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36596523977495)

 Após configurar corretamente o sistema gere o lote novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16791759475607)

 CAUSA:**

Nas preferências comerciais da **Empresa** - Comercial » Preferências » Empresa encontramos o campo "Usar modo Síncrono para envio do xml" na aba **NF-e/NFC-e** (Seção NFC-e), caso o campo esteja desmarcado ao emitir uma NFC-e o sistema assume o modo "Assíncrono" para envio do xml. No entanto, **caso esteja enviando apenas uma nota ocorre a rejeição 452.**