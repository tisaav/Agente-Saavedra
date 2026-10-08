# Configurações que influenciam no cálculo das médias

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32909754314007-Configura%C3%A7%C3%B5es-que-influenciam-no-c%C3%A1lculo-das-m%C3%A9dias](https://ajuda.sankhya.com.br/hc/pt-br/articles/32909754314007-Configura%C3%A7%C3%B5es-que-influenciam-no-c%C3%A1lculo-das-m%C3%A9dias)  
> **ID:** `32909754314007` | **Última Atualização:** 2026-08-17T20:43:14Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/41069765226519)

 Ausência de eventos que utilizem médias:**

Para que as médias sejam exibidas corretamente na tela **Cálculos** (Pessoal+ » Cadastros » Eventos), na aba **Médias**, é necessário que exista ao menos um cálculo de evento de média de férias ou de 13º salário na folha em questão, mesmo que o valor calculado seja **R$ 0,00**.

Por esse motivo, em algumas folhas mensais ou de férias, a aba **Médias** pode não apresentar informações quando não houver nenhum evento de média processado na folha. 
 

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/41069765227415)

 Sequência dos eventos:**

Se apenas alguns eventos forem exibidos enquanto outros não aparecem, verifique a sequência do evento. Os eventos que compõem a base de cálculo (como horas extras e DSR) devem possuir uma sequência inferior à do evento de média que os utiliza.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/41069755386903)

**SOLUÇÃO:**

Para consultar a sequência de um evento, acesse a tela **"Eventos"** (Pessoal+ >> Cadastros >> Eventos), selecione o evento desejado e localize o campo **"Sequência"**. Ajuste o mesmo com valor menor que o evento de médias.

![image (9).png](https://ajuda.sankhya.com.br/hc/article_attachments/33226584201495)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41069755387799)

 **Médias com valor inferior ao esperado**

Na aba **Médias** da tela **Cálculos** Pessoal+ » Rotinas Folha » Cálculos), podem ser apresentados valores inferiores aos esperados. Esse comportamento ocorre quando as informações não foram atualizadas corretamente na tela **Acumulados do Ano** (Pessoal+ » Consultas » Acumulados do Ano).

Para identificar a situação, compare os valores de cada referência exibidos na aba **Médias** com os valores efetivamente calculados nas respectivas folhas.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/41069755386903)

**SOLUÇÃO:**

Caso sejam encontradas divergências, reabra a referência pela tela **Gerenciador de Folhas** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e realize o fechamento novamente. Esse procedimento atualizará os acumulados e corrigirá os valores apresentados na aba **Médias**. 

**Após o processo recalcule a folha para que o evento passe a ser considerado na aba de médias.**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41069755387927)

 **Evento não compondo as médias**

Quando um evento que deveria compor as médias não é apresentado na aba **Médias** da tela **Cálculos** (Pessoal+ » Rotinas Folha » Cálculos), isso indica que ele pode não estar configurado para incidência em médias.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/41069755386903)

**SOLUÇÃO:**

Acesse a tela **Eventos (Pessoal+ » Cadastros » Eventos)** e, na aba **Avançado**, verifique o campo **Incide sobre Médias**.

Confirme se o campo está configurado como:

- 

**Incide nas médias pelo valor**, ou

- 

**Incide nas médias pelo índice**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41069765230871)

Caso a configuração esteja incorreta, realize o ajuste conforme a regra desejada e recalcule a folha para que o evento passe a ser considerado na aba de médias.