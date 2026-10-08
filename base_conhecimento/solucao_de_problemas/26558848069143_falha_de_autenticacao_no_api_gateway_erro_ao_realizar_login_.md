# Falha de Autenticação no API Gateway: Erro ao realizar login com ERP

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26558848069143-Falha-de-Autentica%C3%A7%C3%A3o-no-API-Gateway-Erro-ao-realizar-login-com-ERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/26558848069143-Falha-de-Autentica%C3%A7%C3%A3o-no-API-Gateway-Erro-ao-realizar-login-com-ERP)  
> **ID:** `26558848069143` | **Última Atualização:** 2026-07-22T14:41:17Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/26558848062615)

**MENSAGENS**

Dependendo do endpoint utilizado, o erro pode se apresentar de duas formas:

**Método **`**/login**`

```text
{
   "bearerToken": null,
   "error": {
       "codigo": "GTW3407",
       "descricao": "Não foi possivel realizar login com Erp."
   }
}
```

 

**Método **`**/authenticate**`

```text
{
   "error": "HTTP 400 Erro ao se autenticar com o serviço externo."
}
```

  

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/40464358414359)

**SITUAÇÃO**

O incidente ocorre durante o consumo dos endpoints de autenticação do **API Gateway**.

A principal diferença é que o endpoint `/login` retorna o código específico **[GTW3407]**, enquanto o método mais recente, `/authenticate`, retorna uma mensagem de erro genérica (**HTTP 400**). Em ambos os casos, a falha indica que o Gateway não conseguiu validar as credenciais do usuário junto ao ERP.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/26558810350487)

**SOLUÇÃO**

Para resolver o erro, realize as validações abaixo na ordem indicada:

**1. Identificar o Usuário no Gateway**

1. 

Acesse **Configurações > Avançado > Configurações Gateway**.

1. 

Na aba **Aplicações Vinculadas**, localize a aplicação que você está utilizando.

1. 

Identifique o usuário preenchido no campo **Cód. Usuário vinculado**.

**2. Validar Restrições no Cadastro de Usuários**

1. 

Acesse **Configurações > Controle de Acesso > Usuários**.

1. 

Localize o usuário identificado no passo anterior e verifique:

  - 

**Data limite de acesso:** Se o campo estiver preenchido com uma data passada, atualize-o ou remova o valor para liberar o acesso.

  - 

**Carga horária para acesso:** Verifique se há uma carga horária restritiva. Caso precise ajustar as regras de horário, acesse a tela **Configurações > Cadastros > Carga Horária**.

[!IMPORTANT] Lembre-se: Como a API "simula" o login de um usuário, qualquer regra que impeça esse usuário de acessar o Sankhya via navegador também impedirá o funcionamento da API.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/26558848065303)

**CAUSA**

Este erro geralmente é causado por **restrições de acesso no cadastro do usuário** que está vinculado à aplicação no Gateway. As situações mais comuns são:

- 

**Data Limite de Acesso:** O usuário está com a data de validade de acesso expirada.

- 

**Carga Horária:** A tentativa de login ocorre fora do horário permitido para aquele usuário.

- 

**Inconsistência de Vínculo:** O usuário definido nas configurações do Gateway possui alguma trava de segurança no ERP (ex: usuário bloqueado ou com senha expirada).