# 📋 Guia de Automação: Retenções Federais de Órgãos Públicos e Trigger Anexo III

> **Público:** Faturamento, Fiscal, Financeiro e Suporte de TI  
> **Legislação Base:** Instrução Normativa RFB nº 1.234/2012 (Artigo 2º e Anexo III)  
> **Status:** Homologado, Testado e Ativo em Produção  

---

## 📌 1. O Problema (O que o usuário viu)

Nas vendas de materiais e dispositivos médicos realizadas pela Saavedra para **hospitais públicos federais** e entidades da administração direta (como o Grupo Hospitalar Conceição - GHC, Hospital de Clínicas de Porto Alegre - HCPA, etc.), o sistema Sankhya gerava notas fiscais com retenção cheia de impostos federais (5,85% ou 9,45%, somando PIS, COFINS, CSLL e IRRF).

Porém, pela legislação federal específica para a área médica:
1. Os dispositivos e materiais médicos da Saavedra possuem alíquota **ZERO de PIS e COFINS** na retenção na fonte.
2. Apenas o **IRRF (1,2%)** e a **CSLL (1,0%)** devem ser retidos pelo hospital público federal (totalizando **2,2%** de retenção).

### O Sintoma Operacional:
* O hospital federal recebia a nota fiscal e recusava o pagamento ou pagava a menor, gerando inconsistências no contas a receber do Financeiro.
* O faturamento precisava ajustar manualmente os impostos de cada nota fiscal, correndo o risco de erro humano.
* **Incidente Crítico Posterior:** Ao criar a automação inicial para zerar as retenções, as **notas de devolução de clientes ou fornecedores (`TIPMOV = 'D'`)** também estavam tendo seus impostos zerados indevidamente pela trigger, causando descompasso fiscal entre a nota de origem e a nota de retorno.

---

## ❓ 2. Por que isso aconteceu? (Explicação Simples)

1. **A Regra Geral vs. A Exceção Médica:**  
   No Brasil, todo órgão público federal retém quase 6% de imposto ao pagar uma fatura (PIS, COFINS, CSLL e IRRF juntos). Essa é a regra geral.  
   Porém, a Receita Federal criou uma lista especial (chamada de **Anexo III da IN 1.234**) dizendo que para determinados materiais médicos (como sondas, seringas, cateteres e próteses), a retenção de **PIS e COFINS não deve ser cobrada** do fornecedor.

2. **A Limitação Nativa do ERP:**  
   O Sankhya aplica regras fiscais padronizadas por Tipo de Operação (TOP) ou por Parceiro. Ele não conseguia sozinho olhar linha por linha do pedido e decidir: *"Este item é do Anexo III, então não retém PIS/COFINS; já a taxa de entrega ou outro item comum retém tudo"*.

3. **O Efeito Colateral na Devolução:**  
   Na primeira versão da automação em banco de dados, o comando rodava para **todas** as notas que continham os códigos dos produtos médicos. Quando um cliente devolvia uma mercadoria, a nota de devolução precisa ser uma cópia espelho exata da nota de saída original. Como a automação não diferenciava se era venda ou devolução, ela tentava zerar o imposto da devolução, provocando divergência contábil e fiscal.

---

## ✅ 3. O que fizemos para arrumar?

### Passo 1: Construção da Automação de Banco de Dados (Trigger)
Criamos uma regra automática inteligente no banco de dados do Sankhya, chamada **`TRG_SAAVEDRA_RETENCAO_ANEXO3`**, vinculada à tabela de cálculo de impostos por item (`TGFIMN`).

A trigger funciona como um fiscal eletrônico que age em fração de segundo no momento da emissão da nota:
* Ela verifica se o cliente é um órgão público federal sujeito à IN 1.234/2012.
* Ela analisa a NCM (classificação fiscal) de cada produto faturado.
* Se a NCM do produto constar na lista médica oficial do Anexo III, a trigger automaticamente zera a retenção do **PIS (CODIMP = 1)** e da **COFINS (CODIMP = 2)**, mantendo intactas as retenções devidas de IRRF e CSLL.

