# 📊 Documentação Técnica e Correções: Dashboard Sankhya 2302

**Componente:** `2302 - ACOMPANHAMENTO CONTRATOS DE LICITACAO`  
**Identificador Sankhya:** Gadget `57` (Tabela `TSIGDG`, `NUGDG = 57`)  
**Data da Implementação / Homologação:** Outubro de 2026  
**Ambiente:** Sankhya ERP / MGE - Data-Source: `MGEDS` (SQL Server)  
**Status em Produção:** Homologado e Ativo em Produção  

---

## 1. Visão Geral

O **Dashboard 2302** é o painel gerencial utilizado pelo setor de licitações e contratos para acompanhar o cumprimento, faturamento, pedidos programados e saldos disponíveis de contratos públicos e termos aditivos decorrentes de licitações (módulo `LGH` da Sankhya).

Durante os trabalhos de suporte e melhoria contínua, foram realizadas **duas intervenções estruturais críticas** neste dashboard:
1. **Inclusão do Campo `MODALIDADE` (Identificador de Aditivos e Tipos de Licitação):** Trazendo a classificação de modalidades a partir do Dash 2301.
2. **Correção do Cálculo de Saldos em Termos Aditivos / Prorrogações (Caso HCPA):** Desacoplamento do faturamento entre contratos que compartilham o mesmo número de Pregão.

---

## 2. Intervenção 1: Inclusão do Campo `MODALIDADE`

### 2.1. O Desafio
* No **Dash 2301** (`DASH - ACOMPANHAMENTO PORTAL LICITACAO`), as propostas eram classificadas pela modalidade (`LGH_LICMOD.DESCRICAO`), permitindo saber se tratava-se de *Pregão Eletrônico*, *Dispensa*, *Compra Direta* ou *Aditivo de Contrato*.
* No **Dash 2302**, os usuários viam apenas o número do contrato e pregão, sem identificar diretamente na grade se aquele contrato correspondia a um Aditivo ou a outra modalidade específica.
* A consulta SQL original do Dash 2302 não continha ligação com o cabeçalho de licitação (`LGH_LICCAB`) e possui cláusulas de agregação (`GROUP BY`), exigindo que qualquer campo novo fosse tratado sem quebrar agrupamentos ou descartar linhas.

### 2.2. Solução Técnica Aplicada
1. **Junção com Fallback (`LEFT JOIN`):**
   ```sql
   LEFT JOIN LGH_LICCAB ON LGH_LICCAB.NULIC = ISNULL(NULLIF(LGH_LICCONT.NULIC, 0), TCSCON.LGH_NULINC)
   LEFT JOIN LGH_LICMOD ON LGH_LICMOD.NUMODALIDADE = LGH_LICCAB.NUMODALIDADE
   ```
2. **Projeção no `SELECT`:**
   ```sql
   LGH_LICMOD.DESCRICAO AS MODALIDADE,
   ```
3. **Agrupamento (`GROUP BY`):**
   ```sql
   LGH_LICMOD.DESCRICAO,
   ```
4. **Metadados XML do Grid Sankhya:**
   ```xml
   <field name="MODALIDADE" label="MODALIDADE" type="S" visible="true" useFooter="false">
   </field>
   ```

---

## 3. Intervenção 2: Resolução de Saldo Negativo em Termos Aditivos (Caso HCPA)

### 3.1. Cenário e Problema Identificado
Uma usuária reportou que no Dash 2302 o novo termo aditivo do HCPA estava nascendo com saldo negativo e com pedidos do contrato anterior pendentes:
* **Contrato 8:** Contrato original HCPA (Vigência 16/09/2022 a 16/09/2026).
* **Contrato 332:** Aditivo 1304 (Prorrogação para 16/09/2026 a 16/09/2027).
* **Problema:** Ambos os contratos compartilhavam o mesmo número de Pregão (`TCSCON.AD_PREGAO = '463/2022'`).

### 3.2. Causa Raiz
As subqueries do Gadget 57 que calculavam `QTD_PROGRAMADA`, `QTD_FATURADA`, `SLD_PRODUTO` e `SLD_DISPONIVEL` amarravam as notas e pedidos por **Pregão**:
```sql
CON.AD_PREGAO = TCSCON.AD_PREGAO AND TGFITE.CODPROD = LGH_LICITECON.CODPROD
```
Como o pregão era idêntico, o Aditivo novo (332) somava todas as notas emitidas ao longo de 4 anos pelo Contrato 8. Como a cota anual do aditivo era menor que o total faturado em 4 anos, a conta `QtdPrevista - QtdFaturada` resultava em **valores negativos** (ex: `-160`, `-90`, `-330`).

### 3.3. Correção Aplicada
As subqueries foram reescritas para amarrar o faturamento e as programações estritamente ao contrato daquela linha (`TGFCAB.NUMCONTRATO = LGH_LICITECON.NUMCONTRATO`):

```sql
-- Faturado individualizado por Contrato/Aditivo:
(SELECT ISNULL(SUM(TGFITE.QTDNEG),0) 
 FROM TGFCAB 
 INNER JOIN TGFITE ON TGFITE.NUNOTA = TGFCAB.NUNOTA 
 WHERE TGFCAB.TIPMOV = 'V' AND 
     TGFCAB.SERIENOTA = 2 AND 
     TGFCAB.CODTIPOPER IN ('1000','1100','1107') AND 
     TGFCAB.NUMCONTRATO = LGH_LICITECON.NUMCONTRATO AND 
     TGFITE.CODPROD = LGH_LICITECON.CODPROD) AS QTD_FATURADA
```

A mesma amarração foi aplicada para:
* `QTD_PROGRAMADA`
* `VLR_FATURADO`
* `SLD_PRODUTO`
* `SLD_DISPONIVEL`
* `PER_ATENDIDO`

### 3.4. Resultado Obtido
* **Contrato Original (8):** Manteve seu histórico de faturamento e saldo restante fidedigno.
* **Aditivo (332):** Passou a nascer com 0 faturado, 0 programado e 100% de saldo livre disponível.

---

## 4. Arquivos Armazenados na Workspace

| Arquivo | Descrição |
| :--- | :--- |
| [dashboardMetadata_corrigido.xml](file:///c:/Users/SAAV166/Documents/Agente/Dashboards/metadata_2302_-_acompanhamento_contratos_de_licitacao/dashboardMetadata_corrigido.xml) | **Versão Final Homologada e em Produção**. Contém a coluna `MODALIDADE` e as subqueries corrigidas por contrato. |
| [dashboardMetadata_backup_original.xml](file:///c:/Users/SAAV166/Documents/Agente/Dashboards/metadata_2302_-_acompanhamento_contratos_de_licitacao/dashboardMetadata_backup_original.xml) | Backup da consulta anterior para referência histórica. |
| [DOCUMENTACAO_E_CORRECOES_DASHBOARD_2302.md](file:///c:/Users/SAAV166/Documents/Agente/Dashboards/metadata_2302_-_acompanhamento_contratos_de_licitacao/DOCUMENTACAO_E_CORRECOES_DASHBOARD_2302.md) | Este documento técnico de referência. |
| [05_dashboards_licitacoes_2301_2302.md](file:///c:/Users/SAAV166/Documents/Agente/base_conhecimento/ambiente_saavedra/05_dashboards_licitacoes_2301_2302.md) | Registro detalhado na Base de Conhecimento do Ambiente Saavedra. |
