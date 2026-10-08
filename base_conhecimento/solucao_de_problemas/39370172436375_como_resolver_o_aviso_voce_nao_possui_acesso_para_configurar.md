# Como resolver o aviso "Você não possui acesso para configurar a grade"?

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39370172436375-Como-resolver-o-aviso-Voc%C3%AA-n%C3%A3o-possui-acesso-para-configurar-a-grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39370172436375-Como-resolver-o-aviso-Voc%C3%AA-n%C3%A3o-possui-acesso-para-configurar-a-grade)  
> **ID:** `39370172436375` | **Última Atualização:** 2026-08-29T19:42:58Z

---

Este aviso aparece quando o usuário tenta configurar a grade de uma tela no sistema Sankhya, mas não possui as permissões necessárias. Mesmo que o usuário tenha a permissão **"Configurar"** habilitada em seus acessos, o sistema pode continuar exibindo esta mensagem se o parâmetro de controle não estiver corretamente configurado.
 

A configuração de acesso às grades permite que administradores controlem quais usuários podem personalizar o layout das telas, garantindo padronização quando necessário ou flexibilidade para usuários específicos.
 

 

### **Quando este aviso aparece**

O aviso **"Você não possui acesso para configurar a grade"** pode aparecer em diversas telas do sistema, incluindo:
 

- 

**"Portal de Pedidos"** (Comercial » Pedido Web » Portal de Pedidos) - na edição de registros.
 

1. 

**"Central de Vendas"** (Comercial » Rotinas » Central de Vendas) - na aba itens, modo formulário.
 

1. 

**"Portal de Cotação"** (Cotação » Rotinas » Portal de Cotação Online) - na cotação de compras.
 

1. 

Outras Centrais e Portais do sistema.
 

 

### **Como habilitar o acesso à configuração de grade**

Para permitir que o usuário configure as grades das telas, siga os passos abaixo:
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39370157847831)

  Acesse a tela **"Acessos"** (Configurações » Controle de Acesso » Acessos).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39370157861015)

  Localize o usuário ou grupo de usuários que precisa ter acesso à configuração de grade.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39370172432791)

  Selecione a rotina ou módulo específico onde o usuário precisa configurar a grade.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39370157874839)

  Habilite a opção **"Configurar"** para o usuário ou grupo selecionado.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39370172433175)

  Acesse a tela de **"Preferências"** (Configurações » Avançado » Preferências).

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39370172433559)

  Localize e habilite o parâmetro **"UTLCGFACCESSGRD - Usa permissão de acesso de Configurar para grid"**.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/39370157875479)

  Salve as alterações e oriente o usuário a desconectar e reconectar no sistema para que as permissões sejam aplicadas.

 

 

### **Como funciona o controle de configuração de grade**

Quando o parâmetro **UTLCGFACCESSGRD** está habilitado, o sistema passa a respeitar as permissões configuradas na tela de **"Acessos"**. Isso significa que:
 

- 

Usuários com a permissão **"Configurar"** poderão personalizar as grades das telas.
 

1. 

Usuários sem a permissão visualizarão apenas a configuração padrão definida pelo usuário **"SUP"**.
 

1. 

Qualquer configuração de grade realizada anteriormente por usuários sem permissão será ignorada, e a configuração do **"SUP"** será carregada.
 

 

### **Configuração padrão pelo usuário SUP**

Para garantir que todos os usuários sem permissão de configuração visualizem um layout padronizado, o usuário **"SUP"** deve configurar a grade da forma desejada. Esta configuração servirá como padrão para todos os usuários que não possuem a permissão **"Configurar"**.
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39370157847831)

  Acesse o sistema com o usuário **"SUP"**.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39370157861015)

  Abra a tela desejada e configure a grade conforme o layout padrão necessário.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39370172432791)

  Remova a permissão **"Configurar"** dos usuários que devem visualizar apenas o layout padrão.

 

 

### **Observações importantes sobre centrais e portais**

Ao configurar acessos para **"Centrais"**, a configuração será absorvida pelas telas relacionadas. Observe a correspondência:
 

- 

**"Central de Vendas"** → **"Portal de Vendas"**.
 

1. 

**"Central de Compras"** → **"Portal de Compras"**.
 

1. 

**"Central de Movimentações Internas"** → **"Portal de Movimentações Internas"**.
 

1. 

**"Central de Produção"** → **"Ordens de Produção"**.
 

Além disso, há uma configuração diferente para cada **"Tipo de Movimento"**. Quando uma configuração específica não é encontrada pelo sistema, ele utilizará a configuração padrão.
 

 

### **Solução para configurações que não atualizam**

Se após configurar a grade pelo usuário **"SUP"** o layout não estiver sendo aplicado corretamente para outros usuários, pode ser necessário:
 

- 

Verificar se o parâmetro **UTLCGFACCESSGRD** está habilitado.
 

1. 

Confirmar que a permissão **"Configurar"** foi removida dos usuários que devem ver apenas o padrão.
 

1. 

Realizar uma atualização do sistema, pois algumas versões podem apresentar inconsistências que são corrigidas em atualizações.
 

1. 

Orientar os usuários a desconectar e reconectar no sistema.