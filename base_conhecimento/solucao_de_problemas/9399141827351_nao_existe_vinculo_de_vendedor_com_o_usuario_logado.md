# Não existe vínculo de vendedor com o usuário logado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9399141827351-N%C3%A3o-existe-v%C3%ADnculo-de-vendedor-com-o-usu%C3%A1rio-logado](https://ajuda.sankhya.com.br/hc/pt-br/articles/9399141827351-N%C3%A3o-existe-v%C3%ADnculo-de-vendedor-com-o-usu%C3%A1rio-logado)  
> **ID:** `9399141827351` | **Última Atualização:** 2026-07-22T15:08:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18603188019863)

 MENSAGEM:**

[CORE_E02037]  Não existe vínculo de vendedor com o usuário logado.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18603172394775)

 SITUAÇÃO:**

Ao tentar visualizar os pedidos no portal de vendas a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18603172402839)

 CAUSA:**

Não possuir vendedor informado no cadastro do usuário e opção Ver pedidos/notas (web): 'Do Vendedor' marcada.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18603188066199)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18603172412695)

 Verifique no cadastro do **usuário** *(Configurações » Controle de Acesso » Usuários)* se o campo vendedor está preenchido, caso não esteja basta informar um vendedor para esse usuário.

![usuarios.png](https://ajuda.sankhya.com.br/hc/article_attachments/18603188075927)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18603188087575)

 Ver na Configuração da aba Segurança no Cadastro deste usuário, campo: **Ver pedidos/notas (web)**: Se estiver como 'Do Vendedor' é preciso que exista um vendedor vinculado ao usuário logado. Caso queria visualizar os lançamentos de todos vendedores, deverá modificar a opção para 'De todos'.