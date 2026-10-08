# Erro ao imprimir/visualizar DANFE : "Erro no modelo do documento adotado para impressão. Detalhes: null"

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39359196046103-Erro-ao-imprimir-visualizar-DANFE-Erro-no-modelo-do-documento-adotado-para-impress%C3%A3o-Detalhes-null](https://ajuda.sankhya.com.br/hc/pt-br/articles/39359196046103-Erro-ao-imprimir-visualizar-DANFE-Erro-no-modelo-do-documento-adotado-para-impress%C3%A3o-Detalhes-null)  
> **ID:** `39359196046103` | **Última Atualização:** 2026-08-13T19:20:37Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39359227665047)

 Mensagem**

Documento [número]: Erro no modelo do documento adotado para impressão. Detalhes: null

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39359196042007)

 Situação**

Este erro ocorre ao tentar "**Imprimir o DANFE**" ou "**Visualizar a nota fiscal**" após a aprovação da nota. O sistema apresenta a mensagem de erro indicando problema no modelo de impressão, impedindo a geração do documento.

**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/42701839289367)

Principais causas do erro**

- 
**XML não retornado/gravado no sistema:** embora a nota tenha sido "Aprovada" com sucesso pela SEFAZ, o XML autorizado não foi retornado ou não foi gravado no sistema. Como o modelo de impressão busca as informações diretamente do XML da nota fiscal, a ausência desse arquivo impede a geração do documento.

- 
**XML presente, porém com inconsistência:** o XML foi gravado no sistema, mas contém tags obrigatórias ausentes, com valores inválidos ou fora do padrão esperado pelo modelo de impressão. Nesse caso, o modelo tenta ler um campo que não existe ou está nulo no XML, resultando no mesmo erro ("Detalhes: null").

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39359227668631)

 Causa**

Se o problema persistir após validar XML e modelo de impressão, se faz necessario analise do log, pois "Detalhes: null" é um erro genérico que pode mascarar causas distintas.