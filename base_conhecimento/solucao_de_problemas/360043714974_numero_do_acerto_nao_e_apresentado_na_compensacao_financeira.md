# Número do Acerto não é apresentado na Compensação Financeira para desfazer

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043714974-N%C3%BAmero-do-Acerto-n%C3%A3o-%C3%A9-apresentado-na-Compensa%C3%A7%C3%A3o-Financeira-para-desfazer](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043714974-N%C3%BAmero-do-Acerto-n%C3%A3o-%C3%A9-apresentado-na-Compensa%C3%A7%C3%A3o-Financeira-para-desfazer)  
> **ID:** `360043714974` | **Última Atualização:** 2026-07-22T16:00:26Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290163558295)

 SITUAÇÃO:**

Quando acessado a Rotina Compensação Financeira para desfazer um Acerto, porém o número do acerto não é apresentado ao efetuar a consulta.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290149027991)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290149032855)

 Acesse: Configurações » Avançado » Preferências

Parâmetro: **"DIASCONSACERTO - Dias para consulta de acertos"**

Aumente o valor no campo Inteiro.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290149035415)

 Acesse: Financeiro » Rotinas » Compensação Financeira e efetue a consulta novamente.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290149041815)

 NOTA:**

Este parâmetro é utilizado para fins de performance e deve ser configurado com a menor quantidade de dias possíveis para o negócio da empresa. Assim, mais rápido será a execução da busca dos acertos realizados, para consulta ou possível anulação.

Por padrão o valor informado no parâmetro é 180 dias. Caso o acerto seja superior a 180 dias, deverá aumentar o valor, até que consiga o resultado na busca do número do acerto na rotina de Compensação Financeira.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17290149043991)

 CAUSA:**

Ocorre ao buscar um acerto que foi feito a "X" dias e a quantidade de dias do parâmetro DIASCONSACERTO é menor que "X" dias.