# Ajuste necessário para evitar desconto incorreto de DSR em casos sem faltas

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36025663098391-Ajuste-necess%C3%A1rio-para-evitar-desconto-incorreto-de-DSR-em-casos-sem-faltas](https://ajuda.sankhya.com.br/hc/pt-br/articles/36025663098391-Ajuste-necess%C3%A1rio-para-evitar-desconto-incorreto-de-DSR-em-casos-sem-faltas)  
> **ID:** `36025663098391` | **Última Atualização:** 2026-08-27T18:28:44Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36025829643159)

** SITUAÇÃO:**

Ao realizar o cálculo da folha de pagamento, foi identificado que o evento de desconto de DSR está sendo apresentado indevidamente, mesmo sem existirem faltas lançadas. Essa ocorrência acontece mesmo com a regra de cálculo configurada com o campo “Atualiza Atrasos p/ Descontos de DSR” definido como “Nunca atualiza”

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36025829644183)

** SOLUÇÃO:**

Para evitar que o desconto de DSR seja apresentado de forma indevida no cálculo da folha, é necessário definir um limite de horas de atraso no campo “Limite de Atrasos para Perda de DSR”, conforme a regra estabelecida pela empresa.

Para ajustar a configuração, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36157305943575)

 Acesse a tela** ''Regra de Cálculo'' ***(Pessoal+» Cadastros), *na aba **''Ponto''**, e localize os campos:

- 

“**Atualiza Atrasos p/ Descontos de DSR”**

- 

**“Limite de Atrasos para Perda de DSR”**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36157305945879)

 Mantenha o campo Atualiza Atrasos p/ Descontos de DSR configurado como “**Nunca atualiza**”;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36157305947287)

 Preencha o campo Limite de Atrasos para Perda de DSR com o valor desejado (por exemplo, 1000, equivalente a 10 horas; 

Após essa configuração, o sistema passará a considerar o limite de horas informado, deixando de aplicar o desconto de DSR de forma indevida.

 

![image (43).png](https://ajuda.sankhya.com.br/hc/article_attachments/36157305948823)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36025829651735)

** CAUSA:**

Mesmo com o campo Atualiza Atrasos p/ Descontos de DSR configurado como “Nunca atualiza”, o desconto de DSR foi gerado porque o campo Limite de Atrasos para Perda de DSR não estava devidamente preenchido.

Quando este campo permanece com o valor 0 (zero), o sistema interpreta que qualquer atraso já ultrapassa o limite permitido, resultando automaticamente na aplicação do desconto de DSR durante o cálculo da folha.