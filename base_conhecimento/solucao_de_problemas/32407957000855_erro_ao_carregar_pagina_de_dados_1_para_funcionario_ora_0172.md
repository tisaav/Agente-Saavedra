# Erro ao carregar página de dados 1 para Funcionário. ORA-01722: número inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32407957000855-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-Funcion%C3%A1rio-ORA-01722-n%C3%BAmero-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/32407957000855-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-Funcion%C3%A1rio-ORA-01722-n%C3%BAmero-inv%C3%A1lido)  
> **ID:** `32407957000855` | **Última Atualização:** 2026-09-03T13:18:21Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32552604842903)

 **MENSAGEM:**

Erro ao carregar página de dados 1 para Funcionário.

ORA-01722: número inválido

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32407924824983)

 **SITUAÇÃO:**

Ao tentar acessar a tela de funcionários, é exibida a mensagem acima.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32407924826391)

** SOLUÇÃO:**

Para corrigir o problema, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32536336059543)

 Na Tela **"Código de Afastamento"** *(Pessoal+ » Cadastros » Código de Afastamento)*, identifique o código de afastamento que contém letras no campo **CODAFAST**. 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32536336061975)

Após a identificação, verifique se existe algum **Tipo de Rescisão ***(Pessoal+ » Cadastros » Tipo de Rescisão) *que utilizou este código de letras, pois será necessário ajustar.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32536297617815)

Após ajustar o tipo de rescisão, utilizando apenas o código numérico correto, exclua o código de afastamento que contém letras.  

 

Feita a correção, o acesso à tela ''**Configuração de Funcionários''** será realizado sem a exibição de mensagens de erro.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32407956995607)

** CAUSA:**

O erro está relacionado a tabela TFPAFA, na tela Código de Afastamento. 

O sistema tenta interpretar o conteúdo do campo **CODAFAST** como um valor numérico, porém foi identificado um valor inválido, com letras como.** Exemplo:****  S , J**. 

Essa mensagem indica que está sendo feita uma tentativa de conversão numérica na **TFPFUN **na tela Configuração Funcionários sobre um campo que contém **letras**, o que não é permitido, pois exige valores numéricos.