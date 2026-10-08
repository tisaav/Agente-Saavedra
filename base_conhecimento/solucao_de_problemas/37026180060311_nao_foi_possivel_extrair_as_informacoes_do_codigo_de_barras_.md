# Não foi possível extrair as informações do código de barras "" na posição [0, 5]

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37026180060311-N%C3%A3o-foi-poss%C3%ADvel-extrair-as-informa%C3%A7%C3%B5es-do-c%C3%B3digo-de-barras-na-posi%C3%A7%C3%A3o-0-5](https://ajuda.sankhya.com.br/hc/pt-br/articles/37026180060311-N%C3%A3o-foi-poss%C3%ADvel-extrair-as-informa%C3%A7%C3%B5es-do-c%C3%B3digo-de-barras-na-posi%C3%A7%C3%A3o-0-5)  
> **ID:** `37026180060311` | **Última Atualização:** 2026-07-22T14:22:02Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37026180040855)

 **MENSAGEM:**

Não foi possível extrair as informações do código de barras "" na posição [0, 5]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37026180042263)

SOLUÇÃO:**

O PDVWEB possui uma regra interna que interpreta **automaticamente** qualquer produto cuja **referência se inicia com o número ''2''** como um **item de balança**.

Isso significa que, nessas situações, o sistema passa a esperar que o código de barras do produto siga o padrão de balança (geralmente **EAN-13**), contendo informações como **peso ou valor**. Quando isso não ocorre, a validação falha e o erro é apresentado.

**Como corrigir:**

Se o produto não for um item de balança, siga o passo abaixo:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37035355302679)

 **Altere a referência do produto diretamente no cadastro, modificando-a para que não se inicie com o número **''2''**, evitando que o sistema interprete o item como um produto de balança.

Link: [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37026180043415)

CAUSA:**

O erro ocorre devido a um **comportamento padrão do PDVWEB**, relacionado à forma como o sistema interpreta os** códigos de barras dos produtos**.


---

### 🔗 Links e Referências Internas:

- [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047)