# Como configurar o código DUN para aparecer no XML da NF-e?

> **Módulo:** Melhores Praticas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39354906421655-Como-configurar-o-c%C3%B3digo-DUN-para-aparecer-no-XML-da-NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/39354906421655-Como-configurar-o-c%C3%B3digo-DUN-para-aparecer-no-XML-da-NF-e)  
> **ID:** `39354906421655` | **Última Atualização:** 2026-09-03T14:10:27Z

---

O código DUN (GTIN-14) é utilizado para identificar a unidade logística de um produto, sendo amplamente empregado em operações de venda no atacado. Para que esse código seja enviado no XML da NF-e, é necessário configurar o cadastro do produto para que o sistema utilize o EAN/GTIN da unidade alternativa na tag cEAN.

 

### **

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/43217635477271)

Configuração necessária no cadastro de produtos**

Para que o código DUN seja gerado corretamente no XML da NF-e, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39354860593687)

 Acesse a tela **"Produtos"** (Comercial Arquivo Cadastros Produtos) e localize o produto desejado.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39354860593943)

 Clique na aba **"Impostos"** do cadastro do produto.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39354906421271)

 Localize o campo **"EAN/GTIN produto p/NF-e"** e configure-o como **"****Cód.Barras da Unid.Alternativa ou a Referência****"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39354906421399)

 Salve as alterações realizadas no cadastro.

 

### **

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/43217635477271)

Como funciona a geração da tag cEAN**

Após realizar a configuração do campo **"EAN/GTIN produto p/NF-e"**, o sistema irá buscar automaticamente o código cadastrado no **"DUN"** do produto e incluí-lo na tag **"cEAN"** do XML da NF-e durante a emissão da nota fiscal.

Esta configuração é **obrigatória** para que o código seja transmitido corretamente no documento fiscal eletrônico, atendendo às exigências de vendas no atacado e garantindo a rastreabilidade dos produtos.

 

### **

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43217635478039)

Pontos importantes**

• O código **"DUN"** deve estar previamente cadastrado no produto para que possa ser referenciado no XML.

• A configuração deve ser realizada **individualmente para cada produto** na aba **"Impostos"**.

• Após a configuração, emita uma NF-e de teste e verifique o XML gerado para confirmar que a tag **"cEAN"** está sendo preenchida corretamente.

• Esta configuração é especialmente importante para empresas que realizam **vendas no atacado**, onde o código EAN/GTIN é uma exigência dos clientes.