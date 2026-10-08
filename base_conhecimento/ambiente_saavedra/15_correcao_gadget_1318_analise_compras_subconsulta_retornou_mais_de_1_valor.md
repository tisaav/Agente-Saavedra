# 📋 Guia de Resolução: Correção de Erro de Subconsulta no Gadget 1318 - Análise de Compras

> **Público:** Compradores, Gestores de Suprimentos, Diretoria e Suporte de TI  
> **Telas do Sankhya:** Gadget 1318 (Análise de Compras) / Portal de Compras / Construtor de Componentes de BI  
> **Status:** Resolvido, Testado e Homologado em Produção  

---

## 📌 1. O Problema (O que o usuário viu)

Ao abrir o **Gadget 1318 - ANALISE COMPRAS** (utilizado diariamente pelo setor de compras e suprimentos da Saavedra para análise de estoque, cobertura e sugestão inteligente de reposição):

* O painel travava com uma tela cinza e exibia o seguinte pop-up de erro impeditivo do Sankhya:
  > **[Gadget 1318 - ANALISE COMPRAS] A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, <, <=, >, >= ou quando ela é usada como uma expressão.**  
  > **Código : CORE_E05294**
* A falha impedia completamente a geração da grade com as sugestões de compra, cálculo de dias de cobertura e médias de venda para os produtos e marcas da empresa.

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

1. **A Regra de Ouro das Subconsultas no Banco de Dados:**  
   Em uma consulta SQL, quando uma coluna depende de uma busca secundária (subconsulta escalar), ela é obrigada a devolver **exatamente 1 valor** (uma única célula). Se a busca devolver duas ou mais linhas, o banco de dados aborta a consulta inteira com o código `CORE_E05294`.

2. **A Falha no Filtro de Metas (`SELLIN_MES`):**  
   Na consulta principal do gadget (`grd_029`), a coluna de meta mensal de vendas (`SELLIN_MES`) buscava dados na tabela de metas do ERP (`TGFMET` para a meta `CODMETA = 17`) com a seguinte condição:
   ```sql
   MONTH(DTREF) = MONTH(GETDATE())
   ```
   **O erro:** O sistema verificava apenas o mês (mês 10 - Outubro), mas **não filtrava o ano**. Como na base de dados já existiam metas cadastradas tanto para **Outubro/2025** quanto para **Outubro/2026** (especialmente para as marcas da Becton Dickinson: `5 - BD UCC`, `6 - BD PIB`, `7 - BD PIO` e `8 - BD AAD`), a subconsulta encontrava 2 registros para a mesma marca.

3. **Ausência de Agregação (`SUM`):**  
   Além de não filtrar o ano vigente, a expressão fazia `SELECT TGFMET.PREVDESP` sem utilizar `SUM()` nem `ISNULL()`. Assim, ao encontrar 2 linhas com valores de meta, o sistema quebrava imediatamente.

4. **Inconsistência Lógica Adicional Identificada (`PED_COM_MES`):**  
   No campo de pedidos de compras do mês (`PED_COM_MES`), existia um problema similar: a cláusula usava `MONTH(C.DTNEG) = MONTH(GETDATE())` sem travar o ano. Embora não causasse erro de subconsulta por possuir `SUM()`, ela estava somando indevidamente pedidos de compras de todos os outubros do histórico da empresa.

---

## ✅ 3. O que fizemos para arrumar?

### Passo 1: Blindagem da Subconsulta de Metas (`SELLIN_MES`)
Reescrevemos a subconsulta inserindo duas proteções fundamentais:
* **Filtro de Ano Vigente:** Adicionada a cláusula `AND YEAR(DTREF) = YEAR(GETDATE())`.
* **Agregação Segura e Tratamento de Nulos:** Envelopado o campo com `ISNULL(SUM(TGFMET.PREVDESP), 0)`. Isso garante matematicamente que a subconsulta sempre retorne um único número escalar (mesmo que no futuro uma meta seja desdobrada por vendedor ou filial).

### Passo 2: Correção do Histórico em `PED_COM_MES`
* Adicionado o filtro de ano `AND YEAR(C.DTNEG) = YEAR(GETDATE())` para que a coluna reflita estritamente as compras do mês atual do ano corrente.

