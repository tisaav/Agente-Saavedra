# Melhores Práticas para o uso da 'Análise de Giro'

> **Módulo:** Melhores Praticas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580334-Melhores-Pr%C3%A1ticas-para-o-uso-da-An%C3%A1lise-de-Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580334-Melhores-Pr%C3%A1ticas-para-o-uso-da-An%C3%A1lise-de-Giro)  
> **ID:** `360044580334` | **Última Atualização:** 2026-07-30T03:30:24Z

---

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/42331432118295)

 **SITUAÇÃO**

Os indicadores da tela "Análise de Giro" (Comercial >> Consulta >> Análise de Giro)  permanecem zerados, mesmo após baixas de produtos e configuração dos Tipos de Operação (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP).

Todos os indicadores da tela são gerados por uma única rotina de consolidação, que grava os dados na tabela TGFGIR1. Se essa consolidação não roda ou filtra o registro para fora, todos os indicadores ficam zerados, não apenas um específico.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/42331432118807)

 **SOLUÇÃO**

Para resolver este problema, execute os seguintes passos:

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16536420084759)

 Em "Cadastro de Produtos" (Comercial >> Cadastros >> Produtos), aba "Medidas e Estoque" >> "Estoque", verifique se **"Calcular giro pelo agendador"** está marcado como "Sim" para os produtos desejados.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16536436181783)

 Verifique se o **"Agendador de Consolidação da Análise de Giro"** está ativo e em execução.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42331432119575)

 Em "Tipos de Operação", aba "Geral", verifique o campo **"Análise de Giro"**:

- 
**Venda (Saída)** para TOPs de venda;

- 
**Devolução de venda (Entrada)** para TOPs de devolução.

- Se estiver como "Desconsiderar", a TOP fica de fora do cálculo.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42331432122391)

 Confirme se a nota atende aos critérios exigidos pela consolidação:

- Status **"Liberada"** (Atendimento e Pendente não entram);

- Valor total maior que 0;

- Todos os itens com valor unitário e quantidade negociada maiores que 0.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42331432122903)

 Aguarde a próxima execução do agendador ou execute-o manualmente na tela "Análise de Giro" para reprocessar os dados.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42331432123287)

 Se persistir, acesse "Cache do Servidor" (Configurações >> Avançado >> Cache do Servidor), feche a tela "Análise de Giro", descarte o cache e retorne ao sistema.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/42331432123671)

 **CAUSA**

- 
**Produto** não marcado para calcular giro pelo agendador.

- 
**Agendador de consolidação** inativo.

- 
**TOP** configurada como "Desconsiderar" no campo Análise de Giro.

- 
**Nota** fora da situação exigida: não liberada, valor zerado, ou item com valor/quantidade zerada.

- 
**Cache** do navegador ou servidor com dados antigos.

Essas configurações se aplicam para **todos** os indicadores da tela, pois derivam da mesma consolidação.

**Observação:** por ser rotina de primeiro uso na empresa, recomenda-se que um consultor apresente o funcionamento do processo e valide a configuração conforme a necessidade do cliente