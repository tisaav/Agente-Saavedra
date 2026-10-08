# Envio de notas por e-mail - Erro: Operação requer uma transação ativa

> **Módulo:** Solucao de Problemas | **Subseção:** Acessos/Banco de Dados  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20501015133335-Envio-de-notas-por-e-mail-Erro-Opera%C3%A7%C3%A3o-requer-uma-transa%C3%A7%C3%A3o-ativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/20501015133335-Envio-de-notas-por-e-mail-Erro-Opera%C3%A7%C3%A3o-requer-uma-transa%C3%A7%C3%A3o-ativa)  
> **ID:** `20501015133335` | **Última Atualização:** 2026-07-22T14:50:58Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20501000660887)

 **MENSAGEM:**

Ao realizar o envio de notas por e-mail, poderá ser apresentado o seguinte erro: Operação requer uma transação ativa.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20501000662167)

 SOLUÇÃO:**

Quando for necessária a atualização do banco de dados, verifique a versão do Driver Oracle. Uma possível causa do erro pode ser a incompatibilidade entre as duas versões.

Siga as orientações abaixo para uma possível solução:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20501015126551)

 Compare as versões por meio da tela **Administração do Servidor** *(Configurações » Avançado » Administração do Servidor)*  aba "Geral";

![Administrador do Servidor 17-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20644579953047)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20501000668055)

 Atualize o Driver Oracle para garantir a compatibilidade com a versão mais recente do banco de dados (conforme item 1);

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20501000669591)

 Reinicie a aplicação e limpe o cache do navegador;

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20594874436503)

 Em seguida, caso a solução seja efetiva, será possível realizar o envio dos e-mails novamente;

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20595074097431)

 IMPORTANTE:**

Se o erro persistir, acione a equipe de atendimento do Service Desk para uma análise efetiva.