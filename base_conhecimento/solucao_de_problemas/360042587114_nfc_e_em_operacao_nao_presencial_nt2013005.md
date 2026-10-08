# NFC-e em operação não presencial (NT2013/005)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042587114-NFC-e-em-opera%C3%A7%C3%A3o-n%C3%A3o-presencial-NT2013-005](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042587114-NFC-e-em-opera%C3%A7%C3%A3o-n%C3%A3o-presencial-NT2013-005)  
> **ID:** `360042587114` | **Última Atualização:** 2026-09-18T20:54:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459847197591)

 MENSAGEM: **

[717-Rejeição]: NFC-e em operação não presencial (NT2013/005).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459868490647)

 SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459847207959)

 Acesse: *Arquivo » Cadastros » Tipos de Operação - TOP*

Aba: "**NF-e/NFC-e"**

Campo: "**Indicador de Presença para NF-e/NFC-e"** = 1 ou 4

- 1- Operação Presencial

- 4- NFC-e com entrega em domicílio

Caso a operação de Venda seja NÃO PRESENCIAL, opte pela Emissão de uma NF-e onde o indicador de Presença poderá ser 2, 3 ou 9.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459868499735)

 Após o ajuste, gere o lote novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459868504855)

 CAUSA:**

Quando for emitida uma NFC-e e o Indicador de Presença do Comprador (indPres) for diferente de "1 - Operação presencial" ou diferente de "4 - NFC-e com entrega em domicílio".

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459868507799)

 OBSERVAÇÃO:**

([NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=)) - Nota Técnica.