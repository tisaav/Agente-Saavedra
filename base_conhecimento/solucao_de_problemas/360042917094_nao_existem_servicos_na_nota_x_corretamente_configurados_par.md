# Não existem serviços na nota 'X' corretamente configurados para a emissão da Nota Fiscal Eletrônica de Serviços

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042917094-N%C3%A3o-existem-servi%C3%A7os-na-nota-X-corretamente-configurados-para-a-emiss%C3%A3o-da-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7os](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042917094-N%C3%A3o-existem-servi%C3%A7os-na-nota-X-corretamente-configurados-para-a-emiss%C3%A3o-da-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7os)  
> **ID:** `360042917094` | **Última Atualização:** 2026-07-22T16:05:01Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117005029527)

 MENSAGEM:**

[CORE_E00576] Não existem serviços na nota 'X' corretamente configurados para a emissão da Nota Fiscal Eletrônica de Serviços.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117034980247)

 SITUAÇÃO:**

Mensagem apresentada na emissão de nota fiscal de serviço.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117034983319)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117034987287)

 Certifique-se que os itens inseridos na nota foram cadastrados na tela **"Serviço"** (Caminho de acesso: Configurações » Cadastros » Produtos » Serviços):

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/12069677724439)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117005042711)

 Caso o cadastro tenha sido realizado na tela **"Produtos"**, a emissão de NFS-e não será permitida, visto que será validado o **"USOPROD = 'S'"**. Realizado o cadastro corretamente, refaça o lançamento. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117005046167)

 CAUSA:**

Mensagem apresentada na emissão de nota fiscal de serviços quando o 'Usado como' do produto difere de 'Serviço'.