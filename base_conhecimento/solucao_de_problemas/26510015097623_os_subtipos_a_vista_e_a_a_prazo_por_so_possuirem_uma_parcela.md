# Os Subtipos 'A vista' e a 'A prazo', por só possuirem uma parcela, não permitem marcar o campo 'Fixa vencimento'

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26510015097623-Os-Subtipos-A-vista-e-a-A-prazo-por-s%C3%B3-possuirem-uma-parcela-n%C3%A3o-permitem-marcar-o-campo-Fixa-vencimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/26510015097623-Os-Subtipos-A-vista-e-a-A-prazo-por-s%C3%B3-possuirem-uma-parcela-n%C3%A3o-permitem-marcar-o-campo-Fixa-vencimento)  
> **ID:** `26510015097623` | **Última Atualização:** 2026-07-22T14:41:47Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26510015086999)

 **MENSAGEM:**

[CORE_E00763] Os Subtipos 'A vista' e a 'A prazo', por só possuírem uma parcela, não permitem marcar o campo 'Fixa vencimento'.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26510015085719)

 SITUAÇÃO: **

Ao marcar o campo 'Fixa Vencimento' no tipo de negociação o erro é apresentado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26510015089175)

SOLUÇÃO:**

Para permitir a marcação do campo **"Fixa Vencimento"** no sistema, use um tipo de negociação com subtipo** "A prazo"** que possua mais de uma parcela cadastrada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26509999286807)

CAUSA:**

O erro ocorre ao marcar o campo Fixa Vencimento em um tipo de negociação A vista ou A prazo que tenha apenas uma parcela cadastrada. O sistema não suporta a fixação de vencimentos quando há apenas uma parcela.