### Passo 3: Atualização do Componente no Sankhya
* O XML de configuração do componente foi atualizado na tabela interna de gadgets (`TSIGDG`, registro `NUGDG = 72`), restabelecendo o funcionamento imediato para todos os usuários do sistema.

---

## 👤 4. Como o usuário valida no dia a dia?

1. No Sankhya, abra o **Portal de Compras** ou busque por **1318 - ANALISE COMPRAS**.
2. Preencha os parâmetros de filtro:
   * **Meses de Venda:** Ex: `4`
   * **Meses Estoque:** Ex: `3`
   * **Dias p/ receber o produto:** Ex: `7`
   * **Marca:** Deixe em branco para todas ou selecione marcas específicas (ex: marcas BD `5`, `6`, `7` ou `8`).
   * **Perfil do Cliente:** Selecione os perfis desejados.
3. Clique em **Aplicar / Concluir**.
4. **Resultado:**
   * A tela abre de imediato sem nenhum pop-up de erro.
   * Os campos `SELLIN_MES` exibem a meta exata do mês/ano corrente.
   * As colunas de Estoque, Cobertura, Média Dia/Mês e Sugestão de Compras operam com dados 100% íntegros.

---

## 🔧 5. Detalhes Técnicos (Para TI e Banco de Dados)

* **Componente:** `1318 - ANALISE COMPRAS`
* **Identificador no Banco:** Tabela `TSIGDG`, campo `NUGDG = 72`.
* **Tabela de Metas:** `TGFMET` (`CODMETA = 17` - Metas por Marca/Produto).

### Comparativo do SQL (Antes vs Depois)

#### 1. Coluna `SELLIN_MES`:
```sql
-- ANTES (Causava o estouro CORE_E05294 com retorno de 2 linhas):
(SELECT TGFMET.PREVDESP 
 FROM TGFMET 
 WHERE TGFMET.CODMETA = 17 
   AND TGFMET.MARCA = PRO.CODMARCA 
   AND MONTH(DTREF) = MONTH(GETDATE())) AS SELLIN_MES

-- DEPOIS (Corrigido, blindado e restrito ao ano atual):
(SELECT ISNULL(SUM(TGFMET.PREVDESP), 0) 
 FROM TGFMET 
 WHERE TGFMET.CODMETA = 17 
   AND TGFMET.MARCA = PRO.CODMARCA 
   AND MONTH(DTREF) = MONTH(GETDATE()) 
   AND YEAR(DTREF) = YEAR(GETDATE())) AS SELLIN_MES
```

#### 2. Coluna `PED_COM_MES`:
```sql
-- ANTES (Somava todos os anos do histórico no mesmo mês):
(SELECT ISNULL(SUM(I.VLRTOT),0)  
 FROM TGFITE AS I, TGFCAB AS C, TGFPRO AS P 
 WHERE MONTH(C.DTNEG) = MONTH(GETDATE()) 
   AND I.CODPROD = P.CODPROD 
   AND I.CODCFO <> 0 
   AND P.CODMARCA = PRO.CODMARCA 
   AND C.CODTIPOPER IN (100) 
   AND I.NUNOTA = C.NUNOTA 
   AND (C.TIPMOV = 'P') 
   AND (C.STATUSNOTA = 'L')) AS PED_COM_MES

-- DEPOIS (Restrito ao ano corrente):
(SELECT ISNULL(SUM(I.VLRTOT),0)  
 FROM TGFITE AS I, TGFCAB AS C, TGFPRO AS P 
 WHERE MONTH(C.DTNEG) = MONTH(GETDATE()) 
   AND YEAR(C.DTNEG) = YEAR(GETDATE()) 
   AND I.CODPROD = P.CODPROD 
   AND I.CODCFO <> 0 
   AND P.CODMARCA = PRO.CODMARCA 
   AND C.CODTIPOPER IN (100) 
   AND I.NUNOTA = C.NUNOTA 
   AND (C.TIPMOV = 'P') 
   AND (C.STATUSNOTA = 'L')) AS PED_COM_MES
```

### Arquivos de Backup e Configuração Salvos no Repositório
* `base_conhecimento/ambiente_saavedra/15_correcao_gadget_1318_analise_compras_subconsulta_retornou_mais_de_1_valor.md` (Esta documentação)
* `gadget_1318_corrigido.xml` (Arquivo XML completo homologado)
