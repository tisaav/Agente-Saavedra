# não gerado quando difere do CR configurado na integração financeira

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35834304653719-n%C3%A3o-gerado-quando-difere-do-CR-configurado-na-integra%C3%A7%C3%A3o-financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/35834304653719-n%C3%A3o-gerado-quando-difere-do-CR-configurado-na-integra%C3%A7%C3%A3o-financeira)  
> **ID:** `35834304653719` | **Última Atualização:** 2026-07-29T13:21:13Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35834396450839)

** SITUAÇÃO:**

Ao gerar a integração financeira, o sistema não preenche automaticamente a aba **''Rateio''** com o **Centro de Resultado (CR) **do departamento do funcionário quando este é diferente do CR definido na configuração da integração.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35834396454679)

 **SOLUÇÃO:**

O parâmetro “**Permite rateio para único CR/Projeto – FPRATEIOUNICO**” deve ser habilitado quando houver necessidade de gerar rateio para um único Centro de Resultado (CR), especialmente em situações em que o CR do funcionário seja diferente do CR configurado na integração financeira.

**Para ativar o parâmetro:**

- 

Acesse a tela **''Preferências''** (Configurações» Avançado); 

- 

Localize o parâmetro FPRATEIOUNICO;

- 

Ative-o conforme demonstrado na imagem abaixo.

![image (58).png](https://ajuda.sankhya.com.br/hc/article_attachments/36310899970583)

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35834403885207)

** CAUSA:**

O rateio não é gerado para um único** **Centro de Resultado (CR) porque, por padrão, o sistema só processa o rateio quando existem lançamentos para mais de um CR na mesma integração.

Além disso, o CR do funcionário é diferente do CR configurado na integração financeira, e o parâmetro FPRATEIOUNICO não está habilitado, o que impede a geração do rateio em situações com apenas um CR.