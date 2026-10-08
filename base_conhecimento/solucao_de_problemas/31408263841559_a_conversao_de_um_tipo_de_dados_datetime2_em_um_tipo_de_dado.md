# A conversão de um tipo de dados datetime2 em um tipo de dados datetime resultou em um valor fora do intervalo

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31408263841559-A-convers%C3%A3o-de-um-tipo-de-dados-datetime2-em-um-tipo-de-dados-datetime-resultou-em-um-valor-fora-do-intervalo](https://ajuda.sankhya.com.br/hc/pt-br/articles/31408263841559-A-convers%C3%A3o-de-um-tipo-de-dados-datetime2-em-um-tipo-de-dados-datetime-resultou-em-um-valor-fora-do-intervalo)  
> **ID:** `31408263841559` | **Última Atualização:** 2026-07-22T14:33:08Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31408263834647)

 **MENSAGEM:**
A conversão de um tipo de dados datetime2 em um tipo de dados datetime resultou em um valor fora do intervalo.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31408263835415)

SOLUÇÃO:**
Esse erro geralmente ocorre no SQL Server ao realizar um processamento do arquivo de retorno, quando tenta converter um valor `datetime2` para `datetime`, mas o valor não é compatível com o intervalo permitido pelo tipo `datetime`.
Para correção, acesse o layout utilizado no processamento através da tela** "Configuração Arquivo de Retorno"** (*Caminho: Financeiro » EDI Bancário » Configuração Arquivo de Retorno*) e altere os campos relacionados a data para o seguinte formato:
 
**DATABAIXADDMMYYYY**
**DATACREDITODDMMYYYY**
**DATAVENCIMENTODDMMYYYY**
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/31408263836183)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31408322175511)

CAUSA:**

Esse erro ocorre quando um valor de data/hora lido durante o processamento do arquivo de retorno está fora do intervalo permitido pelo tipo de dado `datetime` do SQL Server.