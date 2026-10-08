# Rejeição 890: GTIN inexistente no Cadastro Centralizado de GTIN (CCG) [nItem:999]

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16869639272087-Rejei%C3%A7%C3%A3o-890-GTIN-inexistente-no-Cadastro-Centralizado-de-GTIN-CCG-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/16869639272087-Rejei%C3%A7%C3%A3o-890-GTIN-inexistente-no-Cadastro-Centralizado-de-GTIN-CCG-nItem-999)  
> **ID:** `16869639272087` | **Última Atualização:** 2026-07-22T14:54:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16869639263383)

  MENSAGEM:**

GTIN inexistente no Cadastro Centralizado de GTIN (CCG) [nItem:999]

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16869645486615)

 CAUSA:**

A nota técnica informa que, para vendas de produção em estabelecimento onde os produtos utilizem NCM que consta no **Anexo I** da NT 2021.003_v1_10 e CFOP utilizado na operação esteja citado no **Anexo II** da mesma NT o GTIN (tag:cEAN) deve ser um valor válido no portal** CCG-Cadastro Centralizado de GTIN**,  caso contrário, acontecerá a rejeição. 

 **Anexo I** : 

![mceclip2.png](https://atendimento.tecnospeed.com.br/hc/article_attachments/8087753576855/mceclip2.png)

** Anexo II** :

![mceclip3.png](https://atendimento.tecnospeed.com.br/hc/article_attachments/8087822608023/mceclip3.png)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16869615346711)

 SOLUÇÃO:**
 

Para verificar o código GTIN informado no cadastro do produto é necessário realizar o passo a passo abaixo:

Acessar: Cadastro do produto
Aba: Imposto 
Campo: EAN/GTIN Produto p/ NF-e

Nele consta as opções onde poderá estar registrado o GTIN:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16868797024151)

Após realizar a correção do código é necessário redigitar o item da nota e gerar o lote. 
Caso não seja necessário informar o GTIN é necessário colocar no campo EAN/GTIN Produto p/ NF-e a opção não informar. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16921078378135)

 

📌 Em caso de dúvidas sobre as regras a serem aplicadas para o seu processo, consulte o seu contador. 

Segue os links para consultar o GTIN nacional e para consultar os códigos da Tabela Prefixo GS1

[https://dfe-portal.svrs.rs.gov.br/Nfe/Gtin](https://dfe-portal.svrs.rs.gov.br/Nfe/Gtin)

[https://www.gs1.org/standards/id-keys/company-prefix](https://www.gs1.org/standards/id-keys/company-prefix)