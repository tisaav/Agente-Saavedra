# Reimpressão do Danfe as parcelas do financeiro estão saindo diferente do que está no sistema

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26557100802199-Reimpress%C3%A3o-do-Danfe-as-parcelas-do-financeiro-est%C3%A3o-saindo-diferente-do-que-est%C3%A1-no-sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/26557100802199-Reimpress%C3%A3o-do-Danfe-as-parcelas-do-financeiro-est%C3%A3o-saindo-diferente-do-que-est%C3%A1-no-sistema)  
> **ID:** `26557100802199` | **Última Atualização:** 2026-07-22T14:41:21Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26647498350103)

 **SITUAÇÃO:**

Reimpressão do Danfe as parcelas do financeiro estão saindo diferente do que está no sistema.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26557100797591)

SOLUÇÃO:**

Neste caso a solução está ligada ao parâmetro **"Imprimir faturas no DANFE pelo xml- FINANCEXMLDANFE"** *(Caminho: Configurações » Avançado » Preferências):*

- 
**Quando ligado**, ao imprimir o DANFE, será impresso em conformidade com o XML da nota;

- 
**Quando desligado** será impresso em conformidade com o financeiro da nota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26557087016855)

CAUSA:**

Ocorre quando por algum motivo o é alterado a data de vencimento de um financeiro na movimentação

financeira por algum motivo e o parâmetro está FINANCEXMLDANFE ligado.