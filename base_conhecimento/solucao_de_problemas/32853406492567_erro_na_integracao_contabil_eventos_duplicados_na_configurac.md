# Erro na Integração Contábil – Eventos Duplicados na Configuração da Integração Contábil

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32853406492567-Erro-na-Integra%C3%A7%C3%A3o-Cont%C3%A1bil-Eventos-Duplicados-na-Configura%C3%A7%C3%A3o-da-Integra%C3%A7%C3%A3o-Cont%C3%A1bil](https://ajuda.sankhya.com.br/hc/pt-br/articles/32853406492567-Erro-na-Integra%C3%A7%C3%A3o-Cont%C3%A1bil-Eventos-Duplicados-na-Configura%C3%A7%C3%A3o-da-Integra%C3%A7%C3%A3o-Cont%C3%A1bil)  
> **ID:** `32853406492567` | **Última Atualização:** 2026-07-29T13:19:58Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32853406481175)

** MENSAGEM:**

**Falha:** Existem eventos duplicados na conta contábil com registro fiscal da empresa: **‘xxxx’** 

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32853406481431)

** SITUAÇÃO:**

Durante o processo de **integração contábil da folha de pagamento**, o sistema apresentou a mensagem de falha informando a existência de eventos duplicados vinculados aos mesmos parâmetros** contábeis**.
 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32853406483223)

** SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32853420825879)

 ** Acesse a tela Configuração de Integração Contábil** (Pessoal+ » Cadastros » Configuração de Integração Contábil)** buscar o registro fiscal, o grupo de contabilização e tipo de contabilização e busque pelo código apresentado na mensagem da falha.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32853406484631)

 Percebe-se que ele vai vir em duplicidade, dessa forma realizar a exclusão da sequência maior, pois ela indica que foi a última a ser criada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32853420827799)

 Após a exclusão, faça novamente o processo de integração contábil.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33048743137687)

 CAUSA:**

Esse erro ocorre quando dois ou mais eventos estão configurados de forma duplicada na rotina de Configuração da Integração Contábil, utilizando:

- O mesmo registro fiscal,

- O mesmo Grupo de Contabilização, e

- O mesmo Tipo de  Contabilização

Neste caso específico, foi identificado que o evento ‘xxxx’ estava cadastrado duas vezes com os mesmos parâmetros contábeis.