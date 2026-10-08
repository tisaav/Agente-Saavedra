# Falha no reconhecimento da autoria ou integridade do arquivo digital

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043200913-Falha-no-reconhecimento-da-autoria-ou-integridade-do-arquivo-digital](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043200913-Falha-no-reconhecimento-da-autoria-ou-integridade-do-arquivo-digital)  
> **ID:** `360043200913` | **Última Atualização:** 2026-07-22T16:06:31Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447963707927)

 MENSAGEM:**

[202-Rejeição]: Falha no reconhecimento da autoria ou integridade do arquivo digital.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447963711511)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

Quando houver alguma alteração nos *templates* utilizados pela Sefaz, caso seja gerada alguma nota que não esteja de acordo com o padrão exigido, a resposta será essa rejeição. **Na maioria das vezes essa rejeição está relacionada a uma falha da própria SEFAZ.**

Neste caso, aguarde a estabilização dos servidores da Secretaria da Fazenda e gere o lote/enviar a nota novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16447963712407)

 CAUSA**:

Quando é feito o envio de uma NF-e, os *templates* são como moldes da mensagem. Os *Webservices* aguardam essa mensagem de acordo com esse template, portanto, se houver alterações no arquivo template e o emitente da NF-e não estiver gerando essa NF-e de acordo com o novo template, a nota será rejeitada.