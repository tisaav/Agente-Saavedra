# Erro: "HttpServiceBroker: Nenhum provedor foi encontrado para o serviço 'XXXXX'." em integração

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37347640474519-Erro-HttpServiceBroker-Nenhum-provedor-foi-encontrado-para-o-servi%C3%A7o-XXXXX-em-integra%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37347640474519-Erro-HttpServiceBroker-Nenhum-provedor-foi-encontrado-para-o-servi%C3%A7o-XXXXX-em-integra%C3%A7%C3%A3o)  
> **ID:** `37347640474519` | **Última Atualização:** 2026-07-22T14:13:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37347640466327)

 **MENSAGEM:**

"statusMessage": "HttpServiceBroker: Nenhum provedor foi encontrado para o serviço 'CACSP.incluirNota'."

 

![2025-12-30_12-59.png](https://ajuda.sankhya.com.br/hc/article_attachments/37347640466583)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37347661939607)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37396250477335)

 Identifique o serviço informado no erro:

```text
CACSP.incluirNota
```

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37396250482455)

 **Verifique o módulo da URL utilizada na requisição.

- 

Confira se a chamada está sendo feita para:

```text
/gateway/v1/mge/service.sbr
```

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37396250484887)

 Ajuste o módulo da URL, se necessário.

- O serviço **CACSP.incluirNota** pertence ao módulo **MGECOM **e não funciona no módulo MGE.

- A URL correta do módulo MGECOM:

```text
/gateway/v1/mgecom/service.sbr?serviceName=CACSP.incluirNota&outputType=json
```

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37396250487447)

 Execute novamente a requisição.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37396236519575)

 Após o ajuste da URL, o serviço será localizado corretamente e o erro não ocorrerá.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37396236522775)

 OBSERVAÇÃO: **As URLs citadas são exemplos. O mesmo erro pode ocorrer com outros serviços e módulos sempre que a requisição for feita em um módulo diferente daquele ao qual o serviço pertence.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37347661940503)

CAUSA:**

O erro ocorre porque o serviço chamado **não pertence ao módulo informado** na requisição.

**Exemplo:**

Ao tentar incluir uma nota utilizando a URL do módulo **MGE**, a requisição falha, pois o serviço `CACSP.incluirNota` pertence ao módulo **MGECOM** e só funciona quando chamado nesse módulo. Ou seja, a requisição está apontando para o módulo errado, e o **Gateway** não encontra nenhum provedor que possa processar a chamada.