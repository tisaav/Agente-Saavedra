# Ao salvar o item na central de vendas o mesmo some da tela

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26406302009367-Ao-salvar-o-item-na-central-de-vendas-o-mesmo-some-da-tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/26406302009367-Ao-salvar-o-item-na-central-de-vendas-o-mesmo-some-da-tela)  
> **ID:** `26406302009367` | **Última Atualização:** 2026-07-22T14:42:16Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26431874245399)

 **SITUAÇÃO:**

Ao salvar o item na central de vendas o mesmo some da tela, mas o valor é somado no total da nota.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26406324189975)

SOLUÇÃO:**

Acesse a tela **"Preferências"** *(Caminho: Configurações » Avançado » Preferências) *e marque o parâmetro  **"TEMMPVENDA"**= 'S'. Esse problema acontece também nas telas de Transferência, requisição e Central de atendimento ao Fornecedor.

Central de compras:  Parâmetro '**TEMMPCOMPRA**'

Central de Mov. Internas (Requisição) :  Parâmetro '**TEMMPREQ**'

Central de Mov. Internas (Transferência):  Parâmetro '**TEMMPTRAN**'

 

 

 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/26406301986199)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26406324195735)

CAUSA:**

Esse problema acontece por que no cadastro do produto o campo 'Usado como'  está como matéria prima e o parâmetro TEMMPVENDA está desligado.  Se for na central de Compras o parâmetro **TEMMPCOMPRA = **'Desligado**'** Se for na tela de Requisição o parâmetro **TEMMPREQ = 'Desligado' **se for na Tela de Transferência o parâmetro **TEMMPTRAN = 'Desligado'**