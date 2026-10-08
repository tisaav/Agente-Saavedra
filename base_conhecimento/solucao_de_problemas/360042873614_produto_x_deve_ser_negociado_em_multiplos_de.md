# Produto 'X' deve ser negociado em múltiplos de ' '

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042873614-Produto-X-deve-ser-negociado-em-m%C3%BAltiplos-de](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042873614-Produto-X-deve-ser-negociado-em-m%C3%BAltiplos-de)  
> **ID:** `360042873614` | **Última Atualização:** 2026-07-22T16:05:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575109655)

 MENSAGEM:**

[CORE_E03246] Produto 'X' deve ser negociado em múltiplos de ' '.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109586506519)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575114519)

 Necessário que o campo **"Quantidade"** respeite a configuração abaixo, realizada no cadastro do respectivo item:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575116695)

 Tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** *(Caminho de acesso: Configurações » Cadastros » Produtos)*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575116695)

 Aba **"Medidas e estoque"** » **"Estoque" **» Campo** "Agrupamento Mínimo"**:

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14548961124759)

 

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575116695)

 O campo** agrupamento mínimo** comporta os dados pertinentes ao agrupamento mínimo para a venda ou compra do produto, ou seja, a negociação desse produto só poderá ser feita com quantidades múltiplas do valor (4 casas decimais) informado nesse campo.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575116695)

 Informando no campo Agrupamento mínimo o valor 0 (zero), será aceita qualquer quantidade na compra;

**Vejamos um exemplo:**

Tem-se o produto Ovo com sua Unidade padrão = unidade, é definido um agrupamento mínimo de 12 para o mesmo. Na inserção do item na nota, o campo "Quantidade" deverá ser preenchido com um múltiplo de 12.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458169722135)

 IMPORTANTE:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575116695)

********************

**[Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-)**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575116695)

**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575116695)

**

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575116695)

********[78 - Liberação de agrupamento mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#78-liberaodeagrupamentomnimo)******

| Essa validação pode ser controlada por Tipo de Operação, conforme marcação "Valida agrupamento mínimo?" da tela "Tipos de Operação - TOP"(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba "Estoque": Valida agrupamento mínimo?:Por meio deste campo, define-se qual validação será executada de acordo com o agrupamento mínimo definido no "", aba Medidas e estoque. São apresentadas as seguintes opções:  Não valida: Esta opção caracteriza que o agrupamento mínimo não será validado;  Valida e bloqueia: Com esta opção selecionada, caso haja algum item negociado com a quantidade que não respeite o agrupamento mínimo e efetuado o bloqueio deste lançamento;  Valida e exige liberação: Esta opção funciona de forma semelhante a opção anterior, sendo que ao invés de ocorrer o bloqueio, será solicitada a liberação do evento "" para que um usuário com alçada autorize o lançamento. |
| --- |

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16109575118871)

 CAUSA:**

Mensagem apresentada ao realizar movimentações no sistema inserindo no campo 'quantidade' um valor que não seja múltiplo do valor definido como agrupamento mínimo.


---

### 🔗 Links e Referências Internas:

- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-)
- [78 - Liberação de agrupamento mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#78-liberaodeagrupamentomnimo)