### Passo 2: Correção do Bug de Devoluções
Identificamos que notas de devolução não podiam sofrer alteração automática. Atualizamos o código da trigger para inserir uma trava expressa:
* **Filtro Aplicado:** A automação só é executada se o tipo de movimento da nota for **Venda (`TIPMOV = 'V'`)**.
* Se for **Devolução (`TIPMOV = 'D'`)**, Transferência ou Outras Entradas, a trigger é imediatamente ignorada, permitindo que a nota espelhe 100% os impostos da operação original sem distorções.

### Passo 3: Cadastro Centralizado das NCMs Contempladas
Cadastramos na lista da regra as principais famílias de NCMs operadas pela Saavedra:
* `3006.70.00` – Géis lubrificantes para exames e sondagens
* `3926.90.30` – Bolsas coletoras e artigos de plástico para uso médico
* `9018.31.19` – Seringas especiais e conexões
* `9018.39.10` / `9018.39.21` / `9018.39.29` / `9018.39.99` – Cateteres, sondas e agulhas
* `9018.90.95` / `9018.90.99` – Instrumentos e aparelhos de medicina/cirurgia
* `9021.10.10` / `9021.10.99` – Artigos e aparelhos ortopédicos / próteses

---

## 👤 4. Como o usuário valida no dia a dia?

### Para o Faturamento:
1. Emita a nota fiscal normalmente para o órgão público federal (ex: Grupo Hospitalar Conceição).
2. Na tela de **Central de Vendas**, acesse **Outras Opções ➔ Resumo de Impostos Retidos**.
3. Verifique os valores destacados:
   * **PIS Retido:** `R$ 0,00`
   * **COFINS Retida:** `R$ 0,00`
   * **IRRF Retido:** `1,20%` calculado corretamente
   * **CSLL Retida:** `1,00%` calculado corretamente
4. **Total Retido na Nota:** Exatamente **2,20%** sobre os produtos médicos.

### Para o Financeiro:
* No financeiro da nota faturada (título a receber), o valor líquido a receber será o valor total dos produtos menos apenas os 2,20%, batendo exatamente com o valor que o hospital público irá creditar na conta bancária da Saavedra.

### Para as Devoluções:
* Ao emitir nota de devolução (`TIPMOV = 'D'`), os impostos serão clonados da nota de compra ou venda original sem que a trigger zere nada.

---

## 🔧 5. Detalhes Técnicos (Para TI e Fiscal)

* **Objeto Criado:** `TRIGGER TRG_SAAVEDRA_RETENCAO_ANEXO3`
* **Tabela Monitorada:** `TGFIMN` (Impostos do Item da Nota)
* **Tabelas de Apoio:** `TGFCAB` (Cabeçalho da Nota), `TGFPRO` (Cadastro de Produtos), `TGFPAR` (Cadastro de Parceiros)
* **Condições Lógicas Implementadas:**
  ```sql
  -- Apenas executa para vendas
  IF (@TIPMOV = 'V' AND @TIPMOV <> 'D')
  BEGIN
      -- Verifica se NCM consta na lista do Anexo III da IN 1234/2012
      IF @NCM IN ('30067000','39269030','90183119','90183910','90183921','90183929',
                  '90183999','90189095','90189099','90211010','90211099')
         AND @CODIMP IN (1, 2) -- 1 = PIS Retido, 2 = COFINS Retida
      BEGIN
          UPDATE TGFIMN
             SET VALOR = 0,
                 ALIQUOTA = 0,
                 BASE = 0
           WHERE NUNOTA = @NUNOTA
             AND SEQUENCIA = @SEQUENCIA
             AND CODIMP = @CODIMP;
      END
  END
  ```
* **Impacto Operacional:** Fim das glosas contratuais e divergências em ordens bancárias de hospitais públicos federais.
