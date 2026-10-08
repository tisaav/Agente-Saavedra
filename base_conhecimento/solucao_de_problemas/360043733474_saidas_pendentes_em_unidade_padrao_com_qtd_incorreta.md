# Saídas pendentes em unidade padrão com qtd. incorreta

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733474-Sa%C3%ADdas-pendentes-em-unidade-padr%C3%A3o-com-qtd-incorreta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733474-Sa%C3%ADdas-pendentes-em-unidade-padr%C3%A3o-com-qtd-incorreta)  
> **ID:** `360043733474` | **Última Atualização:** 2026-07-22T15:59:18Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198957187223)

 MENSAGEM:**

[Erro: SQL-50001] Saídas pendentes em unidade padrão com qtd. incorreta.
Produtos: xxx Endereço:xxx Unidades:xx Saidas pendentes:x.xxxx.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198957190807)

 SITUAÇÃO:**

Ao enviar uma OC(Ordem de Carga), para expedição(WMS), pela Rotina Formação de Carga, ocorre a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198957193879)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198957197207)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*, aba **Geral**, preencha o Campo: **"Unidade Padrão".**

 

![produtos.png](https://ajuda.sankhya.com.br/hc/article_attachments/14499206758935)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198941903255)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*, aba **WMS**, e cadastre o Endereçamento (Ter um registro da Unidade UN).

 

![produtos2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14499213563159)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198941905687)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*, aba **Unidades Alternativas **e realize um registro da Unidade maior que a Unidade Padrão.

 

![produtos3.png](https://ajuda.sankhya.com.br/hc/article_attachments/14499264636183)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16198957204759)

 C****AUSA**

Para evitar que este erro aconteça é necessário configurar a unidade do produto no picking com a menor unidade, a qual geralmente é a unidade padrão.

**Não** configurar Unidade Alternativa do produto no Picking.