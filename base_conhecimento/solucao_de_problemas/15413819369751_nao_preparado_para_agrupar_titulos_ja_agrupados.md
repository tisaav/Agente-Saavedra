# Não preparado para agrupar títulos já agrupados

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15413819369751-N%C3%A3o-preparado-para-agrupar-t%C3%ADtulos-j%C3%A1-agrupados](https://ajuda.sankhya.com.br/hc/pt-br/articles/15413819369751-N%C3%A3o-preparado-para-agrupar-t%C3%ADtulos-j%C3%A1-agrupados)  
> **ID:** `15413819369751` | **Última Atualização:** 2026-07-22T14:56:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16539643079447)

 MENSAGEM:**

[CORE_E00735] Não preparado para agrupar títulos já agrupados.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16539643098135)

 CAUSA:**

Ocorre ao tentar agrupar títulos que já estão agrupados.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16539643082775)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16539643083799)

 Agrupar Pagamentos: quando marcada, agrupará títulos de mesmo "Parceiro" e mesmo "Vencimento" para a geração do arquivo de remessa. Ao agrupar os títulos, será registrada no "Financeiro", no campo "Nosso Número" dos títulos agrupados, a informação: "PG + o Nro. único de um dos títulos".

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16539616139031)

 Habilitando a opção de agrupar pagamentos, a geração do arquivo de remessa só ocorrerá para títulos de despesa, que não estejam baixados e que não possuam o "Nosso Número" preenchido com "PG + o Nro único de um dos títulos".

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16539643092375)

 Caso alguma dessas situações não sejam satisfeitas, o sistema emitirá uma mensagem de alerta e não fará a geração do arquivo.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16539643096599)

 Se o processo de geração for interrompido, inicie o processo novamente, já que vários títulos poderão ter preenchido o campo "Nosso Número" durante a corrida.

Portanto, o usuário deve verificar qual título teve um problema e também verificar a existência de títulos já agrupados. Caso seja identificado algum problema, retire e gere o novamente