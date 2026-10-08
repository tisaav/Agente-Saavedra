# Não foi possível obter página "X[1]", pois o processo demorou demais. Código: CORE_E00359

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9088374877207-N%C3%A3o-foi-poss%C3%ADvel-obter-p%C3%A1gina-X-1-pois-o-processo-demorou-demais-C%C3%B3digo-CORE-E00359](https://ajuda.sankhya.com.br/hc/pt-br/articles/9088374877207-N%C3%A3o-foi-poss%C3%ADvel-obter-p%C3%A1gina-X-1-pois-o-processo-demorou-demais-C%C3%B3digo-CORE-E00359)  
> **ID:** `9088374877207` | **Última Atualização:** 2026-07-22T15:10:37Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19277454994327)

 MENSAGEM:**

[CORE_E00359] Não foi possível obter página "X[1]", pois o processo demorou demais.

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34101055019287)

**

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19277500053655)

SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34101069213207)

** Parâmetro ''**MAXRSLTSIZE'':**

O parâmetro MAXRSLTSIZE limita a quantidade de registros retornados nas consultas das telas. Quando configurado com um valor muito alto ou desativado, pode causar lentidão e exceder o tempo máximo de resposta. Ajustá-lo para restringir os registros ajuda a evitar esse problema.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34101069215255)

 **Timeout da consulta** ''-Djape.global.query.timeout'': **

O argumento -Djape.global.query.timeout define o tempo limite para execução de consultas SQL, com valor padrão de 600 segundos. Consultas que excedem esse tempo geram erro. Aumentar o limite é possível, mas deve ser feito com cautela, pois pode ocultar problemas de desempenho.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34101310907031)

**Local para ajuste:

- Linux: WILDFLY_INSTALL/bin/standalone.conf

- Windows: WILDFLY_INSTALL/bin/standalone.conf.bat

⚠️ **Importante:** Antes de qualquer alteração, é essencial validar se a tela realmente precisa de tanto tempo para concluir a consulta. Aumentar o timeout resolve o erro imediato, mas não trata a causa raiz de lentidão.

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34101055026327)

 **Parâmetro **''DESABPAGINA'':**

O parâmetro DESABPAGINA desativa a paginação nas consultas, fazendo com que todos os dados sejam retornados de uma vez. Isso pode reduzir o tempo de execução em alguns casos, ao evitar múltiplas chamadas ao banco. No entanto, seu uso deve ser criterioso, pois pode aumentar o volume de dados retornado e agravar problemas de desempenho se não for combinado com filtros adequados e ajuste do MAXRSLTSIZE.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19277500048151)

 CAUSA:**

A causa raiz do erro está relacionada ao tempo excessivo de execução das consultas SQL acionadas por determinadas telas do sistema. Isso geralmente ocorre devido a:

- 

Volume elevado de dados processados de uma só vez;

- 

Ausência ou uso inadequado de filtros nas consultas;

- 

Má configuração de parâmetros de performance (como MAXRSLTSIZE, DESABPAGINA e -Djape.global.query.timeout);

- 

Consultas mal otimizadas ou uso de visões complexas que exigem alto tempo de processamento.

Caso o problema persista mesmo após seguir as orientações deste artigo, recomenda-se abrir um chamado com o time de Service Desk.