# Código inválido. Utilizar código da "Tabela de Códigos Situação Tributária do PIS

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110814-C%C3%B3digo-inv%C3%A1lido-Utilizar-c%C3%B3digo-da-Tabela-de-C%C3%B3digos-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria-do-PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110814-C%C3%B3digo-inv%C3%A1lido-Utilizar-c%C3%B3digo-da-Tabela-de-C%C3%B3digos-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria-do-PIS)  
> **ID:** `360044110814` | **Última Atualização:** 2026-07-22T15:53:03Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610371100055)

 MENSAGEM:**

Código inválido. Utilizar código da "Tabela de Códigos Situação Tributária do PIS.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610344503703)

 SITUAÇÃO:**

Mensagem retornada na validação da 'Escrituração Fiscal Digital', quando enviado código CST de PIS que diverge da Tabela de Códigos Situação Tributária do PIS registrada pela SEFAZ.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610371116823)

 CAUSA:**

Ocorre quando enviado código CST de PIS que diverge da Tabela de Códigos Situação Tributária do PIS registrada pela SEFAZ.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610344513431)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610344529687)

 Identifique através do registro rejeitado, qual o código produto e número documento responsáveis pela causa do erro.

**Exemplo**

|C100|0|1|000004682|55|00|0|**7113**|31181013564754000116550000000071131032052930|24102018|24102018|100,00|0|17,00|0,00|117,00|1|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,02|0,09|0,00|0,00|

- REGISTRO C100 >> POSIÇÃO 8 >> NUM_DOC = 7113

|C170|1|**11006**||3,00000|UN|117,00|17,00|0|000|1102|12|0,00|0,00|0,00|0,00|0,00|0,00|0|49||0,00|0,00|0,00|**00**|3,00|0,0000||0,6500|0,02|00|3,00|0,0000||3,0000|0,09||

- REGISTRO C170 >> POSIÇÃO 3 >> COD_ITEM = 11006

- REGISTRO C170 >> POSIÇÃO 25 >> CST_PIS = 00

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610344535319)

 Identificado o item, n° documento e CST enviado, é necessário realizar os devidos ajustes para o CST que se enquadre na Tabela de Códigos Situação Tributária do PIS, conforme orientações de sua contabilidade.

**Importante:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610344529687)

 **Identificado CST'S indevidos, avalie as configurações atuais de PIS, de forma a prevenir que o problema não volte a ocorrer.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610344535319)

 Para notas de saída, emissão própria, já aprovadas, necessário uma sintonia junto ao Contador da empresa, para avaliar a solução adequada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610344537111)

 Tabela de Códigos estabelecidos através da Instrução Normativa RFB nº 1.009: