# CORE_E05076: O produto XXX - não possui lastro ou camadas informados para uma unidade alternativa

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34894940140055-CORE-E05076-O-produto-XXX-n%C3%A3o-possui-lastro-ou-camadas-informados-para-uma-unidade-alternativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/34894940140055-CORE-E05076-O-produto-XXX-n%C3%A3o-possui-lastro-ou-camadas-informados-para-uma-unidade-alternativa)  
> **ID:** `34894940140055` | **Última Atualização:** 2026-07-22T14:26:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34894940135447)

 **MENSAGEM**

[CORE_E05076] O produto XXX não possui lastro ou camadas informados para uma unidade alternativa

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445948470039)

 **SITUAÇÃO**

Esta mensagem aparece quando o usuário está realizando operações no **sistema WMS** com produtos que possuem **unidades alternativas** configuradas, mas que não têm os campos de **lastro e camadas** devidamente preenchidos para essas unidades.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34894940136087)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445916612375)

 Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445916613655)

 Filtre o **produto informado na mensagem de erro**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445948477975)

 Acesse a aba **"WMS"** do produto.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445916617111)

 Na seção **"Norma de Paletização"**, verifique se o campo **"Exige Lastro e Camadas"** está marcado.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445916618391)

 Caso esteja marcado, configure o **lastro e camadas** para o produto principal nos campos correspondentes.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445948485655)

 Acesse a aba **"Unidades Alternativas"**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35445948487575)

 Caso o produto trabalhe com **unidade alternativa,** preencha os campos **"Lastro"** e **"Camadas"** da unidade.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34894940137623)

 **CAUSA**

Esta mensagem ocorre quando o produto está configurado para **exigir lastro e camadas** na norma de paletização, mas alguma **unidade alternativa** do produto não possui os campos **"Lastro"** e **"Camadas"** devidamente preenchidos.