# Compensação financeira no FastService

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043727494-Compensa%C3%A7%C3%A3o-financeira-no-FastService](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043727494-Compensa%C3%A7%C3%A3o-financeira-no-FastService)  
> **ID:** `360043727494` | **Última Atualização:** 2026-07-22T15:59:39Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363411758487)

 SITUAÇÃO:**

Ao efetuar o lançamento de um cupom fiscal para um parceiro que possui um crédito, a compensação financeira não ocorre. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363411761559)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363434709015)

 Acesse a tela **"Preferências"*** (Caminho de acesso: Configurações » Avançado):*

- Parâmetro **"TIPTITCREDCLI-Tipo de título para compensação de Crédito": **informe neste parâmetro um título que foi criado para simbolizar Crédito de Cliente;

- Parâmetro: **"****AVISARCREDCLI-Avisar que o cliente possui Crédito?":* ***ligado

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363411764247)

 Acesse: FastService  » Menu » Preferências » Todas as Preferências

Aba: **"Miscelânia"**

- Avisar que o cliente possui crédito: marcado

- Tipo de Titulo para compensação de crédito/troca: informe o código do tipo de titulo

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363434715031)

 Acesse: FastService » Menu » Preferências » Todas as Preferências

Aba: **"Cupom Modelo"**

- Nas preferências do FastService, cadastramos as notas modelo. Nessas, é possível identificar várias informações pertinentes ao processo de venda, compensação e etc;

- Essas configurações são encontradas na aba Cupom Modelo. A atenção que temos que tomar nesse momento é referente ao parceiro.

- Isso se dá visto que nesse processo é identificado o parceiro padrão das vendas (no caso de nota modelo de venda). Caso o parceiro identificado no ato da despesa for o mesmo identificado na nota modelo, a compensação não será questionada. O parceiro identificado na nota modelo é o 'Consumidor final'.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363434716183)

 Tipo de título identificado na nota de 'Despesa' lançada para a empresa identificando o parceiro receptor desse valor:

- Por último, temos a preocupação de identificação do tipo de título no ato do lançamento da despesa para o parceiro identificado. Esse lançamento pode ser efetuado através de mais de uma forma. Para exemplificar, vamos mostrar o lançamento de uma movimentação financeira;

- Tomamos o cuidado de identificar o tipo de título de crédito na Despesa para a empresa. Isso se faz necessário para definir os títulos que devem ser compensados. Ou seja, podemos efetuar o lançamento de despesas para a empresa em questão que não serão compensados e, para isso, é só identificar um tipo de título diferente do parâmetro **"TIPTITCREDCLI";**

- Após esse processo, será possível efetuar a compensação de crédito no FastService. É só identificar o parceiro (sendo diferente do parceiro identificado na nota modelo) no ato da venda e a mensagem** 'Esse parceiro possui um crédito de R$__,__. Deseja compensar o valor de R$__,__?';**

- Caso o botão 'Sim' seja clicado, a compensação do crédito será efetuada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363411774999)

CAUSA:**

A compensação de crédito na venda é utilizada quando é identificado uma despesa lançada para a empresa da nota modelo para um parceiro identificado neste ato.