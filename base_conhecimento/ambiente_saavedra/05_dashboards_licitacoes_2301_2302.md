# 📊 Dashboards de Licitações (Dash 2301 e 2302) — Mapeamento e Inclusão de Modalidade

Este documento registra a arquitetura das consultas SQL e a resolução técnica aplicada para integrar o campo **MODALIDADE** no **Dash 2302** a partir da estrutura existente no **Dash 2301** (ERP Sankhya / Módulo LGH de Licitações).

---

## 1. Contexto dos Dashboards

* **Dash 2301 (`DASH - ACOMPANHAMENTO PORTAL LICITAÇAO`):**
  * **Foco:** Visão das propostas e itens licitados (`LGH_LICITE` e `LGH_LICCAB`).
  * **Origem da Modalidade:** O cabeçalho da licitação possui a chave estrangeira `NUMODALIDADE` ligada à tabela `LGH_LICMOD`.
  * **Exibição:** Campo `MODALIDADE` (ex: *Compra Direta, Pregão Eletrônico, Concorrência, Dispensa Eletrônica, Aditivo de Contrato*).

* **Dash 2302 (`DASH - ACOMPANHAMENTO CONTRATOS DE LICITACAO`):**
  * **Foco:** Gestão de contratos decorrentes das licitações (`LGH_LICITECON`, `LGH_LICCONT` e `TCSCON`), saldos previstos, faturados e estoque disponível.
  * **Necessidade:** Exibir a **Modalidade** da licitação vinculada a cada contrato sem quebrar filtros, cálculos de saldo ou descartar linhas.

---

## 2. Desafio Técnico e Modelo de Dados

No ERP Sankhya, a estrutura do módulo de licitações (`LGH`) relaciona os dados da seguinte forma:

```
[ LGH_LICMOD ] (Modalidades)
       │  NUMODALIDADE
       ▼
[ LGH_LICCAB ] (Cabeçalho da Licitação: NULIC, PROCESSO, PREGAO)
       ▲
       │  NULIC
       ├─────────────────────────────────────────┐
       │                                         │
[ LGH_LICCONT ] (Vínculo Licitação x Contrato)    [ TCSCON ] (Contrato Comercial / Nativo)
   NUMCONTRATO / NULIC                             NUMCONTRATO / LGH_NULINC
       │                                         │
       └────────────────────┬────────────────────┘
                            │ NUMCONTRATO
                            ▼
                    [ LGH_LICITECON ] (Itens do Contrato)
```

### O Desafio:
1. O Dash 2302 parte de contratos (`LGH_LICITECON` / `LGH_LICCONT` / `TCSCON`) e **não tinha** junção direta com o cabeçalho da licitação (`LGH_LICCAB`).
2. Contratos podem ter a chave gravada nativamente em `LGH_LICCONT.NULIC` ou no campo complementar `TCSCON.LGH_NULINC`.
3. Não podia haver multiplicação de linhas (`JOIN 1:N`) e nem descarte de contratos que eventualmente não possuíssem licitação (`INNER JOIN`).
4. A consulta do Dash 2302 possui cláusula `GROUP BY`. Em SQL Server, qualquer coluna incluída no `SELECT` que não seja função de agregação **deve** obrigatoriamente constar no `GROUP BY`.

---

## 3. Solução Técnica Aplicada

### Passo 1: `JOIN` Seguro com Fallback (`ISNULL` + `NULLIF`)
Utilizamos `LEFT JOIN` com fallback inteligente: se `LGH_LICCONT.NULIC` for nulo ou zero, o sistema busca `TCSCON.LGH_NULINC`.

```sql
LEFT JOIN LGH_LICCAB ON LGH_LICCAB.NULIC = ISNULL(NULLIF(LGH_LICCONT.NULIC, 0), TCSCON.LGH_NULINC)
LEFT JOIN LGH_LICMOD ON LGH_LICMOD.NUMODALIDADE = LGH_LICCAB.NUMODALIDADE
```

* **Garantia de Não Descarte:** Por ser `LEFT JOIN`, contratos sem licitação continuam aparecendo normalmente (o campo fica em branco, sem quebrar o dashboard).
* **Garantia de Não Duplicação:** Como `NULIC` é a chave primária de `LGH_LICCAB` e `NUMODALIDADE` é a chave primária de `LGH_LICMOD`, a relação é estritamente `1:1`.

