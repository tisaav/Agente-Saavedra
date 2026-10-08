# General SQL error. A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, <, <=, >, >= ou quando ela

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7918407272087-General-SQL-error-A-subconsulta-retornou-mais-de-1-valor-Isso-n%C3%A3o-%C3%A9-permitido-quando-a-subconsulta-segue-um-ou-quando-ela](https://ajuda.sankhya.com.br/hc/pt-br/articles/7918407272087-General-SQL-error-A-subconsulta-retornou-mais-de-1-valor-Isso-n%C3%A3o-%C3%A9-permitido-quando-a-subconsulta-segue-um-ou-quando-ela)  
> **ID:** `7918407272087` | **Última Atualização:** 2026-07-29T13:24:31Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16584259544215)

**MENSAGEM**

A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, , =, >, >= ou quando ela é usada como uma expressão.

Em ambientes Oracle, a mensagem pode aparecer como: **"ORA-01427: a subconsulta de uma única linha retorna mais de uma linha"**.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/42310014968855)

**SITUAÇÃO**

Este erro pode ocorrer em diversas situações no sistema:

- Ao tentar **"imprimir pedidos de venda"** ou notas fiscais com modelos personalizados;

- Ao tentar imprimir o **"recibo de pagamento"**;

- Ao acessar a tela de **"Movimentação Financeira"** (Financeiro >> Movimentação Financeira) após atualizações do sistema;

- Ao realizar **"estorno de lançamentos"** financeiros;

- Ao processar **"reajuste salarial"** (Pessoal >> Consultas >> Reajuste Salarial) na folha de pagamento;

- Ao adicionar **"produtos em notas fiscais"** ou executar recálculo de custos;

- Ao processar vendas via **"TEF"** que geram duplicação de parcelas.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16584275189015)

**SOLUÇÃO**

A solução varia conforme o contexto em que o erro ocorre. Siga as orientações específicas para cada situação:

 

**Para erros em recibos de pagamento:**

Acesse a tela **"Lançamento de Movimento"** (Pessoal >> Lançamentos >> Lançamento de Movimento), aba **"Visualização"** e confira se existe o mesmo evento lançado mais de uma vez na mesma referência.

![lan_amento.png](https://ajuda.sankhya.com.br/hc/article_attachments/7920615016471)

Verifique também se existe o evento lançado na mesma sequência. Caso positivo, ajuste para uma sequência diferente.

![lan_amento2.png](https://ajuda.sankhya.com.br/hc/article_attachments/7922609017495)

**Para erros em modelos de impressão (JRXML):**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/42310014970391)

 Identifique a subconsulta que está retornando múltiplos registros no modelo de documento personalizado.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/42310014972439)

 Verifique se há **"duplicidade de registros"** nas tabelas consultadas (exemplo: tabela **"TGFPAP"** para produtos por parceiro).

![3](https://ajuda.sankhya.com.br/hc/article_attachments/42310014974103)

 Ajuste a consulta SQL adicionando cláusulas de restrição como **"ROWNUM = 1"** ou funções de agregação (**"MAX"**, **"MIN"**).

![4](https://ajuda.sankhya.com.br/hc/article_attachments/42310014974615)

 Corrija ou remova os **"registros duplicados"** no cadastro que está causando o problema.

 

**Para erros na Movimentação Financeira:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/42310014970391)

 Acesse a tela **"DBExplore"** (Configurações >> Avançado >> DBExplore) e identifique o número do acerto com erro.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/42310014972439)

 Verifique se existem **"duas despesas para o mesmo NUFIN"**, ambas do tipo **"Adiantamento"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/42310014974103)

 Execute a intervenção no banco de dados nas tabelas **"TGFFIN"** e **"TGFFRE"** conforme orientação técnica:

- DELETE FROM TGFFRE WHERE NUACERTO = [número_do_acerto];

- UPDATE TGFFIN SET NUCOMPENS = NULL WHERE NUCOMPENS IS NOT NULL;

 

**Para erros no Reajuste Salarial:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/42310014970391)

 Acesse a tela de **"Reajuste Salarial"** (Pessoal >> Consultas >> Reajuste Salarial).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/42310014972439)

 Utilize o filtro para selecionar **"apenas colaboradores ativos"** através da flag correspondente.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/42310014974103)

 Execute novamente o processo de reajuste com o filtro aplicado.

 

**Para erros ao adicionar produtos em notas:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/42310014970391)

 Identifique se o erro está relacionado a **"campos adicionais"** na tabela **"TGFITE"**.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/42310014972439)

 Acesse a tela **"Campos Adicionais"** (Configurações >> Cadastros >> Campos Adicionais) e localize o campo com problema.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/42310014974103)

 Revise a **"expressão SQL"** do campo adicional, garantindo que ela retorne apenas um valor.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/42310014974615)

 Ajuste a expressão adicionando cláusulas de restrição ou funções de agregação conforme necessário.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16584275194135)

**CAUSA**

Este erro ocorre quando uma **"subconsulta SQL"** que deveria retornar apenas um registro está retornando múltiplos valores. As causas mais comuns incluem:

- 
**"Duplicidade de registros"** em tabelas de cadastro (produtos, parceiros, configurações, eventos de folha);

- 
**"Consultas SQL mal estruturadas"** em modelos de documentos personalizados (JRXML);

- 
**"Expressões incorretas"** em campos adicionais que não possuem cláusulas de restrição adequadas;

- 
**"Processos executados incorretamente"** que geraram registros duplicados (exemplo: acertos financeiros, adiantamentos);

- 
**"Melhorias implementadas"** em atualizações do sistema que expõem inconsistências de dados pré-existentes;

- 
**"Falta de filtros adequados"** ao processar rotinas que envolvem múltiplos registros (exemplo: reajuste salarial sem filtro de colaboradores ativos).

 

**Observação importante:** A correção de consultas SQL em modelos customizados (JRXML) e campos adicionais pode exigir conhecimento técnico avançado. Caso necessário, considere solicitar apoio especializado para implementar as correções adequadamente.