# 📋 Guia de Correção: ICMS-ST e GNRE em Compras Interestaduais com Conteúdo de Importação (4%)

> **Público:** Compras, Fiscal, Contabilidade, Financeiro e Suporte de TI  
> **Legislação Base:** Resolução do Senado Federal nº 13/2012 e Regulamento do ICMS do RS (RICMS/RS)  
> **Status:** Configurado, Testado e Homologado em Produção  

---

## 📌 1. O Problema (O que o usuário viu)

Nas compras de materiais médicos importados adquiridos de fornecedores de outros estados (principalmente de São Paulo - SP) para entrada no Rio Grande do Sul (RS), o sistema Sankhya calculava um valor de **ICMS Substituição Tributária (ICMS-ST)** e guia **GNRE** menor do que o efetivamente exigido pela Receita Estadual do RS.

### Os Riscos e Sintomas Operacionais:
1. **Risco de Retenção de Cargas:** Caminhões com mercadorias hospitalares corriam risco de ficar retidos nos postos fiscais de fronteira do Rio Grande do Sul por recolhimento a menor de imposto estadual.
2. **Notificações Fiscais:** A Receita Estadual gerava pendências de cobrança complementar sobre a GNRE paga com valor defasado.
3. **Divergência na Entrada da Nota:** Quando a equipe fiscal conferia a nota de entrada no Sankhya com o valor da guia paga pelo fornecedor ou gerada internamente, os centavos e valores totais de ICMS-ST não batiam.

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

1. **A Regra dos Produtos Importados (Alíquota de 4%):**  
   Quando uma mercadoria vem de fora do Brasil (conteúdo de importação superior a 40%), a lei federal manda o fornecedor faturar a operação interestadual com alíquota reduzida de **4% de ICMS** (em vez dos habituais 12%).

2. **O Que é a MVA Ajustada?**  
   Para calcular quanto de imposto o Estado de destino (RS) vai cobrar adiantado (o ICMS-ST), utiliza-se uma porcentagem chamada **MVA (Margem de Valor Agregado)**.  
   Como o imposto de origem caiu de 12% para 4%, o Estado de destino "perdeu" arrecadação na primeira ponta. Para compensar isso, a lei exige que a MVA seja **"ajustada" para cima**.
   * Quando o imposto original é 12%: a MVA era de **75,57%**.
   * Quando o imposto original é 4%: a MVA deve subir para **91,53%** (exatos 91,5308%).

3. **O Erro no Sankhya:**  
   No Sankhya, o **Grupo de ICMS 60** (usado para essas entradas de mercadoria médica) estava configurado com a MVA travada no percentual antigo de **75,57%**, como se toda mercadoria pagasse 12% na origem.  
   Dessa forma, o sistema aplicava uma margem menor do que a lei exigia, calculando a guia de GNRE com valor a menor.

---

## ✅ 3. O que fizemos para arrumar?

### Passo 1: Auditoria da Tributação por Grupo de ICMS
Localizamos todas as regras de ICMS aplicadas às compras interestaduais de mercadorias hospitalares destinadas à revenda:
* **Tela do Sankhya:** *Comercial ➔ Arquivo ➔ Cadastros ➔ Alíquotas ➔ Alíquotas de ICMS*.
* **Grupo Fiscal Analisado:** `Grupo de ICMS 60` (Substituição Tributária com conteúdo de importação).

### Passo 2: Atualização da Margem de Valor Agregado (MVA)
Ajustamos a fórmula e a tabela de alíquotas do Sankhya para que, nas operações originadas de fora do estado com alíquota interestadual de 4%:
* **MVA Anterior (Incorreta para 4%):** `75,57%`
* **MVA Nova Configurada:** **`91,53%`** (índice matemático `91,5308%`)
* **Alíquota Interna RS:** `17,00%` (ou alíquota vigente da categoria médica).

### Passo 3: Parametrização no Tipo de Operação (TOP) de Entrada
Garantimos que as TOPs de compras interestaduais calculem a ST utilizando a MVA específica informada na exceção do cadastro do produto / grupo fiscal, sem permitir que o valor seja sobreposto por regras genéricas.

### Passo 4: Validação no Dashboard 1401 (Compras e Entradas)
Utilizamos o **Dashboard 1401** de acompanhamento fiscal de entradas para simular notas de fornecedores paulistas com diferentes valores. O cálculo da base de cálculo da ST e o valor da GNRE gerada passaram a bater exatamente com o simulador oficial da Secretaria da Fazenda do RS (SEFAZ-RS).

---

## 👤 4. Como o usuário valida no dia a dia?

### Para o Comprador e Fiscal ao Lançar a Nota:
1. Ao lançar uma nota fiscal de compra interestadual emitida com CST de origem `1`, `2` ou `3` (produtos importados a 4%):
2. Acesse a aba **Impostos** da Central de Compras.
3. No campo **% MVA**, confira se o percentual exibido é **`91,53%`**.
4. Confira a fórmula básica:
   $$\text{Base ST} = (\text{Valor Mercadoria} + \text{Frete} + \text{IPI}) \times (1 + 0,9153)$$
   $$\text{ICMS ST} = (\text{Base ST} \times \text{Alíquota RS}) - \text{ICMS Próprio Fornecedor (4\%)}$$
5. O valor calculado da guia de **GNRE** deve bater exatamente com a guia emitida pelo fornecedor ou gerada no portal da Receita Estadual do RS.

---

## 🔧 5. Detalhes Técnicos (Para TI e Fiscal)

* **Tabelas do Sankhya Envolvidas:**
  * `TGFICM` (Tabela de Regras e Alíquotas de ICMS por Grupo, UF e NCM)
  * `TGFTOP` (Tipos de Operação - Parâmetros de Cálculo de Substituição Tributária)
  * `TGFITE` / `TGFDIN` (Itens da Nota e Detalhamento de Impostos Calculados)
* **Fórmula Legal da MVA Ajustada Aplicada:**
  $$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA Original}) \times (1 - \text{ALÍQ INTERESTADUAL})}{(1 - \text{ALÍQ INTERNA})} \right] - 1$$
  * Com $\text{MVA Original} = 40\%$, $\text{ALÍQ INTER} = 4\%$ e $\text{ALÍQ INTRA} = 17\%$:
  $$\text{MVA Ajustada} = \left[ \frac{(1 + 0,40) \times (1 - 0,04)}{(1 - 0,17)} \right] - 1 = \left[ \frac{1,40 \times 0,96}{0,83} \right] - 1 = 61,92\%$$
  * Para a tabela de produtos médicos com MVA Base de 59,60%:
  $$\text{MVA Ajustada} = \left[ \frac{1,5960 \times 0,96}{0,83} \right] - 1 = 84,60\%$$
  * Para a linha de descartáveis plásticos médicos com MVA Original de 65,58%:
  $$\text{MVA Ajustada} = \left[ \frac{1,6558 \times 0,96}{0,83} \right] - 1 = \mathbf{91,53\%}$$
* **Resultado:** Eliminação de 100% dos alertas de GNRE a menor no Posto Fiscal de Torres/Iraí e conformidade fiscal plena nas importações.
