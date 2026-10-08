# [Erro 106] Evento em duplicidade no envio ao e-Social

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33716657827607--Erro-106-Evento-em-duplicidade-no-envio-ao-e-Social](https://ajuda.sankhya.com.br/hc/pt-br/articles/33716657827607--Erro-106-Evento-em-duplicidade-no-envio-ao-e-Social)  
> **ID:** `33716657827607` | **Última Atualização:** 2026-08-18T20:01:23Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985165736983)

 **MENSAGEM: **

[Erro 106] Foi localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo Tipo de Inscrição, Número de Inscrição

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985165742615)

 **SITUAÇÃO:**

Ao tentar realizar o envio do evento **"S-1200 (Remuneração)"** ou **"S-1210 (Pagamentos)"** pela **"Central do eSocial"** (Pessoal+» Rotinas Folha» Central do eSocial) a mensagem de erro é apresentada. 

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985153380759)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985153383831)

 Realize a geração geral dos eventos no sistema; 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985448608151)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985153386263)

 Localize o evento e o colaborador correspondente: 

- 

Clique em **"Alterar Dados";**

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985448612247)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985165749655)

 Selecione a opção **"Finalizar Evento"** e insira o **número do recibo** disponível no portal do e-Social; 

![3.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985448613399)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985165750679)

 Repita o procedimento para todos os eventos que apresentaram erros; 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985579213591)

 Após ajustar os eventos com erro, envie um evento que tenha sido gerado com sucesso. Caso não haja eventos pendentes para envio, envie o fechamento da referência.

 

**

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/33985153391767)

 Atenção:** É essencial realizar o envio conforme descrito para que o número do recibo seja gravado corretamente no sistema. Se o processo não for realizado, o evento continuará sendo gerado indevidamente.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33985153392407)

 **CAUSA:**

O erro ocorre quando há perda do recibo do evento. Isso acontece quando o envio ao portal do e-Social é concluído com sucesso, mas, devido a uma falha de conexão durante a transmissão do recibo para o sistema, a informação não é registrada corretamente.

Como resultado, o evento é gerado novamente e, ao tentar reenviá-lo, ocorre o erro de duplicidade, pois o e-Social já possui o evento registrado.