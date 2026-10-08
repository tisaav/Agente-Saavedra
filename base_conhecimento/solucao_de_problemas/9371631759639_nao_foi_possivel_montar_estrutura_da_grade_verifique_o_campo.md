# Não foi possível montar estrutura da grade, verifique o campo detalhe

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9371631759639-N%C3%A3o-foi-poss%C3%ADvel-montar-estrutura-da-grade-verifique-o-campo-detalhe](https://ajuda.sankhya.com.br/hc/pt-br/articles/9371631759639-N%C3%A3o-foi-poss%C3%ADvel-montar-estrutura-da-grade-verifique-o-campo-detalhe)  
> **ID:** `9371631759639` | **Última Atualização:** 2026-07-22T15:08:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612957684759)

 MENSAGEM:**

[CORE_E02491] Não foi possível montar estrutura da grade, verifique o campo detalhe.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612965359255)

 SITUAÇÃO:**

Ao acessar a tela do Planejamento orçamentário ou Planejamento de Metas/Orçamentos a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612971408151)

 CAUSA:**

Esta mensagem ocorre quando a configuração da Meta/Orçamento utiliza um campo de detalhamento hierárquico (como Gerente) sem que sua base de origem (como Vendedor) esteja presente na estrutura de campos significativos, ou quando há inconsistência no cadastro do Vendedor.

Também pode ocorrer quando a meta utiliza o campo significativo Executante, mas não existem registros de Vendedores/Compradores ativos com o tipo 'Executante' cadastrados no sistema.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612935424535)

 SOLUÇÃO:**

Verifique a configuração da estrutura do planejamento no campo "detalhar por" caso esteja por exemplo configurado para pegar o "Vendedor do Item" é necessário acessar o cadastro do vendedor e verificar a configuração definida no campo "Tipo":

![vendedor.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612957719319)

Além da verificação do tipo de vendedor, certifique-se de que:

1. 

Se o campo **Detalhar por** estiver definido como **Gerente**, acesse a tela **Configuração da Estrutura de Metas/Orçamentos **e confirme se o campo **Vendedor** está marcado como **Campo Significativo**.

1. 

Verifique se os vendedores envolvidos possuem um Gerente vinculado em seu cadastro (Tela **Vendedores**, campo **Gerente**).

1. 

Se a meta utilizar o campo Executante, acesse a tela Vendedores/Compradores e valide se existem usuários ativos com o campo Tipo definido como 'Executante'. O sistema exige pelo menos um registro correspondente para criar a estrutura da grade.