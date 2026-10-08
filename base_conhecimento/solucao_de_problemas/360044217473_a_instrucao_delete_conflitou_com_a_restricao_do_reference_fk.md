# A instrução DELETE conflitou com a restrição do REFERENCE "FK_TGFFIN_TSICTA"

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044217473-A-instru%C3%A7%C3%A3o-DELETE-conflitou-com-a-restri%C3%A7%C3%A3o-do-REFERENCE-FK-TGFFIN-TSICTA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044217473-A-instru%C3%A7%C3%A3o-DELETE-conflitou-com-a-restri%C3%A7%C3%A3o-do-REFERENCE-FK-TGFFIN-TSICTA)  
> **ID:** `360044217473` | **Última Atualização:** 2026-07-22T16:00:22Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292333243415)

 MENSAGEM:**

A instrução DELETE conflitou com a restrição do REFERENCE "FK_TGFFIN_TSICTA". O conflito ocorreu no banco de dados "SANKHYA_PROD", tabela "sankhya.TGFFIN", column 'CODCTABCOINT'.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292333259543)

 SITUAÇÃO:**
Ao tentar excluir uma conta bancária apresenta o erro abaixo:

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292372288919)

 SOLUÇÃO:**
Considere o comportamento da aplicação conforme abaixo:

 

Não se pode excluir uma conta que tenha sido utilizado em movimentações no sistema. Considere analisar algum relatório financeiro para verificar onde esta conta foi utilizada e, caso seja possível, excluir os títulos criado com esta conta, então será possível excluir a conta bancária.

O mais recomendável é verificar se a Conta Bancária possui algum saldo e efetuar a transferência para outra conta e então **desativar **a conta e não exclui-la.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292372304279)

 CAUSA:**

Esta mensagem ocorre quando o usuário tenta excluir alguma Conta Bancária que já não é utilizada mais. Porém esta conta foi utilizada em alguma rotina, seja algum título financeiro na baixa ou em alguma nota de compra ou venda e outros.

Então, existe uma relação entre a conta e o lançamento e por restrição de integridade de informação não se recomenda excluir a conta, salvo se os lançamento forem excluídos.