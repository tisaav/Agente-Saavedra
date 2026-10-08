# 741 Rejeição: O contratante deve ser igual ao emitente do MDFe quando indicado proprietário do veículo

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35379135676567-741-Rejei%C3%A7%C3%A3o-O-contratante-deve-ser-igual-ao-emitente-do-MDFe-quando-indicado-propriet%C3%A1rio-do-ve%C3%ADculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35379135676567-741-Rejei%C3%A7%C3%A3o-O-contratante-deve-ser-igual-ao-emitente-do-MDFe-quando-indicado-propriet%C3%A1rio-do-ve%C3%ADculo)  
> **ID:** `35379135676567` | **Última Atualização:** 2026-07-22T14:25:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688799395991)

  **MENSAGEM**

741 Rejeição: O contratante deve ser igual ao emitente do MDFe quando indicado proprietário do veículo

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688778262551)

  **SITUAÇÃO**

Ao emitir um MDF-e, ao informar o proprietário ou possuidor do veículo, mas não preencher o grupo **"Contratante"** ou, se preenchido, não corresponder ao mesmo CNPJ/CPF do emitente, ocorre a rejeição **"741"**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688778277527)

  **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688799401367)

  Acesse a tela **"Viagens de Transporte (MDF-e)" **(Comercial » Rotinas » Viagens de Transporte (MDF-e)), va até a aba **"MDF-e", **sub aba **"Contratantes".**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688799418519)

  Verifique se o grupo **"Contratante"** está preenchido.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35379327315863)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688799420055)

  Se o grupo **"Contratante"** estiver preenchido, confira se os dados informados correspondem ao mesmo CNPJ/CPF do emitente do MDF-e.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688799433879)

  Se necessário, ajuste os dados do **"Contratante"** para que estejam corretos e correspondam ao emitente.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688799435927)

  Salve as alterações e tente emitir novamente o MDF-e.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35688799438871)

  **CAUSA**

A rejeição **"741"** ocorre devido à validação implementada na NT 2021.002. Quando o proprietário do veículo for informado, se for Pessoa Jurídica, o campo **"Contratante"** deve ser preenchido com o mesmo parceiro. Se o proprietário for Pessoa Física, o **"Contratante"** deve ser preenchido como a empresa emitente.