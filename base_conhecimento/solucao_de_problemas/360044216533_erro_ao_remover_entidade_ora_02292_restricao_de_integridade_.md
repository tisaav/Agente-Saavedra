# Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.FK_TGFREF_NUFIN_TGFFIN) violada - registro filho localizado

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044216533-Erro-ao-remover-entidade-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFREF-NUFIN-TGFFIN-violada-registro-filho-localizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044216533-Erro-ao-remover-entidade-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFREF-NUFIN-TGFFIN-violada-registro-filho-localizado)  
> **ID:** `360044216533` | **Última Atualização:** 2026-07-22T16:00:31Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582861217943)

 MENSAGEM:**

Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.FK_TGFREF_NUFIN_TGFFIN) violada - registro filho localizado.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582861221271)

 SITUAÇÃO:**

Ao acessar o Portal de Vendas, e tentar efetuar o Cancelamento de uma Nota, a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582861228183)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582846497303)

 Acesse: Financeiro » Gerente » Gerência de Cobrança

Faça um filtro pelo parceiro da Nota ou um filtro personalizado pelo Número único do Financeiro da Nota, que precisa ser cancelado.

Apresentará na grade de 'Títulos' os titulo(s) da Nota que esta tentando cancelar.

Acesse a aba: **"Histórico Cobrança"** e exclua todos os registros para um ou cada título financeiro da Nota.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582846498455)

 Após o processo, a NF-e pode ser cancelada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16582861238551)

 CAUSA:**

Ocorre quando os títulos financeiro da NF-e que está tentando Cancelar possui registro de Histórico de Cobrança, impedindo o cancelamento.