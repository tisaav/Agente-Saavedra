# O  código do Agente Nocivo não está na padronização

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4659135548439-O-c%C3%B3digo-do-Agente-Nocivo-n%C3%A3o-est%C3%A1-na-padroniza%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/4659135548439-O-c%C3%B3digo-do-Agente-Nocivo-n%C3%A3o-est%C3%A1-na-padroniza%C3%A7%C3%A3o)  
> **ID:** `4659135548439` | **Última Atualização:** 2026-07-29T13:23:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343089746711)

 MENSAGEM**:

E0103 [eSocial/evtExpRisco/infoExpRisco/agNoc/codAgNoc] Conteúdo com largura abaixo do mínimo: 6 < 9O tamanho da informação inserida no campo do cadastro é menor do que aquela prevista no layout do e-social. Reveja a sua configuração.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343073559575)

 CAUSA:**

O código do Agente Nocivo não esta na padronização 00.00.000.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343073560727)

 SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343073562647)

 Realize o o cadastro das informações dos agentes nocivos na **Rotina/SESMT/ Ambiente de trabalho/ Agente nocivos  **conforme a **Tabela 24 - Agentes Nocivos e Atividades - Aposentadoria Especial.**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343073567127)

 O código do Agente Nocivo deve seguir a padronização 00.00.000. O seu código de Ausência de agente nocivo ou de atividades previstas no Anexo IV do Decreto 3.048/1999.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343089763223)

 Caso o código não esteja no formato supracitado, rode o script via banco de dados para criação da tabela TFPAGNOC.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343073572887)

 Logo após os ajustes feitos no cadastro, gere os eventos novamente e envie S-2240.