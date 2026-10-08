# Parcelas pagas por compensação no DANFE

> **Módulo:** Fiscal e Contábil | **Subseção:** NF-e e NFC-e  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600454-Parcelas-pagas-por-compensa%C3%A7%C3%A3o-no-DANFE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600454-Parcelas-pagas-por-compensa%C3%A7%C3%A3o-no-DANFE)  
> **ID:** `360044600454` | **Última Atualização:** 2026-09-15T16:51:36Z

---

Nosso sistema conta com um recurso que permite a impressão do Danfe, e neste consta a verificação se o título está baixado e se o tipo de título utilizado em seu lançamento é compensação de crédito. Se estes casos forem atendidos, no final da descrição da seção **"Fatura/Duplicata"** no Danfe, será apresentada a palavra **"[pago]"**.

Para que esta impressão ocorra, é necessário que o processo de geração do Danfe de cada empresa seja analisado, pois é preciso que o parâmetro **"Imprimir faturas no DANFE pelo xml - FINANCEXMLDANFE"** esteja desativado. Além disso, deve-se realizar a ativação do parâmetro **"Destacar financeiro pago por compensação no danfe? - DESFINPGCOMPDNF"**.

Consideremos abaixo, o processo no sistema envolvido neste procedimento:

- 
Na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) atente-se para a configuração dos seguintes parâmetros:

1. 
Avisar que o cliente possui Crédito? - AVISARCREDCLI: **Ativado**

1. 
Compensar crédito do cliente automaticamente - COMPENSACREDCLI: **Ativado**

1. 
Destacar financeiro pago por compensação no danfe? - DESFINPGCOMPDNF: **Ativado**

1. 
Top Baixa de Despesa de Compensação de Crédito - TOPBAIDESPCOMP: **Informado**

1. 
Top Baixa de Receita de Compensação de Crédito - TOPBAIRECCOMP: **Informado**

1. 
Tipo de título para compensação de Crédito - TIPTITCREDCLI: **Informado**

1. 
Avisar que o cliente possui Crédito? - AVISARCREDCLI: **Ativado**

1. 
Imprimir faturas no DANFE pelo xml - FINANCEXMLDANFE:** Desativado**

- 
Na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) deve-se possuir um tipo de negociação adequado que atenda ao processo de geração de Crédito para o cliente.

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/8444711105431)

- É necessário que o cliente possua um crédito para ele lançado. Por exemplo, o cliente realizou uma devolução e ficou com um crédito a ser compensado quando efetuar uma nova compra.

- 
Ao efetuar a venda para o cliente que possui o crédito a ser compensado, o sistema irá fazê-lo no financeiro da nota, baixando o título e modificando o Tipo de Título para a informação salva no parâmetro **"Tipo de título para compensação de Crédito - TIPTITCREDCLI"**.

Consideremos o exemplo de um Danfe impresso contendo a informação **"[pago]"**:

![clip2441.bmp](https://ajuda.sankhya.com.br/hc/article_attachments/8444531261207)

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)
- [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)