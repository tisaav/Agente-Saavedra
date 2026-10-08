# [PROD_E00615] Não foi encontrado um modelo de etiqueta para realizar a pesagem. O modelo de etiqueta pode ser configurado no cadastro do produto, no cadastro da empresa da planta de manufatura ou no parâmetro "MODETIPES".

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32769764919447--PROD-E00615-N%C3%A3o-foi-encontrado-um-modelo-de-etiqueta-para-realizar-a-pesagem-O-modelo-de-etiqueta-pode-ser-configurado-no-cadastro-do-produto-no-cadastro-da-empresa-da-planta-de-manufatura-ou-no-par%C3%A2metro-MODETIPES](https://ajuda.sankhya.com.br/hc/pt-br/articles/32769764919447--PROD-E00615-N%C3%A3o-foi-encontrado-um-modelo-de-etiqueta-para-realizar-a-pesagem-O-modelo-de-etiqueta-pode-ser-configurado-no-cadastro-do-produto-no-cadastro-da-empresa-da-planta-de-manufatura-ou-no-par%C3%A2metro-MODETIPES)  
> **ID:** `32769764919447` | **Última Atualização:** 2026-07-22T14:30:25Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32769771008151)

 **MENSAGEM**

[PROD_E00615] Não foi encontrado um modelo de etiqueta para realizar a pesagem. O modelo de etiqueta pode ser configurado no cadastro do produto, no cadastro da empresa da planta de manufatura ou no parâmetro "MODETIPES". 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32769764912919)

SOLUÇÃO**

O sistema verifica o **modelo de etiqueta para pesagem** seguindo uma ordem de prioridade. Para resolver a mensagem, é necessário garantir que pelo menos um dos locais abaixo esteja configurado:

**1. Verifique o modelo de etiqueta no Produto**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774663024279)

 Acesse a tela ****[''Produto''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa)** **(Configurações» Cadastros» Produtos» Produtos).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774632569751)

 Na aba** ''Manufatura''**, sub aba **''Pesagem''. **

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774663027607)

 Verifique se existe um modelo configurado no campo **''Modelo de Etiqueta''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774663029143)

 Caso esteja vazio, **inclua** o modelo desejado.

 

##### **2. Verifique o modelo de etiqueta na Empresa**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774663024279)

 Acesse a tela ****[''Empresa''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774632569751)

 Abra a aba ''Manufatura'' e verifique se o campo ''Modelo de Etiqueta'' está preenchido.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774663027607)

 Confira se o campo ''Modelo de Etiqueta'' está preenchido na aba Manufatura. Se não houver nenhum modelo configurado, **cadastre** o modelo que deverá ser utilizado.

 

##### **3. Verifique o parâmetro MODETIPES**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774663024279)

 Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774632569751)

 No campo ''**Chave ou descrição''**, pesquise pelo parâmetro **''****MODETIPES**** - Modelo de etiqueta pesagem''.**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36774663027607)

 Caso esteja vazio, **configure** um modelo para que o sistema possa utilizá-lo.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32769771010199)

CAUSA:**

A mensagem aparece quando **nenhum modelo de etiqueta** está configurado no produto, na empresa ou no parâmetro.

Como o sistema não encontra nenhum modelo para usar na pesagem, ele mostra esse aviso.


---

### 🔗 Links e Referências Internas:

- [''Produto''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa)