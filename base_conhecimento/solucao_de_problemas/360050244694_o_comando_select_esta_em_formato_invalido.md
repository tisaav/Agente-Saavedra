# O comando SELECT está em formato inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360050244694-O-comando-SELECT-est%C3%A1-em-formato-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050244694-O-comando-SELECT-est%C3%A1-em-formato-inv%C3%A1lido)  
> **ID:** `360050244694` | **Última Atualização:** 2026-07-22T15:30:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585675007895)

 MENSAGEM:**

O comando SELECT está em formato inválido.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585675014167)

 CAUSA:**

Utilização de querys em relatórios/dashboards que utilizam a expressão WITH.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585690091287)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585675034903)

 Acesse o servidor onde o Wildfly está instalado e na pasta WILDFLY_HOME/standalone/bin localize o seguinte arquivo:

- Se o sistema operacional for Linux, abrir para edição o arquivo **standalone.conf**

- Se Windows, o arquivo a ser editado é o **standalone.conf.bat**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585675043479)

 Localize então em tal arquivo, o argumento: **-Djape.jdbc.check.select=true** e alterá-lo para false, ficando: **-Djape.jdbc.check.select=false**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585675053847)

 Em seguida reinicie o sistema a partir do próprio servidor para que a alteração entre em vigor.