# Já existe um registro de venda com a SERIENOTA X e o NUMNOTA X na TGFCAB

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9684540070423-J%C3%A1-existe-um-registro-de-venda-com-a-SERIENOTA-X-e-o-NUMNOTA-X-na-TGFCAB](https://ajuda.sankhya.com.br/hc/pt-br/articles/9684540070423-J%C3%A1-existe-um-registro-de-venda-com-a-SERIENOTA-X-e-o-NUMNOTA-X-na-TGFCAB)  
> **ID:** `9684540070423` | **Última Atualização:** 2026-07-22T15:06:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16778137475735)

 MENSAGEM:**

[CHK_E00011]: Já existe um registro de venda com a SERIENOTA X e o NUMNOTA X na TGFCAB.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16778151637911)

 SITUAÇÃO:**

Ao tentar receber algumas vendas realizadas no Checkout a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16778137482647)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16778151643927)

 Verifique se já existem notas com a mesma Série e numeração na TGFCAB.

Confira no cadastro do **"****Tipo de operação-TOP"** *(Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) *o **"Controle de numeração"** que foi configurado para a Empresa e Série em questão.

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16778137485591)

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/9684414306711)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16778151648919)

 No campo "**Último código**" deverá um **"Valor"** para que seja identificado que a partir do próximo lançamento aquela determinada numeração e com isso acabou gerando a duplicidade.

 

**Exemplo:**

Se a última nota gerada com a Série 16 na Empresa 3 no Sankhya /w foi a "50", deveria ter sido configurado no checkout a última numeração que foi utilizada para que o sistema seguisse a sequência corretamente. Abaixo um Print de onde deveria ser configurado essa numeração.

 

![2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16778151650455)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16778151652119)

CAUSA:**

Numeração repetida no Checkout.