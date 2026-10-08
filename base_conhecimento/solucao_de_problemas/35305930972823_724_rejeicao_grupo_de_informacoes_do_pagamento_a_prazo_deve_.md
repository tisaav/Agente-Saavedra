# 724 Rejeição: Grupo de informações do pagamento a prazo deve ser informado

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35305930972823-724-Rejei%C3%A7%C3%A3o-Grupo-de-informa%C3%A7%C3%B5es-do-pagamento-a-prazo-deve-ser-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/35305930972823-724-Rejei%C3%A7%C3%A3o-Grupo-de-informa%C3%A7%C3%B5es-do-pagamento-a-prazo-deve-ser-informado)  
> **ID:** `35305930972823` | **Última Atualização:** 2026-07-22T14:25:33Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35305930962583)

 **MENSAGEM**

724 Rejeição: Grupo de informações do pagamento a prazo deve ser informado

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35674847506711)

 **SITUAÇÃO**

Ao emitir o MDF-e (modelo 58) com **"Modal"** igual a **"1 – Rodoviário"**, **"Tipo do Emitente"** igual a **"1 – Prestador de serviço de transporte"** ou **"3 – Prestador de serviço de transporte que emitirá CT-e Globalizado"**, e **"Indicador da Forma de Pagamento"** igual a **"1 – Pagamento a Prazo"**, sem informar o **"Grupo de Informações do Pagamento a Prazo"**, o sistema apresenta a rejeição.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35305992061335)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35674834253719)

  Acesse tela **"Viagens de Transporte (MDF-e)" **(Comercial » Rotinas » Viagens de Transporte (MDF-e)), vá até a aba **"MDF-e", **sub aba **"Pagamento de frete", **por fim sub aba **"Geral"**.

 

![724 Rejeição Grupo de informações do pagamento a prazo 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/35674847509911)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35674847511319)

  Selecione a opção **"Pagamento a Prazo"** no campo **"Forma de Pagamento"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35674834256791)

  Na aba **"Informações do pagamento a prazo"** (ainda na tela Viagens de Transporte (MDF-e)), informe a **"parcela"** e a **"data de vencimento"**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35305930966039)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35305930966935)

 **CAUSA**

O erro ocorre quando é selecionada a forma de pagamento a prazo, mas não são informados os dados de **"parcelas"**, **"vencimento"** e **"valor"** no grupo de informações do pagamento a prazo.