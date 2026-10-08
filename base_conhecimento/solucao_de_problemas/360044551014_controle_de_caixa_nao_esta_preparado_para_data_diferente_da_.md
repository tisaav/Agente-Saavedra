# Controle de caixa não está preparado para data diferente da data do servidor

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044551014-Controle-de-caixa-n%C3%A3o-est%C3%A1-preparado-para-data-diferente-da-data-do-servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044551014-Controle-de-caixa-n%C3%A3o-est%C3%A1-preparado-para-data-diferente-da-data-do-servidor)  
> **ID:** `360044551014` | **Última Atualização:** 2026-07-22T15:51:41Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605249627671)

 MENSAGEM**:

[CORE_E01726] Controle de caixa não esta preparado para data diferente da data do servidor.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605275808023)

 CAUSA**:

Ocorre quando a baixa de um titulo está sendo efetuado em uma conta que é do tipo CAIXA PDV. Conta do TIPO CAIXA PDV, sempre requer abertura de caixa e a movimentação é sempre diário.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605249640855)

 SOLUÇÃO**:

- Considere o comportamento da Aplicação, conforme abaixo:

Quando a conta que está sendo efetuado for do tipo 'Caixa PDV', o comportamento do sistema é não deixar efetuar baixa com data futura, retroativa ou caixa fechado.

- Considere efetuar a baixa com a data atual, ou usar outra conta que não seja do tipo 'Caixa PDV'.

**Para verificar qual o tipo de Conta, acesse:**

- Configurações » Cadastros » Bancários » Contas
aba: Cadastros
Campo: Tipo da Conta