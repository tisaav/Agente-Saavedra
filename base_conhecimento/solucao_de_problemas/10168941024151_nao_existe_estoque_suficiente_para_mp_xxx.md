# Não existe estoque suficiente para MP XXX

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10168941024151-N%C3%A3o-existe-estoque-suficiente-para-MP-XXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/10168941024151-N%C3%A3o-existe-estoque-suficiente-para-MP-XXX)  
> **ID:** `10168941024151` | **Última Atualização:** 2026-07-22T15:04:22Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276807689879)

 MENSAGEM:**

[CORE_E01247] Não existe estoque suficiente para MP XXX.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276830776087)

 SITUAÇÃO:**

Ao inserir um item que é kit no pedido a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276807692055)

 SOLUÇÃO:**

Quando o item que é kit é inserido no pedido, o sistema tenta localizar o local onde o mesmo se encontra.

Assim, primeiro verifique se os 'componentes' possuem  o campo "CODLOCALMP"  preenchido. 

Vale destacar que,  para que consiga informar o "Controle" nos componentes, o parâmetro** 'Mostrar o controle da aba de componentes - CONTROLECOMPON', **na tela **Preferências** *(Configurações » Avançado » Preferências), *deve estar ligado. Desse modo, observe se o parâmetro está em conformidade. 

 

![preferencias 23-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276807698327)

 

Após habilitar o parâmetro acima (caso ele esteja desligado), acesse o cadastro de **Produtos** *(Caminho de acesso à tela: Configurações » Cadastros » Produtos » Produtos), *vá até a aba 'Componentes' e informe o local para o componente.

 

![Produtos 23-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276807698967)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19276830776727)

 CAUSA:**

Ocorre quando o componente está sem local definido ("Local" do componente está igual à 0).