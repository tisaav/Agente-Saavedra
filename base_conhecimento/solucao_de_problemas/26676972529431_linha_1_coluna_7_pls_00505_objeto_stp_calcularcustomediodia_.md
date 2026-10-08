# linha 1, coluna 7: PLS-00505 objeto STP_CALCULARCUSTOMEDIODIA Invalido ORA-06550 linha 1, coluna 7: PL/SQL Statement ignored

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26676972529431-linha-1-coluna-7-PLS-00505-objeto-STP-CALCULARCUSTOMEDIODIA-Invalido-ORA-06550-linha-1-coluna-7-PL-SQL-Statement-ignored](https://ajuda.sankhya.com.br/hc/pt-br/articles/26676972529431-linha-1-coluna-7-PLS-00505-objeto-STP-CALCULARCUSTOMEDIODIA-Invalido-ORA-06550-linha-1-coluna-7-PL-SQL-Statement-ignored)  
> **ID:** `26676972529431` | **Última Atualização:** 2026-07-22T14:40:49Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26676972507927)

 **MENSAGEM:**

ORA-06550 linha 1, coluna 7: PLS-00505 objeto STP_CALCULARCUSTOMEDIODIA Invalido ORA-06550 linha 1, coluna 7: PL/SQL Statement ignored 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26676972510359)

SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26676987771927)

 Acesse a tela **"Preferências"** *(Caminho: Configurações » Avançado » Preferências) *e altere o parâmetro **"CALCCUSTOASSINC"** para a opção **"Transação por nota".**

 

Através do parâmetro Cálculo de Custo Assíncrono - CALCCUSTOASSINC que, por padrão é apresentado desativado, determine como o sistema procederá com o cálculo de custos, conforme as seguintes opções:

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450222051095)

 **Transação por Nota:** o sistema efetuará uma transação por nota para realizar o cálculo de custos;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450222051095)

 **Transação por item:** por essa opção tem-se uma transação item à item para realização do cálculo de custos;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450222051095)

 **Desabilitado:** o cálculo do custo não será feito de maneira assíncrona.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26676987776279)

CAUSA:**

Quando o cálculo do custo não é feito de maneira assíncrona, a quantidade de linhas de custos a serem calculadas podem ocasionar o erro.