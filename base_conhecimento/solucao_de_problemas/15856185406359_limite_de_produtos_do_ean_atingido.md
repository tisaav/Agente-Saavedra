# Limite de produtos do EAN atingido

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/15856185406359-Limite-de-produtos-do-EAN-atingido](https://ajuda.sankhya.com.br/hc/pt-br/articles/15856185406359-Limite-de-produtos-do-EAN-atingido)  
> **ID:** `15856185406359` | **Última Atualização:** 2026-07-22T14:56:00Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15856195584535)

 MENSAGEM:**

[CORE_E01824] Limite de produtos do EAN atingido.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15856195589527)

 CAUSA:**

Ocorre porque a quantidade de números disponíveis para criação do EAN13 foi atingido.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15856240769559)

 SOLUÇÃO:**

O EAN13 é composto por 13 números, dos treze dígitos, doze são dos dados referentes ao produto e um é o dígito verificador.
 Na tela 'Configuração de EAN13' o campo 'Código EAN' refere-se ao números que serão apresentado no inicio do código, ou seja, caso seja cadastrado o seguinte número: '1234567', estes serão os sete primeiro dígitos do código de barras.
 Ao final na numeração tem-se o dígito verificador (usaremos o 3 como exemplo).
 O campo 'Sequencial' é utilizado para a geração do código (os números entre o 'Código EAN' e o dígito verificador: 1234567**XXXXX**3). 
 O Aviso "Limite de produtos do EAN atingido!" refere-se a estes números do campo 'Sequencial'. Caso seja cadastrado 'zero' o sistema irá gerar códigos de barras até utilizar todos os números (0 a 99999), ao atingir o último número o aviso é apresentado.

Acessar a tela "Configuração do gerador de código EAN13",    incluir um novo CODIGO EAN  e uma nova  'SEQUENCIA'