# Erro ao processar relatório formatado do envio de email

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9136004992023-Erro-ao-processar-relat%C3%B3rio-formatado-do-envio-de-email](https://ajuda.sankhya.com.br/hc/pt-br/articles/9136004992023-Erro-ao-processar-relat%C3%B3rio-formatado-do-envio-de-email)  
> **ID:** `9136004992023` | **Última Atualização:** 2026-07-22T15:10:25Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033356687383)

 MENSAGEM:**

[CORE_E05181]  Erro ao processar relatório formatado do envio de email.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033375130647)

 SITUAÇÃO:**

Ao tentar confirmar o lançamento de uma nota fiscal a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033375137687)

 CAUSA: **

Quando a logo não está inserida corretamente no caminho definido no parâmetro **"Pasta de modelos para impressão -** ***SERVDIRMOD" ***.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19033356702615)

 SOLUÇÃO:**

Analise o caminho apresentado na mensagem e certifique-se de que a logo está inserida corretamente nele, confira também se esse caminho da logo está cadastrado no parâmetro **"Pasta de modelos para impressão -** ***SERVDIRMOD" ***.

 

**Importante: **Se o erro for apresentado utilizando uma determinada TOP, verifique se o arquivo em TXT inserido na aba e-mail da TOP é realmente necessário. Caso não seja, retire-o e tente confirmar o lançamento novamente.