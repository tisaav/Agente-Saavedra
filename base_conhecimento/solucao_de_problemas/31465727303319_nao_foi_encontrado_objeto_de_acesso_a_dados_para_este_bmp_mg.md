# Não foi encontrado objeto de acesso a dados para este BMP: mge-dwf:NFSENAT

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/31465727303319-N%C3%A3o-foi-encontrado-objeto-de-acesso-a-dados-para-este-BMP-mge-dwf-NFSENAT](https://ajuda.sankhya.com.br/hc/pt-br/articles/31465727303319-N%C3%A3o-foi-encontrado-objeto-de-acesso-a-dados-para-este-BMP-mge-dwf-NFSENAT)  
> **ID:** `31465727303319` | **Última Atualização:** 2026-07-22T14:32:59Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31465715889175)

 **MENSAGEM:**

Não foi encontrado objeto de acesso a dados para este BMP: mge-dwf:NFSENAT

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31465727293335)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36803475731351)

 Acesse a tela ****[''Tipo de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36803461381399)

 Na aba **''NFS-e'', **desmarque** **o campo **''NFS-e por natureza''**, conforme a imagem abaixo:

 

![mceclip1 (2).png](https://ajuda.sankhya.com.br/hc/article_attachments/36803461383447)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36803461384215)

 Após desmarcar essa opção, gere uma nova nota ou duplique a existente, pois esse campo possui caráter histórico e não é atualizado retroativamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/31465715891479)

CAUSA:**

O erro ocorre devido à marcação **“NFS-e por natureza”**.

Quando essa opção está habilitada, o sistema tenta localizar informações na tabela adicional **NFSENAT**, utilizada por algumas prefeituras.

Como essa tabela não existe no ambiente em questão, o sistema não encontra os dados necessários e retorna a mensagem de erro.


---

### 🔗 Links e Referências Internas:

- [''Tipo de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)