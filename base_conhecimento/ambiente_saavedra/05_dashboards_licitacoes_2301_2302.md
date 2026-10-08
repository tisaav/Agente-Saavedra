# 📋 Guia de Resolução: Dashboards de Licitações (Dash 2301 e 2302) — Inclusão de Modalidade e Correção de Termos Aditivos

> **Público:** Setor de Licitações e Contratos, Comercial, Faturamento, Diretoria e Suporte de TI  
> **Telas do Sankhya:** Dash 2302 (`DASH - ACOMPANHAMENTO CONTRATOS DE LICITACAO`), Dash 2301 (`DASH - ACOMPANHAMENTO PORTAL LICITACAO`) / Gadget 57  
> **Status:** Resolvido, Testado e Homologado em Produção  

---

## 📌 1. O Problema (O que o usuário viu)

No setor de licitações da Saavedra, dois problemas operacionais sérios estavam ocorrendo no painel principal de gestão de contratos (**Dash 2302**):

1. **Falta de Identificação de Modalidades e Aditivos:**  
   Na grade do Dash 2302, os usuários conseguiam ver o número do pregão e o contrato, mas **não sabiam qual era a modalidade da licitação** (por exemplo: se aquele contrato veio de um *Pregão Eletrônico*, de uma *Dispensa*, de uma *Compra Direta* ou se tratava-se de um **Termo Aditivo de Contrato**). Para descobrir isso, o colaborador precisava sair do painel e consultar manualmente outros módulos ou o Dash 2301.

2. **Termos Aditivos com Saldo Negativo e Pedidos "Fantasmas" (Caso Crítico do HCPA):**  
   Quando um contrato antigo de licitação recebia um aditivo de prorrogação (exemplo: **Contrato 8 do HCPA** que foi prorrogado pelo **Aditivo 1304 / Contrato 332**), a linha do novo aditivo nascia no dashboard com:
   * **Saldo de produto negativo** (ex: `-160`, `-90`, `-330` unidades).
   * **Pedidos programados do contrato antigo aparecendo indevidamente na linha do novo aditivo**.
   * Isso gerava desespero operacional na equipe, pois parecia que a Saavedra já havia entregue mais produtos do que o cliente tinha direito no novo aditivo, quando na verdade o novo aditivo mal havia começado e seu saldo deveria estar 100% zerado e livre!

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

Para entender de forma muito fácil:

### A) Por que a modalidade não aparecia?
No sistema Sankhya, as informações de editais e propostas ficam em uma gaveta chamada `LGH_LICCAB` (Cabeçalho da Licitação) e as modalidades em `LGH_LICMOD`.  
Porém, o painel Dash 2302 foi construído olhando apenas para a gaveta de contratos (`TCSCON` e `LGH_LICITECON`). Como as duas gavetas não estavam interligadas na consulta do painel, a coluna "Modalidade" simplesmente não existia para ser exibida na tela.

### B) Por que o saldo do Aditivo ficava negativo?
Pense que o Hospital de Clínicas (HCPA) fez um Pregão em 2022 (`Pregão 463/2022`).
* Nos primeiros 4 anos (Contrato 8), a Saavedra faturou **1.160 unidades** de um produto.
* Em 2026, o hospital renovou a parceria através de um **Termo Aditivo de 1 ano** (Contrato 332) para fornecer mais **1.000 unidades**.
* Como o aditivo é continuação da mesma licitação, os dois contratos carregavam o mesmo número de pregão (`463/2022`).
* **A falha na fórmula:** O painel calculava o saldo somando todas as notas emitidas que tivessem o pregão `463/2022`. Com isso, a linha do novo aditivo somava as notas dos 4 anos anteriores inteiros!
* **A conta errada:**  
  $$\text{Saldo} = 1.000 \text{ (Previsto do Aditivo)} - 1.160 \text{ (Faturado dos últimos 4 anos)} = \mathbf{-160 \text{ unidades}}$$
* Além disso, se o contrato antigo tivesse 20 agulhas programadas para entrega, essas 20 agulhas pulavam para dentro do aditivo novo.

---

## ✅ 3. O que fizemos para arrumar?

### Passo 1: Construção da "Ponte" para trazer a Modalidade ao Grid
Criamos uma junção inteligente e segura (`LEFT JOIN`) com verificação dupla (`ISNULL` e `NULLIF`).  
O sistema agora busca a licitação tanto se ela estiver cadastrada nativamente pelo módulo de licitações (`LGH_LICCONT.NULIC`) quanto se estiver preenchida no contrato comercial (`TCSCON.LGH_NULINC`).
* **Resultado:** Se o contrato tiver licitação, ele mostra com clareza: *"Pregão Eletrônico"*, *"Dispensa Eletrônica"*, *"Aditivo de Contrato"*, etc. Se for um contrato avulso sem licitação, a linha continua aparecendo normalmente, sem travar o painel.

