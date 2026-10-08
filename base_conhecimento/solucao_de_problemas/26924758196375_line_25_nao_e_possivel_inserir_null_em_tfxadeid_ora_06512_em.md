# LINE 25 - Nao é possível inserir NULL em ("TFXADE"."ID") ORA-06512: em "TRG_FX_TFXPRC"

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26924758196375-LINE-25-Nao-%C3%A9-poss%C3%ADvel-inserir-NULL-em-TFXADE-ID-ORA-06512-em-TRG-FX-TFXPRC](https://ajuda.sankhya.com.br/hc/pt-br/articles/26924758196375-LINE-25-Nao-%C3%A9-poss%C3%ADvel-inserir-NULL-em-TFXADE-ID-ORA-06512-em-TRG-FX-TFXPRC)  
> **ID:** `26924758196375` | **Última Atualização:** 2026-07-22T14:40:33Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26924758145687)

 **MENSAGEM:**

Ao realizar alguma alteração no cadastro de produtos, é apresentada a mensagem abaixo.

**ORA-01400: nao é possível inserir NULL em ("TFXADE"."ID") ORA-06512: em "TRG_FX_TFXPRC", line 25 ORA-04088: erro durante a execução do gatilho ‘TRG_FX_TFXPRC'**

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26924758152983)

SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26924758157207)

 O erro ocorre quando a Trigger 'TRG_FX_TFXADE' não existe no banco de dados.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450236620567)

 Para recriar esse objeto, faça a atualização do sistema para que os Scripts do banco sejam executados novamente. Ou, entre em contato com o Service Desk da Sankhya para obter o Script a ser executado, visto que pode sofrer alterações conforme novos releases do sistema.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26924758165911)

CAUSA:**

Ocorre quando uma Trigger nativa do sistema não existe na base de dados.