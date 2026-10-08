# A data informada deve ser maior ou igual que 01/01/1890 e não poderá ser maior que a data atual

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7607470136599-A-data-informada-deve-ser-maior-ou-igual-que-01-01-1890-e-n%C3%A3o-poder%C3%A1-ser-maior-que-a-data-atual](https://ajuda.sankhya.com.br/hc/pt-br/articles/7607470136599-A-data-informada-deve-ser-maior-ou-igual-que-01-01-1890-e-n%C3%A3o-poder%C3%A1-ser-maior-que-a-data-atual)  
> **ID:** `7607470136599` | **Última Atualização:** 2026-07-29T13:24:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16530693201559)

 MENSAGEM**:

Erro 1281 - A data informada deve ser maior ou igual que 01/01/1890 e não poderá ser maior que a data atual. Elemento: /eSocial/evtMonit/exMedOcup/aso/dtAso[AAAA-MM-DD]*
*

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16530693205015)

 SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16530655053975)

 Entre na rotina: MGE Pessoal Rotinas\SESMT\ ASO - Atestado de Saúde Ocupacional; 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16530693207447)

 Avalie a data da realização do ASO e corrija esta data, pois é necessário respeitar o critério '*A data informada deve ser maior ou igual que 01/01/1890 e não poderá ser maior que a data atual.'*

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16530693208343)

 Logo após ajustar as datas do exame, faça a geração dos eventos novamente e libere para envio o evento S2220;

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16530655058583)

 CAUSA:**

O erro ocorre pela data do ASO estar incorreta.