---

### Passo 2: Projeção no `SELECT`
Incluída a coluna com o alias padronizado `MODALIDADE` logo após o `PREGAO`:

```sql
SELECT LGH_LICITECON.NUMCONTRATO CONTRATO,
	TCSCON.LGH_PROCESSO AS NR_PROCESSO,
	TCSCON.AD_PREGAO AS PREGAO,
	LGH_LICMOD.DESCRICAO AS MODALIDADE,
	LGH_LICCONT.NUMEROCONTRATOCLIENTE AS CONT_CLIENTE,
    ...
```

---

### Passo 3: Conformidade com o `GROUP BY`
Adicionado `LGH_LICMOD.DESCRICAO` à cláusula `GROUP BY`, evitando o erro de compilação SQL Server:

```sql
GROUP BY 
	LGH_LICITECON.NUMCONTRATO,
	TCSCON.LGH_PROCESSO,
	TCSCON.AD_PREGAO,
	LGH_LICMOD.DESCRICAO,
	LGH_LICCONT.NUMEROCONTRATOCLIENTE,
    ...
```

---

### Passo 4: Metadados XML do Grid Sankhya
Para que o Sankhya reconheça a nova coluna e a renderize com visibilidade e tipagem de String (`type="S"`), foi inserido o bloco nos `<metadata>` do gadget:

```xml
<field name="MODALIDADE" label="MODALIDADE" type="S" visible="true" useFooter="false">
</field>
```

---

## 4. Resumo das Tabelas Envolvidas

| Tabela | Descrição | Papel no Dash | Chave de Ligação |
| :--- | :--- | :--- | :--- |
| `LGH_LICMOD` | Modalidades de Licitação | Fornece `DESCRICAO` da modalidade | `NUMODALIDADE` |
| `LGH_LICCAB` | Cabeçalho da Licitação | Ponte entre contrato e modalidade | `NULIC` / `NUMODALIDADE` |
| `LGH_LICCONT` | Vínculo Contratos x Licitação | Armazena o `NULIC` gerador do contrato | `NUMCONTRATO` / `NULIC` |
| `TCSCON` | Contrato Padrão ERP | Armazena dados gerais e `LGH_NULINC` | `NUMCONTRATO` |
| `LGH_LICITECON` | Itens Contratados | Tabela base de produtos e valores do contrato | `NUMCONTRATO` / `CODPROD` |

---

## 5. Resolução de Saldo Negativo e Programações em Termos Aditivos

### Cenário Identificado:
Quando um contrato antigo de licitação (ex: Contrato `8` do HCPA) recebe um Termo Aditivo / Prorrogação (ex: Contrato `332` do Aditivo `1304`), ambos compartilham o mesmo número de Pregão (`TCSCON.AD_PREGAO = '463/2022'`).

### Causa do Problema:
As subqueries de cálculo de `QTD_PROGRAMADA`, `QTD_FATURADA`, `SLD_PRODUTO` e `SLD_DISPONIVEL` estavam agrupando pelo pregão compartilhado:
```sql
CON.AD_PREGAO = TCSCON.AD_PREGAO AND TGFITE.CODPROD = LGH_LICITECON.CODPROD
```
Isso fazia com que o Aditivo novo (332) herdasse todo o histórico de faturamento dos 4 anos do contrato anterior (Contrato 8), gerando **saldos negativos** (`Previsto do Aditivo - Faturado de 4 Anos`) e exibindo programações pendentes do contrato antigo na linha do novo termo.

### Correção Aplicada (Gadget 57):
Amarração direta das subqueries ao contrato específico da linha (`NUMCONTRATO`):
```sql
TGFCAB.NUMCONTRATO = LGH_LICITECON.NUMCONTRATO AND TGFITE.CODPROD = LGH_LICITECON.CODPROD
```
* **Contratos sem aditivo:** Permanecem inalterados.
* **Contratos com aditivo:** Cada contrato/aditivo passa a exibir rigorosamente seu próprio previsto, seu faturamento individual e seu saldo livre real.

