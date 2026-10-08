# Folha de autônomo | Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35934605273751-Folha-de-aut%C3%B4nomo-Erro-724-N%C3%A3o-foi-localizado-um-evento-de-remunera%C3%A7%C3%A3o-do-trabalhador-para-o-per%C3%ADodo-e-com-mesmo-demonstrativo-de-pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/35934605273751-Folha-de-aut%C3%B4nomo-Erro-724-N%C3%A3o-foi-localizado-um-evento-de-remunera%C3%A7%C3%A3o-do-trabalhador-para-o-per%C3%ADodo-e-com-mesmo-demonstrativo-de-pagamento)  
> **ID:** `35934605273751` | **Última Atualização:** 2026-07-29T13:21:18Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/35934605266583)

 MENSAGEM**

Erro 724 - Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento.

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/41145387592983)

 SITUAÇÃO**

Este erro ocorre ao tentar enviar o evento **"S-1210"** (Pagamentos de Rendimentos do Trabalho com Retenção de IRRF) para o eSocial através da **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial). O sistema indica que não foi localizado um evento de remuneração correspondente para o período informado.

 

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/35934620760855)

 SOLUÇÃO**

A solução varia conforme a causa identificada. Siga os passos abaixo de acordo com a situação:

**Para funcionários CLT (evento S-1200 não enviado):**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/35934620762775)

Acesse a **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e verifique se o evento **"S-1200"** (Remuneração de Trabalhador) foi enviado para o período de referência correspondente.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/35934620763671)

Caso o evento **"S-1200"** não tenha sido enviado, gere e envie este evento antes de tentar enviar o **"S-1210"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/35934605269399)

Após o envio bem-sucedido do **"S-1200"**, retorne à **"Central do eSocial"** e envie o evento **"S-1210"**.
 

**Para trabalhadores autônomos (divergência no identificador de demonstrativo):**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/35934620762775)

Acesse as folhas da referência em questão do autônomo — tanto a **"Folha Suplementar"** (TFPBSU) quanto a **"Folha Mensal"** (TFPBAS).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/35934620763671)

Verifique as **"Datas de Pagamento"** de ambas as folhas. Certifique-se de que as duas folhas estejam com as datas de pagamento dentro da referência correspondente (Ex: referência 10/2025, os pagamentos devem ser entre 01/10/2025 a 31/10/2025).

![3](https://ajuda.sankhya.com.br/hc/article_attachments/35934605269399)

Caso as datas estejam diferentes ou fora da referência, corrija a **"Data de Pagamento"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/41145364935191)

Gere e envie novamente o evento **"S-1210"** através da **"Central do eSocial"**.

**Para eventos retidos no console do eSocial:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/35934620762775)

Acesse o **"Console do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e verifique se há eventos retidos ou pendentes.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/35934620763671)

Caso identifique eventos retidos, realize a exclusão destes eventos diretamente pelo console.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/35934605269399)

Envie novamente o evento **"S-1200"** através da **"Central do eSocial"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/41145364935191)

Após o envio bem-sucedido do **"S-1200"**, envie o evento **"S-1210"**.

**Para folhas de dissídio com eventos RRA não configurados:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/35934620762775)

Verifique se os eventos da folha de dissídio estão corretamente configurados como **"RRA"** (Rendimentos Recebidos Acumuladamente).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/35934620763671)

Caso os eventos não estejam configurados como **"RRA"**, exclua as folhas do período de referência.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/35934605269399)

Configure os eventos necessários como **"RRA"** na tela **"Eventos"** 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/41145364935191)

Recalcule a folha de dissídio com os eventos corretamente configurados.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/41145364935703)

Recalcule a folha mensal do período.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/41145387593879)

Realize a retificação do evento **"S-1200"** através da **"Central do eSocial"**.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/41145387594007)

Gere e envie o evento **"S-1210"**.

 **

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/35934620768151)

 CAUSA**

O erro 724 ocorre quando o eSocial não consegue localizar o vínculo entre o evento de pagamento **"S-1210"** e o evento de remuneração correspondente (**"S-1200"**, **"S-1202"** ou **"S-1207"**). As principais causas são:

• **Evento de remuneração não enviado:** o evento **"S-1200"** do período de referência não foi gerado ou enviado ao eSocial antes da tentativa de envio do **"S-1210"**.

• **Divergência no identificador de demonstrativo:** para trabalhadores autônomos, as datas de pagamento estão em referência posterior ao cálculo, impedindo a montagem correta do IDMDEV (Ex: REF. 10/2025 com pagamento na REF. 11/2025).

• **Eventos retidos no console:** existem eventos pendentes ou retidos no console do eSocial que impedem o correto processamento dos novos eventos.

• **Configuração incorreta de eventos RRA:** em folhas de dissídio, os eventos não foram configurados como Rendimentos Recebidos Acumuladamente, causando inconsistência no envio.

• **Tipo de pagamento incompatível:** o campo **"Identificador de Recibo de Pagamento"** não está corretamente vinculado ao tipo de pagamento informado, conforme a regra: Tipo de Pagamento [1] deve estar em **"S-1200"**; Tipo [4] em **"S-1202"**; Tipo [5] em **"S-1207"**.