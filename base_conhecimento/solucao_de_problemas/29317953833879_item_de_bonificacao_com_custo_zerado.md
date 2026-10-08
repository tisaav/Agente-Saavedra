# Item de Bonificação com custo zerado

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/29317953833879-Item-de-Bonifica%C3%A7%C3%A3o-com-custo-zerado](https://ajuda.sankhya.com.br/hc/pt-br/articles/29317953833879-Item-de-Bonifica%C3%A7%C3%A3o-com-custo-zerado)  
> **ID:** `29317953833879` | **Última Atualização:** 2026-07-22T14:37:16Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29317921327255)

 **MENSAGEM:**

Item de bonificação com custo zerado.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29317953819159)

SOLUÇÃO:**

Quando é realizado um primeiro lançamento gerador de custos de itens bonificados, onde o **Tipo de Operação -TOP** *(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)* está com a marcação Bonificação realizada ("TGFTOP.BONIFICACAO = S"), o sistema irá calcular somente os Custos médio, todos os outros custos são copiados da referência anterior, pois a bonificação apenas modifica a quantidade do produto e não seu custo.

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/29317953817495)

**

 

Quando não houver custos na referência anterior, o sistema irá imputar os valores de custo zerado. Nesse caso é necessário verificar se a TOP utilizada está correta e verificar a melhor prática para essa operação na sua empresa.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/29567940986135)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29317953821335)

CAUSA:**

Ocorre quando é realizado lançamento de compra onde a TOP está configurada para atualizar custo e o campo bonificação está marcado, e os produtos lançados na nota não possuem custo anterior.