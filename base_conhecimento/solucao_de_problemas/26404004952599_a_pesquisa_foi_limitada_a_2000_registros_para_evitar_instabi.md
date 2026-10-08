# A pesquisa foi limitada a 2000 registros para evitar instabilidade

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26404004952599-A-pesquisa-foi-limitada-a-2000-registros-para-evitar-instabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/26404004952599-A-pesquisa-foi-limitada-a-2000-registros-para-evitar-instabilidade)  
> **ID:** `26404004952599` | **Última Atualização:** 2026-09-09T20:52:38Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26403974136727)

 **MENSAGEM:**

A pesquisa foi limitada a 2000 registros para evitar instabilidade

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26403974138391)

SOLUÇÃO:**

A limitação é determinada pelo parâmetro **"MAXRSLTSIZE" - Qtd. máx. linhas result. consultas"**, que define o máximo de linhas resultantes na consulta.

Em ambientes locais, ele pode ser modificado conforme necessidade, mas é preciso ter cuidado, pois um aumento excessivo pode causar lentidão.
Em ambientes de nuvem, a alteração não é permitida, sendo necessário acionar a hospedeira e solicitar a desativação do gatilho que bloqueia a alteração, para que ela esteja ciente da alteração do parâmetro e dos possíveis impactos na lentidão.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41288295457047)

 ****OBSERVAÇÃO:**** **A limitação não foi implementada no Layout HTML5 (Interface 2016). Portanto, essas configurações só tem impacto no layout Flex (Interface 2010).

A mensagem de carregamento exibida durante a consulta é um comportamento padrão do sistema e continuará sendo apresentada mesmo após a alteração do parâmetro ''MAXRSLTSIZE''. Esse parâmetro apenas aumenta a quantidade de registros retornados na consulta e exportados para XLS, não interferindo na exibição da mensagem.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26404004939031)

CAUSA:**

Ocorre conforme configuração do parâmetro que limita o numero máximo de linhas nas consultas.