# Somente é aceita autorização assíncrona da NFC-e se Lote contiver mais do que uma nota regra GAP03a-3

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9762431835031-Somente-%C3%A9-aceita-autoriza%C3%A7%C3%A3o-ass%C3%ADncrona-da-NFC-e-se-Lote-contiver-mais-do-que-uma-nota-regra-GAP03a-3](https://ajuda.sankhya.com.br/hc/pt-br/articles/9762431835031-Somente-%C3%A9-aceita-autoriza%C3%A7%C3%A3o-ass%C3%ADncrona-da-NFC-e-se-Lote-contiver-mais-do-que-uma-nota-regra-GAP03a-3)  
> **ID:** `9762431835031` | **Última Atualização:** 2026-07-24T12:42:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19604294592407)

 MENSAGEM:**

[CORE_E06902] Somente é aceita autorização assíncrona da NFC-e se o Lote contiver mais do que uma nota (regra GAP03a-3). Para envio de somente uma NFC-e, necessário enviar de forma síncrona. Verifique as Preferências da Empresa, Aba NF-e/NFC-e, o campo “Usar modo Síncrono para envio do XML” para NFC-e.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19604294592791)

 SITUAÇÃO:**

Ao realizar um lançamento de nota nos portais ou PDV Web a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19604303222167)

 CAUSA:**

Quando o campo **"Usar modo Síncrono para envio do XML" **não está selecionado.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19604294595991)

 SOLUÇÃO:**

Acesse a tela **Empresa** *(Caminho de acesso à tela: Comercial » Preferências » Empresa),* vá até a aba 'CT-e' e habilite o campo "Usar modo Síncrono para envio do XML".

![empresa 06-12.png](https://ajuda.sankhya.com.br/hc/article_attachments/19604303232407)

Ao habilitar a marcação **"Usar modo Síncrono para envio do XML" **(localizada nesta seção e na seção NFC-e), o XML será enviado em modo síncrono; por outro lado, não selecionando a marcação, o envio será em modo assíncrono.