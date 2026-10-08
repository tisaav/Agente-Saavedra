# Agrupamento de Serviços no Faturamento de Contratos e Serviços

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599994-Agrupamento-de-Servi%C3%A7os-no-Faturamento-de-Contratos-e-Servi%C3%A7os](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599994-Agrupamento-de-Servi%C3%A7os-no-Faturamento-de-Contratos-e-Servi%C3%A7os)  
> **ID:** `360044599994` | **Última Atualização:** 2026-07-29T13:49:38Z

---

O processo abaixo, está ligado à necessidade de lançamento de Notas Fiscais de Serviço (nota fiscal mista) onde deve-se substituir os serviços a serem incluídos na nota por um único serviço. Este comportamento possibilita que todos os serviços, especificados no contrato, sejam agrupados em um só. Tal agrupamento, ocorre no momento em que o contrato é faturado e o pedido/nota é gerado. Abaixo, estão detalhadas as configurações necessárias:

No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), na aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro), habilite a marcação **"Agrupa serviços faturamento"**:

![financeiro.png](https://ajuda.sankhya.com.br/hc/article_attachments/23864477131287)

Ainda no cadastro de Tipos de Operação - TOP, na aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), defina o campo **"Kit/Componentes - Impressão e Livro Fiscal"** com a opção **"Kit"** para que apenas este seja impresso:

![financeiro 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/23864440343575)

Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025239374-Empresa), efetue a marcação **"Agrupa serviços faturamento"** encontrado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e), dentro da sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) em [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos):

![NFS-e.png](https://ajuda.sankhya.com.br/hc/article_attachments/23864440352535)

No cadastro de [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas), informe no campo **"Serviço único faturamento"** o serviço que será responsável por agrupar os serviços inseridos na nota de serviço em apenas um:

![NFSe.png](https://ajuda.sankhya.com.br/hc/article_attachments/23864440355863)

Caso na Empresa e no Tipo de Operação - TOP, a marcação Agrupa serviços faturamento acima citada esteja realizada, mas na tela Natureza de Receitas e Despesas não tenha um Serviço único faturamento informado, o sistema irá apresentar uma mensagem alertando sobre a necessidade de tal preenchimento. O cálculo dos impostos será feito com base somente no serviço único faturamento informado.

As configurações até aqui citadas, irão impactar no uso das telas [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos) e [Faturamento de Pedidos/OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS). 

Ao realizar o faturamento do contrato, será gerado um pedido/nota com todos os serviços informados no contrato bem como também será gerado o serviço agrupador.

**Observação:** será modificado o **"USOPROD"** para **"D"** de forma a representar no pedido/nota os serviços informados no contrato como se fossem componentes do serviço agrupador; o USOPROD será alterado para **"S"** para expressar que o serviço agrupador é o serviço a ser considerado no pedido/nota.

**Nota:** tratando-se de Nota de Serviços, quando esta possuir uma configuração para agrupamento em serviço único, apenas o serviço único terá o cálculo de impostos.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)
- [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025239374-Empresa)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)
- [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e)
- [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)
- [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas)
- [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos)
- [Faturamento de Pedidos/OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS)