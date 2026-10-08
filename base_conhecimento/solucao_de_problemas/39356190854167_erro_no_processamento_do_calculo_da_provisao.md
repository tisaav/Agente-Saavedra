# Erro no Processamento do Cálculo da Provisão.

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39356190854167-Erro-no-Processamento-do-C%C3%A1lculo-da-Provis%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/39356190854167-Erro-no-Processamento-do-C%C3%A1lculo-da-Provis%C3%A3o)  
> **ID:** `39356190854167` | **Última Atualização:** 2026-09-26T01:29:33Z

---

**Não é possível gerar a provisão de férias, pois não há folha de pagamento calculada para o período informado.**
 

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/42315261841431)

 **Situação**

Ao tentar calcular e integrar as provisões de férias de alguma competência, o sistema apresenta a mensagem de que não existe folha de pagamento calculada para o período informado. Em razão dessa inconsistência, o processamento e a integração contábil das provisões mensais de férias dos colaboradores não podem ser concluídos.

 

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/42315261842455)

 **Solução**

Para resolver este incidente, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39356190847127)

 Acesse a tela **Gerenciador de Folhas** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e verifique se há uma folha de pagamento calculada para a competência.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39356190847511)

 Caso não haja folha de pagamento calculada para a competência, realize o cálculo da folha de salário antes de efetuar o processamento da provisão de férias.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39356160920983)

 Verifique se os colaboradores possuem períodos aquisitivos cadastrados. Para isso, acesse a tela **Requisições** (Pessoal+ » Rotinas Folha » Requisições), clique no ícone de **Férias**, aplique os filtros de empresa, departamento e colaborador e, em seguida, clique na opção **"Aquisitivo"** para consultar os períodos cadastrados.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39356160923159)

 Confirme se os períodos aquisitivos estão cadastrados com as datas corretas e sem informações inconsistentes que possam interferir no cálculo. 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39356190848791)

 Verifique se não existem provisões calculadas para competências posteriores do cálculo atual. Caso existam, realize a exclusão dessas provisões, pois o cálculo deve ser processado em ordem cronológica, respeitando a sequência das competências.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39356160924439)

 Após confirmar que a folha de salário foi calculada, que os períodos aquisitivos estão cadastrados corretamente e que não há provisão calculada em competências posteriores, acesse novamente a rotina de cálculo da provisão de férias e realize o processamento.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/39356160924823)

 Após realizar os ajustes necessários, execute o cálculo da provisão referente à competência e verifique se o processamento é concluído sem erros. Em seguida, após a geração das provisões, realize a integração contábil dos valores calculados.

 

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/42315261843863)

 **Causa**

O erro ocorre porque o sistema necessita de uma folha de pagamento calculada como base para processar a provisão de férias. Sem a folha mensal calculada, não existem valores de referência para a apuração proporcional das provisões.

Além disso, inconsistências nos períodos aquisitivos, como datas incorretas ou ausência de períodos cadastrados, podem impedir o processamento correto da provisão.

Outro ponto importante é que o cálculo das provisões deve seguir a ordem cronológica das competências. Dessa forma, caso existam provisões já calculadas para competências posteriores à que está sendo processada, o sistema não permitirá o cálculo da competência anterior. Nessa situação, será necessário excluir as provisões das competências subsequentes e, em seguida, recalcular a provisão da competência desejada, como janeiro/2025.