# Erro 303 - Não foi localizado o contrato de trabalho do trabalhador CPF: 'x' e Categoria: 'x'

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16842127409047-Erro-303-N%C3%A3o-foi-localizado-o-contrato-de-trabalho-do-trabalhador-CPF-x-e-Categoria-x](https://ajuda.sankhya.com.br/hc/pt-br/articles/16842127409047-Erro-303-N%C3%A3o-foi-localizado-o-contrato-de-trabalho-do-trabalhador-CPF-x-e-Categoria-x)  
> **ID:** `16842127409047` | **Última Atualização:** 2026-07-29T13:17:56Z

---

[303] Não foi localizado o contrato de trabalho do trabalhador CPF: 'X', Matrícula: 'X' e Categoria: Desconhecida.

[304] Não existe um contrato de trabalho para o CPF: 'X', Matrícula: 'X'  ou este encontra-se encerrado na data do evento.

 

### 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309823756567)

**SITUAÇÃO**

Ao tentar transmitir o evento **"S-2399"** (Trabalhador Sem Vínculo de Emprego/Estatutário - Término) para o eSocial, o sistema retorna os erros 303 e 304, indicando que não foi localizado um contrato de trabalho ativo para o trabalhador na data do evento.

 

### 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309818008215)

**SOLUÇÃO**

Para resolver este erro, verifique as seguintes situações:

**Situação 1: Evento S-2300 não enviado ao eSocial**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/41065461697687)

 Verifique se o evento **"S-2300"** (Trabalhador Sem Vínculo de Emprego/Estatutário - Início) foi enviado ao eSocial.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/41065468305815)

 Caso não tenha sido enviado, gere e transmita o evento **"S-2300"** antes de enviar o **"S-2399"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/41065468308119)

 Após a confirmação do envio do **"S-2300"**, gere e envie o evento **"S-2399"**.

**Situação 2: Evento S-2300 enviado ao eSocial**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/41065461697687)

 Verifique se o evento **"S-2300"** (Trabalhador Sem Vínculo de Emprego/Estatutário - Início) foi enviado ao eSocial e com qual matricula ele foi enviado. 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/41065468305815)

Confira se a matricula enviada é a mesma que consta no sistema nos campos Matricula e/ou Matrícula Alternativa na tela **Configuração Funcionários** (Configurações » Cadastros » Pessoal » Configuração Funcionários)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/41065468308119)

 Se estiver diferente é necessário ajustar o campo Matrícula Alternativa incluindo o matricula que consta no e-Social. 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41065461705367)

 Faça uma geração geral e depois tente enviar novamente o evento. 

 

### 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309818008599)

**CAUSA**

Os erros 303 e 304 ocorrem quando:

- 

O evento **"S-2300"** não foi enviado previamente ao eSocial, sendo necessário cadastrar o contrato de trabalho antes de encerrá-lo.
 

1. 

O contrato de trabalho já se encontra **e-Social** com matricula diferente do sistema.