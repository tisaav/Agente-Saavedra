# Explosão de lote do WMS

> **Módulo:** Melhores Praticas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4402884385431-Explos%C3%A3o-de-lote-do-WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/4402884385431-Explos%C3%A3o-de-lote-do-WMS)  
> **ID:** `4402884385431` | **Última Atualização:** 2026-07-22T15:24:11Z

---

O termo explosão de lote é muito utilizado no WMS, sendo o mesmo aquele que realizará a busca de uma determinada mercadoria que trabalhe com controle e data de validade. No sistema, atualmente, temos 3 formas para realizar o processo no WMS, que são elas:

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451140008727)

 Onde no pedido pode ser informado o lote ou realizada a explosão de lote, deverá ser informado o item, tendo os parâmetros **"****LOTAUTCENT" e "LOTEDTVAL" **habilitados.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451140008727)

 Habilitado o parâmetro **"****LOTEENVIOWMS" **em um pedido, onde haja um produto com lote armazenado no WMS, este item não deverá ter seu campo **"CONTROLE (LOTE)"** preenchido. Devendo, assim, o pedido  ser confirmado e no envio para o WMS o sistema irá explodir o item no Pedido gravando os lotes encontrados, buscando o de menor validade e assim por diante, até atender a quantidade do pedido.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451140008727)

 Na tela** Comercial » Preferências » Empresa Aba 'WMS'** a marcação** "Utiliza explosão de lote na separação"** estando preenchida desta forma irá ser enviado ao WMS e as tarefas de separação irão ser preenchidas no campo controle com #EXPLODLOTE. No ato da separação no coletor, é permitido que o separador selecione o produto independente do seu lote. Desta forma, não fica condicionado a um lote específico, podendo ser pego o lote que o separador melhor encontrar em seu processo.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16342785203735)

 OBSERVAÇÃO:**

Ao realizar estas marcações, certifique que não está com o parâmetro **"LOTEENVIOWMS"** Habilitado e a marcação na tela **'Utiliza explosão de lote na separação'.** Com as duas marcações o sistema irá realizar divergências nas tarefas e causará inconsistência, não realizando a separação de maneira correta.