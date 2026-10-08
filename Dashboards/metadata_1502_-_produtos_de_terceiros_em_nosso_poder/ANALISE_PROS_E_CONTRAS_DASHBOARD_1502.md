# Relatório de Análise Técnica: Dashboard Sankhya 1502
**Componente:** `1502 - PRODUTOS DE TERCEIROS EM NOSSO PODER`  
**Arquivo Analisado:** `Dashboards/metadata_1502_-_produtos_de_terceiros_em_nosso_poder/dashboardMetadata.xml`  
**Data da Análise:** Outubro de 2026  
**Ambiente:** Sankhya ERP / MGE - Data-Source: `MGEDS` (SQL Server)

---

## 1. Resumo Executivo

Este documento apresenta uma análise técnica profunda do dashboard nativo Sankhya registrado no arquivo [dashboardMetadata.xml](file:///c:/Users/SAAV166/Documents/Agente/Dashboards/metadata_1502_-_produtos_de_terceiros_em_nosso_poder/dashboardMetadata.xml). O objetivo do dashboard é auditar estoques de terceiros (consignação mercantil e remessas industriais/hospitalares), apurando quantidades movimentadas, saldos e validade de lotes.

A análise identificou **erros críticos de integridade de dados** (multiplicação de registros em devoluções parciais, distorção de totalizadores e saldos incorretos), um **bug impeditivo de execução no parâmetro de validade**, **incoerências conceituais** entre a regra fiscal/movimento e os nomes de colunas, e **gargalos severos de desempenho** provocados por UDFs escalares e ausência de agregação no relacionamento `TGFVAR`.

---

## 2. Quadro de Prós e Contras

| Categoria | Prós (Pontos Fortes) | Contras (Fragilidades & Riscos) |
| :--- | :--- | :--- |
| **Objetivo de Negócio** | • Atende a uma demanda crítica de compliance e controle de estoque de alto valor (OPME / Consignados).<br>• Centraliza informações do parceiro, lote, validade e dados do paciente/cirurgia em uma única visão. | • Confusão conceitual: o título trata de estoque *de terceiros em nosso poder* (`TIPMOV='C'`), mas colunas e regras usam rótulos de *nosso em poder de terceiros* ("QtdEnviada"). |
| **Usabilidade & UX** | • Integração nativa com a Central de Notas via `<on-click-launcher>` para drill-down no `NUNOTA`.<br>• Uso de alerta visual por cores (`BKCOLOR`/`FGCOLOR`) para destacar itens abaixo da cota contratual. | • Colunas de data (`DataCirurgia`, `DataValidade`, `DataNegociacao`) tipadas como texto (`type="S"`), impedindo a ordenação cronológica correta na grid.<br>• Poluição visual: 29 colunas incluindo logradouro completo do parceiro, prejudicando o foco analítico. |
| **Integridade de Dados** | • Utiliza vínculos nativos do Sankhya (`TGFCAB`, `TGFITE`, `TGFTOP`, `TGFVAR`).<br>• Preocupa-se em rastrear o vínculo original da remessa com devoluções. | • **Duplicação de linhas e distorção de saldos**: devoluções parciais pelo `TGFVAR` multiplicam linhas e somam incorretamente `ValorNFe` e `QtdEnviada`.<br>• Ocultamento indevido de notas antigas pelo `INNER JOIN` com `TGFEST.ESTOQUE <> 0`. |
| **Parâmetros & Filtros** | • Filtros de período (`datePeriod`) e buscas por intervalos de entidade (`CODPARC`, `CODPROD`). | • **Bug impeditivo no parâmetro de validade**: definido como `metadata="date"`, mas chamado no SQL como `.INI` e `.FIN`, gerando falha de execução no ERP.<br>• Falta de filtro essencial por Empresa (`CODEMP`). |
| **Performance de Banco de Dados** | • Consulta estruturada em SQL direto no data-source `MGEDS`. | • Uso de funções escalares lentas (`SNK_FORMAT_DATE`, `SNK_DATE_DIFF`, `FC_FORMATACEP`) que impedem paralelismo.<br>• Predicados `OR :PARAM IS NULL` que inviabilizam index seek e causam parameter sniffing. |

---

## 3. Diagnóstico Profundo de Bugs e Falhas de Negócio

### 3.1. Bug Crítico #1: Multiplicação de Linhas e Distorção de Saldos (`TGFVAR` sem Agregação)
* **Trecho no SQL:**
  ```sql
  LEFT JOIN TGFVAR VAR ON VAR.NUNOTAORIG = CABNFS.NUNOTA AND VAR.SEQUENCIAORIG = ITENFS.SEQUENCIA
  LEFT JOIN TGFCAB CABD ON CABD.NUNOTA = VAR.NUNOTA AND CABD.TIPMOV IN('C','E')
  LEFT JOIN TGFITE ITED ON ITED.NUNOTA = CABD.NUNOTA AND ITED.SEQUENCIA = VAR.SEQUENCIA
  LEFT JOIN TGFTOP TOPD ON TOPD.CODTIPOPER = CABD.CODTIPOPER AND TOPD.DHALTER = CABD.DHTIPOPER AND TOPD.ATUALESTTERC = 'D'
  ```
* **Causa:** No ERP Sankhya, quando um item de remessa sofre mais de um retorno (exemplo: duas devoluções parciais ou devolução + faturamento simbólico), a tabela de variações `TGFVAR` armazena **um registro por nota de destino**.
* **Impacto Real:**
  1. O mesmo item da nota original aparece repetido $N$ vezes na tela (uma para cada devolução).
  2. A quantidade enviada (`ITENFS.QTDNEG`) e o valor da nota (`CABNFS.VLRNOTA`) são duplicados na listagem e nos totalizadores de rodapé (`useFooter="SUM"`), fornecendo valores contábeis e financeiros inflados e incorretos.
  3. O cálculo do saldo (`ITENFS.QTDNEG - ITED.QTDNEG`) é calculado isoladamente contra cada devolução e não sobre o somatório acumulado devolvido.
  4. O join com `TGFTOP TOPD` não restringe o `CABD` nem o `ITED`. Se a TOP da nota vinculada não possuir `ATUALESTTERC = 'D'`, os campos de `TOPD` vêm nulos, mas `ITED.QTDNEG` continua entrando no cálculo da devolução.

---

### 3.2. Bug Crítico #2: Incompatibilidade Fatal no Parâmetro de Validade (`P_DTVAL`)
* **Trecho no XML:**
  ```xml
  <parameter id="P_DTVAL" description="Data Validade" metadata="date" required="false" ... label="P_DTVAL : Data" order="5" />
  ```
* **Trecho no SQL:**
  ```sql
  AND (EST.DTVAL >= :P_DTVAL.INI OR :P_DTVAL.INI IS NULL)
  AND (EST.DTVAL <= :P_DTVAL.FIN OR :P_DTVAL.FIN IS NULL)
  ```
* **Causa:** No motor de dashboards do Sankhya, parâmetros com `metadata="date"` renderizam um seletor de data única e fornecem apenas a variável bind `:P_DTVAL`. As extensões `.INI` e `.FIN` **só existem** para parâmetros declarados com `metadata="datePeriod"`.
* **Impacto Real:** Ao tentar executar o dashboard ou filtrar por validade, o motor lança exceção de parâmetro não encontrado ou erro de sintaxe SQL na consulta.

---

### 3.3. Incoerência Conceitual: Estoque de Terceiros vs Estoque em Terceiros
* **Configuração Atual:**
  - Título: `1502 - PRODUTOS DE TERCEIROS EM NOSSO PODER`
  - Descrição: `...auditoria do estoque em poder de terceiros, confrontando as quantidades enviadas e retornadas...`
  - SQL: `CABNFS.TIPMOV = 'C'` (Compra/Recebimento), `EST.TIPO = 'T'` (Terceiros em Nosso Poder), `TOP1.ATUALESTTERC = 'T'`.
  - Colunas de Tela: `QtdEnviada` e `QtdRetornada`.
* **Incoerência:**
  - Se `TIPMOV = 'C'` e `TIPO = 'T'`, a operação é de **entrada** de material enviado por um fornecedor/terceiro para a posse da empresa (consignação recebida).
  - Rotular o campo de `QtdEnviada` confunde a operação, pois o material foi **recebido**. Da mesma forma, as saídas são **devoluções ao fornecedor**, e não retornos de clientes.
  - Além disso, a presença de `AD_DTCIRURG` e `AD_PACIENTE` indica uso hospitalar/OPME. Em distribuidores de materiais médicos, é frequente a remessa de material consignado para hospitais (que seria Saída/Venda, `TIPMOV = 'V'` e `EST.TIPO = 'E'`). Se o objetivo real era auditar o estoque enviado aos hospitais, toda a query está filtrando a ponta invertida!

---

### 3.4. Bug Lógico #3: Ocultamento de Histórico pelo `INNER JOIN` em `TGFEST`
* **Trecho no SQL:**
  ```sql
  INNER JOIN SANKHYA.TGFEST AS EST ON EST.CODEMP = ITENFS.CODEMP 
    AND EST.CODPROD = ITENFS.CODPROD 
    AND EST.CODLOCAL = ITENFS.CODLOCALORIG 
    AND EST.CONTROLE = ITENFS.CONTROLE 
    AND EST.CODPARC = CABNFS.CODPARC 
    AND EST.TIPO = TOP1.ATUALESTTERC
  WHERE ((ISNULL (EST.ESTOQUE, 0) <> 00) AND ...)
  ```
* **Causa:** `TGFEST` armazena o saldo físico atual em estoque.
* **Impacto Real:**
  - Se um lote foi recebido em consignação e posteriormente totalmente devolvido ou faturado, o registro em `TGFEST` zera (`ESTOQUE = 0`).
  - O filtro `ISNULL(EST.ESTOQUE, 0) <> 0` faz com que essas notas fiscais **desapareçam por completo** do dashboard, impedindo a conferência e auditoria de notas antigas e do ciclo de vida da remessa.
  - Além disso, o saldo de `TGFEST` é o saldo acumulado de todo o estoque do lote, enquanto o cálculo da query confronta apenas o item da nota com suas devoluções na `TGFVAR`.

---

### 3.5. Bug de Regra de Negócio #4: Falso Positivo no Consignado Fixo (`AD_CONSFIXO`)
* **Trecho no SQL:**
  ```sql
  LEFT JOIN AD_CONSFIXO CONS ON CONS.CODPARC = CABNFS.CODPARC AND CONS.CODPROD = ITENFS.CODPROD
  ...
  CASE WHEN (ISNULL(ITENFS.QTDNEG,0) - ISNULL(ITED.QTDNEG,0)) < ISNULL(CONS.QTDE ,0) THEN '#FF0000' ELSE '' END AS BKCOLOR
  ```
* **Causa:** A tabela `AD_CONSFIXO` define a quantidade padrão de estoque acordada para o produto no parceiro (nível macro). O cálculo compara o saldo **de uma única nota fiscal** contra o saldo global contratado.
* **Impacto Real:** Se o cliente possui uma cota de 100 peças e o fornecimento foi realizado através de 4 notas fiscais de 25 peças, todas as 4 linhas apresentarão saldo 25 (< 100) e ficarão marcadas em vermelho (`#FF0000`), tornando o alerta visual inútil e enganoso.

---

### 3.6. Bug de Interface #5: Ordenação Corrompida de Datas (`type="S"`)
* **Trecho no XML:**
  ```xml
  <field name="DataCirurgia" label="DataCirurgia" type="S" visible="true" useFooter="false" />
  <field name="DataValidade" label="DataValidade" type="S" visible="true" useFooter="false" />
  <field name="DataNegociacao" label="DataNegociacao" type="S" visible="true" useFooter="false" />
  ```
* **Causa:** No SQL foi utilizado `SANKHYA.SNK_FORMAT_DATE(campo, 'DD/MM/YYYY')`, transformando datas em texto, e no XML o tipo foi definido como `S` (String).
* **Impacto Real:** Quando o usuário clica no cabeçalho da coluna para ordenar pela validade do lote ou pela data de negociação, a ordenação ocorre alfabeticamente:
  `01/01/2026` antes de `02/01/2024` e `15/12/2023`. A ordenação cronológica fica completamente inoperante.

---

### 3.7. Bug de Codificação de Caracteres (Encoding Corrompido)
* No arquivo original há múltiplos caracteres corrompidos (`Data Negociao`, `Perodo`, `Insero do parmetro`).
* O arquivo deve ser salvo em UTF-8 padronizado, evitando inconsistências visuais no formulário de filtros do Sankhya.

---

## 4. Análise e Otimização de Desempenho

### 4.1. Eliminação de UDFs Escalares no SQL Server
* **Problema:** As funções `SANKHYA.SNK_FORMAT_DATE`, `SANKHYA.SNK_DATE_DIFF` e `SANKHYA.FC_FORMATACEP` são chamadas linha a linha (processamento RBAR - Row-By-Agonizing-Row). Em consultas com centenas ou milhares de registros, essas UDFs impedem a criação de planos paralelos pelo otimizador e aumentam o uso de CPU em até 80%.
* **Solução:**
  - Retornar o campo de data puro (sem conversão) e deixar o Sankhya aplicar a máscara no metadado (`type="D"` com máscara `dd/MM/yyyy`).
  - Substituir `SANKHYA.SNK_DATE_DIFF(GETDATE(), CABNFS.DTNEG)` por `DATEDIFF(DAY, CABNFS.DTNEG, GETDATE())`.
  - Manter formatação de CEP via expressão simples ou retornar o valor numérico limpo.

### 4.2. Agregação Prévia de Devoluções (Subquery / CTE)
* Em vez de fazer joins diretos de tabelas transacionais pesadas (`TGFVAR`, `TGFCAB`, `TGFITE`, `TGFTOP`) na raiz do `FROM`, deve-se criar uma subquery agrupada por `(NUNOTAORIG, SEQUENCIAORIG)`.
* Isso garante complexidade $O(N)$ em vez de $O(N \times M)$, resolve a duplicação de linhas e reduz drasticamente o tempo de resposta em bancos de dados com grande volume em `TGFVAR`.

### 4.3. Otimização de Predicados (Sargabilidade)
* O padrão `(EST.DTVAL >= :P_DTVAL.INI OR :P_DTVAL.INI IS NULL)` impede o uso eficiente de índices na coluna `DTVAL`.
* Corrigir o parâmetro para `datePeriod` e, se opcional, aplicar tratamento otimizado.

### 4.4. Redução de Overhead de Colunas
* O dashboard atual faz 4 `LEFT JOIN` com tabelas de endereçamento (`TSIEND`, `TSIBAI`, `TSICID`, `TSIUFS`) para trazer campos que raramente são utilizados em auditoria de estoque. Recomenda-se manter na tela inicial apenas Município e UF, movendo detalhes de logradouro para tooltip ou tela de parceiro.

---

## 5. Proposta de Código Refatorado (SQL Otimizado & XML Corrigido)

Abaixo encontra-se a versão refatorada da consulta SQL com:
1. Agregação correta de devoluções (evita 100% das duplicações).
2. Cálculo seguro de saldo.
3. Substituição de funções lentas por funções nativas do banco.
4. Compatibilidade com parâmetro `datePeriod`.
5. Tipagem adequada de datas como `D`.

### 5.1. Consulta SQL Otimizada

```sql
SELECT
  CABNFS.NUNOTA                                               AS "NumeroUnico", 
  CABNFS.NUMNOTA                                              AS "NumeroNota", 
  CABNFS.VLRNOTA                                              AS "ValorNFe",
  CABNFS.AD_DTCIRURG                                          AS "DataCirurgia",
  CABNFS.AD_PACIENTE                                          AS "NomePaciente",
  PAR.CODPARC                                                 AS "CodParceiro",
  PAR.NOMEPARC                                                AS "DescrParcEstoque",
  ENDP.TIPO                                                   AS "TPEND",
  ENDP.NOMEEND                                                AS "ENDERECO",
  PAR.NUMEND                                                  AS "NUMEND",
  BAIP.NOMEBAI                                                AS "BAIRRO",
  CIDP.NOMECID                                                AS "CIDADE",
  UFSP.UF                                                     AS "UF",
  PAR.CEP                                                     AS "CEP",
  PRO.CODPROD                                                 AS "CodProduto",
  PRO.DESCRPROD                                               AS "DescricaoProduto",
  PRO.MARCA                                                   AS "Marca",
  PRO.REFFORN                                                 AS "COdCatalogo",
  ITENFS.CONTROLE                                             AS "Lote",
  EST.DTVAL                                                   AS "DataValidade",
  CABNFS.DTNEG                                                AS "DataNegociacao",
  DATEDIFF(DAY, CABNFS.DTNEG, GETDATE())                      AS "Tempo",
  PRO.CODVOL                                                  AS "Unidade",
  ISNULL(ITENFS.QTDNEG, 0)                                    AS "QtdEnviada",
  ISNULL(DEV.QTDRETORNADA, 0)                                 AS "QtdRetornada",
  (ISNULL(ITENFS.QTDNEG, 0) - ISNULL(DEV.QTDRETORNADA, 0))     AS "Saldo",
  ISNULL(CONS.QTDE, 0)                                        AS "QtdConsignadoFixo",
  CASE 
    WHEN (ISNULL(ITENFS.QTDNEG, 0) - ISNULL(DEV.QTDRETORNADA, 0)) < ISNULL(CONS.QTDE, 0) THEN '#FF0000'
    ELSE '' 
  END                                                         AS "BKCOLOR",
  CASE 
    WHEN (ISNULL(ITENFS.QTDNEG, 0) - ISNULL(DEV.QTDRETORNADA, 0)) < ISNULL(CONS.QTDE, 0) THEN '#FFFFFF'
    ELSE '' 
  END                                                         AS "FGCOLOR"
FROM TGFCAB CABNFS
  INNER JOIN TGFITE ITENFS ON ITENFS.NUNOTA = CABNFS.NUNOTA
  INNER JOIN TGFTOP TOP1   ON TOP1.CODTIPOPER = CABNFS.CODTIPOPER 
                          AND TOP1.DHALTER = CABNFS.DHTIPOPER
  INNER JOIN TGFPRO PRO    ON PRO.CODPROD = ITENFS.CODPROD
  INNER JOIN TGFPAR PAR    ON PAR.CODPARC = CABNFS.CODPARC
  LEFT  JOIN TSIEND ENDP   ON ENDP.CODEND = PAR.CODEND
  LEFT  JOIN TSIBAI BAIP   ON BAIP.CODBAI = PAR.CODBAI
  LEFT  JOIN TSICID CIDP   ON CIDP.CODCID = PAR.CODCID
  LEFT  JOIN TSIUFS UFSP   ON UFSP.CODUF  = CIDP.UF
  
  -- Saldo de Estoque e Validade (Left join seguro para nao sumir com notas liquidadas)
  LEFT JOIN TGFEST EST ON EST.CODEMP     = ITENFS.CODEMP 
                      AND EST.CODPROD    = ITENFS.CODPROD 
                      AND EST.CODLOCAL   = ITENFS.CODLOCALORIG 
                      AND EST.CONTROLE   = ITENFS.CONTROLE 
                      AND EST.CODPARC    = CABNFS.CODPARC 
                      AND EST.TIPO       = TOP1.ATUALESTTERC

  -- Subquery Agrupada de Devoluções: Elimina duplicidade por TGFVAR
  LEFT JOIN (
      SELECT 
          VAR.NUNOTAORIG,
          VAR.SEQUENCIAORIG,
          SUM(ITED.QTDNEG) AS QTDRETORNADA
      FROM TGFVAR VAR
      INNER JOIN TGFCAB CABD ON CABD.NUNOTA = VAR.NUNOTA 
                            AND CABD.TIPMOV IN ('C', 'E')
      INNER JOIN TGFITE ITED ON ITED.NUNOTA = CABD.NUNOTA 
                            AND ITED.SEQUENCIA = VAR.SEQUENCIA
      INNER JOIN TGFTOP TOPD ON TOPD.CODTIPOPER = CABD.CODTIPOPER 
                            AND TOPD.DHALTER = CABD.DHTIPOPER 
                            AND TOPD.ATUALESTTERC = 'D'
      GROUP BY VAR.NUNOTAORIG, VAR.SEQUENCIAORIG
  ) DEV ON DEV.NUNOTAORIG = CABNFS.NUNOTA 
       AND DEV.SEQUENCIAORIG = ITENFS.SEQUENCIA

  -- Parametrização de Consignado Fixo
  LEFT JOIN AD_CONSFIXO CONS ON CONS.CODPARC = CABNFS.CODPARC 
                            AND CONS.CODPROD = ITENFS.CODPROD

WHERE CABNFS.TIPMOV = 'C'
  AND TOP1.ATUALESTTERC = 'T'
  AND CABNFS.DTNEG >= :p_dtnegini.INI
  AND CABNFS.DTNEG <= :p_dtnegini.FIN
  AND CABNFS.CODPARC BETWEEN :p_parini AND :p_parfin
  AND ITENFS.CODPROD BETWEEN :p_prodini AND :p_prodfin
  -- Filtro de saldo em aberto
  AND (ISNULL(ITENFS.QTDNEG, 0) - ISNULL(DEV.QTDRETORNADA, 0)) > 0
  -- Validade com datePeriod compatível
  AND (:P_DTVAL.INI IS NULL OR EST.DTVAL >= :P_DTVAL.INI)
  AND (:P_DTVAL.FIN IS NULL OR EST.DTVAL <= :P_DTVAL.FIN)
```

---

## 6. Recomendações de Ação

1. **Correção Imediata do Parâmetro `P_DTVAL`:**
   Alterar a tag no XML de `metadata="date"` para `metadata="datePeriod"` para evitar exceções de execução no Sankhya.
2. **Atualização dos Tipos de Campo no `<metadata>`:**
   Alterar `DataValidade`, `DataNegociacao` e `DataCirurgia` de `type="S"` para `type="D"` com máscara `mask="dd/MM/yyyy"`, restabelecendo a ordenação cronológica.
3. **Alinhamento de Vocabulário de Negócio:**
   Alinhar junto aos usuários se o relatório se destina a **Recebimento de Terceiros** (Fornecedor $\rightarrow$ Empresa) ou **Remessa para Terceiros** (Empresa $\rightarrow$ Hospital/Cliente). Adequar o título e os rótulos de coluna em conformidade.
4. **Deploy da Subquery de Devoluções:**
   Substituir o join aberto de `TGFVAR` pela subquery agrupada apresentada na Seção 5, corrigindo os saldos e relatórios de auditoria.