### Passo 2: Separação Individual de Faturamento por Contrato
Reescrevemos as fórmulas de cálculo de faturamento, pedidos programados e saldos dentro da consulta do **Gadget 57**.  
Em vez de somar pelo pregão genérico, o sistema foi programado para respeitar rigorosamente o **Número do Contrato específico daquela linha** (`TGFCAB.NUMCONTRATO = LGH_LICITECON.NUMCONTRATO`).
* **Resultado:** O contrato antigo (8) continua com seus 4 anos de faturamento e seu saldo restante exato. E o novo Aditivo (332) nasce limpo, com 0 faturado, 0 programado e com todas as 1.000 unidades livres para atendimento!

---

## 👤 4. Como o usuário valida no dia a dia?

Para conferir o funcionamento no Sankhya:

1. Acesse o menu e abra o **Dash 2302 - ACOMPANHAMENTO CONTRATOS DE LICITACAO**.
2. Nos filtros do topo, informe o período desejado ou pesquise pelo parceiro **HCPA** (Hospital de Clínicas de Porto Alegre) ou qualquer outro cliente com aditivo.
3. Clique em **Aplicar**:
   * **Nova Coluna MODALIDADE:** Veja que logo ao lado do número do Pregão existe a coluna **MODALIDADE**, indicando se o registro é um *Pregão Eletrônico*, *Dispensa*, *Aditivo de Contrato*, etc.
   * **Contrato Antigo (Ex: Contrato 8):** Exibe exatamente o saldo residual real que ainda faltava consumir.
   * **Termo Aditivo (Ex: Contrato 332):** Exibe a quantidade total contratada no aditivo com saldo 100% positivo e livre, sem números negativos em vermelho e sem herdar programações antigas.

---

## 🔧 5. Detalhes Técnicos e Código SQL Aplicado

Para referência da equipe de TI e auditoria do banco de dados:

* **Objeto do ERP:** Componente de BI / Gadget `57` (`NUGDG = 57`) na tabela `TSIGDG`.
* **Data-Source:** `MGEDS` (SQL Server).

### 5.1. Relacionamento da Modalidade (Passo 1)
```sql
LEFT JOIN LGH_LICCAB ON LGH_LICCAB.NULIC = ISNULL(NULLIF(LGH_LICCONT.NULIC, 0), TCSCON.LGH_NULINC)
LEFT JOIN LGH_LICMOD ON LGH_LICMOD.NUMODALIDADE = LGH_LICCAB.NUMODALIDADE
```
* Coluna projetada: `LGH_LICMOD.DESCRICAO AS MODALIDADE`
* Adicionada obrigatoriamente à cláusula `GROUP BY`.
* Metadado no XML:
  ```xml
  <field name="MODALIDADE" label="MODALIDADE" type="S" visible="true" useFooter="false">
  </field>
  ```

### 5.2. Correção de Isolamento de Faturamento por Contrato (Passo 2)
Substituição da cláusula de cruzamento nas subqueries:

```sql
-- ANTES (Causava soma indevida entre aditivos e contratos do mesmo pregão):
CON.AD_PREGAO = TCSCON.AD_PREGAO AND TGFITE.CODPROD = LGH_LICITECON.CODPROD

-- DEPOIS (Blindado por Contrato específico da linha):
TGFCAB.NUMCONTRATO = LGH_LICITECON.NUMCONTRATO AND TGFITE.CODPROD = LGH_LICITECON.CODPROD
```

Campos corrigidos com essa amarração:
* `QTD_PROGRAMADA`: Pedidos pendentes vinculados estritamente ao contrato.
* `QTD_FATURADA`: Notas de venda emitidas estritamente para o contrato.
* `VLR_FATURADO`: Valor financeiro já atendido no contrato.
* `SLD_PRODUTO`: `QtdPrevista - QtdFaturada`.
* `SLD_DISPONIVEL`: `QtdPrevista - QtdProgramada - QtdFaturada`.
* `PER_ATENDIDO`: `%` real de cumprimento do contrato/aditivo individual.

---

## 📂 6. Arquivos Relacionados no Projeto

* **XML Homologado e Ativo em Produção:** [`Dashboards/metadata_2302_-_acompanhamento_contratos_de_licitacao/dashboardMetadata_corrigido.xml`](file:///c:/Users/SAAV166/Documents/Agente/Dashboards/metadata_2302_-_acompanhamento_contratos_de_licitacao/dashboardMetadata_corrigido.xml)
* **XML de Backup Histórico:** [`Dashboards/metadata_2302_-_acompanhamento_contratos_de_licitacao/dashboardMetadata_backup_original.xml`](file:///c:/Users/SAAV166/Documents/Agente/Dashboards/metadata_2302_-_acompanhamento_contratos_de_licitacao/dashboardMetadata_backup_original.xml)
* **Arquivo Microsoft Word / Google Docs:** `G:\Drives compartilhados\Informatica\Documentacoes Sankhya - Melhorias e Consertos\05_dashboards_licitacoes_2301_2302.docx`
