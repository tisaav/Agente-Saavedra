# O evento S-1200 referente ao trabalhador autônomo está apresentando erro no envio ao eSocial

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39380806974743-O-evento-S-1200-referente-ao-trabalhador-aut%C3%B4nomo-est%C3%A1-apresentando-erro-no-envio-ao-eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/39380806974743-O-evento-S-1200-referente-ao-trabalhador-aut%C3%B4nomo-est%C3%A1-apresentando-erro-no-envio-ao-eSocial)  
> **ID:** `39380806974743` | **Última Atualização:** 2026-07-29T13:23:27Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39380790395543)

 MENSAGEM**

8 - Grupo informações complementares contratuais do trabalhador deve ser preenchido.

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39380790398487)

 SITUAÇÃO**

Ao tentar enviar o evento **"S-1200"** (Remuneração de Trabalhadores) na **"Central do eSocial"** (Pessoal eSocial Central do eSocial), o sistema retorna erro para trabalhadores autônomos. 

 

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39380806968215)

 SOLUÇÃO**

**Cenário 1: Campo "Situação no eSocial" preenchido incorretament**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39380790399383)

 Acesse a tela **Configuração de Funcionários** (**Configurações » Cadastros » Pessoal » Configuração de Funcionários**) e localize o cadastro do trabalhador autônomo que apresentou o erro.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39380806968983)

 Analise o preenchimento do campo Situação no eSocial e observe as seguintes regras:

**Opção: "Não sujeito à admissão no eSocial"**

Caso o trabalhador esteja configurado com essa opção, verifique se já houve geração ou envio do evento S-2300 para esse autônomo.

- 

Se nunca houve geração ou envio do S-2300, mantenha a configuração atual.

- 

Se já foi gerado ou enviado o S-2300, altere o campo Situação no eSocial para "Oficial: S-2205, S-2206 e S-2306", garantindo compatibilidade com o histórico de eventos enviados ao eSocial.

**Opção: "Oficial: S-2205, S-2206 e S-2306"**

Quando essa opção estiver selecionada, confirme se o evento S-2300 já foi transmitido ao eSocial. Caso o S-2300 ainda não tenha sido enviado, realize o envio do evento antes de prosseguir com o processamento do S-1200.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41234024597271)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39380806969495)

 Após realizar os ajustes necessários, acesse a **Central do eSocial** (**Pessoal+ » Rotinas Folha » Central do eSocial**), gere novamente o evento **S-1200** e efetue um novo envio

**Cenário 2: Matrícula preenchida incorretamente**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39380790399383)

 Acesse a tela **Configuração de Funcionários** (**Configurações » Cadastros » Pessoal » Configuração de Funcionários**) e localize o cadastro do trabalhador autônomo que apresentou o erro.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39380806968983)

 Confira o preenchimento dos campos "**Matrícula" **e "**Matrícula alternativa"**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41234049792663)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41234024601111)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39380806969495)

 Valide qual matrícula está registrada para esse trabalhador no ambiente do eSocial.

A matrícula utilizada pelo sistema deve corresponder à matrícula existente no eSocial, seja pelo campo **Matrícula** ou pelo campo **Matrícula alternativa**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39380806970007)

 Caso exista divergência entre as informações, informe no campo **Matrícula alternativa** a mesma matrícula cadastrada no eSocial.

**Importante:** Nessa situação, não é necessário alterar o campo **Matrícula**. Basta preencher corretamente o campo **Matrícula alternativa** para que o envio do evento seja realizado com sucesso.

** **

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39380806970647)

 Após o ajuste, acesse a **Central do eSocial** (**Pessoal+ » Rotinas Folha » Central do eSocial**), gere novamente o evento **S-1200** e realize um novo envio.

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39380806972311)

 CAUSA**

O erro no envio do evento **S-1200** para trabalhadores autônomos normalmente ocorre devido à inconsistência entre as informações cadastradas no sistema e aquelas já registradas no ambiente do eSocial.

As situações mais comuns são:

- 

O campo **Situação no eSocial** está configurado de forma incompatível com o histórico de eventos do trabalhador, como casos em que o autônomo possui um **S-2300 já enviado**, mas permanece configurado como **"Não sujeito à admissão no eSocial"**.

- 

Divergência na **matrícula do trabalhador**, quando a matrícula utilizada para geração do S-1200 não corresponde à matrícula cadastrada no eSocial. Nesses casos, é necessário ajustar o campo **Matrícula alternativa** para que contenha a mesma informação existente no ambiente do eSocial.