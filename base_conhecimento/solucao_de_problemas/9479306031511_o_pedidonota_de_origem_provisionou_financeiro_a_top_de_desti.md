# O Pedido/Nota de origem provisionou financeiro, a TOP de destino não pode provisionar

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9479306031511-O-Pedido-Nota-de-origem-provisionou-financeiro-a-TOP-de-destino-n%C3%A3o-pode-provisionar](https://ajuda.sankhya.com.br/hc/pt-br/articles/9479306031511-O-Pedido-Nota-de-origem-provisionou-financeiro-a-TOP-de-destino-n%C3%A3o-pode-provisionar)  
> **ID:** `9479306031511` | **Última Atualização:** 2026-07-22T15:07:41Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613926784279)

 MENSAGEM:**

[CORE_E04609] O Pedido/Nota de origem provisionou financeiro, a TOP de destino não pode provisionar.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613926790295)

 SITUAÇÃO:**

Ao faturar um pedido com provisionamento para uma Top que não atualiza financeiro a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613926794263)

 CAUSA:**

Ocorre quando a TOP de origem e destino possuem a mesma configuração de atualização de financeiro.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613926795159)

 SOLUÇÃO:**

Verifique no cadastro do **Tipo de Operação TOP** *(Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP)* de destino o campo "Atualiza Financeira na TOP de origem" se está selecionado.

![topfinanceiro.png](https://ajuda.sankhya.com.br/hc/article_attachments/18613926804631)

Se a marcação **"Atualiza Financeiro na TOP de Origem" **for efetuada, possibilitará que, em um lançamento na Central, a TOP de Destino atualize o financeiro, mesmo que a TOP de Origem já o tenha atualizado.