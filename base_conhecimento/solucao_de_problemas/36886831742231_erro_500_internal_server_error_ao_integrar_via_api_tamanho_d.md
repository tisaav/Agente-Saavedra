# Erro "500 - Internal Server Error" ao integrar via API (Tamanho de Requisição Excedido)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36886831742231-Erro-500-Internal-Server-Error-ao-integrar-via-API-Tamanho-de-Requisi%C3%A7%C3%A3o-Excedido](https://ajuda.sankhya.com.br/hc/pt-br/articles/36886831742231-Erro-500-Internal-Server-Error-ao-integrar-via-API-Tamanho-de-Requisi%C3%A7%C3%A3o-Excedido)  
> **ID:** `36886831742231` | **Última Atualização:** 2026-07-27T20:25:30Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36886831727639)

 **MENSAGEM:**

500 - Internal Server Error

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36886831728535)

SOLUÇÃO:**

##### **

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/40819881044119)

 Revise o tamanho da requisição**

Certifique-se de que o conteúdo total enviado não ultrapasse o limite de **10 MB**. Caso você esteja lidando com arquivos pesados ou grandes volumes de dados, aplique as seguintes boas práticas:

- 

**Quebre o envio:** Divida os dados em múltiplas requisições menores (paginação/lotes).

- 

**Limpe o payload:** Remova campos e informações desnecessárias da requisição para deixá-la mais leve.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/40819864220183)

 ****Validar antes do envio**

Se você estiver desenvolvendo ou gerenciando uma integração, recomendamos implementar uma etapa de validação no código. Essa validação deve checar o tamanho (em bytes) da requisição antes mesmo de submetê-la à Sankhya, evitando que o erro 500 volte a acontecer.

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/40819881045271)

**** Testar novamente**

Após aplicar os ajustes de tamanho e fracionamento, realize um novo teste de envio e confirme se a integração foi processada com sucesso.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36886831729815)

CAUSA:**

Esse erro ocorre quando a requisição enviada ao servidor ultrapassa o limite máximo de tamanho configurado, que é de 10 MB.

Ao receber um volume de dados maior que esse limite, o servidor interrompe o processamento e retorna o código de status 500 (Falha Interna). 

Acesse o conteúdo de ****[Boas Práticas para Integração](https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o) disponível no Sankhya Developer


---

### 🔗 Links e Referências Internas:

- [Boas Práticas para Integração](https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o)