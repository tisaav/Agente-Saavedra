# Impossível preencher campos de tempo em itens de fila: HRINICIAL

> **Módulo:** Solucao de Problemas | **Subseção:** Controle de O.S'S  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044277553-Imposs%C3%ADvel-preencher-campos-de-tempo-em-itens-de-fila-HRINICIAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044277553-Imposs%C3%ADvel-preencher-campos-de-tempo-em-itens-de-fila-HRINICIAL)  
> **ID:** `360044277553` | **Última Atualização:** 2026-07-22T15:59:12Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201268747543)

 MENSAGEM:**

Impossível preencher campos de tempo em itens de fila: HRINICIAL.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201268751127)

 S****ITUAÇÃO:**

Ao tentar gerar o fechamento de ordem de serviço é apresentada a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201297979159)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201297980567)

 Identifique o usuário logado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201297981719)

 Acesse a tela Configurações » Controle de Acesso » Relacionamento entre Usuários.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201268757271)

 No campo usuário, filtre o usuário logado (identificado no item 1).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201268758295)

 Na aba **Membros da fila,** verifique se existem usuários informados.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201268759447)

 Caso a configuração esteja correta, por exemplo, o atual executante deste item é uma "Fila", é necessário que este item seja direcionado a um executante desta fila.

 

![relacionamento_entre_usuarios.png](https://ajuda.sankhya.com.br/hc/article_attachments/14664388475927)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201297986455)

 Caso a configuração esteja incorreta e o atual executante deste item não seja uma fila, exclua-o da aba Membros da fila.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16201268761623)

 CAUSA:**

A mensagem: "Impossível preencher campos de tempo em itens de fila: HRFINAL" é apresentada pois o executante do item o qual estão tentando fechar é uma Fila.