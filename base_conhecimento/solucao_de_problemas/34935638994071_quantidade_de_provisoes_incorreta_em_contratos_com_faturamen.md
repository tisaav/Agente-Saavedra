# Quantidade de provisões incorreta em contratos com faturamento diferente de mensal. Saiba como resolver

> **Módulo:** Solucao de Problemas | **Subseção:** Prestação de Serviços  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34935638994071-Quantidade-de-provis%C3%B5es-incorreta-em-contratos-com-faturamento-diferente-de-mensal-Saiba-como-resolver](https://ajuda.sankhya.com.br/hc/pt-br/articles/34935638994071-Quantidade-de-provis%C3%B5es-incorreta-em-contratos-com-faturamento-diferente-de-mensal-Saiba-como-resolver)  
> **ID:** `34935638994071` | **Última Atualização:** 2026-07-22T14:26:23Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34935638988567)

 **SITUAÇÃO:**

Ao configurar contratos com periodicidade diferente de **mensal** (como trimestral, semestral ou anual), a quantidade de provisões exibida no sistema pode não corresponder ao número esperado, gerando dúvidas sobre o cálculo realizado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34935638988823)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34935632523287)

 A quantidade de provisões geradas é definida de acordo com a **periodicidade do contrato, **na tela **"Contratos" **(Contratos e Serviços > Arquivos > Contratos), aba **"Propriedades", **campo **"Periodicidade do faturamento"**.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34935638988951)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35709187358743)

 Exemplo:** Contrato **T****rimestral** com o campo **Qtd. Provisão = 4**.

O sistema interpreta que o período total é de **4 meses** (Janeiro, Fevereiro, Março e Abril).

Assim, cria **2 provisões**:

- 

**1ª provisão:** Janeiro, Fevereiro e Março.

- 

**2ª provisão:** Abril.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34935632524311)

 Como ajustar?**

Se a intenção é ter **4 títulos de provisões trimestrais ao longo do ano**, o campo "**Qtd. Provisão"** deve ser configurado como **12** (referente aos meses do ano).

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34935638989079)

 

Nesse caso, o sistema criará:

- 

**1ª provisão:** Janeiro, Fevereiro e Março;

- 

**2ª provisão:** Abril, Maio e Junho;

- 

**3ª provisão:** Julho, Agosto e Setembro;

- 

**4ª provisão:** Outubro, Novembro e Dezembro.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34935638989335)

CAUSA:**

O sistema calcula a quantidade de provisões de acordo com a **periodicidade definida no contrato**.
Quando o campo **Qtd. Provisão** é informado com base no número de parcelas desejadas, mas sem considerar a periodicidade (mensal, trimestral, semestral etc.), ocorre a divergência entre a quantidade configurada e a quantidade realmente gerada.