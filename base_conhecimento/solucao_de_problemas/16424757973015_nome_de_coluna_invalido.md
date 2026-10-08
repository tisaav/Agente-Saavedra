# Nome de coluna inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16424757973015-Nome-de-coluna-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/16424757973015-Nome-de-coluna-inv%C3%A1lido)  
> **ID:** `16424757973015` | **Última Atualização:** 2026-07-22T14:55:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16531192779159)

 MENSAGEM: **

Nome de coluna inválido.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16531209132567)

 SITUAÇÃO: **

Ao contabilizar os movimentos bancários a mensagem é apresentada. 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16531209133591)

 SOLUÇÃO:**

Na maior parte das vezes, o problema ocorre em função da configuração da TOP utilizada nos lançamentos das transferências bancárias.
 
Se a TOP em questão se encontrar parametrizada para considerar o Centro de Resultado como variável, poderá ocasionar essa inconsistência. Contudo, no caso da tabela dos movimentos bancários (TGFMBC) não existe nenhum campo que grave essa informação, e atualmente o sistema também não consegue validar essa informação em nenhum outro lugar. 
 
Por isso, ao contabilizar os lançamentos, o sistema retornou a mensagem de erro.
 
Altere o preenchimento do campo **"Tipo de Centro de Resultado"** para **"Constante"** e informe um CR fixo no cadastro da TOP. Com isso, os movimentos serão contabilizados sem apresentar nenhuma inconsistência.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16531233410199)