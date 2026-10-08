# 📋 Guia de Configuração: Reforma Tributária (IBS e CBS) no Sankhya para Dispositivos Médicos

> **Público:** Faturamento, Fiscal, Contabilidade e Suporte de TI  
> **Legislação Base:** Lei Complementar nº 214/2025 (Anexo IV) e Nota Técnica 2025.002 da SEFAZ  
> **Status:** Configurado, Testado em Homologação e Validado  

---

## 📌 1. O Problema (O que o usuário viu)

Durante a fase de testes obrigatórios da nova **Reforma Tributária** (que passa a exigir o envio dos novos impostos **IBS** e **CBS** nas notas fiscais em 2026), a equipe de faturamento emitiu notas de teste para clientes públicos (como o Hospital Conceição - GHC) e as notas foram rejeitadas pela SEFAZ com mensagens de erro:
* **Rejeição 1033:** *Percentual de redução de alíquota não informado ou inválido.*
* **Rejeição 1026:** *Alíquota do IBS da UF inválida.*
* **Rejeição 1036:** *Alíquota do IBS do Município inválida.*

Além disso, a contabilidade (Ademir) solicitou que os materiais médicos da Saavedra fossem enquadrados no benefício legal de **60% de redução de alíquota**, enviando no XML o **CST 200** e o código de classificação **cClassTrib 200030**.

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

A Reforma Tributária extingue o PIS e a COFINS e cria dois novos tributos:
* **CBS (Federal):** Contribuição sobre Bens e Serviços.
* **IBS (Estadual e Municipal):** Imposto sobre Bens e Serviços.

No ano de transição (2026), as notas precisam destacar esses tributos em caráter de teste (sem cobrar valor a mais do cliente).
1. **O Benefício Médico:** A lei determina que Dispositivos Médicos têm direito a uma **redução de 60%** do imposto (a empresa paga apenas 40% do imposto cheio).
2. **A Exigência da SEFAZ:** A SEFAZ **não aceita** que a empresa já envie a alíquota calculada e cortada (ex: mandar 0,36% direto). O computador do governo exige que a nota informe a **alíquota oficial cheia** (0,90% de CBS e 0,10% de IBS) e, em um campo separado, informe que tem **60% de redução**. A própria SEFAZ faz a matemática no servidor dela. Quando a empresa mandava a alíquota já com o desconto aplicado, a SEFAZ rejeitava dizendo que o número estava fora da tabela oficial.
3. **A Questão do Município:** No ano de 2026, a SEFAZ estabeleceu que toda a alíquota de teste do IBS deve ir na linha do Estado (0,10%), deixando a linha do Município zerada/em branco. Se preenchesse o município, o sistema da SEFAZ gerava o erro 1036.

---

## ✅ 3. O que fizemos para arrumar?

### Passo 1: Criação do Grupo de Tributação Inteligente
Em vez de ter que configurar regra individual para cada um dos 428 produtos médicos do catálogo da Saavedra, criamos uma amarração centralizada:
* Criamos o **Grupo IBS/CBS: `4`** (referência ao Anexo IV da lei).
* No cadastro de produtos, associamos os 428 itens médicos (como Dignishield, cateteres Hemosplit, clipes Ultraclip, seringas Enfit) a esse Grupo 4.

### Passo 2: Configuração das Regras de Alíquotas no Sankhya

#### **A. Regra da CBS (Tela: Alíquotas de CBS)**
* **Identificação:** UF Destino = `RS` | Grupo CBS = `4` | NCM = `0` (indica regra geral do grupo).
* **Tributação:**
  * **CST:** `200` *(Operação com Redução de Alíquota)*
  * **cClassTrib:** `200030` *(Dispositivos Médicos do Anexo IV)*
  * **Alíquota Referência:** `0,9000` *(Alíquota oficial de teste)*
  * **% Federal:** em branco *(evita duplicação de cálculo)*
  * **% Redução de Alíquota CBS:** `60,0000`

#### **B. Regra do IBS (Tela: Alíquotas de IBS)**
* **Identificação:** UF Destino = `RS` | Grupo IBS = `4` | NCM = `0`
* **Tributação:**
  * **CST:** `200`
  * **cClassTrib:** `200030`
  * **Alíquota Referência:** `0,1000` *(Alíquota oficial de teste)*
  * **Alíquota IBS Estado:** `0,1000` (ou `0,0500` com Estado 50%)
  * **Alíquota IBS Município:** em branco *(evita o Erro 1036)*
  * **% Redução Estadual e Municipal:** `60,0000`

### Passo 3: Limpeza de Lote e Reemissão
Nas notas que haviam sofrido rejeição, foi aplicado o procedimento de:
1. Reabertura do item na nota (para forçar o Sankhya a reler a nova regra fiscal no banco de dados).
2. Confirmação da nota e execução de **"Limpar Status NF-e"**.
3. Geração de novo lote com transmissão limpa para a SEFAZ.

---

## 👤 4. Como o usuário valida no dia a dia?

Para conferir se a nota fiscal está calculando a Reforma Tributária perfeitamente:
1. Abra a nota na **Central de Vendas**.
2. Clique no ícone de engrenagem / outras opções e selecione **Resumo de Impostos**.
3. As linhas de **CBS** e **IBS** aparecerão calculadas:
   * **CBS:** Base cheia x 0,90% x (100% - 60%) ➔ Valor efetivo de 0,36%.
   * **IBS:** Base cheia x 0,10% x (100% - 60%) ➔ Valor efetivo de 0,04%.
4. No arquivo XML transmitido, estarão presentes as tags:
   * `<CST>200</CST>`
   * `<cClassTrib>200030</cClassTrib>`
   * `<pRedAliq>60.0000</pRedAliq>`

---

## 🔧 5. Detalhes Técnicos (Para TI e Fiscal)

* **Tabelas do Sankhya Envolvidas:**
  * `TGFPRO` (Cadastro de Produtos — campo de grupo de imposto)
  * `TGFTOP` (Tipos de Operação)
  * `TGFDIN` (Tabela de Impostos Calculados da Nota)
  * Tabelas de Alíquotas da Reforma: `TLFAliquotaIbs` e `TLFAliquotaCbs`
* **NCMs Contemplados na Saavedra (Anexo IV):**
  * `3006.70.00`, `3926.90.30`, `9018.31.19`, `9018.39.10`, `9018.39.21`, `9018.39.29`, `9018.39.99`, `9018.90.95`, `9018.90.99`, `9021.10.10`, `9021.10.99`.
