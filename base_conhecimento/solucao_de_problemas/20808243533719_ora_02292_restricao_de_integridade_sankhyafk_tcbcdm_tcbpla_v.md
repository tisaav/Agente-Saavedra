# ORA-02292: restrição de integridade (SANKHYA.FK_TCBCDM_TCBPLA) violada - registro filho localizado

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20808243533719-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TCBCDM-TCBPLA-violada-registro-filho-localizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/20808243533719-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TCBCDM-TCBPLA-violada-registro-filho-localizado)  
> **ID:** `20808243533719` | **Última Atualização:** 2026-07-22T14:50:41Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20808243518743)

 **MENSAGEM:**

**"ORA-02292: restrição de integridade (SANKHYA.FK_TCBCDM_TCBPLA) violada - registro filho localizado" **

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20808259273367)

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20808259278871)

SOLUÇÃO:**

Para solução deve-se realizar uma consulta via banco (DBExplorer) através do seguinte SELECT: 

 

**SELECT * FROM TCBCDM WHERE CODCTACTB = 'código da conta reduzida'**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20808243520535)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20808243522583)

 

O resultado do SELECT apresentará o campo 'CODDMT' (Código Hierárquia Demonstrativo). O preenchimento desse campo será o código da hierarquia das contas na tela. Detalhe: Consultar aba por aba, até identificar a conta; 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20808259283607)

 

Identificando a Conta Reduzida na tela, basta excluir esse registro e o sistema permitirá exclusão da Conta normalmente na tela Plano de Contas.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20808259284375)

CAUSA:**

O erro é apresentado quando a Conta Reduzida tem vinculo com a tela Demonstrativos ECD. Para obter sucesso na exclusão da Conta, é necessário excluir o vinculo da conta com a tela.