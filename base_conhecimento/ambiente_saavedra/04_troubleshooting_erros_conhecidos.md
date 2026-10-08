# 🚨 Troubleshooting e Resolução de Erros Específicos — Saavedra Representações

Este guia compila os erros reais enfrentados no ambiente da **Saavedra Representações**, suas causas raízes técnicas e as soluções definitivas testadas e homologadas.

---

## Incidente 1: Erro `CORE_E05181: Unable to get next record` ao Confirmar Pedido de Venda

### Cenário:
O usuário tenta confirmar um pedido de venda na **Central de Vendas** ou **Portal de Vendas** (ex: pedido 70296 para o parceiro **258 - UNIMED**).
* **Sintoma:** O sistema exibe o erro fatal `CORE_E05181: Unable to get next record`, o pedido não é confirmado e o e-mail automático com o PDF do pedido não é disparado para o cliente nem para o estoque.
* **Paradoxo Inicial:** A TOP 1005 (Simples Remessa) funcionava normalmente para o mesmo parceiro 258, mas a TOP 1000 (Venda NFE) quebrava com erro no mesmo modelo de relatório (Modelo 14).

### Causas Raízes e Soluções:

#### 1.1. Incompatibilidade de Tipo no CRM do Médico (`CAB.AD_CRM`)
* **Causa:** No arquivo `PEDIDO_DE_VENDA.jrxml`, o campo `CRM` estava configurado no Jasper como `java.lang.Integer`. Na consulta SQL antiga, havia a cláusula `COALESCE(CAB.AD_CRM, ' ')`. Quando o pedido da Unimed não tinha CRM preenchido ou tinha espaço em branco, o banco enviava `' '` para uma variável inteira do Java, gerando uma exceção de conversão que derrubava o motor do Jasper.
* **Solução Definitiva:**
  1. No SQL: Tratar o campo com `CAST(CAB.AD_CRM AS VARCHAR) AS CRM`.
  2. No XML do Jasper: Declarar o campo como `String`: `<field name="CRM" class="java.lang.String"/>`.

#### 1.2. Divisão por Zero na Unidade Alternativa de Medida (`TGFVOA`)
* **Causa:** No sub-relatório `ITENS_PEDIDO_DE_VENDA.jrxml`, o cálculo de conversão de volume realizava divisão direta pela quantidade da unidade alternativa: `ITE.QTDNEG / VOA.QUANTIDADE` e `ITE.VLRUNIT / VOA.QUANTIDADE`. Se algum produto do pedido possuísse unidade alternativa com quantidade zerada (`0`), ocorria divisão por zero no SQL Server.
* **Solução Definitiva:**
  - Proteger a divisão utilizando a função `NULLIF`:
    ```sql
    ITE.QTDNEG / NULLIF(VOA.QUANTIDADE, 0)
    ITE.VLRUNIT / NULLIF(VOA.QUANTIDADE, 0)
    ```

#### 1.3. Bloqueio por `INNER JOIN` com Histórico de Condição de Venda (`TPV.DHALTER`)
* **Causa:** A consulta original realizava:
  ```sql
  INNER JOIN TGFTPV TPV ON CAB.CODTIPVENDA = TPV.CODTIPVENDA AND CAB.DHTIPVENDA = TPV.DHALTER
  ```
  Se a Condição de Venda vinculada à Unimed foi editada no sistema após a criação do pedido, o `DHTIPVENDA` gravado no pedido não bate com o novo `DHALTER` da tabela `TGFTPV`. O `INNER JOIN` descartava o registro inteiro, resultando em consulta vazia e erro no Jasper.
* **Solução Definitiva:** Alterar a junção para `LEFT JOIN` e garantir `LEFT JOIN` em todas as tabelas acessórias (Endereços, Cidades, Bairros, Transportadoras e Vendedores).

#### 1.4. Subqueries com Múltiplas Linhas em `TGFPAP` e `TGFCTT`
* **Causa:** Quando a Unimed ou o hospital parceiro possuía mais de uma referência de produto na tabela `TGFPAP`, subqueries diretas como `(SELECT CODPROPARC FROM TGFPAP WHERE ...)` retornavam 2 ou mais linhas, quebrando a consulta com erro de subquery escalar.
* **Solução Definitiva:** Adicionar `TOP 1` em todas as subqueries:
  ```sql
  (SELECT TOP 1 COALESCE(CODPROPARC, NULL) FROM TGFPAP WHERE CODPARC = CAB.CODPARC AND CODPROD = ITE.CODPROD)
  (SELECT TOP 1 NOMECONTATO FROM TGFCTT WHERE CODCONTATO = CAB.CODCONTATO AND CODPARC = CAB.CODPARC)
  ```

#### 1.5. Tipagem da Data do Registro RMS (`PRO.AD_DTRMS`)
* **Causa:** O sub-relatório declarava `AD_DTRMS` como `java.lang.String`, mas o banco de dados retornava um objeto `java.sql.Timestamp` / `Date`, gerando `ClassCastException`.
* **Solução Definitiva:** Forçar a conversão para texto no próprio SQL Server: `CONVERT(VARCHAR, PRO.AD_DTRMS, 103) AS AD_DTRMS`.

#### 1.6. Tipagem do Frete Unitário (`VLRFRETEUNIT`)
* **Causa:** A expressão `COALESCE(0, 0)` no SQL devolvia um `INT`, mas o Jasper esperava `java.math.BigDecimal`.
* **Solução Definitiva:** `CAST(0 AS DECIMAL(10,2)) AS VLRFRETEUNIT`.

---

## Incidente 2: Erro `CORE_E02496: Não foi possível converter o arquivo para um jrxml válido`

### Cenário:
O usuário edita o arquivo de modelo no Sankhya (tela *Modelos de Nota Fiscal/Duplicatas/Boleto(s)*) e, ao salvar ou anexar, o ERP rejeita o upload com o erro `CORE_E02496`.
* **Causa Raiz:** O arquivo `.jrxml` foi salvo contendo apenas o bloco SQL (`<![CDATA[SELECT ...]]>`), tendo sido apagada a estrutura de cabeçalho e fechamento XML do JasperReports (`<jasperReport> ... </jasperReport>`).
* **Solução:** O arquivo `.jrxml` precisa manter toda a estrutura XML completa, contendo `<jasperReport>`, declaração de `<parameter>`, `<queryString>`, `<field>`, `<variable>`, `<detail>` e `<band>`. Nunca colar apenas a query SQL isolada dentro do arquivo de modelo.

---

## Incidente 3: Relatório Formatado 67 não aparece na lista (pula do 66 para o 68)

### Cenário:
Ao acessar a tela **Relatórios Formatados**, o usuário busca pelo relatório `67 - PEDIDO DE VENDA - POA` e ele não é listado na grade.
* **Causa Raiz:** No painel lateral esquerdo da tela de Relatórios Formatados, a opção **"Filtro personalizado"** está ativada (chave verde ligada) e filtrando apenas certas categorias. Se o relatório 67 estiver sob outra categoria ou `<Sem Categoria>`, o filtro o oculta.
* **Solução:**
  1. No painel esquerdo da tela, clique no link **Limpar**.
  2. Desligue a chave verde **Filtro personalizado**.
  3. Digite `67` no campo de busca de código e clique em **Aplicar**. O relatório será exibido normalmente.
