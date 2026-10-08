# Tela "Gestão de Licenças" não aparece mesmo após liberação de acesso

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39378066483351-Tela-Gest%C3%A3o-de-Licen%C3%A7as-n%C3%A3o-aparece-mesmo-ap%C3%B3s-libera%C3%A7%C3%A3o-de-acesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/39378066483351-Tela-Gest%C3%A3o-de-Licen%C3%A7as-n%C3%A3o-aparece-mesmo-ap%C3%B3s-libera%C3%A7%C3%A3o-de-acesso)  
> **ID:** `39378066483351` | **Última Atualização:** 2026-08-19T19:32:56Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39378066478615)

 **MENSAGEM**

A tela "Gestão de Licenças" não é exibida, mesmo com a liberação de acesso concedida ao usuário.
 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39378066478871)

 **SITUAÇÃO**

O usuário tenta acessar o caminho **Configurações > Avançado > Gestão de Licenças**, mas a tela não consta no menu. Isso impede o gerenciamento de acessos e a liberação de licenças travadas.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39378020512663)

 **SOLUÇÃO**

Para resolver este problema, siga os passos abaixo:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39378020513175)

 **Verifique o Parâmetro:**

Acesse **Configurações > Avançado > Preferências** e busque por `**INITSASONLINE**`.

- 

*Caso não exista, crie-o manualmente:* * **Chave:** `**INITSASONLINE**`** **| **Tipo:** Lógico | **Valor:** Ligado.

- 

M**ódulo/Menu/Aba:** Configurações / Diversas / Diversas.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39378020513431)

 **Reinicie o parâmetro**

- 

Desligue o parâmetro `INITSASONLINE` e **Salve**.

- 

Ligue o parâmetro novamente e **Salve**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39378066479895)

 **Validação**

- 

Peça ao usuário afetado para atualizar o sistema (F5) ou realizar um novo login.

- 

Verifique se a tela **Gestão de Licenças** passou a ser exibida no caminho: ***Configurações > Avançado > Gestão de Licenças***.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39378020515735)

 **CAUSA**

A ausência da tela ocorre devido à falta de inicialização do serviço SAS Online no ambiente. O parâmetro `**INITSASONLINE**`** **força a ativação dessa interface moderna de gestão.