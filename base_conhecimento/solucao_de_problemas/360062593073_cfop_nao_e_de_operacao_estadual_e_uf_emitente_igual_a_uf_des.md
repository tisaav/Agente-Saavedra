# CFOP não é de Operação Estadual e UF emitente igual à UF destinatário

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360062593073-CFOP-n%C3%A3o-%C3%A9-de-Opera%C3%A7%C3%A3o-Estadual-e-UF-emitente-igual-%C3%A0-UF-destinat%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360062593073-CFOP-n%C3%A3o-%C3%A9-de-Opera%C3%A7%C3%A3o-Estadual-e-UF-emitente-igual-%C3%A0-UF-destinat%C3%A1rio)  
> **ID:** `360062593073` | **Última Atualização:** 2026-07-22T15:25:41Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302421294871)

 MENSAGEM**:

[Rejeição 523]: O CFOP não é de operação Estadual e UF emitente igual à UF do destinatário

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302421297815)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302431032983)

 Trata-se de uma operação DENTRO do Estado?

- Nesse caso será necessário ajustar o CFOP informado para um **CFOP que inicie com 1 ou 5**. Visto que caso o  CFOP inicie por 2 ou 6 (operação interestadual) a UF do emitente deve ser obrigatoriamente **diferente da do destinatário.**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302431034391)

 Trata-se de uma operação FORA do Estado?

- Nesse caso será necessário que o endereço do emitente (UF) seja diferente do endereço do destinatário (UF). Verifique o cadastro do parceiro, redigite o cabeçalho da nota e gere um novo lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302421301783)

CAUSA:**

Essa validação em questão, confronta a UF do endereço do emitente e do destinatário com o **CFOP.**  Caso o CFOP que foi informado não atenda a operação, ou seja, uma operação estadual com **CFOP** iniciado com 2 ou 6, será retornada a rejeição.