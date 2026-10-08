# Rastreamento de Estoque de ICMS ST utilizando Unidade Alternativa

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35308460104599-Rastreamento-de-Estoque-de-ICMS-ST-utilizando-Unidade-Alternativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/35308460104599-Rastreamento-de-Estoque-de-ICMS-ST-utilizando-Unidade-Alternativa)  
> **ID:** `35308460104599` | **Última Atualização:** 2026-07-22T14:25:31Z

---

A **melhor prática em sistemas de gestão (ERP, fiscal e estoque)** é sempre cadastrar a **unidade padrão do produto como a menor unidade de controle**. Pelos seguintes motivos: 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687036238103)

 Precisão:** evita arredondamentos e perdas na conversão para múltiplos maiores.

- 

Exemplo:

  - 

Unidade padrão = **UN** (1 peça).

  - 

Unidade alternativa = **CX** com 12 UN.

  - 

Se a unidade padrão fosse **CX**, seria necessário frações (0,0833 CX = 1 UN), gerando imprecisão.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687036238103)

 Flexibilidade:** a partir da menor unidade é possível criar qualquer unidade alternativa, seja maior ou menor.

- 

Exemplo:

  - 

Padrão = **UN**.

  - 

Alternativas = **DUZIA = 12 UN**, **PACOTE = 50 UN** etc.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687036238103)

 Consistência fiscal:** documentos fiscais como NF-e e SPED trabalham com unidade de comercialização e unidade de estoque.

- 

Com a menor unidade na base, não há risco de destacar valores fracionados incorretos.

**Importante:** Para que o sistema calcule corretamente a unidade alternativa, ele **sempre parte da unidade padrão**.

 

### **Exemplo Prático: **

#### **Unidade Padrão x Alternativa**

- 

**Produto cadastrado:**

  - 

Unidade padrão: **KG** (Quilograma).

  - 

Unidade alternativa: **LT** (Lata).

- 

**Configuração:**

  - 

1 Lata = 20 KG.

  - 

Fator de conversão: **1 LT → 20 KG**.

- 

Na tela **"Produtos",** aba **"Geral",** campo **"Unidade Padrão" **selecione a opção "**KG Quilograma"**

 

![Rastreamento de Estoque de ICMS ST utilizando Unidade 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687771873943)

 

- 

Na mesma tela, aba **"Unidade Alternativa", **cadastre uma unidade alternativa de acordo com o produto cadastrado (fazendo as devidas conversões) 

 

![Rastreamento de Estoque de ICMS ST utilizando Unidade 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687776247319)

 

#### **Entrada de Mercadoria (Central de Compras)**

- 

Compra realizada: **60 KG**.

- 

Com **ICMS ST destacado** com **CST 010**.

- 

Valor total de ST destacado: **1.185,30**.

- 

Valor de ST por KG: **19,75**.

 

![Rastreamento de Estoque de ICMS ST utilizando Unidade 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687771875991)

 

Essa informação alimenta a tabela **TGFITS**, que registra os saldos de estoque de ICMS ST, para amparar as futuras saídas.

 

![Rastreamento de Estoque de ICMS ST utilizando Unidade 4.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687771877399)

 

#### **Saída de Mercadoria (Central de Vendas)**

- 

Venda realizada: **1 Lata**.

- 

Conversão aplicada: **1 LT = 20 KG**.

- 

Valor de ST calculado:

  - 

ST por KG = 19,75.

  - 

19,75 × 20 = **395,10** (valor de ST consumido da TGFITS).

 

![Rastreamento de Estoque de ICMS ST utilizando Unidade 5.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687771878167)

 

Obedecendo o fator de conversão, o sistema saiu com 20KG = 1LT

 

![Rastreamento de Estoque de ICMS ST utilizando Unidade 6.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687776253463)

![Rastreamento de Estoque de ICMS ST utilizando Unidade 7.png](https://ajuda.sankhya.com.br/hc/article_attachments/35687776254615)

 

#### **Conclusão**

Ao cadastrar a menor unidade como **unidade padrão**, o sistema consegue:

- 

Garantir precisão na rastreabilidade do ICMS ST;

- 

Calcular corretamente o valor proporcional nas saídas;

- 

Evitar inconsistências fiscais e erros de arredondamento;

Para detalhes sobre as configurações de rastreabilidade, consulte o manual oficial: [Rastreabilidade de Estoque ICMS ST – Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/5818008318231-Rastreabilidade-de-Estoque-ICMS-ST)


---

### 🔗 Links e Referências Internas:

- [Rastreabilidade de Estoque ICMS ST – Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/5818008318231-Rastreabilidade-de-Estoque-ICMS-ST)