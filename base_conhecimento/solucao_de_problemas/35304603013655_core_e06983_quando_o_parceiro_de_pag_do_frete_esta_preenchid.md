# CORE_E06983 - Quando o parceiro de pag. do frete está preenchido as outras formas de pagamento devem estar vazias!

> **Módulo:** Solucao de Problemas | **Subseção:** Distribuição  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35304603013655-CORE-E06983-Quando-o-parceiro-de-pag-do-frete-est%C3%A1-preenchido-as-outras-formas-de-pagamento-devem-estar-vazias](https://ajuda.sankhya.com.br/hc/pt-br/articles/35304603013655-CORE-E06983-Quando-o-parceiro-de-pag-do-frete-est%C3%A1-preenchido-as-outras-formas-de-pagamento-devem-estar-vazias)  
> **ID:** `35304603013655` | **Última Atualização:** 2026-07-22T14:25:34Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35304632629783)

 **MENSAGEM:**

[CORE_E06983] Quando o parceiro de pag. do frete está preenchido as outras formas de pagamento devem estar vazias!

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35304632631959)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35675750618519)

 Acesse a tela  **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)) e identifique o registro que está gerando o erro;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35675764400279)

 Acesse esse registro em questão, nele vá até a até a aba** "MDF-e"**, sub aba **"Pagamento de frete"**, por fim sub aba **"Geral" ** e veja se o campo **"Parceiro de Pag. do Frete" **está preenchido;

 

![CORE_E06983 Quando o parceiro de pag. do frete está preenchido as outras.png](https://ajuda.sankhya.com.br/hc/article_attachments/35675750623895)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35675764405911)

 Caso o campo Parceiro de Pag. do Frete esteja preenchido, os campos abaixo devem estar vazios:

- Banco

- Agência 

- Chave Pix

Assim, **limpe **os campos **Banco, Agência e Chave Pix** e **deixe apenas** o campo **Parceiro de Pagamento do Frete preenchido.**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35304632632599)

CAUSA:**

Quando os dados bancários são informados e já tem os dados de pagamentos  com o parceiro informados para a vista ou a prazo.