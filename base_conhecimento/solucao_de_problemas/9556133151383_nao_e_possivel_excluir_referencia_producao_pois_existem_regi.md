# Não é possível Excluir Referência Produção, pois existem registros com status "Finalizado" 

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9556133151383-N%C3%A3o-%C3%A9-poss%C3%ADvel-Excluir-Refer%C3%AAncia-Produ%C3%A7%C3%A3o-pois-existem-registros-com-status-Finalizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/9556133151383-N%C3%A3o-%C3%A9-poss%C3%ADvel-Excluir-Refer%C3%AAncia-Produ%C3%A7%C3%A3o-pois-existem-registros-com-status-Finalizado)  
> **ID:** `9556133151383` | **Última Atualização:** 2026-07-22T15:07:24Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606331227287)

 MENSAGEM:**

[LIV_E00061] Não é possível Excluir Referência Produção, pois existem registros com status "Finalizado".

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606331238167)

 SITUAÇÃO:**

Ao tentar excluir e gerar o REINF novamente, a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606323484567)

 CAUSA:**

Tentativa de exclusão de referências em ambiente Produção.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18606331245335)

 SOLUÇÃO:**

Não é possível excluir referências no ambiente "Produção" uma vez que já foi executada a ação "Gerar", e nessa ação, gerou algum evento e o mesmo está com o campo Status igual a "Finalizado", inclusive o evento R1000.