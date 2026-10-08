# Melhores Práticas para configuração de um Vendedor visualizar apenas seus lançamentos

> **Módulo:** Melhores Praticas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579794-Melhores-Pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-de-um-Vendedor-visualizar-apenas-seus-lan%C3%A7amentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579794-Melhores-Pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-de-um-Vendedor-visualizar-apenas-seus-lan%C3%A7amentos)  
> **ID:** `360044579794` | **Última Atualização:** 2026-07-22T15:51:28Z

---

Existem alguns processos da área Comercial que requer que seus vendedores visualizem e façam movimentações somente com determinados clientes de sua respectiva carteira, ou seja, restrição para que outros vendedores não visualizem lançamentos originados de outro vendedor.

Vejamos a seguir uma boa prática para configuração desta restrição.

O Sistema Sankhya/Jiva W existe uma expressão chamada: **ctx[usuario_logado]** e **ctx[emp_usu_logado].**

- Vejamos a configuração básica.

1. Acesse o sistema com o usuário SUP

1. Configurações » Controle de Acesso » Usuários
No cadastro do usuário, vincule o Código do Vendedor, no campo 'Vendedor'
Vincule o código da Empresa(se desejar), no campo 'Empresa'

1. Acesse a Rotina desejada. [Exemplo: Financeiro » Rotinas » **Movimentação Financeira**]

1. Clique para abrir o 'Assistente de Filtro'.

1. Clique em 'Editar filtro padrão'.

1. Escolha uma das opções de filtro indicada abaixo e cole nesta opção

1. Salve o registro.

**Observação**: Somente o usuário SUP tem permissão de inserir/alterar e excluir este filtro padrão. Os usuários não visualizara esta opção, portanto não poderá altera-lo ou exclui-lo.

- Vejamos um exemplo de uso das expressões na rotina de 'Movimentação Financeira'.

Abaixo foram definidas três possibilidades para configurar tal filtro:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196223882647)

 Desta forma o USUÁRIO 'XXXXX', visualiza apenas títulos que ele mesmo lançou e para a empresa que está vinculada ao seu cadastro e o usuário SUP visualiza tudo.

*( ctx[usuario_logado] <> 0 and *
*Financeiro.CODEMP = ctx[emp_usu_logado] AND *
*Financeiro.CODUSU = ctx[usuario_logado] ) or *
*ctx[usuario_logado] = 0*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196223885719)

 Se desejar que apenas o USUÁRIO 'XXXXX', visualize apenas títulos que são da Empresa 2(por exemplo), independente de quem lançou o título use apenas o filtro abaixo, usuário SUP visualiza tudo:

*( ctx[usuario_logado] <> 0 and *
*Financeiro.CODEMP = ctx[emp_usu_logado]) or *
*ctx[usuario_logado] = 0*

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19196223892119)

 Se desejar que apenas o USUARIO 'XXXXX', visualize apenas títulos que ele próprio lançou independente da empresa vinculada ao usuário, use o filtro dessa forma,o usuário SUP visualiza tudo:

*( ctx[usuario_logado] <> 0 AND *
*Financeiro.CODUSU = ctx[usuario_logado] ) or *
*ctx[usuario_logado] = 0*