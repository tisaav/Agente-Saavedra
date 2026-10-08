# Tipo de operação não está ativo. Nota de Nro unico: xxx

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14224197305495-Tipo-de-opera%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-ativo-Nota-de-Nro-unico-xxx](https://ajuda.sankhya.com.br/hc/pt-br/articles/14224197305495-Tipo-de-opera%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-ativo-Nota-de-Nro-unico-xxx)  
> **ID:** `14224197305495` | **Última Atualização:** 2026-07-22T14:59:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948895305751)

 MENSAGEM:**

[ORA-20101]: Tipo de operação não está ativo. Nota de Nro unico: xxx 
[ORA-06512]: em "xx.TRG_UPD_TGFCAB", line xx
[ORA-04088]: erro durante a execução do gatilho 'xx.TRG_UPD_TGFCAB'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948895310999)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970698218135)

 Inicialmente, verifique se a TOP do lançamento está realmente ativa na tela **"Tipos de Operação". **Se estiver ativa, siga para tratativa abaixo:

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970698222871)

 Acesse a tela **"Monitor de Consulta**" e inicie o Monitoramento; 

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970681790743)

 Volte na Central de Venda e confirme a nota, nesse ponto será apresentada o erro: 

[ORA-20101]: Tipo de operação não está ativo. Nota de Nro unico: xxx

 

Volte no Monitor de Consulta e pare o Monitoramento.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970698226199)

 OBSERVAÇÃO:**

Manual sobre a rotina Monitor de Consulta 

[Monitor de Consultas – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108733-Monitor-de-Consultas)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970698227607)

 Após parar o monitoramento, será gerado um arquivo com Monitor de Processo e outro com Monitor de Consulta;

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970681798935)

 Abra o Monitor de Processo e busque pelo erro, será apresentado o ID;

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16749156719895)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970698232343)

 Feito isso, abra o Monitor de Consulta e busque pelo mesmo ID apresentado no Monitor de Processo; 

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970681804695)

 Nele vai ser possível identificar qual top esta sendo solicitada no erro;

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16749158601367)

 

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16970681808407)

 Acesse o cadastro da TOP e ative a.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16948936081815)

 CAUSA:**

Geralmente ocorre quando está utilizando uma TOP que está ativa, mas consta outra TOP vinculada, por exemplo, top denegada e essa está desativada

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450679379607)

 **TOP 1100**

 

![Tipo de operação não está ativo. Nota de Nro unico xxx 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/17036347621527)

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450679379607)

 **TOP 1114**

 

![Tipo de operação não está ativo. Nota de Nro unico xxx 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/17036419399191)


---

### 🔗 Links e Referências Internas:

- [Monitor de Consultas – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108733-Monitor-de-Consultas)