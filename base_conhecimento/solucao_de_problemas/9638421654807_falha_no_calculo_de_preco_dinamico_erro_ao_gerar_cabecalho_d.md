# Falha no cálculo de preço dinâmico Erro ao gerar cabeçalho de nota/pedido. SQL-50001 Tipo de Operação XX não está ativo na nota de Nro Único: XXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9638421654807-Falha-no-c%C3%A1lculo-de-pre%C3%A7o-din%C3%A2mico-Erro-ao-gerar-cabe%C3%A7alho-de-nota-pedido-SQL-50001-Tipo-de-Opera%C3%A7%C3%A3o-XX-n%C3%A3o-est%C3%A1-ativo-na-nota-de-Nro-%C3%9Anico-XXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/9638421654807-Falha-no-c%C3%A1lculo-de-pre%C3%A7o-din%C3%A2mico-Erro-ao-gerar-cabe%C3%A7alho-de-nota-pedido-SQL-50001-Tipo-de-Opera%C3%A7%C3%A3o-XX-n%C3%A3o-est%C3%A1-ativo-na-nota-de-Nro-%C3%9Anico-XXXX)  
> **ID:** `9638421654807` | **Última Atualização:** 2026-07-22T15:07:04Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363614770455)

 MENSAGEM:**

[CORE_E02294] Falha no cálculo de preço dinâmico Erro ao gerar cabeçalho de nota/pedido. SQL-50001 Tipo de Operação XX não está ativo na nota de Nro Único:XXXX.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363637529367)

SOLUÇÃO:**

Verifique o modelo vinculado no parâmetro **"****MODCALCPRECDIN"**. Localize o modelo na tela **"Modelo de Notas e Pedidos"** e identifique a TOP que consta no campo **"Tipo Operação", **avalie se ela realmente deveria estar sendo utilizada e proceda com a ativação pela tela Tipos de Operação - TOP ou altere a TOP do modelo para uma que esteja ativa.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363637530519)

CAUSA:**

Em sua maioria o erro apresenta devido ao parâmetro MODCALCPRECDIN estar preenchido com um Modelo de Notas e Pedidos que referencia uma TOP que estava desativada.