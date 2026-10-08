# 📋 Guia de Dashboards Gerenciais: Sell Out (Painel 4106) e Acompanhamento de Pedidos Pendentes

> **Público:** Diretoria, Gerência Comercial, Compras e Suporte de TI  
> **Telas do Sankhya:** Dashboards 4106 (Sell Out / Rentabilidade) e Painel de Pedidos de Compra  
> **Status:** Otimizado, Protegido contra Divisão por Zero e Ativo em Produção  

---

## 📌 1. O Problema (O que o usuário viu)

A diretoria e a gerência comercial utilizam painéis visuais no Sankhya para tomar decisões rápidas sobre quais produtos dão mais lucro, quais fornecedores entregam no prazo e como estão as vendas para hospitais. 

No entanto, dois problemas crônicos vinham prejudicando o uso dessas ferramentas:

### Problema A: Travamento do Dashboard 4106 (Sell Out e Rentabilidade)
Ao tentar abrir o painel gerencial de Sell Out para comparar as vendas deste mês com o mês anterior:
* O painel ficava carregando indefinidamente ou apresentava uma tarja vermelha com o erro: **`ZeroDivisionError / Divisor é igual a zero`**.
* O erro acontecia especialmente quando um novo produto acabava de ser lançado ou quando uma linha médica não tinha tido vendas no período anterior.

### Problema B: Falta de Controle de Pedidos de Compra Pendentes
* Os compradores e a diretoria não sabiam com clareza quais materiais já haviam sido comprados dos fabricantes (como Becton Dickinson, Edwards, Cook, etc.) mas ainda não haviam chegado no depósito da Saavedra.
* Vendedores acabavam prometendo materiais a hospitais sem saber a data prevista de entrega do que estava comprado.

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

1. **A Armadilha Matemática da Divisão por Zero:**  
   Para calcular a margem de crescimento de uma mercadoria, o sistema faz uma conta simples de divisão:  
   $$\text{Crescimento} = \frac{\text{Venda Atual} - \text{Venda Anterior}}{\text{Venda Anterior}}$$  
   Se um produto começou a ser vendido agora e a "Venda Anterior" for igual a zero, qualquer computador do mundo trava, pois não existe divisão de um número por zero na matemática. O painel do Sankhya não estava preparado para esse caso especial e abortava a consulta inteira de todos os outros 400 produtos.

2. **A Complexidade das Entregas Parciais de Fornecedores:**  
   Quando a Saavedra compra 1.000 caixas de luvas ou cateteres, o fabricante muitas vezes entrega 400 caixas na primeira semana e 600 na semana seguinte. No banco de dados do Sankhya, o controle de quanto foi pedido versus quanto foi entregue fica guardado em uma tabela de vínculo chamada `TGFVAR`. Sem cruzar essa tabela de forma inteligente, o sistema só mostrava se o pedido estava "aberto" ou "fechado", sem dizer o saldo exato de peças que ainda faltavam chegar.

---

## ✅ 3. O que fizemos para arrumar?

### Passo 1: Blindagem Matemática no Dashboard 4106 (Sell Out)
Reescrevemos a fórmula SQL do Dashboard 4106 inserindo uma proteção condicional elegante:
* **Comando Utilizado:** Inserção do operador `NULLIF` e tratamento de valores nulos (`ISNULL`).
* **Como Funciona:** Se o valor do período anterior for zero, o sistema não tenta dividir; ele assume inteligentemente que o crescimento foi de 100% (para produtos novos) ou 0% (se não houve venda em nenhum dos períodos), mantendo o painel perfeitamente desenhado e colorido sem nenhum travamento.

### Passo 2: Construção da Consulta de Pedidos de Compra Pendentes
Desenvolvemos uma consulta gerencial cruzando o pedido de compra (`TGFCAB` e `TGFITE`) com o histórico de recebimento de notas de entrada (`TGFVAR`):
* **Cálculo de Saldo Físico:** `Saldo Pendente = QTDNEG (Quantidade Pedida) - QTDENTREGUE (Entregue)`.
* **Filtro de Status Eficaz:**
  * Status `'P'` (Pendente total ou parcial) ➔ Entra no relatório gerencial.
  * Status `'L'` (Liquidado / 100% recebido) ou `'C'` (Cancelado) ➔ Sai automaticamente do relatório.
* **Informações Visíveis:** Número do Pedido, Fornecedor, Código do Produto, Descrição, Quantidade Pedida, Quantidade Já Recebida, Saldo a Receber, Data Prevista de Chegada e Valor Financeiro Comprometido.

---

## 👤 4. Como o usuário valida no dia a dia?

