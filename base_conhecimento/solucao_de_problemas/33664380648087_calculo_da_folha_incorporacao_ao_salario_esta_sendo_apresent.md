# Cálculo da Folha: Incorporação ao Salário Está Sendo Apresentada como Média

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33664380648087-C%C3%A1lculo-da-Folha-Incorpora%C3%A7%C3%A3o-ao-Sal%C3%A1rio-Est%C3%A1-Sendo-Apresentada-como-M%C3%A9dia](https://ajuda.sankhya.com.br/hc/pt-br/articles/33664380648087-C%C3%A1lculo-da-Folha-Incorpora%C3%A7%C3%A3o-ao-Sal%C3%A1rio-Est%C3%A1-Sendo-Apresentada-como-M%C3%A9dia)  
> **ID:** `33664380648087` | **Última Atualização:** 2026-08-27T18:30:54Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33984615531287)

 **MENSAGEM: **

Os valores dos eventos do tipo **"Movimento" **lançados através da tela **"Lançamento de Movimento"** (Pessoal+» Rotinas Folha» Lançamento de Movimento) e utilizados na **"incorporação ao salário" **não são apresentados corretamente na variável **VLRINCORPORA** durante o cálculo da folha de pagamento.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33984615533591)

 **SITUAÇÃO: **

Ao realizar lançamentos de eventos do tipo Movimento na tela Lançamento de Movimento para utilização na incorporação ao salário, os valores não são considerados na variável VLRINCORPORA durante o cálculo da folha, devido à competência em que o lançamento foi registrado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33984615536279)

 **SOLUÇÃO: **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33984615539351)

 Certifique-se de que os eventos do tipo Movimento estejam lançados em uma das seguintes condições:

- 

Na competência vigente do cálculo; ou

- 

Na competência imediatamente anterior, desde que esta ainda esteja aberta.

**Exemplo**

**Se o cálculo da folha está sendo realizado na competência 07/2025, há duas formas válidas de garantir a correta incorporação dos valores:**

- 

Feche a folha na referência 06/2025 para permitir lançamentos de movimento na competência 07/2025; 

- 

Feche a folha na referência 05/2025 para permitir lançamentos de movimento na competência 06/2025, desde que não haja folha fechada para o colaborador na competência 06/2025.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33984615554711)

 **CAUSA: **

A apresentação incorreta dos valores ocorre quando os eventos do tipo Movimento são lançados em competências que não são a vigente do cálculo ou a imediatamente anterior (desde que esta esteja aberta), impossibilitando a correta apuração da variável VLRINCORPORA durante o processamento da folha de pagamento.