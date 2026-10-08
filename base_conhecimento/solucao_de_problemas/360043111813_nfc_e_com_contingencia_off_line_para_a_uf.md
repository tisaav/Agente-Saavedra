# NFC-e com contingência off-line para a UF

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043111813-NFC-e-com-conting%C3%AAncia-off-line-para-a-UF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043111813-NFC-e-com-conting%C3%AAncia-off-line-para-a-UF)  
> **ID:** `360043111813` | **Última Atualização:** 2026-07-22T16:07:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482905813015)

 MENSAGEM:**

[712-Rejeição]: NFC-e com contingência off-line para a UF.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482928023575)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

Algumas Secretarias (SEFAZ) estaduais não aceitam esse tipo de contingência. A Sefaz de São Paulo é um exemplo, a UF não aceita a contingência off-line.

Para que não ocorra a mensagem, siga as instruções abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482905818647)

 Acesse: *Comercial » Preferências » Empresa*

- Aba: **"NF-e/NFC-e"**

- NFC-e Campo **"Envio em Contingência":** Não usar contingência

 

![NFC-e_com_conting_ncia_off-line_para_a_UF.png](https://ajuda.sankhya.com.br/hc/article_attachments/14536890184855)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482928027159)

 Após o ajuste, inutilize a numeração das notas emitidas que estão com a rejeição acima e efetue um novo lançamento no ambiente, fora da contingência.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482928029591)

 OBSERVAÇÃO: **

Para emitir NFC-e em modo contingência para essas UFs que rejeitam, somente se faz através do FastService (PDV) com a integração do SAT.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16482905826199)

 CAUSA:**

Quando for emitida uma NFC-e em contingência "9 - off-line" e a UF autorizadora não aceitar esse tipo de contingência, será retornado a rejeição.