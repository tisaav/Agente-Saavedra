# Não pode Alterar/Excluir uma tabela com data anterior a ultima data da tabela

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/25511981681303-N%C3%A3o-pode-Alterar-Excluir-uma-tabela-com-data-anterior-a-ultima-data-da-tabela](https://ajuda.sankhya.com.br/hc/pt-br/articles/25511981681303-N%C3%A3o-pode-Alterar-Excluir-uma-tabela-com-data-anterior-a-ultima-data-da-tabela)  
> **ID:** `25511981681303` | **Última Atualização:** 2026-07-22T14:45:29Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25511973498135)

 **MENSAGEM:**

ORA-20101: Não pode Alterar/Excluir uma tabela com data anterior a ultima data da tabela.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25511981668631)

SOLUÇÃO:**

Caso a mensagem seja apresentada ao tentar duplicar uma tabela, defina uma data de vigor na tabela de destino que seja posterior à última data vigor da tabela de origem.

Se estiver tentando alterar ou excluir uma tabela com data de vigor anterior à última data de vigor da tabela o sistema não irá permitir. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/25511973519383)

CAUSA:**

A mensagem é apresentada ao acessar a tela** "Tabela de Preço",** clicar na opção **"Copiar Tabela"** e inserir uma data de vigor anterior à data de vigor da tabela copiada. 

Também ao tentar alterar ou excluir uma tabela com data de vigor anterior à última data de vigor da tabela, a mensagem é apresentada.