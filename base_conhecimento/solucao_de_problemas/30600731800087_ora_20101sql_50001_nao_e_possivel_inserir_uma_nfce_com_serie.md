# ORA-20101/SQL-50001: Não e possivel inserir uma NFCe com serie e cod.empresa que ja estejam sendo utilizados por um Checkout

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30600731800087-ORA-20101-SQL-50001-N%C3%A3o-e-possivel-inserir-uma-NFCe-com-serie-e-cod-empresa-que-ja-estejam-sendo-utilizados-por-um-Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/30600731800087-ORA-20101-SQL-50001-N%C3%A3o-e-possivel-inserir-uma-NFCe-com-serie-e-cod-empresa-que-ja-estejam-sendo-utilizados-por-um-Checkout)  
> **ID:** `30600731800087` | **Última Atualização:** 2026-07-22T14:35:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30600685021591)

 **MENSAGEM:**

ORA-20101/SQL-50001: Não e possível inserir uma NFCe com serie e cod.empresa que ja estejam sendo utilizados por um Checkout. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30600731792023)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33355127754391)

 Na tela **''Central de Vendas''** (Comercial» Rotinas» Central de Vendas) verifique a série que está informada no **''Cabeçalho''**. Caso seja uma série utilizada no Sankhya Checkout, escolha outra série para a emissão do documento.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33355127757207)

 Caso seja necessário cadastrar uma nova série: 

- Acesse a tela **''Tipos de Operação - TOP''** (Comercial» Arquivo» Cadastros» Tipos de Operação - TOP).

- Filtre pela TOP que está sendo utilizada, clique no botão** "Outras opções"** >>** "Controle de Numeração"** e, no pop-up** "Controle de Numeração TOP"**, clique no botão **''Cadastrar Controle de Numeração (+)'' **para incluir um novo registro.   

 

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33355067209111)

Saiba mais sobre [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30600731793943)

 CAUSA:**

Ao utilizar o **Sankhya Checkout**, não é permitido utilizar a mesma série para vendas no** SankhyaOM** (Central de Vendas).

Essa validação foi implementada para prevenir erros de duplicidade de chave na emissão de documentos, uma vez que o Checkout possui um banco de dados distinto do SankhyaOM, não realizando a validação da numeração no SankhyaOM antes da emissão do documento.

As numerações são atualizadas posteriormente, durante o processo de sincronização dos dados de vendas do Checkout para o SankhyaOM.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...)