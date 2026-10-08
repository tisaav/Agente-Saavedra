# Um ou mais produtos da nota não possuem código de barras cadastrado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001885241-Um-ou-mais-produtos-da-nota-n%C3%A3o-possuem-c%C3%B3digo-de-barras-cadastrado](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001885241-Um-ou-mais-produtos-da-nota-n%C3%A3o-possuem-c%C3%B3digo-de-barras-cadastrado)  
> **ID:** `1500001885241` | **Última Atualização:** 2026-07-22T15:25:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287002070807)

 MENSAGEM**:

Um ou mais produtos da nota não possuem código de barras cadastrado. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287002074263)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286987447319)

 Acesse a Validação de Configuração do WMS em: *WMS » Rotinas » Validação de Configurações do WMS*

Filtro por:
Tipo de Validações: Produto

Clique no botão de filtro e selecione as opções:
[X] Produtos sem código de barras (Propriedades)
[X] Produtos sem código de barras (Unidade alternativa)

Clique em OK, depois 'Aplicar'.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360102952353)

 

O resultado, apresentara os produtos que estão com cadastros incompletos.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286987450775)

 Acesse o cadastro de Produtos em: *Configurações » Cadastros » Produtos » Produtos*
Aba: **"****Geral"**
Campo: **"Referência"**

Aba: **"****Unidade alternativa"
**Campo: **"Código de Barras"**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287002084631)

 Após os ajustes, efetue o envio para o recebimento novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16287002088471)

 CAUSA:**

Ocorre quando os produtos enviados para o recebimento não possuem código de barras, devidamente configurado.