# Erro no Evento - Adiantamento Quinzenal por Valor não Desconta IRRF

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39390209522455-Erro-no-Evento-Adiantamento-Quinzenal-por-Valor-n%C3%A3o-Desconta-IRRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/39390209522455-Erro-no-Evento-Adiantamento-Quinzenal-por-Valor-n%C3%A3o-Desconta-IRRF)  
> **ID:** `39390209522455` | **Última Atualização:** 2026-07-29T13:23:36Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390255656983)

**MENSAGEM**

O sistema não está gerando o desconto de IRRF ao calcular a folha de adiantamento quinzenal. O cálculo retorna valor zerado para o imposto de renda, mesmo quando o funcionário possui base tributável que deveria gerar o desconto.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390255658135)

**SITUAÇÃO**

Ao calcular a folha de adiantamento quinzenal, o sistema não aplica o desconto de IRRF para os colaboradores. A base de cálculo é somada corretamente (folha mensal + adiantamento), porém o valor do IRRF retorna zerado, enquadrando incorretamente o valor na faixa de isenção. Esta situação ocorre especificamente quando o evento de adiantamento utilizado é personalizado e está sem a característica adequada vinculada.

- **Evento de adiantamento sem configuração adequada de incidências**

- **Evento de IRRF do adiantamento inativo ou incorreto**

- **Sequência incorreta de eventos na regra de cálculo**

- **Fórmula personalizada sem considerar o IRRF**

- **Valor mínimo de desconto configurado no evento de IRRF**

- **Utilização de evento personalizado ao invés do padrão**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390255659543)

**SOLUÇÃO**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390255662359)

 Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento de adiantamento quinzenal utilizado na folha .

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390209481367)

 Verifique se o evento de adiantamento possui a **"Característica"** corretamente vinculada. A fórmula de IRRF valida o evento por característica, portanto eventos personalizados sem característica não são reconhecidos no cálculo.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41146620089111)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390255674135)

 Ainda na tela **"Eventos"** (**Pessoal+ » Cadastros » Eventos**), acesse o evento de **adiantamento** e verifique as seguintes configurações. 

Na aba **Avançado**, confira se o campo **IRRF** está devidamente preenchido como **"IRRF"**. Em seguida, acesse a aba **Bases de Cálculo** e valide se a **base de IRRF** está cadastrada para o evento.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41146626961047)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41146626961431)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390209485975)

 Caso existam **dois eventos de adiantamento** cadastrados na base, identifique qual deles está sendo efetivamente utilizado no processamento da folha de pagamento e mantenha apenas esse evento com a característica vinculada.

O outro evento, que não está sendo utilizado, deve ser ** desativado**, garantindo que permaneça apenas um evento de adiantamento ativo e configurado para utilização no sistema.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390209489431)

 Verifique se a fórmula do evento **"IRRF"** (geralmente evento 9040) está utilizando a fórmula padrão Sankhya. Caso esteja vinculada a uma fórmula personalizada, esta pode não validar corretamente a tabela de isenção e as características dos eventos causando erro no calculo de IRRF. 

 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39390209511575)

**CAUSA**

O problema ocorre por duas causas principais:

**1. Evento de adiantamento sem característica:** A fórmula de IRRF valida os eventos por característica. Quando o evento de adiantamento quinzenal é personalizado e está sem a característica vinculada, o sistema não o reconhece no momento do cálculo, resultando em base zerada para o IRRF.
 

**2. Fórmula personalizada desatualizada:** Fórmulas personalizadas de IRRF podem não contemplar a validação da tabela de isenção atualizada conforme a Lei nº 15.270/2025, nem reconhecer corretamente as características dos eventos. Isso faz com que o cálculo ignore as deduções legais e não aplique corretamente as faixas de tributação e isenção.