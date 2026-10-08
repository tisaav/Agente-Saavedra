# Como evitar duplicidade do evento de Confirmação da Operação na Sefaz?

> **Módulo:** Melhores Praticas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39377240719127-Como-evitar-duplicidade-do-evento-de-Confirma%C3%A7%C3%A3o-da-Opera%C3%A7%C3%A3o-na-Sefaz](https://ajuda.sankhya.com.br/hc/pt-br/articles/39377240719127-Como-evitar-duplicidade-do-evento-de-Confirma%C3%A7%C3%A3o-da-Opera%C3%A7%C3%A3o-na-Sefaz)  
> **ID:** `39377240719127` | **Última Atualização:** 2026-09-08T18:50:23Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066644503)

 **SITUAÇÃO:**

A rejeição **"Duplicidade de evento"** ocorre quando é realizada uma nova tentativa de envio do evento de **Confirmação da Operação** para uma NF-e que já possui esse evento registrado na Sefaz.

De acordo com as regras da Sefaz, o evento de **Confirmação da Operação** pode ser registrado **uma única vez por documento fiscal**. Dessa forma, após a confirmação ter sido registrada com sucesso, uma nova tentativa de envio para a mesma NF-e será rejeitada.

Essa rejeição é um retorno oficial da **Sefaz** e não representa uma falha do ERP Sankhya.
 

#### 
**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340105993495)

****Regra da Sefaz sobre eventos duplicados**

Conforme estabelecido na **Nota Técnica 2020.001 v1.50**, o evento de **Confirmação da Operação** possui uma regra específica de ocorrência única por documento fiscal.

Diferentemente de outros eventos de manifestação do destinatário, que podem possuir regras diferentes de quantidade de ocorrências, a **Confirmação da Operação não pode ser registrada novamente após sua efetivação**.

Por isso, ao tentar enviar o mesmo evento novamente, a Sefaz retorna: **Rejeição: Duplicidade de evento.**

 

#### 
**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340105993495)

****Como verificar a situação da manifestação**

Antes de enviar uma nova Confirmação da Operação:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066645271)

Acesse o **Portal de Importação de XML**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066647063)

Localize a NF-e que será manifestada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066648599)

Consulte o campo **Situação da Manifestação**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066649111)

Verifique se a Confirmação da Operação já consta como registrada.

Caso a confirmação já tenha sido registrada, **não realize um novo envio**, pois a Sefaz rejeitará a tentativa como evento duplicado.

Essa consulta deve ser realizada sempre antes de uma nova manifestação, principalmente quando houver dúvidas sobre o resultado de um envio anterior.

 

#### 
**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340105993495)

****Validação no portal da Sefaz**

Também é possível realizar uma conferência diretamente no portal da **Sefaz** responsável pelo documento fiscal.

Para isso:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066645271)

Acesse o portal da Sefaz.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066647063)

Consulte a NF-e utilizando sua **chave de acesso**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066648599)

Acesse o **histórico de eventos** do documento.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340066649111)

Verifique se o evento **Confirmação da Operação** já foi registrado.

Essa consulta permite confirmar diretamente na Sefaz se o evento foi efetivado, servindo como uma validação adicional antes de qualquer nova tentativa.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43340105997719)

 **CAUSA:**

A **Confirmação da Operação** é um evento de manifestação do destinatário que pode ser registrado **uma única vez por NF-e**.

Quando o evento já foi registrado e o usuário tenta enviá-lo novamente, a Sefaz retorna **"Rejeição: Duplicidade de evento"**.

Portanto, antes de realizar uma nova manifestação, deve-se consultar a **Situação da Manifestação no Portal de Importação** e, se necessário, confirmar o registro diretamente no **histórico de eventos da NF-e na Sefaz**.
 

###