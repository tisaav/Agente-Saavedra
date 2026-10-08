# Modelo de nota para ajuste de Entrada de estoque não existe ou está incorreto. Verifique o cadastro da empresa ou o parâmetro "NOTASAIAJUSTEST"

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045582733-Modelo-de-nota-para-ajuste-de-Entrada-de-estoque-n%C3%A3o-existe-ou-est%C3%A1-incorreto-Verifique-o-cadastro-da-empresa-ou-o-par%C3%A2metro-NOTASAIAJUSTEST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045582733-Modelo-de-nota-para-ajuste-de-Entrada-de-estoque-n%C3%A3o-existe-ou-est%C3%A1-incorreto-Verifique-o-cadastro-da-empresa-ou-o-par%C3%A2metro-NOTASAIAJUSTEST)  
> **ID:** `360045582733` | **Última Atualização:** 2026-07-22T15:33:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538629287959)

 MENSAGEM:**

[INV_E00003]  Modelo de nota para ajuste de Entrada de estoque não existe ou está incorreto. Verifique o cadastro da empresa ou o parâmetro "**NOTASAIAJUSTEST**". Nro modelo:

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538645804951)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538629294999)

 Acesse a tela "**Modelo de Notas e Pedidos"  ***(Caminho de acesso: Comercial » Consulta)*:

- Nesta tela são cadastrados os Modelos que serão utilizados com os dados padrões do lançamento das respectivas notas de ajuste. 

- Necessário o cadastro de um modelo de 'Ajuste de Entrada' e outro modelo de 'Ajuste de Saída'.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538645808407)

 O cadastro acima irá gerar 'Nro único' para cada modelo criado e tais números deverão ser inseridos conforme necessidade a seguir:

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28454031797911)

Modelo por empresa:**

Se for utilizar um modelo para cada empresa, preencha os campos **"Modelo Ajuste de Entrada de Estoque"** ou **"Modelo Ajuste de Saída de Estoque",** da aba **"Estoque/Preço"** da tela **"Empresa*****"** (Caminho de acesso: Financeiro » Preferências)*:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15470445464087)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28454031797911)

 Modelo Único:**

Se for utilizar um modelo único, configure os parâmetros abaixo, informando os modelos gerados conforme item 1:

Tela **"Preferências"** *(Caminho de acesso: Configurações » Avançado):*

- **"Nota Modelo Ajuste Estoque (Entrada) - NOTAENTAJUSTEST";**

- **"Nota Modelo Ajuste Estoque (Saída) - NOTASAIAJUSTEST".**

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538645811991)

 O sistema irá primeiramente buscar o modelo da empresa, caso não o encontre configurado na empresa, ele buscará o modelo do parâmetro. Se não conseguir encontrar o modelo em nenhum lugar, será apresentada a mensagem de validação.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538645814423)

 CAUSA:**

Ao tentar realizar ajuste de estoque, caso o sistema não localize os modelos de notas e pedidos para esse ajuste, será apresentada a mensagem.