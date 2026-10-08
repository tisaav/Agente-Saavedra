# Pacotes não sincronizados pelo Datasync

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360047122813-Pacotes-n%C3%A3o-sincronizados-pelo-Datasync](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047122813-Pacotes-n%C3%A3o-sincronizados-pelo-Datasync)  
> **ID:** `360047122813` | **Última Atualização:** 2026-07-22T15:32:16Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426738345623)

 SITUAÇÃO:**

Na tentativa de realizar uma venda de determinado produto incluído recentemente no W, através do Fast Service, o mesmo não é localizado. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426738351255)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426738355607)

 Na máquina do caixa (onde o Fast está instalado), acesse no navegador o endereço do Console Datasync (o endereço inicia-se com "localhost") seguido da porta (por exemplo: 8080).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426754065687)

 Informe o usuário e senha:

 

![Imagem](https://ajuda.sankhya.com.br/hc/user_images/ZdUrLv3VaCqKMNcU6zTIfA.png)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426754069015)

 Selecione a aba **Monitoramento**, em seguida, clique na sub-aba **Pacotes com pendências**.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426738363543)

 Verifique se há pacotes listados como pendentes, em caso afirmativo, guarde a informação da coluna **nó de origem**.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426738365847)

 É provável que esse pacote em questão esteja corrompido, por isso não foi recepcionado pelo datasync da filial.

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426754077335)

 Para solucionar a questão, existem duas alternativas:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426738371607)

 Identifique o pacote que está corrompido no computador onde o Datasync está instalado na máquina da matriz, e insira o manualmente na pasta do Datasync da filial, esse procedimento fará que os pacotes pendentes sejam sincronizados

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426738371607)

 Na hipótese do pacote estar corrompido também na matriz, a ação recomendada é  na aba Monitoramento, na sub-aba Pacotes com pendências, selecione cada um dos itens pendentes, clique no botão **"ignorar pendência"** e confirme. O ato de ignorar a pendência permitirá que o Datasync recepcione os demais pacotes que não estão corrompidos, o que acarretará no aparecimento do produto, pois os pacotes acumulados por pendências impede a correta sincronização do Datasync entre a matriz e filial.

 

Caso ainda apresente erro, entre em contato com o Service Desk.