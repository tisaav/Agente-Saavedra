# WMS_E01058: A tarefa selecionada se encontra fechada ou em execução no coletor

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34776622060951-WMS-E01058-A-tarefa-selecionada-se-encontra-fechada-ou-em-execu%C3%A7%C3%A3o-no-coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/34776622060951-WMS-E01058-A-tarefa-selecionada-se-encontra-fechada-ou-em-execu%C3%A7%C3%A3o-no-coletor)  
> **ID:** `34776622060951` | **Última Atualização:** 2026-07-22T14:26:45Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34776634776599)

 **MENSAGEM**

[WMS_E01058] A tarefa selecionada se encontra fechada ou em execução no coletor.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35444867587863)

 **SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta buscar uma tarefa pelo coletor de dados ou pela tela de **"Execução de Tarefas Impressas"** e a tarefa já está sendo executada por outro usuário ou já foi finalizada.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34776634777111)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35444899693975)

 Acesse a tela **"Gerência do WMS"** (WMS » Gerência » Gerência do WMS) para verificar o status da tarefa selecionada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35444867592727)

 Verifique se a tarefa está em execução e identifique qual usuário está executando a tarefa.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35444867595415)

 **Se a rotina estiver sendo executada pelo coletor de dados:** 

- 

Acesse o coletor com o usuário da tarefa

- 

Rejeite todas as tarefas que ainda estão em execução

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35444867597335)

 **Se a rotina estiver sendo executada pela tela de Execução de Tarefas Impressas:**

- 

Acesse a tela **"Execução de Tarefas Impressas WMS"** (WMS » Rotinas » Execução de Tarefas Impressas WMS)

- 

Clique em **"Cancelar a Execução do Mapa"**

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34776634777879)

 **CAUSA**

A mensagem ocorre quando uma tarefa já está sendo executada por um usuário ou já foi finalizada, impedindo que outro usuário acesse a mesma tarefa simultaneamente.