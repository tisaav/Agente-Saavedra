# Produto não é consignado, não pode atualizar estoque de terceiros e próprio simultaneamente 

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579454-Produto-n%C3%A3o-%C3%A9-consignado-n%C3%A3o-pode-atualizar-estoque-de-terceiros-e-pr%C3%B3prio-simultaneamente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579454-Produto-n%C3%A3o-%C3%A9-consignado-n%C3%A3o-pode-atualizar-estoque-de-terceiros-e-pr%C3%B3prio-simultaneamente)  
> **ID:** `360043579454` | **Última Atualização:** 2026-07-22T16:01:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108331898391)

 MENSAGEM:**

ORA-20101: Produto não é consignado, não pode atualizar estoque de terceiros e próprio simultaneamente.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108331900695)

 SITUAÇÃO:**

Ao tentar confirmar uma nota de Compra, pelo **"Portal de Compras"** é retornada a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108331901975)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458155380887)

 Cenário 1:** Caso a atualização de estoque tenha que ser **"Atualizar Estoque Próprio e Estoque de Terceiro"**.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108364575383)

** Insira no campo **"Parceiro Consignante"** um valor correspondente ao Parceiro da Nota. O campo fica disponível na aba **"Geral"** no Cadastro de **"[Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** *(Caminho de acesso: Configurações » Cadastros » Produtos » Produtos)*.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458155380887)

 Cenário 2:** Caso a atualização de estoque não deve atualizar estoque próprio e de terceiro.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108364575383)

** Ajuste no cadastro da TOP *(Caminho para acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)* as atualizações:

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108331904279)

** Aba **"[Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)", **Campo "**Atualização do Estoque". **Para atualização de estoque próprio.

**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108331904279)

** Aba **"[Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoquedeterceiros)", **Campo **"Estoque com/de Terceiros". **Para atualização de estoque de Terceiro.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108364575383)

** Ajustar para atualizar somente uma das condições, de acordo com a movimentação da Nota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108364577559)

 CAUSA:**

Ocorre para movimentações de comodato, consignação ou produtos para produção externa, quando é necessário atualizar ambos os estoque e não possui parceiro consignante no(s) cadastro(s) do(s) produto(s).


---

### 🔗 Links e Referências Internas:

- [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)
- [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)
- [Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoquedeterceiros)