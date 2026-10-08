# Dashboard auxiliar do BLOCO K

> **Módulo:** Fiscal e Contábil | **Subseção:** Escrituração dos livros  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159-Dashboard-auxiliar-do-BLOCO-K)  
> **ID:** `4411588603159` | **Última Atualização:** 2026-09-15T14:42:24Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313173992471)

**

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313157862935)

****
```

| Módulo: Configurações>Controle de Acesso RemotoVersão disponível: A partir da 4.11 |
| --- |

Por meio desta tela, você pode realizar a conferência de forma detalhada das informações pertinentes a geração do Bloco K da EFD ICMS/IPI, por exemplo, a quantidade de produtos e insumos utilizados na produção, quais produtos foram produzidos, entre outras.  

Inicialmente, é necessário informar no Painel de Filtros a **"Empresa"** e o **"Período" **dos registros que deseja visualizar. A **"Data inventário"** deve ser preenchida apenas para o registro K200 - Estoque Escriturado.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411589574167)

Ainda no Painel de Filtros, você pode definir qual o **"Status Ordem de Produção"** que serão exibidos os registros, conforme as seguintes marcações: 

- Todas;

- OP Iniciadas e Concluídas no Período de Apuração;

- OP Iniciadas e não Concluídas no Período de Apuração;

- OP Iniciadas em Período Anterior e Concluídas no Período de Apuração;

- OP Iniciadas em Período Anterior e não Concluídas no Período de Apuração.

Com os filtros configurados, acione o botão **"Atualizar"**, assim, ao clicar em cada registro serão apresentadas as informações pertinentes a ele. Trataremos a seguir, sobre cada um:

[K200 - Estoque Escriturado](#K200-EstoqueEscriturado)

[K230 - Produção Própria - Itens Produzidos](#K230-Produ%C3%A7%C3%A3oPr%C3%B3pria-ItensProduzidos)

[K210 - Desmontagem de mercadoria - Item de Origem](#K210-Desmontagemdemercadoria-ItemdeOrigem)  

[K250 - Industrialização efetuada por terceiros](#K250-Industrializa%C3%A7%C3%A3oefetuadaporterceiros)

[K280 - Correção de Apontamento - Estoque Escriturado](#K280-Corre%C3%A7%C3%A3odeApontamento-EstoqueEscriturado)

#### 
**K200 - Estoque Escriturado**

O registro K200- Estoque Escriturado apresenta o saldo em estoque de cada produto no último dia do período de apuração do Bloco K. Clicando em uma linha, serão apresentados no painel inferior os detalhes do registro K200 - Estoque escriturado - Detalhado por Posse.

![k200_registro.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4411692795543)

Lembrando que este registro será gerado após a execução da Cópia e Contagem de estoque (Processo de inventário). Para isso, é necessário ligar o parâmetro **"GERAK200CTE"**, que habilitará na tela [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263), aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263#abaconfigura%C3%A7%C3%B5es), o campo **"****Data da contagem p/ K200" **onde você deverá informar a data da contagem. Caso o parâmetro esteja desligado, será considerado o estoque que consta no último dia da geração do SPED Fiscal da referência em questão. 

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411604222103)

[[voltar ao topo]](#comosfiltros)

#### 
**K230 - Produção Própria - Itens Produzidos**

No painel superior serão apresentadas as informações do registro K230 - Produção Própria - Itens produzidos, isto é, os dados da produção acabada de um produto em processo e finalizado. Ao clicar sobre um registro, no painel inferior serão exibidos os detalhes do registro K235 - Produção Própria -Insumos consumidos referentes ao consumo do insumo (MP).

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411682198551)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451059495959)

 Ao clicar duas vezes sobre um registro o sistema irá direcioná-lo a tela Ordens de Produção - Nova, onde você poderá verificar as informações pertinentes ao registro indicado.

[[voltar ao topo]](#comosfiltros)

#### 
**K210 - Desmontagem de mercadoria - Item de Origem**

Neste painel, temos os detalhes referentes ao registro K210 - Desmontagem de mercadorias - Item de origem, que tem o objetivo de escriturar a desmontagem de mercadorias dos tipos, por exemplo, matéria-prima, embalagem, entre outras. Ao clicar sobre um registro, no painel inferior serão apresentadas as informações relacionadas ao registro K215 - Desmontagem de mercadorias - Item de destino, que possui a finalidade de escriturar a desmontagem (com ou sem ordem de serviço) de mercadorias.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411688261015)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451059495959)

 Ao clicar duas vezes sobre um registro o sistema irá direcioná-lo a tela Ordens de Produção - Nova, onde você poderá verificar as informações pertinentes ao registro indicado.

[[voltar ao topo]](#comosfiltros)

#### 
**K250 - Industrialização efetuada por terceiros**

No painel superior serão exibidas as informações do registro K250 - Industrialização efetuada por terceiros - itens produzidos, isto é, os produtos que foram industrializados por terceiros e sua respectiva quantidade. Ao clicar sobre um registro, no painel inferior temos os dados detalhados do registro K255 - Industrialização efetuada por terceiros - itens consumidos.

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411688304791)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451059495959)

 Ao clicar duas vezes sobre um registro o sistema irá direcioná-lo a tela Ordens de Produção - Nova, onde você poderá verificar as informações pertinentes ao registro indicado.

[[voltar ao topo]](#comosfiltros)

#### 
**K280 - Correção de Apontamento - Estoque Escriturado**

Neste painel, temos os detalhes do registro K280 - Correção de Estoque Escriturado, que tem o objetivo de escriturar a correção de apontamento do Registro K200.

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411688455703)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28451059495959)

 Clicando duas vezes sobre um registro o sistema irá direcioná-lo a [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), exibindo a nota que foi realizado o ajuste.

[[voltar ao topo]](#comosfiltros)


---

### 🔗 Links e Referências Internas:

- [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263)
- [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263#abaconfigura%C3%A7%C3%B5es)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)