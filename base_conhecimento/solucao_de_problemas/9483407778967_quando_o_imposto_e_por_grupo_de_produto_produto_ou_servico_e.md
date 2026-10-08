# Quando o imposto é por Grupo de Produto, Produto ou Serviço e tiver o campo 'No Financeiro de Origem Estoque' = 'Subtrair' todos os registros devem ter a mesma alíquota e redução de base

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9483407778967-Quando-o-imposto-%C3%A9-por-Grupo-de-Produto-Produto-ou-Servi%C3%A7o-e-tiver-o-campo-No-Financeiro-de-Origem-Estoque-Subtrair-todos-os-registros-devem-ter-a-mesma-al%C3%ADquota-e-redu%C3%A7%C3%A3o-de-base](https://ajuda.sankhya.com.br/hc/pt-br/articles/9483407778967-Quando-o-imposto-%C3%A9-por-Grupo-de-Produto-Produto-ou-Servi%C3%A7o-e-tiver-o-campo-No-Financeiro-de-Origem-Estoque-Subtrair-todos-os-registros-devem-ter-a-mesma-al%C3%ADquota-e-redu%C3%A7%C3%A3o-de-base)  
> **ID:** `9483407778967` | **Última Atualização:** 2026-07-22T15:07:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666415004055)

 MENSAGEM:**

[CORE_E01887]  Quando o imposto é por Grupo de Produto, Produto ou Serviço e tiver o campo 'No Financeiro de Origem Estoque' = 'Subtrair' todos os registros devem ter a mesma alíquota e redução de base.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666382115863)

 SITUAÇÃO:**

Ao tentar alterar o campo "No Financeiro de Origem Estoque" a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666382127639)

 CAUSA:**

Ocorre quando existe divergência na % da alíquota dos serviços informados na tela de Impostos.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666415042327)

 SOLUÇÃO:**

Acesse a tela **Impostos** *(Configurações » Cadastros » Impostos)* aba Serviço e verifique  se todos os serviços informados possuem a mesma alíquota.

Isso é necessário quando o campo "No Financeiro de Origem Estoque" estiver definido como Subtrair.

![impostos.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666415052311)

 

**Importante: **Orientamos verificar com a contabilidade a necessidade de configurar uma alíquota diferente e caso realmente tenha a necessidade, será necessário que um consultor de implantação avalie este processo.