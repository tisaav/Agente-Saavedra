# Cálculo de DSR considerando mais dias úteis do que o esperado. Como resolver ?

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360051751274-C%C3%A1lculo-de-DSR-considerando-mais-dias-%C3%BAteis-do-que-o-esperado-Como-resolver](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051751274-C%C3%A1lculo-de-DSR-considerando-mais-dias-%C3%BAteis-do-que-o-esperado-Como-resolver)  
> **ID:** `360051751274` | **Última Atualização:** 2026-07-29T13:21:50Z

---

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610263788695)

 **CAUSA:**

Foi feito a marcação do campo "ESTENDER PERÍODO PARA ADEQUAÇÃO AO ESOCIAL" indevidamente, pois o mesmo não estava fazendo mudança do período de apuração do ponto para se adequar ao Esocial, ou seja só vai utilizar esta marcação apenas para mudança do período de apuração. 

** **

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610263796631)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610263797527)

 No cadastro da empresa << Informações Gerais, verificar se foi cadastrado corretamente o 'Dia Início apuração'.

De acordo com este período de apuração verificar no log como foram calculados os campos abaixo para a respectiva referência:

- DIASUTEISTRAB =

- DIASNAOUTEISTRAB =

Caso o cálculo apresente divergências, é válido verificar a seguinte marcação:

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610263803159)

 Acesse o módulo Controle de Ponto. Na tela "Controle do ponto" verificar se o campo "ESTENDER PERÍODO PARA ADEQUAÇÃO AO ESOCIAL" está marcado.

- ***ADEQUAÇÃO AO E-SOCIAL: ******O processo de estender o período de apuração, deve ser realizado apenas para mudança do período de apuração do ponto, para o primeiro dia do mês. A alteração do período de apuração, deve ocorrer após o fechamento do ponto e atualização do movimento.***

Se a situação não se enquadrar no caso acima, desmarque essa opção e recalcule a folha mensal do funcionário.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610263808663)

 Valide se o cálculo foi realizado conforme esperado.