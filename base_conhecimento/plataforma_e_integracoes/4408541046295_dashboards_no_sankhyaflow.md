# Dashboards no SankhyaFlow

> **Módulo:** Plataforma e Integrações | **Subseção:** Flow  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4408541046295-Dashboards-no-SankhyaFlow](https://ajuda.sankhya.com.br/hc/pt-br/articles/4408541046295-Dashboards-no-SankhyaFlow)  
> **ID:** `4408541046295` | **Última Atualização:** 2026-08-26T15:55:56Z

---

```text

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313311269399)

 Versão: a partir da 4.6
```

O Dashboard é uma ferramenta acessória que permite acessar os Componentes de BI durante a execução de uma tarefa na Lista de Tarefas e é utilizado para direcionar os usuários durante a execução de seu trabalho, permitindo que sejam realizadas consultas/análises para tomadas de decisões, como por exemplo, consultar o histórico financeiro de um parceiro para realizar uma liberação de limite de crédito em uma venda.

Em nosso caso de uso, apresentaremos o processo de **"Solicitação de compras simplificado"**:

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408534277015)

****

| Processo de Solicitação de compras simplificado |
| --- |

Esse processo permite que qualquer colaborador realize uma solicitação de compras. Ao realizar esse solicitação, o responsável pelo Centro de Resultado do solicitante fará uma análise do planejamento orçamentário do seu departamento (orçamento previsto X realizado), para verificar se tem saldo disponível no mês vigente e se será possível aprovar ou não a solicitação de compras. Caso ela seja aprovada, o processo seguirá para a cotação dos produtos e, em seguida, será gerado o Pedido de Compras.

Para que o responsável pelo CR do solicitante possa analisar a solicitação de compras com base no planejamento orçamentário do seu departamento, devemos adicionar na tarefa **"Analisar solicitação de compra"**, o Componente de BI **"Planejamento orçamentário (CR)"** que será apresentado como dashboard na tarefa:

![flow10.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4408534975383)

****

| Adicionando Dashboard (Componentes de BI) na tarefa |
| --- |

**Observação:** para que os dados no Dashboard tenham relação com o processo, a consulta deve estar relacionada com o ID Instância do Processo (IDINSTPRN) ou com o ID Instância da Tarefa (IDINSTTAR). Para isso, é obrigatório que o componente possua os parâmetros IDINSTPRN ou IDINSTTAR, que serão alimentados automaticamente durante a abertura do Dashboard.

Nesse exemplo iremos utilizar como parâmetro nos componentes, o ID Instância do Processo (IDINSTPRN) como filtro da consulta; sendo assim, criamos primeiramente o parâmetro:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408542626327)

****

| Parâmetro IDINSTPRN no componente |
| --- |

Agora devemos inserir o IDINSTPRN como filtro da consulta desse [Dashboard](https://drive.google.com/file/d/1gP_zg5iYVE5nluRk1rpFsTJkodY4LNkV/view) (Componentes de BI), conforme as imagens abaixo:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408624686359)

****

| Componente de BI - Nível Principal (Planejamento Previsto X Realizado) |
| --- |

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4408624665879)

****

| Componente de BI - Detalhe dos lançamentos realizados |
| --- |

**Nota:** nesse exemplo, a consulta retornará campos do Formulário Embarcado do processo. Sendo assim, buscaremos na coluna NUMINT (número inteiro) da tabela de variáveis TWFIVAR, o conteúdo dos campos **"CODEMP"** (Código da Empresa) e **"CODCENCUS"** (Código do CR).

Para mais informações acesse a documentação sobre o [Construtor de Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI).

Conforme as configurações realizadas anteriormente, iremos apresentar a visualização do Dashboard durante a execução da tarefa Analisar solicitação de compras na Lista de Tarefas.

Nesse exemplo, a colaboradora Maria solicitou a compra de um notebook, informando um valor previsto de R$3.200,00. Juliane, responsável pela tarefa Analisar solicitação de compras (responsável pelo CR do solicitante), acessou o Dashboard de Planejamento Orçamentário (CR) durante a execução dessa tarefa, para verificar se será possível aprovar ou não a solicitação com base no valor previsto informado.

Na análise, Juliane verificou o orçamento previsto de R$10.000,00 X realizado de R$5.197,00 do mês de junho e os detalhes dos lançamentos realizados:

![flow11.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4408543028247)

****

| Visualização de dashboard na tarefa (lista de tarefas) |
| --- |

Sendo assim, de acordo com essa análise a compra será aprovada.

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Construtor de Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI)