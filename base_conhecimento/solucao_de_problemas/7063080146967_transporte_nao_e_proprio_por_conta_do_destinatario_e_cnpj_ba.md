# Transporte não é próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Destinatário

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7063080146967-Transporte-n%C3%A3o-%C3%A9-pr%C3%B3prio-por-conta-do-Destinat%C3%A1rio-e-CNPJ-Base-ou-CPF-do-Transportador-igual-ao-CNPJ-Base-ou-CPF-do-Destinat%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/7063080146967-Transporte-n%C3%A3o-%C3%A9-pr%C3%B3prio-por-conta-do-Destinat%C3%A1rio-e-CNPJ-Base-ou-CPF-do-Transportador-igual-ao-CNPJ-Base-ou-CPF-do-Destinat%C3%A1rio)  
> **ID:** `7063080146967` | **Última Atualização:** 2026-07-22T15:15:20Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16480741635223)

  MENSAGEM**:

849 - Rejeição: Transporte não é próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Destinatário.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16480741639959)

 CAUSA:**

O erro ocorre quando a modalidade do frete é diferente de 4 e o CNPJ Base ou CPF  do transportador **igual **ao CNPJ Base ou CPF do Destinatário.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16480741642647)

 SOLUÇÃO:**

Se for NF-e de entrada (tpNF=0) e Modalidade do Frete <> 4, o CNPJ Base ou CPF do transportador deve ser **diferente** do CNPJ Base ou CPF do Destinatário.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16480767502615)

 OBSERVAÇÃO:**

Regra de validação não se aplica quando CNPJ/CPF do transportador não for informado.