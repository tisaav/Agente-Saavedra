# Não é possível alterar o parceiro de movimentos originados do estoque

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15471992049559-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-o-parceiro-de-movimentos-originados-do-estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/15471992049559-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-o-parceiro-de-movimentos-originados-do-estoque)  
> **ID:** `15471992049559` | **Última Atualização:** 2026-07-22T14:56:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538383562519)

 MENSAGEM:**

[CORE_E02420]: Não é possível alterar o parceiro de movimentos originados do estoque.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538411881751)

 CAUSA:**

Ocorre quando o parâmetro **"Proíbe a troca de parceiro em financeiro de nota? - PROIBTRCPARFIN" **está ligado e há tentativa de alterar o parceiro do lançamento.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538411865751)

 SOLUÇÃO:**

Em algumas situações podem ser necessárias algumas modificações nos títulos na **"Movimentação Financeira",** mesmo que estes tenham sido originados das Centrais (campo Origem = Estoque); tal comportamento é controlado pelos parâmetros **"Qdo originado da Central não permitir alterar nada - ALTERAFIN"** e **"Proíbe a troca de parceiro em financeiro de nota? - PROIBTRCPARFIN"** da seguinte maneira:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538383571863)

 Se o parâmetro Qdo originado da Central não permitir alterar nada - ALTERAFIN for habilitado, será feito o bloqueio de qualquer alteração nos títulos que tiveram origem nas Centrais;

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538383574807)

 **OBSERVAÇÃO:**

O parâmetro mencionado acima não será aplicado quando as funcionalidades do botão **"Baixar"** forem utilizadas (tela ****["Movimentação Financeira - Baixa de Títulos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534)).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538383579287)

 Caso o parâmetro Qdo originado da Central não permitir alterar nada -ALTERAFIN seja desabilitado e o parâmetro Proíbe a troca de parceiro em financeiro de nota? - PROIBTRCPARFIN for habilitado, será feito o bloqueio de modificações nos títulos de origem nas Centrais, nos seguintes campos:

 

| Vlr do Desdobramento; | Tipo Operação; |
| --- | --- |
| Dt. Negociação; | Receita/Despesa; |
| Empresa; | Provisão; |
| Moeda; | Vlr Moeda; |
| Parceiro. |  |

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16538411878551)

 Com ambos os parâmetros desligados, teremos o bloqueio de alterações nos títulos originados das Centrais, nos seguintes campos:

 

| Vlr do Desdobramento; | Tipo Operação; |
| --- | --- |
| Dt. Negociação; | Receita/Despesa; |
| Empresa; | Provisão; |
| Moeda; | Vlr Moeda. |


---

### 🔗 Links e Referências Internas:

- ["Movimentação Financeira - Baixa de Títulos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534)