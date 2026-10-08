# Tipo de Transportador deve ser diferente de TAC

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043772434-Tipo-de-Transportador-deve-ser-diferente-de-TAC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043772434-Tipo-de-Transportador-deve-ser-diferente-de-TAC)  
> **ID:** `360043772434` | **Última Atualização:** 2026-07-22T15:59:11Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201309540119)

 MENSAGEM:**

457 - Rejeição: Tipo de Transportador deve ser diferente de TAC.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201309544215)

 SITUAÇÃO:**

Mensagem apresentada na geração do MDF-e.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201331640855)

 SOLUÇÃO:**

Quando a carga é própria e o dono do veículo terceiros:

-  Informe CNPJ do proprietário do veículo [esse deve ser diferente do CNPJ do emitente do MDF-e];

- Preencha corretamente o RNTRC;

- A opção **"Veículo da EMPRESA"**, no cadastro do veículo, deve estar DESMARCADA.

Caso seja um veículo próprio:

- Opção Veículo da EMPRESA, no cadastro do veículo, deve estar MARCADA:

 

![veiculos.png](https://ajuda.sankhya.com.br/hc/article_attachments/14663943345815)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201331642263)

 CAUSA:**

Se tipo emitente informado for igual a Prestador de Serviço de Transporte (tpEmit=1), modal = Rodoviário e CNPJ do proprietário do veículo não for informado ou for igual ao CNPJ do Emitente do MDF-e: A informação do tipo de transportador (tpTransp) deverá ser diferente de TAC (2).