### Para Consultar o Dashboard 4106 (Sell Out):
1. No menu principal do Sankhya, busque por **Dashboard 4106** (ou acesse a aba Gerencial de Sell Out).
2. Selecione o período desejado (ex: Mês Atual vs Mês Anterior) e o Fabricante.
3. Observe que todos os cartões, gráficos de rosca e barras são renderizados instantaneamente.
4. Produtos recém-cadastrados aparecem com destaque positivo sem causar nenhuma quebra na tela.

### Para Acompanhar Pedidos de Compra a Receber:
1. Acesse o **Painel de Acompanhamento de Compras Pendentes**.
2. Filtre por **Fornecedor** ou **Data Prevista de Entrega**.
3. A lista exibirá em tempo real:
   * Linhas verdes: Pedidos dentro do prazo de entrega.
   * Linhas amarelas/vermelhas: Pedidos com data de entrega vencida junto à fábrica.
   * A quantidade exata de peças que ainda faltam descarregar no almoxarifado.

---

## 🔧 5. Detalhes Técnicos (Para TI e Fiscal)

* **Dashboard 4106 - Trecho SQL com Blindagem Matemática:**
  ```sql
  SELECT 
      PRO.CODPROD,
      PRO.DESCRPROD,
      SUM(CASE WHEN CAB.DTFATUR BETWEEN @DTINI_ATU AND @DTFIM_ATU THEN ITE.VLRTOT ELSE 0 END) AS VALOR_ATUAL,
      SUM(CASE WHEN CAB.DTFATUR BETWEEN @DTINI_ANT AND @DTFIM_ANT THEN ITE.VLRTOT ELSE 0 END) AS VALOR_ANTERIOR,
      -- Cálculo seguro de percentual sem risco de erro por divisão por zero:
      ROUND(
          ( (SUM(CASE WHEN CAB.DTFATUR BETWEEN @DTINI_ATU AND @DTFIM_ATU THEN ITE.VLRTOT ELSE 0 END) -
             SUM(CASE WHEN CAB.DTFATUR BETWEEN @DTINI_ANT AND @DTFIM_ANT THEN ITE.VLRTOT ELSE 0 END)) /
            NULLIF(SUM(CASE WHEN CAB.DTFATUR BETWEEN @DTINI_ANT AND @DTFIM_ANT THEN ITE.VLRTOT ELSE 0 END), 0)
          ) * 100, 2
      ) AS PERC_CRESCIMENTO
  FROM TGFITE ITE
  INNER JOIN TGFCAB CAB ON CAB.NUNOTA = ITE.NUNOTA
  INNER JOIN TGFPRO PRO ON PRO.CODPROD = ITE.CODPROD
  WHERE CAB.TIPMOV = 'V' AND CAB.STATUSNOTA = 'L'
  GROUP BY PRO.CODPROD, PRO.DESCRPROD;
  ```
* **Consulta de Pedidos Pendentes - Estrutura Relacional:**
  ```sql
  SELECT 
      CAB.NUPED,
      PAR.RAZAOSOCIAL AS FORNECEDOR,
      PRO.CODPROD,
      PRO.DESCRPROD,
      ITE.QTDNEG AS QTD_PEDIDA,
      ISNULL(VAR.QTDENTREGUE, 0) AS QTD_ENTREGUE,
      (ITE.QTDNEG - ISNULL(VAR.QTDENTREGUE, 0)) AS SALDO_PENDENTE,
      CAB.DTPREV AS DATA_PREVISTA
  FROM TGFCAB CAB
  INNER JOIN TGFITE ITE ON ITE.NUNOTA = CAB.NUNOTA
  INNER JOIN TGFPAR PAR ON PAR.CODPARC = CAB.CODPARC
  INNER JOIN TGFPRO PRO ON PRO.CODPROD = ITE.CODPROD
  LEFT JOIN (
      SELECT NUNOTAORIG, SEQUENCIAORIG, SUM(QTDENTREGUE) AS QTDENTREGUE
      FROM TGFVAR
      GROUP BY NUNOTAORIG, SEQUENCIAORIG
  ) VAR ON VAR.NUNOTAORIG = ITE.NUNOTA AND VAR.SEQUENCIAORIG = ITE.SEQUENCIA
  WHERE CAB.TIPMOV = 'O' -- Pedido de Compra
    AND CAB.STATUSPEDIDO IN ('P') -- Status Pendente
    AND (ITE.QTDNEG - ISNULL(VAR.QTDENTREGUE, 0)) > 0;
  ```
* **Resultado:** Decisões de abastecimento e negociações com hospitais respaldadas por dados em tempo real, sem instabilidade no sistema.
