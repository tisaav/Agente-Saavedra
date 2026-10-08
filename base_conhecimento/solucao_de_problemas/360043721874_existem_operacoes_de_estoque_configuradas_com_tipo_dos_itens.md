# Existem operações de estoque configuradas com tipo dos itens igual à 'Lista de materiais de todas as atividades' e não existe nenhuma atividade definida como 'Lista de matéria-prima padrão'

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043721874-Existem-opera%C3%A7%C3%B5es-de-estoque-configuradas-com-tipo-dos-itens-igual-%C3%A0-Lista-de-materiais-de-todas-as-atividades-e-n%C3%A3o-existe-nenhuma-atividade-definida-como-Lista-de-mat%C3%A9ria-prima-padr%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043721874-Existem-opera%C3%A7%C3%B5es-de-estoque-configuradas-com-tipo-dos-itens-igual-%C3%A0-Lista-de-materiais-de-todas-as-atividades-e-n%C3%A3o-existe-nenhuma-atividade-definida-como-Lista-de-mat%C3%A9ria-prima-padr%C3%A3o)  
> **ID:** `360043721874` | **Última Atualização:** 2026-07-22T16:00:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365082036247)

 MENSAGEM:**

Existem operações de estoque configuradas com tipo dos itens igual à 'Lista de materiais de todas as atividades' e não existe nenhuma atividade definida como 'Lista de matéria-prima padrão', então estas operações não serão executadas por falta de itens.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365110584087)

 SITUAÇÃO:**

Ao tentar iniciar uma atividade de Produção, ocorre a mensagem a seguir.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365110586647)

SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365110589591)

 Acesse: *Produção » Cadastros » Processo Produtivo* e selecione o processo clicando no botão **"Roteiro"**.

Acesse a atividade que deseja marcar na Aba: **"Geral"**, marcando a opção: **"****Lista de matéria-prima padrão".**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365110591383)

 Acesse: *Produção » Rotinas » Operações de Produção* e selecione a produção. 'Inicie' a Produção.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365082059031)

 OBSERVAÇÃO:** esta marcação se faz necessária caso o processo produtivo possua 2 (duas) ou mais atividades e apenas uma das atividades possua a Lista de matérias-primas configurada, mesmo que as outras atividades façam apenas processos de movimentação de transferências de locais de produção/armazenamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16365110594967)

CAUSA:**

A partir da versão 3.23 do Sankhya-W, foi criada uma validação, para não permitir configurar atividades, cuja operação de estoque esteja configurada a opção **"Tipos de Itens":** **"Lista de materiais de todas as atividades"**.