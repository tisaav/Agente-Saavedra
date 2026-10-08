# Valor do campo 'Cód. tipo de ligação' deve estar entre 1 e 3

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110674-Valor-do-campo-C%C3%B3d-tipo-de-liga%C3%A7%C3%A3o-deve-estar-entre-1-e-3](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110674-Valor-do-campo-C%C3%B3d-tipo-de-liga%C3%A7%C3%A3o-deve-estar-entre-1-e-3)  
> **ID:** `360044110674` | **Última Atualização:** 2026-07-22T15:53:19Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611249606039)

 MENSAGEM:**

Valor do campo 'Cód. tipo de ligação' deve estar entre 1 e 3.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611249608343)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611249614999)

 Verifique na tela **"Empresa"** *(Caminho de acesso: Comercial » Preferências) »* aba Livros Fiscais » Nota fiscal de conta de Energia Elétrica » Campo** "Cód.Tipo de Ligação"**:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14919353871895)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611222178327)

 Defina esse campo de acordo com a necessidade da empresa, com uma das opções abaixo:

- Bifásico

- Monofásico

- Trifásico

Quando preenchidos os campos "**Cód.Tipo de Ligação**" e "**Cód.Grupo de Tensão**", o sistema usará os dados inseridos e os informará no lançamento do Pedido/Nota na Central em seus correspondentes do Pedido/Nota, isso quando a opção "**Permite informar Ligação na Central**", estiver **desmarcada**.

Se a opção Permite informar Ligação na Central estiver **marcada** e na Configuração do Layout da Nota estiver configurado para visualização destes campos, no menu do **["Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)"**, serão apresentados os campos sem preenchimento e ficará a cargo do usuário informar estes campos na central.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611222187799)

 IMPORTANTE:** 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611249614999)

 Estes dados são de responsabilidade do usuário;

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611222178327)

 Além de informá-los na Configuração do Layout da Nota é necessário também que a top utilizada para o lançamento tenha o código do modelo de Nota Fiscal igual a 6;

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611222190231)

 Os dados inseridos nesses campos nas movimentações da Central irão compor o registro C500 referente a Notas de Energia Elétrica do SPED Fiscal;

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611249622167)

 Para as notas lançadas antes da configuração feita na empresa, será necessário ajuste via banco de dados, setando a informação na tabela. Ou, relançar as notas setando a marcação Permite informar Ligação na Central e preencher o campo ao efetuar o lançamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16611255783447)

CAUSA:**

Na validação do SPED Fiscal, a mensagem é retornada quando realizado emissão/lançamentos de notas com Modelo de Documento 6 e não informado o Cód. Tipo de Ligação.


---

### 🔗 Links e Referências Internas:

- ["Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)