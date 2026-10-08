# Trabalhar com POS e TEF no Fast Service

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044230533-Trabalhar-com-POS-e-TEF-no-Fast-Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044230533-Trabalhar-com-POS-e-TEF-no-Fast-Service)  
> **ID:** `360044230533` | **Última Atualização:** 2026-07-22T15:59:38Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199715203607)

 SITUAÇÃO:**

Como configurar Fast Service para trabalhar com POS e TEF?

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199753611671)

 SOLUÇÃO:**

Considere o comportamento da aplicação, conforme abaixo:

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199753614231)

 Solução TEF:**
Acesse: *Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título*:

- Para o FastService acionar o gerenciador do TEF é necessário que no cadastro do tipo de título esteja com o campo **"Forma pagamento TEF"** preenchido:

- Forma pagamento TEF: com a REDE que aquele tipo de título pertence (REDECARD,CIELO,ETC..)

 

![tipo_de_titulo.png](https://ajuda.sankhya.com.br/hc/article_attachments/14535475292695)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199715215767)

 OBSERVAÇÃO:**
Lembrando que o cliente pode ter contrato com mais de uma rede tef e neste caso o sistema também irá enviar a descrição do cadastro de tipo de titulo até que o parâmetro: "**IMPDESCTEFHOMOL-Usar forma de pagamento padrão para TEF?"** seja ativado.
Com o parâmetro ligado, o Fast mandará para a ECF a descrição padrão CARTÃO para tipos de títulos com o campo Forma pagamento TEF: preenchido com uma das redes já cadastradas.
 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199715217559)

 Solução POS:**
Neste caso a única diferença com o TEF é que o campo Forma pagamento TEF não poderá ser preenchido, uma vez que esta modalidade não é integrada ao sistema.
 
Sem este campo preenchido o sistema não irá chamar o TEF ao passar uma venda com este tipo de título.
 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199715218455)

Acesse: *Financeiro » Arquivos » Cadastros » Tipos de Título » Grupos de Tipos de Título*

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199715215767)

 OBSERVAÇÃO:**
 
Uma forma mais ágil e fácil de trabalhar com POS e TEF é realizar o cadastro de um Grupo de tipo de títulos com o nome **Cartão** e vincular ao cadastro dos tipos de títulos para POS, assim seguindo a mesma descrição do TEF na ECF.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/12826606044439)

 
**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199715215767)

 OBSERVAÇÃO:**
Caso o campo Forma de pagamento TEF esteja preenchido e a marcação Utiliza POS esteja marcada, para limpar o campo Forma de pagamento TEF desabilite o parâmetro "**HABFISCALPOSTIT"; **
 
**

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/7604169559063)

**
 

Para trabalhar com o parâmetro: "**USADESCGRUPOTIT-Utiliza descrição do grupo do tipo de titulo?"**, neste caso o sistema enviará à ECF a descrição do cadastro do grupo de tipos de títulos vinculado ao tipo de titulo em questão.

 

![tipo_de_titulo2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14535500363927)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199715215767)

 OBSERVAÇÃO:**

A possibilidade do parâmetro USADESCGRUPOTIT da descrição do grupo de tipo de título pode ser utilizada para padronizar qualquer tipo de título para varias ECF's.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199715222167)

 CAUSA:**

Quando não se está configurado corretamente, as opções de TEF/POS nos Tipos de Titulo podem afetar a forma de apresentação das bandeiras.