# A data do evento não pode ser maior que a data do processamento

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043238073-A-data-do-evento-n%C3%A3o-pode-ser-maior-que-a-data-do-processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043238073-A-data-do-evento-n%C3%A3o-pode-ser-maior-que-a-data-do-processamento)  
> **ID:** `360043238073` | **Última Atualização:** 2026-07-22T16:05:54Z

---

** 

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087962713495)

 MENSAGEM:**

Lote de evento para Cancelamento de Nota processado. Mas o evento não foi vinculado a NFe. Status de retorno: 578, motivo: Rejeição: A data do evento não pode ser maior que a data do processamento.

 

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087962717079)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087962722455)

 Ajuste o horário do seu servidor conforme horário oficial do servidor da SEFAZ do seu Estado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088008529431)

 Caso trate-se de um servidor Linux solicite apoio ao seu técnico de T.I.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088008531863)

 Poderá utilizar links de apoio para conferência dessa hora, tal como[http://www.apolo11.com/tictoc/fuso_horario.php.](http://www.apolo11.com/tictoc/fuso_horario.php)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16088008535703)

 Realizado o ajuste, refaça o processo de cancelamento.

 

** 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16087962740503)

 CAUSA:**

Ao tentar realizar o cancelamento de uma NF-e, onde a hora do evento enviado no XML (dhEvento) é superior a hora do servidor da Sefaz, será retornada a rejeição.