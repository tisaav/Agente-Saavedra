# Qual é o processo para preencher o campo 'Em Recebimento WMS' na tela de Consulta de Produto

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20417099471127-Qual-%C3%A9-o-processo-para-preencher-o-campo-Em-Recebimento-WMS-na-tela-de-Consulta-de-Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/20417099471127-Qual-%C3%A9-o-processo-para-preencher-o-campo-Em-Recebimento-WMS-na-tela-de-Consulta-de-Produto)  
> **ID:** `20417099471127` | **Última Atualização:** 2026-07-22T14:51:07Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20433946335383)

 **SITUAÇÃO:**

Qual é o processo para preencher o campo 'Em Recebimento WMS' na tela de Consulta de Produto?

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20417131308567)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20433973271703)

 Ligue o parâmetro **"Desconsidera estoque em doca do WMS? - SUBESTDOCAWMS",**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20433973286423)

 Informe a Data de previsão de entrada no cabeçalho da nota de compra.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20433946364695)

 Ao enviar para o recebimento, utilizando a opção 'Enviar para o recebimento WMS' no botão outras opções dos portais, é necessário escolher uma doca que apenas trabalha com entrada de mercadoria e não entrada/saída.

 

Com as condições realizadas o campo 'Em recebimento WMS' será preenchido com a quantidade do item a receber consultado na rotina de Consulta de Produtos.

**Observações:**

- O sistema considera como 'a receber' todos os produtos que passaram pelo processo no coletor superwaba/totalcross e tiveram a conferência de entrada concluída.

- Após a finalização da tarefa de armazenagem em um desses dispositivos, o campo 'Em Recebimento WMS' será limpo.