# Contato não pode ser excluído porque está informado em algum pedido/nota

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616413-Contato-n%C3%A3o-pode-ser-exclu%C3%ADdo-porque-est%C3%A1-informado-em-algum-pedido-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616413-Contato-n%C3%A3o-pode-ser-exclu%C3%ADdo-porque-est%C3%A1-informado-em-algum-pedido-nota)  
> **ID:** `360044616413` | **Última Atualização:** 2026-07-22T15:54:03Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981712250391)

 MENSAGEM:**

[ORA-20101]: ORA-20101: Contato não pode ser excluído porque está informado em algum pedido/nota.
[ORA-06512]: em "SANKHYA.TRG_DLT_TGFCTT", line 39
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_DLT_TGFCTT'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981720817303)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981712257559)

 Por questões de integridade de informações, não é possível e não recomendamos excluir registros que tenham sido utilizados em lançamentos por alguma rotina do sistema (Lançamento de Nota, Pedido, Financeiro, Livros Fiscais e etc.);

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981712259607)

 Para solução deste caso, recomendamos inativar o Parceiro/Contato, para que o mesmo não seja utilizado em lançamentos futuros.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16981720828439)

CAUSA:**

Ao tentar excluir um parceiro ou contato vinculado a este parceiro, a mensagem será apresentada se esses tiverem sido utilizado em lançamentos de alguma rotina.