# Um erro aconteceu quando tentou inicializar o Borland Database Engine (error $2501)

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111414-Um-erro-aconteceu-quando-tentou-inicializar-o-Borland-Database-Engine-error-2501](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111414-Um-erro-aconteceu-quando-tentou-inicializar-o-Borland-Database-Engine-error-2501)  
> **ID:** `360044111414` | **Última Atualização:** 2026-09-22T18:35:06Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664456194327)

 MENSAGEM:**

Um erro aconteceu quando tentou inicializar o Borland Database Engine (error $2501).

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664456200471)

 SITUAÇÃO:**

Ao tentar acessar algum módulo Delphi do sistema, é retornado o erro.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664479893399)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664456208407)

 Finalize todos os aplicativos que utilizam o BDE. Exemplo: MGe Controle de Produção, MGe Contabilidade, MGe Produção, etc.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664479906967)

 **No Menu Iniciar da máquina busque por 'BDE'. Localizado o ícone, clique com botão direito do mouse: Executar como Administrador

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18664479912727)

 Aberto o BDE, execute os ajustes abaixo:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458083429271)

 Aba: Database

- 
**BLOB SIZE**: 999 (máximo)

- 
**BLOBS TO CACHE**: 2048

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458083429271)

 Aba "Configuration" >> [+] Configuration >> [+] System >> [+] INIT

- 
**SHAREDMEMLOCATION:** 5BDE

- 
**SHAREDMEMSIZE**: 8196

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18864461898647)

 IMPORTANTE: **

Caso o BDE não exista na máquina, será necessário a instalação do mesmo. Esse serviço não é realizado pelo Service Desk Especializado, sendo necessário o direcionamento de um chamado para a Unidade responsável.