# Só é possível incluir uma alíquota com os dados já existentes se o parâmetro "PODEDUPALIQICMS" estiver ligado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9305784643607-S%C3%B3-%C3%A9-poss%C3%ADvel-incluir-uma-al%C3%ADquota-com-os-dados-j%C3%A1-existentes-se-o-par%C3%A2metro-PODEDUPALIQICMS-estiver-ligado](https://ajuda.sankhya.com.br/hc/pt-br/articles/9305784643607-S%C3%B3-%C3%A9-poss%C3%ADvel-incluir-uma-al%C3%ADquota-com-os-dados-j%C3%A1-existentes-se-o-par%C3%A2metro-PODEDUPALIQICMS-estiver-ligado)  
> **ID:** `9305784643607` | **Última Atualização:** 2026-07-22T15:08:52Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666706725399)

 MENSAGEM:**

[CORE_E02108] Só é possível incluir uma alíquota com os dados já existentes se o parâmetro "PODEDUPALIQICMS" estiver ligado.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666706737175)

 SITUAÇÃO:**

Ao incluir em todos os estados, o CST 41, alíquota 0% para a TOP retorno de conserto a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666735905815)

 CAUSA:**

Tentar duplicar uma alíquota.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18666706752023)

 SOLUÇÃO:**

Habilite o parâmetro **PODEDUPALIQICMS **na tela **Preferências** *(Configurações » Avançado » Preferências):*

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9305777362455)

Com o parâmetro **"Permite duplicar cad. de tributação alíquota ICMS? - PODEDUPALIQICMS" **ativo, quando for realizada a duplicação de uma alíquota, todos os dados pertinentes à ela serão reproduzidos também na nova alíquota gerada, tais como, Tributação, Alíquota, Redução da Base etc.