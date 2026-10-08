# Qual Processo preciso fazer para gerar a tarefa de retorno de expedição após cancelamento?

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14971395326615-Qual-Processo-preciso-fazer-para-gerar-a-tarefa-de-retorno-de-expedi%C3%A7%C3%A3o-ap%C3%B3s-cancelamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971395326615-Qual-Processo-preciso-fazer-para-gerar-a-tarefa-de-retorno-de-expedi%C3%A7%C3%A3o-ap%C3%B3s-cancelamento)  
> **ID:** `14971395326615` | **Última Atualização:** 2026-09-09T21:26:44Z

---

Quando a separação é cancelada após o processo de **"Separação"** já ter sido iniciado ou concluído. Ao clicar em outras opções na tela **"Expedição de Mercadorias" (**WMS » Rotinas » Expedição de Mercadorias), e selecionar as opções 'Cancelar Separação' ou 'Cancelar separações desta OC', o sistema altera a situação para "Cancelada-Possui Retorno Merc.". Quando o cancelamento é feito com a situação da separação como 'Conferência validada', a tarefa de retorno de expedição é gerada automaticamente pelo sistema. Entretanto, caso o cancelamento, seja feito em uma situação diferente, será necessário verificar a situação na tela **"Gerência de WMS"** WMS » Gerência » Gerência do WMS.

 

![Cancelamento.gif](https://ajuda.sankhya.com.br/hc/article_attachments/15142695275415)

 

Para realizar o retorno das mercadorias, o sistema deve gerar as tarefas após o cancelamento, apresentando a mensagem no coletor: "A separação X foi cancelada. Leve os produtos para endereço de retorno".

Caso a tarefa não seja gerada automaticamente, siga os procedimentos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43375253981463)

 Acesse a tela **"Gerência de WMS"**, altere o filtro Tipos de tarefa para "Expedição Cancelada" e verifique o campo **"Situação Cancelamento Sep."** e identifique a separação que foi cancelada

 

![CancelamentoMensagem.gif](https://ajuda.sankhya.com.br/hc/article_attachments/15142695280919)

 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43375253982615)

 Realize a tarefa indicada no campo **"Situação Cancelamento Sep',** informando o endereço vinculado a separação podendo ser uma doca de saída ou um endereço checkout para ser gerada a tarefa dependendo do tipo de separação.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43375263262615)

  Após a geração da tarefa de retorno de expedição, Execute ela no coletor a partir da tarefa **"Armazenagm"** para os produtos que participavam das separações canceladas, garantindo a acuracidade do estoque.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43375253983255)

 Após a regularização, os produtos estarão disponíveis para novas separações.

 

Observação: Caso após a realização do processo descrito, a tarefa de retorno de expedição não seja gerada, contacte o suporte para que seja analisado o cenário informando a separação e o momento exato do cancelamento.