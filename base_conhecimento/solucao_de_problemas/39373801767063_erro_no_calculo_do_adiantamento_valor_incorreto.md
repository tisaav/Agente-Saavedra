# Erro no Cálculo do Adiantamento - Valor Incorreto

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39373801767063-Erro-no-C%C3%A1lculo-do-Adiantamento-Valor-Incorreto](https://ajuda.sankhya.com.br/hc/pt-br/articles/39373801767063-Erro-no-C%C3%A1lculo-do-Adiantamento-Valor-Incorreto)  
> **ID:** `39373801767063` | **Última Atualização:** 2026-07-29T13:23:12Z

---

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39373815295895)

 **Situação**

Ao processar a folha de adiantamento, o sistema apresenta um valor diferente do esperado. Isso ocorre principalmente em meses com quantidade de dias diferente de 30, quando a fórmula personalizada utiliza uma divisão fixa por 30 e multiplica pela variável **"&DIASTRA"**, resultando em cálculos proporcionais incorretos.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39373815296151)

 **Solução**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39373815296279)

 Acesse a tela **"Regras de Cálculo"** (Pessoal+ » Cadastros » Regras de Cálculo) e localize a regra de cálculo utilizada pelos funcionários com divergência no adiantamento.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39373815296663)

 Na aba **"Tipo de Mês"**, verifique se a opção **"Calcula resíduo de afastamento em meses que não possuem 30 dias"** está marcada corretamente para a referência atual.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39373801762327)

 Verifique a fórmula personalizada do evento de adiantamento. Se a fórmula utiliza divisão fixa por 30, ajuste-a para utilizar variáveis que se adaptem automaticamente ao tipo de mês configurado na regra de cálculo.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39373815296919)

 Após os ajustes, recalcule a folha de adiantamento para os funcionários afetados e valide se o valor está correto (40% do salário base).

 
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39373815298711)

 **Causa**

O erro ocorre quando a fórmula personalizada do adiantamento utiliza uma divisão fixa por 30 dias e multiplica pela variável **"&DIASTRA"**, que é sensível às configurações do tipo de mês definidas na regra de cálculo. Em meses com 31 dias, por exemplo, a conta realiza uma divisão por 30 e uma multiplicação por 31, fazendo com que o valor final não seja compatível com os 40% esperados.

Além disso, a marcação incorreta da opção **"Calcula resíduo de afastamento em meses que não possuem 30 dias"** no histórico da regra de cálculo pode gerar divergências no cálculo proporcional.

A solução definitiva envolve ajustar a fórmula personalizada para que utilize variáveis dinâmicas, garantindo que mesmo com mudanças nas regras de cálculo ou no tipo de mês, a proporcionalidade seja calculada corretamente.