# 🏷️ Dicionário de Campos Customizados (`AD_`) — Saavedra Representações

No ERP Sankhya, a Saavedra possui campos adicionais (`AD_`) criados no **Construtor de Telas / Dicionário de Dados** para atender a legislação da ANVISA e as particularidades do setor hospitalar/OPME.

---

## 1. Tabela `TGFCAB` (Cabeçalho de Notas e Pedidos)

Estes campos armazenam os dados cirúrgicos, hospitalares e de importação vinculados a cada movimentação:

| Nome do Campo no Banco | Tipo de Dado | Descrição / Uso Operacional | Apresentação no Relatório / Tela |
| :--- | :---: | :--- | :--- |
| `AD_PACIENTE` | `VARCHAR(100)` | Nome completo do paciente submetido ao procedimento cirúrgico. | `Paciente:` |
| `AD_NOMMEDICO` | `VARCHAR(100)` | Nome do médico cirurgião responsável. | `Médico:` |
| `AD_CRM` | `INT` | Número do CRM do médico cirurgião. *(Atenção: no Jasper deve ser tratado como String/Cast para evitar quebra quando nulo).* | `CRM:` |
| `AD_CONVENIO` | `VARCHAR(60)` | Nome do plano de saúde / operadora do paciente (ex: Unimed, IPE, SUS, Bradesco Saúde). | `Convênio:` |
| `AD_DTCIRURG` | `DATETIME` | Data e hora em que a cirurgia foi ou será realizada. | `Data da Cirurgia:` |
| `AD_NUMAFP` | `INT` | Número da Autorização de Fornecimento / Pedido emitido pelo hospital. | `Número AFP:` |
| `AD_PEDCLIENTE` | `VARCHAR(60)` | Número do pedido de compras interno do cliente/hospital. | `Pedido Cliente:` |
| `AD_SOLICITHOSP` | `VARCHAR(60)` | Nome do funcionário ou setor do hospital que solicitou os materiais (ex: Bloco Cirúrgico, Farmácia). | `Solicitante Hospital:` |
| `AD_VALIDADEORCAMENTO` | `DATETIME` | Data limite de validade dos preços e condições cotadas no orçamento. | `Validade do Orçamento:` |
| `AD_OBSERVAOADICIONAL`| `VARCHAR(255)`| Observações adicionais do faturamento e entrega. | `Obs Adicional:` |
| `AD_OBSERVACAO` | `VARCHAR(255)`| Observação geral da nota/pedido. | `Observação:` |
| `AD_GUIAATEND` | `VARCHAR(40)` | Número da Guia de Atendimento / TISS da operadora de saúde. | `Guia de Atendimento` |
| `AD_NUMMATRIC` | `VARCHAR(40)` | Número da matrícula da carteirinha do paciente no convênio. | `Matrícula Convênio` |
| `AD_CLIENTEUSO` | `INT` | Código do parceiro que efetivamente utilizará o material (quando comprado por intermediador). | `Cliente Uso` |

---

## 2. Tabela `TGFPRO` (Cadastro de Produtos / Itens OPME)

A rastreabilidade de materiais e implantes exige o registro sanitário emitido pela ANVISA:

| Nome do Campo no Banco | Tipo de Dado | Descrição / Uso Operacional | Apresentação no Relatório / Tela |
| :--- | :---: | :--- | :--- |
| `AD_RMS` | `VARCHAR(50)` | Número de Registro no Ministério da Saúde / ANVISA do produto. | `RMS:` / `Registro ANVISA` |
| `AD_DTRMS` | `VARCHAR(20)` / `DATETIME` | Data de validade do registro do produto na ANVISA. *(Deve ser formatado com `CONVERT(VARCHAR, ..., 103)` nas consultas SQL do Jasper).* | `Dt. Validade RMS` |
| `AD_IDEXTERNO` | `VARCHAR(60)` | Código identificador em sistemas externos ou de fabricantes parceiros. | `ID Externo` |

---

## 3. Tabela `TGFPAP` (Referências Cruzadas de Produtos por Parceiro)

* **`CODPROPARC`:** Código interno do produto no cadastro do hospital parceiro (ex: código do item dentro da Unimed).
* **`DESCRPROPARC`:** Descrição do item utilizada internamente pelo hospital.
* **⚠️ Regra Crítica:** Em consultas e relatórios, sempre utilize `(SELECT TOP 1 COALESCE(CODPROPARC, NULL) FROM TGFPAP WHERE CODPARC = CAB.CODPARC AND CODPROD = ITE.CODPROD)`. Caso um parceiro cadastre o mesmo produto mais de uma vez em `TGFPAP`, uma subquery sem `TOP 1` resultará em erro fatal de subquery com múltiplas linhas!
