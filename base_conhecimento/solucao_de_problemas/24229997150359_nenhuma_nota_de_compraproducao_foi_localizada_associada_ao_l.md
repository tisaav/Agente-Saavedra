# Nenhuma Nota de compra/produção foi localizada associada ao lote informado

> **Módulo:** Solucao de Problemas | **Subseção:** Produção  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/24229997150359-Nenhuma-Nota-de-compra-produ%C3%A7%C3%A3o-foi-localizada-associada-ao-lote-informado](https://ajuda.sankhya.com.br/hc/pt-br/articles/24229997150359-Nenhuma-Nota-de-compra-produ%C3%A7%C3%A3o-foi-localizada-associada-ao-lote-informado)  
> **ID:** `24229997150359` | **Última Atualização:** 2026-07-24T12:42:34Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24230000900503)

 **MENSAGEM:**

[CORE_E03584] Nenhuma Nota de compra/produção foi localizada associada ao lote informado

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24230000901783)

 **SOLUÇÃO: **

**Observação: **Não é possível fazer um lançamento avulso de amostra, pois o sistema exige que o produto tenha estoque disponível da amostra para fazer a baixa na requisição configurada no parâmetro **"****MODREQAMOSTRAS"**. O processo de Controle de Qualidade de materiais inicia-se com a um movimento que faça a entrada do produto no estoque.

Caso o produto já tenha dado entrada com uma nota antiga, verifique como está a configuração do parâmetro: **"DIASBUSCALOTE - Qtde.Dias"** para busca de lotes em amostras. Esse parâmetro define a quantidade de dias entre os quais acontecerá a busca dos lotes nas notas, se a nota for anterior ao dias configurados ele não localiza o lote.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/24229997148055)

**CAUSA:**

A mensagem é apresentada ao tentar gerar uma amostra manual de um produto que não tem estoque disponível.