# Processo Adequação da NF-e à NT 2020.005 v1.21 (ICMS Diferido e PIS/COFINS ST)

> **Módulo:** Fiscal e Contábil | **Subseção:** Notas Técnicas de NFe e NFCe  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/42733602741527-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2020-005-v1-21-ICMS-Diferido-e-PIS-COFINS-ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/42733602741527-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2020-005-v1-21-ICMS-Diferido-e-PIS-COFINS-ST)  
> **ID:** `42733602741527` | **Última Atualização:** 2026-08-14T20:57:11Z

---

**Caminhos de Acesso:**

- Menu Principal › Preferências › Empresa › aba NF-e/NFC-e › sub-aba Nota Técnica NF-e

- Alíquotas de ICMS › aba Geral

**Você encontra neste artigo:**

[O que é e para que serve](#h_01M010QKMEKB1K4J330EP24CY9)

[O que foi alterado](#h_01M010QKMFS6TFGZAEVJCTRABJ)

[ICMS Diferido (cálculo por dentro)](#h_01M010QKMGKFJM48KRKZX40SY6)

[Grupos PISST e COFINSST](#h_01M010QKMM2GEJS3A9MXKJZRHH)[Pontos de atenção](#h_01M010QRV6TGC2Z2T3F1AE3A1Z)

| ↳     ↳ |  |
| --- | --- |

## **O que é e para que serve**

A **Nota Técnica 2020.005 v1.21** ajusta o cálculo do ICMS Diferido por dentro e passa a gerar os grupos de PIS e COFINS Substituição Tributária no XML da NF-e. Ela depende de configurações específicas no cadastro de Alíquotas de ICMS — sem elas, o comportamento anterior é mantido.

## **O que foi alterado**

### **ICMS Diferido (cálculo por dentro)**

Com a NT 2020.005 configurada, o sistema emite uma nota fiscal com ICMS Diferido desde que: a alíquota cadastrada tenha a marcação **Cálculo Diferimento por Dentro** (aba Geral, tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)) habilitada; o campo **Tipo de Cálculo DIFAL e do FCP** (mesma aba) esteja configurado com a opção **0 - Sem considerar redução da Base**; e a opção **51-Diferimento** do campo **Tributação** esteja definida.

Nessas condições, o XML gera os valores de FCP Diferido na tag <pFCPDif>, e a base de cálculo do ICMS e do FCP passa a ser calculada por dentro, pela fórmula: Valor da operação / (1 - (Alíq ICMS + Alíq FCP)).

### **Grupos PISST e COFINSST**

Para que as notas fiscais eletrônicas sigam as regras fiscais corretamente, o Sankhya Om gera os grupos de tags <PISST> e <COFINSST> no XML. Isso evita erros no envio dos documentos. A geração dessas informações só acontece com a NT 2020.005 - v1.21 ativada nas Preferências da Empresa.

## **Pontos de atenção**

Se nenhuma Nota Técnica estiver ativada nesta sub-aba, o sistema usa automaticamente a versão mais recente disponível — o que pode ativar esta NT sem uma escolha explícita.


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)