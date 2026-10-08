# O valor do campo orig (origem da mercadoria: 0 - Nacional 1 - Estrangeira - Importação direta 2 - Estrangeira - Adquirida no mercado interno) informado não é valido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/18863018746263-O-valor-do-campo-orig-origem-da-mercadoria-0-Nacional-1-Estrangeira-Importa%C3%A7%C3%A3o-direta-2-Estrangeira-Adquirida-no-mercado-interno-informado-n%C3%A3o-%C3%A9-valido](https://ajuda.sankhya.com.br/hc/pt-br/articles/18863018746263-O-valor-do-campo-orig-origem-da-mercadoria-0-Nacional-1-Estrangeira-Importa%C3%A7%C3%A3o-direta-2-Estrangeira-Adquirida-no-mercado-interno-informado-n%C3%A3o-%C3%A9-valido)  
> **ID:** `18863018746263` | **Última Atualização:** 2026-07-22T14:52:02Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18863010271255)

 **MENSAGEM:**

[CORE_E04895] O valor do campo orig (origem da mercadoria: 0 - Nacional
1 - Estrangeira - Importação direta
2 - Estrangeira - Adquirida no mercado interno) informado não é
valido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18863018720663)

SOLUÇÃO:**

Pegue o XML para conferência no botão "NF-e" opção "Gerar XML da NF-e em arquivo para conferência" no portal e após baixado precisa localizar o produto que conta com a Tag <orig> vazia. 

Após localizar o produto, basta entrar no cadastro do mesmo (Tela de Produtos) e classificar o campo "Origem do Produto", localizado na aba "Geral" conforme desejado. 

 

![produtos 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19142036381975)

 

Após a alteração, redigite algo na nota e gere o lote novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18863002208407)

CAUSA:**

Ocorre quando não é classificado a origem do produto no cadastro, pois no XML a tag <orig> fica vazia e apresenta a mensagem de erro.

![xml 17-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19142057235735)