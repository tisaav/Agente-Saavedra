# 🏥 Perfil Operacional e Regras de Negócio — Saavedra Representações

> **Empresa:** SAAVEDRA REPRESENTAÇÕES LTDA  
> **Segmento:** Distribuição Médico-Hospitalar / OPME (Órteses, Próteses e Materiais Especiais)  
> **ERP:** Sankhya Om / Gateway API  

---

## 1. Visão Geral da Operação

A **Saavedra Representações** atua no fornecimento e distribuição de materiais médico-hospitalares e OPME para hospitais, clínicas e operadoras de saúde (ex: Unimed Vale do Sinos, Hospital Geral, Hospital Naval Marcílio Dias, Hospital Cristo Redentor).

O modelo de negócio opera com um fluxo complexo que combina **consignação hospitalar pré-cirúrgica** e **faturamento pós-cirúrgico**:
1. **Remessa em Consignação:** Os materiais estéreis/implantes são enviados antecipadamente aos hospitais para realização dos procedimentos cirúrgicos.
2. **Utilização e Confirmação Cirúrgica:** O hospital consome os itens necessários no paciente durante a cirurgia e informa os dados do paciente, médico responsável, CRM, convênio e autorização de fornecimento (AFP).
3. **Faturamento / Cobrança:** A Saavedra emite o faturamento dos itens efetivamente utilizados e dá baixa simbólica da remessa.

---

## 2. Tipos de Operação (TOPs) Fundamentais na Saavedra

| Código TOP | Descrição da Operação | Tipo de Movimento (`TIPMOV`) | Finalidade Operacional |
| :---: | :--- | :---: | :--- |
| **1005** | **PEDIDO DE SIMPLES REMESSA (CONSIG)** | `P` | Pedido interno para envio de materiais ao hospital/estoque de consignação. Não gera duplicatas financeiras nem impostos cheios. |
| **1106** | **SIMPLES REMESSA (CONSIGNADO)** | `V` | Nota Fiscal de remessa física acompanhando os materiais. |
| **1000** | **PEDIDO DE VENDA NFE** | `P` | Pedido de faturamento da venda padrão. Vincula paciente, convênio, médico e gera parcelas financeiras a receber (`TGFFIN`). |
| **1100** | **VENDA - NFE** | `V` | Emissão da NF-e de venda definitiva. Calcula impostos (ICMS, IPI, PIS, COFINS, IBS, CBS) e transmite para a SEFAZ. |
| **1107** | **VENDA SIMPLES REMESSA (CONSIGNADO)** | `V` | Faturamento dos itens consumidos previamente enviados em consignação. |
| **1209** | **RETORNO DE REMESSA (DEVOLUÇÃO SIMBÓLICA)** | `D` | Devolução simbólica dos materiais consignados faturados. |

---

## 3. Principais Parceiros Hospitalares Mapeados

* **Parceiro 258:** `UNIMED VALE DO SINOS COOPERATIVA DE ASSISTENCIA A SAUDE LTDA` (Hospital Unimed Vale do Sinos - Torre II) — CNPJ `88.258.884/0022-54`.
* **Parceiro 1094:** `HOSPITAL GERAL DE CAXIAS DO SUL`
* **Parceiro 1509:** `HOSPITAL NAVAL MARCILIO DIAS`
* **Parceiro 325:** `HOSPITAL CRISTO REDENTOR`
* **Parceiro 642:** `CENTRO CLINICO GAUCHO`

---

## 4. Particularidades Críticas deste Ambiente

1. **Campos Obrigatórios de Cirurgia:** Todo pedido de venda ou faturamento precisa conter os dados do procedimento cirúrgico (Paciente, Convênio, Médico, CRM, Data Cirurgia, Solicitante Hospitalar).
2. **Disparo Automático de E-mails:** Na confirmação do pedido na Central de Vendas / Portal de Vendas, o sistema gera o PDF do pedido e dispara e-mail automático para o hospital/cliente e para o estoque interno.
3. **Dependência do Relatório Jasper:** Se o relatório de impressão do pedido falhar (SQL quebrado, divisão por zero ou conversão de tipo de dado), **o pedido não confirma e o e-mail não é enviado**, gerando risco de quebra de SLA de entrega de materiais para cirurgias agendadas.
