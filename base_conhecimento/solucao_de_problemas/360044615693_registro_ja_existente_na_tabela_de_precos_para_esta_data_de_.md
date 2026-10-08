# Registro já existente na Tabela de Preços para esta Data de Vigor

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615693-Registro-j%C3%A1-existente-na-Tabela-de-Pre%C3%A7os-para-esta-Data-de-Vigor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615693-Registro-j%C3%A1-existente-na-Tabela-de-Pre%C3%A7os-para-esta-Data-de-Vigor)  
> **ID:** `360044615693` | **Última Atualização:** 2026-07-22T15:54:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618221347863)

 MENSAGEM:**

[CORE_E01698]:  Registro já existente na Tabela de Preços para esta Data de Vigor.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618182800023)

 SOLUÇÃO:**

Valide se já existe **preço **para a Dt.Vigor/Tabela do item que a atualização está sendo realizada;

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458097926935)

 CASO DE USO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618221354391)

 Acesse a tela **"Atualização de preço de venda"** para atualização de preço do produto 16.

- Criado filtro Excecao.CODPROD = 16;

- Defina Data de Vigor (08/01/2019) e Data de atualização (08/01/2019);

- Ao aplicar, clique em **novo **e insira um novo preço para esse produto;

- Apresentada mensagem de erro: Registro já existente na Tabela de Preços para esta Data de Vigor;

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618182807191)

 MOTIVO:**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618221367959)

 Ao filtrar o produto 16, definir a data de vigor e aplicar, já existe um registro de preço para esse produto na Data de Vigor 08/01/2019, dessa forma uma nova inserção não é aceita:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14874209616791)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618182810903)

 Se o novo preço for vigorar em data posterior, ajuste a Data de Vigor do filtro apresentado na tela e, após isso, realize a atualização.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618182813847)

 Caso de fato necessite de ajustar o preço já existente para essa data de vigor, aconselha-se atenção no processo, visto que preços ajustados mais que uma vez na mesma data não trata-se de melhor prática, pois o registro de preços será "perdido".

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618182816151)

CAUSA:**

Ao tentar inserir um preço de venda para itens que já possuem registro na respectiva data de vigor/tabela, será apresentada a mensagem.