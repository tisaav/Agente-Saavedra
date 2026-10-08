# Para definir o Código da FCI a origem do produto (ORIGPROD) deve ser definida entre 3, 5 ou 8. Produto: 'X'

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043578514-Para-definir-o-C%C3%B3digo-da-FCI-a-origem-do-produto-ORIGPROD-deve-ser-definida-entre-3-5-ou-8-Produto-X](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043578514-Para-definir-o-C%C3%B3digo-da-FCI-a-origem-do-produto-ORIGPROD-deve-ser-definida-entre-3-5-ou-8-Produto-X)  
> **ID:** `360043578514` | **Última Atualização:** 2026-07-22T16:01:40Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106529445399)

 MENSAGEM:**

SQL-50001 Para definir o Código da FCI a origem do produto(ORIGPROD) deve ser definida entre 3, 5 ou 8. Produto: 'X'.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106552366743)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106537285143)

 Abra o XML que está sendo importado (Bloco de Notas e/ou Internet Explorer) e verifique para os respectivos itens qual o valor informado na **tag <orig>**, conforme imagem abaixo:

 

![62.png](https://ajuda.sankhya.com.br/hc/article_attachments/14507299367063)

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106537297431)

 **Acesse a tela "****[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)" *(Caminho de acesso: Configurações » Cadastros » Produtos )* e confira se os itens cadastrados no sistema, que estão relacionados aos itens do XML, contém a mesma informação de 'Origem do produto'.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106565286807)

 Exemplo:**

Para o produto do XML exemplificado acima o campo **"Origem do Produto"**, aba **"Geral"** será cadastrado:** 5**, respeitando a tag <orig>5</orig>.

 

![origem_produto_nacional.png](https://ajuda.sankhya.com.br/hc/article_attachments/14507266966551)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106537300119)

 **Feito o ajuste, teste a importação do XML novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16106537301399)

 CAUSA:**

Na importação de XML, a mensagem será apresentada quando os produtos do XML, que possuem vínculos com os produtos do sistema, estão com a origem do Produto diferente de 3, 5 ou 8.


---

### 🔗 Links e Referências Internas:

- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)