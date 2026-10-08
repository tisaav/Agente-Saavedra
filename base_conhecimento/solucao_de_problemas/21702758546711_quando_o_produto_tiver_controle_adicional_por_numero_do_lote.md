# Quando o produto tiver controle adicional por numero do lote e opção tem rasto do lote marcado, o campo unidade do lote e obrigatório

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/21702758546711-Quando-o-produto-tiver-controle-adicional-por-numero-do-lote-e-op%C3%A7%C3%A3o-tem-rasto-do-lote-marcado-o-campo-unidade-do-lote-e-obrigat%C3%B3rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/21702758546711-Quando-o-produto-tiver-controle-adicional-por-numero-do-lote-e-op%C3%A7%C3%A3o-tem-rasto-do-lote-marcado-o-campo-unidade-do-lote-e-obrigat%C3%B3rio)  
> **ID:** `21702758546711` | **Última Atualização:** 2026-07-22T14:49:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21702743633815)

 **MENSAGEM:**

[CORE_E07619] Quando o produto tiver controle adicional por numero do lote e opção tem rasto do lote marcado, o campo unidade do lote e obrigatório.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21702743637143)

CAUSA:**

Acontece quando o parâmetro **"Usar unidade do lote para conversão do qLote - USARUNIDLOTE" **está ligado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/21702758544279)

SOLUÇÃO:**

Existe um parâmetro que habilita esse campo o nome dele é **"Usar unidade do lote para conversão do qLote - USARUNIDLOTE"**, foi feito a correção do fato desse parâmetro estar sendo aplicado de forma indevida na tela em FLEX, ele atua somente em HTML5. Desligando, será possível continuar com o processo.