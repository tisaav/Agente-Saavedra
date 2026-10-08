# Invalid content was found starting with element 'qBCMono'. One of '{"http://www.portalfiscal.inf.br/nfe":vProd}' is expected

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/17271395687831-Invalid-content-was-found-starting-with-element-qBCMono-One-of-http-www-portalfiscal-inf-br-nfe-vProd-is-expected](https://ajuda.sankhya.com.br/hc/pt-br/articles/17271395687831-Invalid-content-was-found-starting-with-element-qBCMono-One-of-http-www-portalfiscal-inf-br-nfe-vProd-is-expected)  
> **ID:** `17271395687831` | **Última Atualização:** 2026-07-22T14:53:33Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17271395682199)

 **MENSAGEM:**

[CORE_E04895] cvc-complex-type.2.4.a: Invalid content was found starting with element 'qBCMono'. One of '{"[http://www.portalfiscal.inf.br/nfe":vProd](http://www.portalfiscal.inf.br/nfe%22:vProd)}' is expected.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17271426025751)

CAUSA:**

Ocorre quando a a NT 2023.001 está ativa e o produto da nota não é combustível.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17271441371927)

SOLUÇÃO:**

Na tela **Empresa  -** *Comercial » Preferências » Empresa* quando ativada a NT 2023.001 irá gerar o grupo de tags do ICMS Monofásico utilizado para quem compra e vende combustível apenas.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17280753448599)

As tags geradas são as destacadas abaixo:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17280872215447)

 

Após desmarcar a configuração:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17280736420247)

 

E gerar lote novamente a nota será aprovada com sucesso, uma vez que ela não tenha combustíveis inclusos.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17270643253655)