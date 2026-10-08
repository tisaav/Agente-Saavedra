# Nota com Valor Igual a Zero. Cancelando Operação

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579594-Nota-com-Valor-Igual-a-Zero-Cancelando-Opera%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579594-Nota-com-Valor-Igual-a-Zero-Cancelando-Opera%C3%A7%C3%A3o)  
> **ID:** `360043579594` | **Última Atualização:** 2026-07-22T16:01:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191888236311)

 MENSAGEM:**

[CORE_E04657] Nota com Valor Igual a Zero. Cancelando Operação.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191888238743)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191902295191)

 Acesse o cadastro da TOP que irá originar o lançamento *(*Caminho de acesso: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).*

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191888240919)

 Na aba **Geral** verifique a informação que consta no campo: **"Usar como preço"**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458142243095)

 Caso de Uso 1:**

- Caso esteja definido, por exemplo: **"Preço de Venda"**, é necessário o produto ter um Preço de Tabela.

- Para comprovar se esse preço existe, acesse a rotina **"[Variação de preços de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753)"** e filtre os respectivos produtos, analisando se algum desses não possui preço de venda.

- Utilize o processo de precificação atual da empresa para corrigir essa situação ou reveja a marcação da TOP.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458142243095)

 Caso de Uso 2:**

- Caso escolha por exemplo, **"Custo de Reposição"**, se faz necessário ter um registro de Custo de Reposição.

- Para comprovar se esse preço existe, acesse a rotina Variação de custos de produtos e filtre os respectivos produtos, analisando se algum desses não possui informações na coluna Custo de Reposição.

- Utilize o processo de atualizações de custo atual da empresa para corrigir essa situação ou reveja a marcação da TOP.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191888243735)

 Por fim, através da rotina "****[Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)" realize uma verificação do estoque atual dos produtos envolvidos, visto que essa mensagem pode ocorrer por ausência de estoque e solicitação de Baixar estoque da TOP utilizada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16191902303127)

 CAUSA:**

Ao realizar uma Devolução de Compra, a mensagem poderá ser apresentada nas seguintes situações:

- Quando não tem estoque do produto;

- Quando não possui registro de CUSTO ou Preço Unitário, de acordo com as definições da TOP de devolução.


---

### 🔗 Links e Referências Internas:

- [Variação de preços de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753)
- [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)