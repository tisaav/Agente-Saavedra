# Não é permitido filtro por empresa quando o custo não é por empresa

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/6978749917847-N%C3%A3o-%C3%A9-permitido-filtro-por-empresa-quando-o-custo-n%C3%A3o-%C3%A9-por-empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/6978749917847-N%C3%A3o-%C3%A9-permitido-filtro-por-empresa-quando-o-custo-n%C3%A3o-%C3%A9-por-empresa)  
> **ID:** `6978749917847` | **Última Atualização:** 2026-07-22T15:15:33Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16478149341335)

 MENSAGEM:**

[CORE_E03963]Não é permitido filtro por empresa quando o custo não é por empresa.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16478149345687)

 SOLUÇÃO:**

O Kardex permite a visualização por empresas apenas nos casos em que o parâmetro **"****CUSTOPOREMP"** esteja habilitado.

**Importante: **esse parâmetro **não deve ser ajustado** sem uma análise criteriosa dos responsáveis pelo gerenciamento de custos na empresa, visto impactos que essa mudança representa no processo de custo. 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16478149349015)

CAUSA: **

Caso o parâmetro esteja desabilitado, os custos gravados na tabela de custos ficam registrados com o CODEMP = 1, não fazendo sentido o filtro por empresas, justificando a mensagem apresentada. 

Isso se faz necessário, pois como o relatório Kardex é um documento oficial, os custos apresentados devem coincidir com as movimentações da empresa. Caso não controle os custos por empresa, não existe a possibilidade de apresentar um estoque separado.