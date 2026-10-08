# Divergência de lotes de produtos não encontrados (Portal de Importação de XML)

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35749438513175-Diverg%C3%AAncia-de-lotes-de-produtos-n%C3%A3o-encontrados-Portal-de-Importa%C3%A7%C3%A3o-de-XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/35749438513175-Diverg%C3%AAncia-de-lotes-de-produtos-n%C3%A3o-encontrados-Portal-de-Importa%C3%A7%C3%A3o-de-XML)  
> **ID:** `35749438513175` | **Última Atualização:** 2026-07-22T14:24:51Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35749426259479)

 **MENSAGEM:**

Divergência de lotes de produtos não encontrados (Portal de Importação de XML)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35749426260375)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36625529711767)

 Acesse a tela ****[''Tipo de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)** **(Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36625529714967)

 Na aba **''Estoque'' **maque o campo **''Atualizar Estoq.a partir da Confirmação''**.

 

![TOP.png](https://ajuda.sankhya.com.br/hc/article_attachments/36625519418391)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36625529716503)

 Após realizar a configuração, exclua o documento gerado na Central.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36625529717143)

 Feche as telas, acesse o sistema e execute um novo processamento no ****[''Portal de Importação da XML''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35749426260631)

CAUSA:**

O erro ocorre no ''Portal de Importação de XML'', quando o campo “Atualizar Estoq. a partir da Confirmação” não está marcado na TOP utilizada para a importação. 

Nessa condição, o sistema atualiza o estoque **imediatamente ao gravar cada item da nota**. Como o controle não foi informado nesse momento, o processo fica inconsistente e a mensagem é exibida.


---

### 🔗 Links e Referências Internas:

- [''Tipo de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [''Portal de Importação da XML''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)