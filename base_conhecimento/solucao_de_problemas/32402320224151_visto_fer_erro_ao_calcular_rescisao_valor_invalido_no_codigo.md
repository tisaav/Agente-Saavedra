# (Visto Fer) Erro ao Calcular Rescisão: Valor Inválido no Código de Afastamento

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32402320224151--Visto-Fer-Erro-ao-Calcular-Rescis%C3%A3o-Valor-Inv%C3%A1lido-no-C%C3%B3digo-de-Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/32402320224151--Visto-Fer-Erro-ao-Calcular-Rescis%C3%A3o-Valor-Inv%C3%A1lido-no-C%C3%B3digo-de-Afastamento)  
> **ID:** `32402320224151` | **Última Atualização:** 2026-07-29T13:19:52Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32552053957015)

** MENSAGEM:**

Falha - Character T is neither a decimal digit number, decimal point, nor "e" notation exponential mark.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32402320217367)

** SITUAÇÃO:**

Ao tentar calcular a rescisão de um funcionário, o sistema exibe a mensagem acima.

 

#### **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309866126615)

 Interpretando a Mensagem do Erro:**

***Character T is neither a decimal digit number, decimal point, nor 'e' notation exponential mark.***

*(O caractere "T" não é um número decimal, ponto decimal ou marca exponencial de notação "e"). *

Essa mensagem indica que há uma tentativa de realizar um cálculo ou conversão numérica sobre um campo que contém **letras**, o que não é permitido nesse contexto. Podendo haver os seguintes cenários:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32533563713943)

 O código de afastamento vinculado ao aviso prévio ou desligamento **foi registrado com letras** (por exemplo: **"T C"**), o que é inválido para o campo **CAUSAAFAST **da tabela **TFPFUN**, que exige exclusivamente valores numéricos.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32533563713943)

O campo **CODAFASTCAGED**, por sua vez, aceita letras por ser do tipo **VARCHAR2**; no entanto, não pode ser utilizado diretamente em operações que exigem valores numéricos. 

 

![192549fd-fdff-4855-8afc-929744d8e4bc.png](https://ajuda.sankhya.com.br/hc/article_attachments/32533209098519)

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32402334974999)

** SOLUÇÃO:**

Para corrigir o problema e permitir o cálculo da rescisão, siga os passos abaixo: 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32532414504855)

 Na Tela **"Código de Afastamento'' ***(Pessoal+» Cadastros » Código de Afastamento)***, **cadastre um novo **Código de Afastamento** utilizando apenas números: 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32532414509207)

 Crie um novo código numérico (por exemplo: 99), contendo as informações compatíveis com o tipo de rescisão a ser realizada, assegurando que não haja o uso de letras.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32533534285207)

 Na tela **"Tipo de rescisão"** *(Pessoal+» Cadastros » Tipo de Rescisão)***,** vincule o novo código ao **Tipo de Rescisão**.

**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32533563722263)

Exclua o aviso anterior do funcionário** (que estava vinculado ao código inválido) e **registre um novo aviso** com o código de afastamento correto.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32533534289815)

 Refaça o cálculo da rescisão.**

**

Após essa correção, o sistema conseguirá interpretar os dados corretamente e concluir o cálculo da rescisão sem apresentar erros.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32402334973847)

** CAUSA:**
O erro está relacionado ao **código da causa do afastamento** vinculado ao aviso prévio ou ao desligamento do funcionário.
O sistema tenta interpretar o conteúdo do campo **"CAUSAAFAST"** como um valor numérico, porém foi identificado um valor inválido contendo letras, como exemplo: '**T C'**. 
Dessa forma, o interpretador da aplicação não consegue realizar conversões ou comparações adequadas, pois espera um valor numérico e recebeu um valor alfanumérico.