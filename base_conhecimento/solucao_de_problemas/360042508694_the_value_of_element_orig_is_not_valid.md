# The value '' of element 'orig' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042508694-The-value-of-element-orig-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042508694-The-value-of-element-orig-is-not-valid)  
> **ID:** `360042508694` | **Última Atualização:** 2026-07-22T16:10:14Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456482978839)

 **MENSAGEM:**

cvc-enumeration-valid: Value '' is not facet-valid with respect to enumeration '[0, 1, 2, 3, 4, 5, 6, 7, 8]'. It must be a value from the enumeration.
cvc-type.3.1.3: The value '' of element 'orig' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456497484823)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456482988695)

 Acesse a tela '"****[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)" (Caminho de acesso:* Configurações » Cadastros » Produtos*).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456482997655)

 Para todos os itens do lançamento, verifique  o campo** "Origem do Produto"**, localizado na aba "**Geral"**:

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456483004823)

 Preencha este campo com uma das opções abaixo, conforme origem correspondente ao respectivo item:

- 0- Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8;

- 1- Estrangeira - Importação direta, exceto a indicada no código 6;

- 2- Estrangeira - Adquirida no mercado interno, exceto a indicado no código 7;

- 3- Nacional - Mercadoria ou bem com conteúdo de importação superior a 40% e inferior ou igual a 70%;

- 4- Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos;

- 5- Nacional, mercadoria ou bem com conteúdo de importação inferior ou igual a 40% (quarenta por cento);

- 6- Estrangeira, Importação direta, sem similar nacional, constante em lista de Resolução CAMEX;

- 7- Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista de Resolução CAMEX;

- 8- Nacional - mercadoria ou bem com conteúdo de importação superior a 70% (setenta por cento);

 

![Captura_de_tela_2023-05-08_113639.png](https://ajuda.sankhya.com.br/hc/article_attachments/14440721916951)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456483007511)

 Preenchido o campo acima para todos os itens, redigite o cabeçalho da nota e gere um novo lote.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456483014423)

 **CAUSA:**

Mensagem apresentada quando existem itens lançados na nota com a informação 'Origem do Produto' (tag <orig>)em branco.


---

### 🔗 Links e Referências Internas:

- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)