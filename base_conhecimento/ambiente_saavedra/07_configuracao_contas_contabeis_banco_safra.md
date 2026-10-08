# 📋 Registro de Configuração: Contas Contábeis dos Fundos de Investimento Banco Safra

> **Público:** Usuários, Financeiro, Contabilidade e Suporte  
> **Data:** 05/10/2026  
> **Status:** Configurado e Validado com Sucesso  

---

## 📌 1. O Cenário / Solicitação

O departamento Financeiro abriu três novas contas de investimento no **Banco Safra** e solicitou a amarração contábil no Sankhya:
* **Safra Vitesse** (conta contábil `7325`)
* **Safra Alfa Polaris Fi RF CP** (conta contábil `7327`)
* **Safra Extra Bancos Special FIC** (conta contábil `7329`)
* E questionou sobre a conta corrente principal do Banco Safra (sugerindo `7299` caso não existisse).

---

## 🔍 2. O que foi verificado no Sistema

1. **Conta Corrente do Banco Safra:** Já existia no plano de contas sob o código **`7280`** (`1.1.1.02.001.7280 - BANCO SAFRA S.A.`), vinculada certinho à conta corrente bancária `584391-9`. Portanto, não foi necessário criar a 7299.
2. **Fundos de Investimento do Safra:** As contas bancárias já haviam sido abertas no sistema, mas estavam apontando provisoriamente para a conta corrente `7280` porque as contas analíticas de aplicação ainda não existiam no grupo `1.1.1.03` do Plano de Contas.

---

## ✅ 3. O que foi configurado e validado

As 3 contas contábeis foram criadas no **Plano de Contas** e amarradas no cadastro de **Contas Bancárias**:

| Cód. Sankhya | Nome da Conta Bancária | Nº da Conta | Conta Contábil Vinculada | Classificação Contábil (Máscara) | Status |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **17** | **SAFRA - PORTO ALEGRE** | `584391-9` | **7280** | `1.1.1.02.001.7280` | ✅ Validado |
| **21** | **SAFRA VITESSE** | `232229483` | **7325** | `1.1.1.03.001.7325` | ✅ Validado |
| **20** | **SAFRA ALFA POLARIS FI RF CP** | `232230150` | **7327** | `1.1.1.03.001.7327` | ✅ Validado |
| **19** | **SAFRA EXTRA BANCOS SPECIAL FIC** | `232228963` | **7329** | `1.1.1.03.001.7329` | ✅ Validado |

---

## 🔧 4. Detalhes Técnicos

* **Tabela do Plano de Contas:** `TCBPLA` (Entidade `PlanoConta`)
  * Conta Pai: `17` (`1.1.1.03.001 - APLICACOES FINANCEIRAS LIQUIDEZ IMEDIATA`)
  * Grau: `6` | Analítica: `S` | Ativa: `S` | Lançamento Manual: `S`
* **Tabela de Contas Bancárias:** `TSICTA` (Campo `CODCTACTB`)
