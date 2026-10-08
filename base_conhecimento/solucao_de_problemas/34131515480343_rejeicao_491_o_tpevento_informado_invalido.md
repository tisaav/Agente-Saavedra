# Rejeição 491: O tpEvento informado inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34131515480343-Rejei%C3%A7%C3%A3o-491-O-tpEvento-informado-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/34131515480343-Rejei%C3%A7%C3%A3o-491-O-tpEvento-informado-inv%C3%A1lido)  
> **ID:** `34131515480343` | **Última Atualização:** 2026-07-22T14:27:38Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34131515457815)

 **MENSAGEM**

Rejeição 491: O tpEvento informado inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34340176260503)

 **SITUAÇÃO**

A mensagem ocorre ao tentar enviar um evento relacionado à NF-e, como **"Carta de Correção"**, **"Cancelamento"**, **"EPEC"** ou **"Manifestação do Destinatário"**, quando o campo **"tpEvento"** informado no XML não é reconhecido ou não corresponde a nenhum código válido segundo o layout definido pela Sefaz.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34131515460119)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34340176260759)

  Verifique o código informado no campo **"tpEvento"** no XML do evento.
 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34340176261783)

  Consulte a tabela oficial de códigos de evento da Sefaz e confirme se o código utilizado é válido.

- 

**110110** – Carta de Correção Eletrônica (CC-e)

- 

**110111** – Cancelamento da NF-e

- 

**110140** – EPEC (Evento Prévio de Emissão em Contingência)

- 

**210200** – Confirmação da Operação (Manifestação do Destinatário)

- 

**210210** – Ciência da Operação

- 

**210220** – Desconhecimento da Operação

- 

**210240** – Operação não Realizada
 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34340133628695)

  Se necessário, corrija o código do evento no XML e tente reenviar o evento.
 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34340176262167)

  Caso a rejeição persista, entre em contato com o suporte **"Sankhya"** para orientações adicionais.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34131545097495)

 **CAUSA**

A rejeição 491 é causada pelo envio de um código de evento (**tpEvento**) inválido ou incompatível com a tabela oficial da Sefaz.